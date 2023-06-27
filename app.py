# Flask imports
from flask import Flask

# Local modules
from index import Index

index = Index("./embeddings", ["./notes", "./letters", "./_private"])
index.refresh()

app = Flask(__name__)

@app.route("/index")
def index():
    pass

@app.route("/search")
def search():
    return "hi"

@app.route("/answer")
def answer():
    return "hi"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
