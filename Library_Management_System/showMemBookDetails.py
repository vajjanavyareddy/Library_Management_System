import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb = create_client(url, key)

def get_members_with_borrowed_books():
    members_resp = sb.table("members").select("*").execute()
    members = members_resp.data or []

    borrow_resp = sb.table("borrow_records").select("*").execute()
    borrow_records = borrow_resp.data or []

    books_resp = sb.table("books").select("*").execute()
    books = books_resp.data or []

    books_dict = {book['book_id']: book for book in books}
    borrowed_by_member = {}
    for br in borrow_records:
        borrowed_by_member.setdefault(br['member_id'], []).append(br)

    result = []
    for member in members:
        member_books = []
        borrowed = borrowed_by_member.get(member['member_id'], [])
        for br in borrowed:
            book = books_dict.get(br['book_id'])
            if book:
                member_books.append({
                    "record_id": br['record_id'],
                    "title": book['title'],
                    "author": book['author'],
                    "borrow_date": br.get('borrow_date'),
                    "return_date": br.get('return_date')
                })
        result.append({
            "member": member,
            "borrowed_books": member_books
        })

    return result

if __name__ == "__main__":
    members_with_books = get_members_with_borrowed_books()
    for entry in members_with_books:
        member = entry["member"]
        books = entry["borrowed_books"]
        print(f"Member: {member['name']} (Email: {member.get('email', 'N/A')})")
        if books:
            print("  Borrowed Books:")
            for book in books:
                print(f"    - {book['title']} by {book['author']}, Borrowed on {book['borrow_date']}, Returned on {book.get('return_date', 'Not returned')}")
        else:
            print("  No borrowed books.")
        print()
