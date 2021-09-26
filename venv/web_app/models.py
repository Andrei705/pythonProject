from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

from string import whitespace

login = LoginManager()
db = SQLAlchemy()
class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder = db.Column(db.String(100), db.CheckConstraint('folder != " "'), nullable=False)
    type_one = db.Column(db.String(100), nullable=False)
    type_two = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return '<Type {}>'.format(self.id)

#  Создание пользователя с хеширование пароля
# class User(UserMixin,db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     password_hash = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#
#
#     def gen_password(self,password):
#         self.password_hash = generate_password_hash(password)
#
#
#     def check_password(self,password):
#         return check_password_hash(self.password_hash, password)
#
#
#     def __repr__(self):
#         return '<{}:{}>'.format(self.id, self.user_name)
#
# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))