from flask import Flask
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(users_id):
    return Users.query.get(int(users_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.VARCHAR(255), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    user_type = db.Column(db.Integer)
    passed_exam = db.Column(db.Integer)
    email_ver = db.Column(db.Integer)
    profile_pic = db.Column(db.String(255), nullable=True, default='default.png')

    def __repr__(self):
        return '<Users %r>' % (self.first_name + " " + self.last_name)



