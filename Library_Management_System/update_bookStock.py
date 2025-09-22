from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def update_stock(book_id,newstock):
    resp=sb.table("books").update({"stock":newstock}).eq("book_id",book_id).execute()
    return resp.data

if __name__ == "__main__":
    bid = int(input("Enter book_id to update: ").strip())
    new_stock = int(input("Enter new stock value: ").strip())
 
    updated = update_stock(bid, new_stock)
    if updated:
        print("Updated record:", updated)
    else:
        print("No record updated — check book_id.")
 