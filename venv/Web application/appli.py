from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.debug =True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/object_db"
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS']= False
db = SQLAlchemy(app)

db.init_app(app)
migrate = Migrate(db, app)

class Type(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    folder = db.Column(db.Text, nullable=False)
    type_one = db.Column(db.Text, nullable=False)
    type_two = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return 'Type %r' % self.folder



@app.route('/')
def form():
    return render_template('form.html')

@app.route('/completion', methods =['POST', 'GET'])
def completion():
    if request.method == "GET":
        return "Error"

    if request.method == "POST":
        folder = request.form['folder']
        type_one = request.form['type_one']
        type_two = request.form['type_two']
        completion_db = Type(folder=folder, type_one=type_one, type_two=type_two)
        db.session.add(completion_db)
        db.session.commit()
        return f'Ok'


if __name__ == "__main__":
    app.run()
