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


    def __repr__(self):
        return f'User {self.username}'


class Pitch:

    all_pitches = []
    
    def __init__(self, pitch_id, category):
    
