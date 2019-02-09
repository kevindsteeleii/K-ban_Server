from flask import Flask, request, jsonify, Blueprint
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import os

# Init
app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" +os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ENV config
app.env = 'development'

# Init db and ma
db = SQLAlchemy(app)
ma = Marshmallow(app)

# import API blueprints
from api.users import users_blueprint
from api.boards import boards_blueprint
from api.tasks import tasks_blueprint
from auth import auth_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(boards_blueprint, url_prefix='/boards')
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')
app.register_blueprint(auth_blueprint)

# Routes and API
@app.route('/')
def index():
    return "<h1>It's working</h1>"
