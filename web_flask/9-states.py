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


@app.route("/states", strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def ciudades_lista(id):
    """ path to print the list of cities """
    state = None
    states = storage.all(State)

    for estado in states.values():
        if id in estados:
            state = states.get(f'State.{id}')
    contenedor = {
            'id': id,
            'states': states.values(),
            'state': state
            }
    return render_template("9-states.html", **contenedor)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
