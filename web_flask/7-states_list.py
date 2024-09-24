#!/usr/bin/python3
"""
    This module Contains a python flask script to fetch from the mysql database

    Routes:
        home: returns 'I am Home'
"""
import sys
import os
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """The Home Page of this web app"""
    return "I am Home"


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(exception=True):
    """This method handles the closure"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000', debug=True)
