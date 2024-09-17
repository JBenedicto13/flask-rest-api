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