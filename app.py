from flask import Flask, jsonify, request, render_template, g
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True


def connect_db():
    sql = sqlite3.connect('data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/viewresults')
def viewresults():
    db = connect_db()
    cur = db.execute('select id, name, location from users')
    results = cur.fetchall()
    data = [res['id'] for res in results]
    return 'The id is {}.'.format(results[0]['id'])

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
