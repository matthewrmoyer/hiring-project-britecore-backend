from app import db

class User(db.Model):
    """docstring for Property"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)


    def __init__(self, name, email):
        self.name = name
        self.email = email
        