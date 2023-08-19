#!/usr/bin/python3
""" Flask web application that lists the city """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def eliminar_session(self):
    """delete the current SQLAlchemy session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ path to print the list of states """
    estados = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           estados=estados, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
