from flask import Flask

app = Flask(__name__)

def add(x, y):
    """This is an add function"""
    return x + y


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"