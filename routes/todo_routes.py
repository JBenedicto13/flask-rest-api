from flask import Blueprint, request
from controllers.todo_controller import get_all_todos, get_todo_by_id

todo_bp = Blueprint('todo', __name__)

@todo_bp.route("/todo", methods=["GET"])
def get_todo():
    id = request.args.get("id", type=int)

    try:
        if id is not None:
            response = get_todo_by_id(id)
        else:
            response = get_all_todos()
        return response.data
    except Exception as e:
        return str(e)