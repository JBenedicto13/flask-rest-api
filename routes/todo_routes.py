from flask import Blueprint, request
from controllers.todo_controller import get_all_todos, get_todo_by_id, add_item

todo_bp = Blueprint('todo', __name__)

@todo_bp.route("/todo", methods=["GET", "POST"])
def handle_todo():
    if request.method == "GET":
        id = request.args.get("id", type=int)
        if id is not None:  # If an ID is provided, get a specific todo
            return get_todo_by_id(id)  # Directly call the controller function
        else:  # If no ID is provided, get all todos
            return get_all_todos()  # Call the function to get all todos

    elif request.method == "POST":
        data = request.get_json()  # Get JSON data from the request
        return add_item(data)  # Directly call the controller function