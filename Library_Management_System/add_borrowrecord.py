import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb = create_client(url, key)

def add_borrow_record(member_id: int, book_id: int, borrow_date=None, return_date=None):
    record = {
        "member_id": member_id,
        "book_id": book_id,
    }
    if borrow_date:
        record["borrow_date"] = borrow_date
    if return_date:
        record["return_date"] = return_date

    resp = sb.table("borrow_records").insert(record).execute()
    
    # Check for error via status_code or data content
    if resp.status_code != 201:  # 201 Created is expected
        print("Error inserting borrow record:", resp.data)
        return None

    return resp.data


if __name__ == "__main__":
    member_id = int(input("Enter member_id: "))
    book_id = int(input("Enter book_id: "))
    borrow_date = input("Enter borrow date (YYYY-MM-DDTHH:MM:SSZ) or leave blank for now: ").strip() or None
    return_date = input("Enter return date (YYYY-MM-DDTHH:MM:SSZ) or leave blank if not returned: ").strip() or None

    result = add_borrow_record(member_id, book_id, borrow_date, return_date)
    if result:
        print("Borrow record added:", result)
    else:
        print("Failed to add borrow record.")
