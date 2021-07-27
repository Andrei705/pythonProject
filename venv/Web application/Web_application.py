from flask import Flask, render_template
from  tinydb import TinyDB, Query


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('date.html')


if __name__ == "__main__":
    app.run()
