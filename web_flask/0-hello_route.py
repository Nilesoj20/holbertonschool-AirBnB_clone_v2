#!/usr/bin/python3
""" script to start a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """fast route displaying a message"""
    return "¡Hola HBNB!"


if __name__ == '__main__':
    """application listen on IP address 0.0.0.0.0 and port 5000"""
    app.run(host='0.0.0.0', port=5000)
