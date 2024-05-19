from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<name>")
def index(name):
    return f"<h1>hello {name}.</h1>"

@app.route("/home")
def home():
    return "<h1>You are at home.</h1>"

@app.route("/jsonify")
def jsonify_data():
    return jsonify({'key': 'value', 'key2': [1, 2, 3]})