import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def add_member(name, email):
    mem = {"name": name,"email": email}
    resp = sb.table("members").insert(mem).execute()
    return resp.data

if __name__ == "__main__":
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    
 
    created = add_member(name, email)
    print("Inserted:", created)
 