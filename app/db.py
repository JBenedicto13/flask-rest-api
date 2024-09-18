import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def get_supabase_client() -> Client:
    response = supabase.table("test").select("*").limit(1).execute()
    if response.data:
        return supabase
    else:
        raise Exception("No data found, connection may not be established.")