from typing import List
import flask
import redis_wrapper
import sqlite3
from flask import request, jsonify, Flask, abort, Response, send_from_directory
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/dbsuccess')
def connect():
    redis_wrapper.set_data(key="foo", value="bar")
    resp = redis_wrapper.get_data(key="foo")
    assert "bar" in str(resp)
    return "ok"

@app.route('/')
def home():
    return send_from_directory('static', "index.html")

@app.route('/new_strokes', methods=['POST'])
def push():
    data = request.json
    print(data["strokes"])
    return "ok"

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>This site is a prototype API</h1>"

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
