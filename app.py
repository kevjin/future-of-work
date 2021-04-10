from typing import List
import flask
import sqlite3
from flask import request, jsonify, Flask, abort, Response, send_from_directory
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def send_static():
    return send_from_directory('static', "index.html")

# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>This site is a prototype API</h1>"

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
