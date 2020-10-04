import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models import Result


@app.route("/")
def hi():
    return "Hello World!"


@app.route("/<name>")
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    print(os.environ["APP_SETTINGS"])
    app.run()
