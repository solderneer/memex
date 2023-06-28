# Flask imports
from flask import Flask, request
from flask_cors import CORS

# Local modules
from index import Index

index = Index("./embeddings", ["./notes", "./letters", "./_private"])
index.refresh()

app = Flask(__name__)
cors = CORS(app)

@app.route("/refresh")
def refresh():
    total, skipped, error = index.refresh()
    return {
        "total": total,
        "skipped": skipped,
        "error": error
    }

@app.route("/search")
def search():
    query = request.args.get('query', '')
    limit = int(request.args.get('limit', '5'))
    return index.search(query, limit)

@app.route("/answer")
def answer():
    return "hi"
