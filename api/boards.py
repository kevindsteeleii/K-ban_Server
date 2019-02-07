from flask import request, jsonify, Blueprint 
from app import db   
from models import Board, board_schema, boards_schema, Task, tasks_schema

boards_blueprint = Blueprint(
    'boards',
    __name__
)

@boards_blueprint.route('', methods=['POST'])
def create_board():
    name = request.json['name']
    user_id = request.json['user_id']

    new_board = Board(name, user_id)
    db.session.add(new_board)
    db.session.commit()

    return board_schema.jsonify(new_board)

@boards_blueprint.route('', methods=['GET'])
def show_boards():
    all_boards = Board.query.all()
    result = boards_schema.dump(all_boards)
    return jsonify(result.data)

@boards_blueprint.route('/<int:id>', methods=['GET'])
def show_board(id):
    board = Board.query.get(id)
    return board_schema.jsonify(board)

@boards_blueprint.route('/<int:id>', methods=['PATCH'])
def patch_board(id):
    board = Board.query.get(id)
    board.name = request.json['name']
    db.session.commit()

    return board_schema.jsonify(board)

@boards_blueprint.route('/<int:id>', methods=['DELETE'])
def remove_board(id):
    board = Board.query.get(id)
    db.session.delete(board)
    db.session.commit()

    return board_schema.jsonify(board)

@boards_blueprint.route('/<int:id>/tasks', methods=['GET'])
def get_tasks(id):
    board_tasks = Task.query.filter_by(board_id=id).all()
    result = tasks_schema.dump(board_tasks)
    return jsonify(result.data)