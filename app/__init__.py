# app/__init__.py
from flask import Flask
from app.config.cors import init_cors
from app.routes.todo_routes import todo_bp

def create_app():
    app = Flask(__name__)
    
    # Initialize CORS
    init_cors(app)

    # Register your blueprints
    app.register_blueprint(todo_bp)
    
    return app
