from flask import Flask, request  # Import request to handle query parameters
from config.db import get_supabase_client
supabase_client = get_supabase_client()

from routes.todo_routes import todo_bp

app = Flask(__name__)
app.register_blueprint(todo_bp)

@app.get("/")
def home():
    try:
        supabase_client = get_supabase_client()  # Call the function to get the client
        print(supabase_client.table("test").select("*").execute())
        return "Server and Database connection is running!"
    except Exception as e:
        return str(e)  # Return the error message if connection fails
    
@app.post("/todo")  # Keep only POST method
def add_todo():
    try:
        data = request.get_json()  # Get JSON data from the request
        name = data.get("name")  # Extract the name from the JSON

        if not name:
            return {"error": "Required Name is missing"}, 400  # Return 400 status code
        
        response = supabase_client.table("todo").insert({"name": name}).execute()
        return {"message": f"{name} was added to the list!"}, 201  # Return 201 status code
    except Exception as e:
        return {"error": str(e)}, 500  # Return 500 status code for server errors