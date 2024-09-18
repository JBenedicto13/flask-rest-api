# app/config/cors.py
from flask_cors import CORS

def init_cors(app):
    """Initialize CORS configuration for the app."""
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5000", "http://localhost:5000"]}})  # Replace "*" with specific origins if needed
