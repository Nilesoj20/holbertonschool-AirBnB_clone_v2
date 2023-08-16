#!/usr/bin/python3
""" script to start a Flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """fast route displaying a message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """new path to /hbnb and displays a message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hbnb_variable(text):
    """new path to /c/text and displays a message"""
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    """application listen on IP address 0.0.0.0.0 and port 5000"""
    app.run(host="0.0.0.0", port=5000)
