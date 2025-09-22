import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def search_books(keyword):
    
    resp = sb.table("books") \
        .select("*") \
        .or_(
            f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%"
        ).execute()
    return resp.data

if __name__ == "__main__":
    keyword = input("Enter keyword to search by title, author, or category: ").strip()
    results = search_books(keyword)
    
    if results:
        print(f"Found {len(results)} book(s):")
        for book in results:
            print(f"- {book['title']} by {book['author']} [{book['category']}], Stock: {book['stock']}")
    else:
        print("No books found matching the keyword.")
