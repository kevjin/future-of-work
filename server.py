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
    print(data["strokes"])
    return "ok"

@app.route('/new_strokes', methods=['GET'])
def get_strokes():
    new_strokes = [[675, 200, 673, 200], [673, 200, 669, 206], [669, 206, 657, 222], [657, 222, 640, 250], [640, 250, 623, 284], [623, 284, 615, 302], [615, 302, 613, 315], [613, 315, 612, 326], [612, 326, 612, 333], [612, 333, 619, 339], [619, 339, 635, 340], [635, 340,657, 340], [657, 340, 691, 340], [691, 340, 725, 336], [725, 336, 754, 328], [754, 328, 770, 322], [770, 322, 780, 316], [780, 316, 789, 307], [789, 307, 791, 299], [791, 299, 785, 285], [785, 285, 770, 270], [770, 270, 743, 254], [743, 254, 694, 245]]
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
