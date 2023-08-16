#!/usr/bin/python3
""" script to start a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """fast route displaying a message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """new path to /hbnb and displays a message"""
    return "HBNB"


if __name__ == '__main__':
    """application listen on IP address 0.0.0.0.0 and port 5000"""
    app.run(host='0.0.0.0', port=5000)
