import flask
import redis_wrapper
from flask import request, jsonify, Flask, abort, Response, send_from_directory


app = Flask(__name__, static_url_path='')
app.config["DEBUG"] = True
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
def push_strokes():
    data = request.json
    # print(data["strokes"])
    redis_wrapper.insert_stroke(data['strokes'])
    return "ok"

@app.route('/new_strokes', methods=['GET'])
def get_strokes():
    new_strokes_raw = redis_wrapper.get_last_n()

    new_strokes = []
    for raw_stroke in new_strokes_raw:
        stroke = raw_stroke.decode("utf-8").split(", ")
        for i in range(len(stroke)):
            stroke[i] = int(stroke[i])
        new_strokes.append(stroke)

    return {
        "strokes": new_strokes
    }

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>This site is a prototype API</h1>"

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
