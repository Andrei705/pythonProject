from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder = db.Column(db.String(52))
    type_one = db.Column(db.text)
    type_two = db.Column(db.text)


    def __init__(self,folder,type_one, type_two):
        self.folder = folder
        self.type_one = type_one
        self.type_two = type_two


    def __repr__(self):
        return 'Type %r' % self.folder