from flask import Flask

app = Flask(__name__)

@app.route("/search")
def search():
    return "hi"

@app.route("/answer")
def answer():
    return "hi"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
