from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
import os
HOST = 'HOST'
@app.route("/")
def index():
    return "Welcome to Dockerize Flask App!"
@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == "__main__":
    app.run(host=os.getenv('HOST', "127.0.0.1") , port=int("5000"), debug=os.getenv('DEBUG', False))
