from config.db import get_supabase_client
supabase_client = get_supabase_client()

def get_todo_by_id(id):
    try:
        response = supabase_client.table("todo").select("*").eq("id", id).execute()
        return {"data": response.data, "message": "Todo retrieved successfully."}  # Uniform return
    except Exception as e:
        return {"data": None, "message": str(e)}, 500  # Handle errors uniformly

def get_all_todos():
    try:
        response = supabase_client.table("todo").select("*").execute()
        return {"data": response.data, "message": "Todos retrieved successfully."}  # Uniform return
    except Exception as e:
        return {"data": None, "message": str(e)}, 500  # Handle errors uniformly

def add_item(data):
    name = data.get("name")  # Extract the name from the JSON
    if not name:
        return {"data": None, "message": "Required Name is missing."}, 400  # Return 400 status code

    try:
        response = supabase_client.table("todo").insert({"name": name}).execute()
        return {"data": response.data, "message": f"{name} was added to the list!"}, 201  # Return 201 status code
    except Exception as e:
        return {"data": None, "message": str(e)}, 500  # Return 500 status code for server errors