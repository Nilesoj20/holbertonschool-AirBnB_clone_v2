#!/usr/bin/python3
""" Flask web application that lists the city """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def eliminar_session(self):
    """delete the current SQLAlchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def city_list():
    """ path to print the list of city """
    estados = storage.all(State).values()
    return render_template('8-cities_by_states.html', estados=estados)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
