from flask import Flask, render_template, request
from  tinydb import TinyDB, Query

app = Flask(__name__)


# def db_tiny():
#     db = TinyDB(r'C:\Users\user\PycharmProjects\pythonProject\venv\Web application\db.json')
#     return db
#
#
# def db_appeal():
#     db = db_tiny()
#     for i in db.all():
#        return i




@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == "POST":
        Email = request.POST
        Phone = request.form["Phone"]
        Date = request.form["Date"]
        Text = request.form["Text"]
        return Email
    else:
       return render_template('create_user.html')


if __name__ == "__main__":
    app.run()
