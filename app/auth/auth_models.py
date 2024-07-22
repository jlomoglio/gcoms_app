try:
    from app import db as db
except ImportError:
    from __name__ import db

from flask_login import UserMixin
# from sqlalchemy.sql import func --> used with dateTime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    #date = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # add a foreign key to the User model

    def __repr__(self):
        return f'<Task {self.title}>'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    #date = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())
    tasks = db.relationship('Task') # add a relationship to the Task model

    def __init__(self, username, email, first_name, last_name, password):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

        def __repr__(self):
            return f'<AuthUser {self.username}>'

