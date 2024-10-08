#!/usr/bin/python3
"""
    This Module contains a script that starts a Flask web application
    Routes:
        home
        route

    Option: strict_slashes=False
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True)
