# app/routes/home_routes.py
from flask import Blueprint
from app.db import get_supabase_client

home_bp = Blueprint("home", __name__)

@home_bp.get("/")
def home():
    try:
        supabase_client = get_supabase_client()  # Call the function to get the client
        print(supabase_client.table("test").select("*").execute())
        return "Server and Database connection is running!"
    except Exception as e:
        return str(e)
