# app.py

from flask import Flask, request, jsonify, flash, redirect  # import flask
from service import ProcessImageService
from werkzeug.utils import secure_filename
import os
import urllib.request
app = Flask(__name__)  # create an app instance


app.config['UPLOAD_FOLDER'] = '../images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.after_request  # Headers
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/ping")     # at the end point /
def ping():             # call method hello
    return "pong"       # which returns "pong"


@app.route('/process', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "sample.jpeg"))
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201

            return jsonify(ProcessImageService().process("test"))

        else:
            resp = jsonify(
                {'message': 'Allowed file types are png, jpg, jpeg'})
            resp.status_code = 400
            return resp


# on running python app.py
if __name__ == "__main__":
    # run the flask app on port 8080
    app.run(debug=True, port=8080)
