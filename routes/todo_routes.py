from flask import Blueprint, request
from controllers.todo_controller import get_all_todos, get_todo_by_id, add_item, update_item, delete_item

todo_bp = Blueprint('todo', __name__)

@todo_bp.route("/todo", methods=["GET", "POST", "PUT", "DELETE"])
def handle_todo():
    if request.method == "GET":
        id = request.args.get("id", type=int)
        if id is not None: 
            return get_todo_by_id(id)  
        else:
            return get_all_todos()  

    elif request.method == "POST":
        data = request.get_json()  
        return add_item(data) 
    
    elif request.method == "PUT":
        id = request.args.get("id", type=int)
        data = request.get_json()
        return update_item(data, id)
    
    elif request.method == "DELETE":
        id = request.args.get("id", type=int)
        return delete_item(id)