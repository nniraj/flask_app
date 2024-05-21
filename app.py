from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route("/<name>")
def index(name):
    return f"<h1>hello {name}.</h1>"

@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return render_template('form.html')

@app.route("/home/<string:name>", methods=['GET'])
def home(name):
    return render_template('home.html', name=name)


@app.route("/jsonify")
def jsonify_data():
    return jsonify({"key": "value", "key2": [1, 2, 3]})


@app.route("/query")
def query():
    name = request.args.get("name")
    location = request.args.get("location")
    return f"<h1>Hi {name}. You are on the {location} Page.</h1>"
