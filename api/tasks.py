from flask import request, Blueprint, jsonify
from app import db
from models import Task, task_schema, tasks_schema

tasks_blueprint = Blueprint(
    'tasks',
    __name__
)

@tasks_blueprint.route('', methods=['POST'])
def create_task():
    content = request.json['content']
    board_id = request.json['board_id']
    new_task = Task(content, board_id)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)

@tasks_blueprint.route('', methods=['GET'])
def all_tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result.data)

@tasks_blueprint.route('/<int:pk>', methods=['GET'])
def show_task(pk):
    task = Task.query.get(pk)
    return task_schema.jsonify(task)

@tasks_blueprint.route('/<int:pk>/<string:update>', methods=['PATCH'])
def update_task(pk, update):
    task = Task.query.get(pk)
    if update == 'transfer':
        task.board_id = request.json['board_id']
    elif update == 'change_content':
        task.content = request.json['content']
    else:
        return jsonify({'msg': "Invalid update variable, last url term must be 'transfer' or 'change_content'."})
    db.session.commit()

    return task_schema.jsonify(task)

@tasks_blueprint.route('/<int:pk>', methods=['DELETE'])
def remove_task(pk):
    task = Task.query.get(pk)
    db.session.delete(task)
    db.session.commit()

    return task_schema.jsonify(task)
