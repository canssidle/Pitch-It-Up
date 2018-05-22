from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

now = datetime.now()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(225),index = True)
    email = db.Column(db.String(225),unique = True,index = True)
    bio = db.Column(db.String(225))
    password_hash = db.Column(db.String(225))
    pitch = db.relationship('Pitch',backref = 'users',lazy = "dynamic")
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        reviews = Comment.query.filter_by(pitch_id=id)
        return = get_comments
    @password.setter
    def mypassword(self,password):
        self.new_password = generate_password_hash(mypassword)
    
    def verify_pass(self,password):
        return check_password_hash(self.new_password,password)


    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):

    __table__ = 'pitch'

    id = (db.Integer,primary_key = True)
    category_id = db.Column(db.Integer)
    pitch = db.Column(db.String)
    category_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment' ,backref = 'pitch',lazy = "dynamic")


    all_pitches = []
    
    def __init__(self, pitch_id, category):
    
