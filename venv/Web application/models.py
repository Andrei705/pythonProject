from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder = db.Column(db.String(100), nullable=False)
    type_one = db.Column(db.String(100), nullable=False)
    type_two = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return '<Type %r>' % self.id