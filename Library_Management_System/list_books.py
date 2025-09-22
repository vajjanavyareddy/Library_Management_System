from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def list_books():
    resp = sb.table("books").select("*").order("book_id", desc=False).execute()
    return resp.data

if __name__ == "__main__":
    books = list_books()
    if books:
        print("Books:")
        for b in books:
            print(f"{b['book_id']}: Title: {b['title']}  \nAuthor: {b['author']} \nCategory: {b['category']}  \nstock: {b['stock']}")
    else:
        print("No books found.")