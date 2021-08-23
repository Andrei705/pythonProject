from flask import Flask, render_template, request
from flask_migrate import Migrate
from models import db, Type


app = Flask(__name__)
app.debug =True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/object_db"
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS']= False

db.init_app(app)
migrate = Migrate(db, app)

@app.route('/object/id=0')
@app.route('/object')
def route():
    date = Type.query.all()
    return render_template('output_bd.html', date=date)


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/completion', methods =['POST', 'GET'])
def completion():
    if request.method == "POST":
        folder = request.form['folder']
        type_one = request.form['type_one']
        type_two = request.form['type_two']
        completion_db = Type(folder=folder, type_one=type_one, type_two=type_two)
        db.session.add(completion_db)
        db.session.commit()
        return 'OK'


if __name__ == "__main__":
    app.run()
