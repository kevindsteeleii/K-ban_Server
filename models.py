from app import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(30))
    password = db.Column(db.String(80))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        # will salt and hash later
        self.password = password

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    color = db.Column(db.String(7))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User',
        backref=db.backref('boards', lazy='dynamic')
    )
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    board = db.relationship(
        'Board',
        backref=db.backref('tasks', lazy='dynamic')
    )

    def __init__(self, content, board_id):
        self.content = content
        self.board_id = board_id

class UserSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'username', 'email')

user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)

class BoardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'user_id')

board_schema = BoardSchema(strict=True)
boards_schema = BoardSchema(many=True, strict=True)

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'content', 'board_id')

task_schema = TaskSchema(strict=True)
tasks_schema = TaskSchema(many=True, strict=True)
