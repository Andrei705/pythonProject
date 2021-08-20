from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from . import db, Type
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/object_db"

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/')


if __name__ == "__main__":
    app.run(debug=True)
