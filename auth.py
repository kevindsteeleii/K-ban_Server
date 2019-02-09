from flask import request, Blueprint, jsonify
from models import User, user_schema

auth_blueprint = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth'
)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    user = User.query.filter_by(username=username).first()

    if user is None:
        return jsonify({"err": "Invalid username."})
    else:
        if user.verify_login(password):
            return user_schema.jsonify(user)
        else:
            return jsonify({"err": "Invalid password."})
