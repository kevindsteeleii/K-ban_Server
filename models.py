from app import db, ma, bcrypt
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(80))
 
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        # will salt and hash later
        self.password = bcrypt.generate_password_hash(password).decode()
    
    def verify_login(self, attempted_password):
        attempted_password = attempted_password.encode()
        return bcrypt.check_password_hash(self.password, attempted_password)

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    color = db.Column(db.String(7))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User',
        single_parent=True,
        cascade="all, delete-orphan",
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
        single_parent=True,
        cascade="all, delete-orphan",
        backref=db.backref('tasks', lazy='dynamic')
    )

    def __init__(self, content, board_id):
        self.content = content
        self.board_id = board_id

class CheckList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    list_item = db.Column(db.String(100))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))

    def __init__(self, list_item, task_id):
        self.list_item = list_item
        self.task_id = task_id

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

class CheckListSchema(ma.Schema):
    class Meta:
        fields = ('id','date_created', 'list_item', 'task_id')

checklist_schema = CheckListSchema(strict=True)
checklists_schema = CheckListSchema( many=True, strict=True)
