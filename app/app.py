# app.py
from flask import Flask, request, jsonify           # import flask
from service import ProcessImageService
app = Flask(__name__)                               # create an app instance


@app.after_request  # Headers
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/ping")     # at the end point /
def ping():             # call method hello
    return "pong"       # which returns "pong"


@app.route("/process", methods=["GET"])
def list_process():
    return jsonify({"teste": "ok"})


@app.route("/process", methods=["POST"])
def create_process():
    return jsonify(ProcessImageService().process("test"))


if __name__ == "__main__":                 # on running python app.py
    app.run(port=8080)                     # run the flask app on port 8080
