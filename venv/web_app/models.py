from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder = db.Column(db.String(100), nullable=False)
    type_one = db.Column(db.String(100), nullable=False)
    type_two = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return '<Type {}>'.format(self.id)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return '<{}:{}>'.format(self.id, self.user_name)