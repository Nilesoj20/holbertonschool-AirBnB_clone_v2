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
def estados_lista():
    """ path to print the list of states """
    estados = storage.all(State).values()
    return render_template('7-states_list.html', estados=estados)


@app.route('/states/<id>', strict_slashes=False)
def ciudades_lista(id):
    """ path to print the list of cities """
    estados = storage.all(State).values()
    for estado in estados:
        if estado.id == id:
            return render_template('9-states.html', estados=estado)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
