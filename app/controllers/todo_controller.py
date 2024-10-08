from app.db import get_supabase_client
from app.utils.return_format import ReturnFormat
supabase_client = get_supabase_client()

def get_todo_by_id(id):
    if not id:
        return ReturnFormat(data=None, message="Required Id is missing.").to_dict(), 400

    try:
        response = supabase_client.table("todo").select("*").eq("id", id).execute()
        return ReturnFormat(data=response.data, message="Todo retrieved successfully.").to_dict()
    except Exception as e:
        return ReturnFormat(data=None, message=str(e)).to_dict(), 500

def get_all_todos():
    try:
        response = supabase_client.table("todo").select("*").execute()
        return ReturnFormat(data=response.data, message="Todos retrieved successfully.").to_dict()
    except Exception as e:
        return ReturnFormat(data=None, message=str(e)).to_dict(), 500

def add_item(data):
    name = data.get("name")
    if not name:
        return ReturnFormat(data=None, message="Required Name is missing.").to_dict(), 400
    try:
        response = supabase_client.table("todo").insert({"name": name}).execute()
        return ReturnFormat(data=response.data, message=f"{name} was added to the list!").to_dict(), 201
    except Exception as e:
        return ReturnFormat(data=None, message=str(e)).to_dict(), 500
    
def update_item(data, id):
    itemId = id
    updated_field = {}

    if "name" in data and data["name"] is not None:
        updated_field["name"] = data["name"]

    if "isFinished" in data and data["isFinished"] is not None:
        updated_field["isFinished"] = data["isFinished"]

    if not itemId:
        return ReturnFormat(data=None, message="Required Id is missing.").to_dict(), 400

    if not updated_field:
        return ReturnFormat(data=None, message="No fields to update.").to_dict(), 400

    try:
        item = get_todo_by_id(id)
        if not item:
            return ReturnFormat(data=None, message="Item not found.").to_dict(), 400
        
        response = supabase_client.table("todo").update(updated_field).eq("id", itemId).execute()
        return ReturnFormat(data=response.data, message=f"{item['data'][0]['name']} has been updated!").to_dict(), 201 
    except Exception as e:
        return ReturnFormat(data=None, message=str(e)).to_dict(), 500
    
def delete_item(id):
    itemId = id
    if not itemId:
        return ReturnFormat(data=None, message="Required Id is missing.").to_dict(), 400

    try:
        item = get_todo_by_id(id)
        response = supabase_client.table("todo").delete().eq("id", itemId).execute()
        return ReturnFormat(data=response.data, message=f"{item['data'][0]['name']} has been deleted!").to_dict(), 201 
    except Exception as e:
        return ReturnFormat(data=None, message=str(e)).to_dict(), 500
    