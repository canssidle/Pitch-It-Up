from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(225))


    def __repr__(self):
        return f'User {self.username}'


class Pitch:

    all_pitches = []
    
    def __init__(self,pitch_id,category)
    
