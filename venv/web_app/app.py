from flask import Flask, render_template, request, abort
from flask_migrate import Migrate
from models import db, Type, login

app = Flask(__name__)
app.debug =False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/object_db"
app.config['SQLALCHEMY_TRACK_MODIFYCATIONS']= False

login.login_view = 'login'
login.init_app(app)
db.init_app(app)
migrate = Migrate(db, app)


@app.route('/object/', defaults={'id':''})
@app.route('/object/<int:id>/')
@app.route('/object/<string:id>/')
def show_db(id):
    print(id)
    date = Type.query.all()
    if id in [0,'']:
        return render_template('output_bd.html', date=date)
    elif id != int:
        abort(400, "Id задана не правельно")


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/completion', methods =['POST'])
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