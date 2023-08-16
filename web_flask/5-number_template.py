#!/usr/bin/python3
""" script to start a Flask web application"""
from flask import Flask, render_template
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hbnb_variable_2(text="is cool"):
    """adding default value to the path variable"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def hbnb_variable_entero(n):
    """using integer converter type"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def hbnb_variable_html(n):
    """displays an HTML page only if n is an integer"""
    return render_template('5-number.html')


if __name__ == '__main__':
    """application listen on IP address 0.0.0.0.0 and port 5000"""
    app.run(host="0.0.0.0", port=5000)
