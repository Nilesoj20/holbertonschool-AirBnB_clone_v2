#!/usr/bin/python3
""" Flask web application that lists the city """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def eliminar_session(self):
    """delete the current SQLAlchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """route to display states"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """route to display cities"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
