from config.db import get_supabase_client
supabase_client = get_supabase_client()

def get_todo_by_id(id):
    return supabase_client.table("todo").select("*").eq("id", id).execute()

def get_all_todos():
    return supabase_client.table("todo").select("*").execute()