from typing import List
import flask
import sqlite3
from flask import request, jsonify, Flask, abort, Response, send_from_directory
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

import redis
r = redis.Redis(host='localhost', port=6379, db=0)


app = Flask(__name__, static_url_path='')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def set_data(key, value):
    try: 
        success=r.set(key, value)
        return success
    except:
        return "error setting data"
def get_data(key):
    
    try: 
        res=r.get(key)
        return res
    except:
        return "Nay!", 202

@app.route('/dbsuccess')
def connect():
    set_data(key="foo", value="bar")
    try:
        res=get_data(key="foo")
        if res == "bar":
            return "ok"
        else:
            return res
    except Exception as e:
        return e

@app.route('/')
def home():
    return send_from_directory('static', "index.html")

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>This site is a prototype API</h1>"

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
