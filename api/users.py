from flask import request, Blueprint, jsonify
from app import db
from models import User, user_schema, users_schema, Board, boards_schema

users_blueprint = Blueprint(
    'users',
    __name__
)

@users_blueprint.route('', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    email = request.json['email']
    password = request.json['password']

    new_user = User(username, email, password)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@users_blueprint.route('', methods=['GET'])
def show_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

@users_blueprint.route('/<int:pk>', methods=['GET'])
def get_user(pk):
    user = User.query.get(pk)
    return user_schema.jsonify(user)

@users_blueprint.route('/<int:pk>/boards', methods=['GET'])
def get_boards(pk):
    user_boards = Board.query.filter_by(user_id=pk)
    result = boards_schema.dump(user_boards)
    return jsonify(result.data)
