#!/usr/bin/python3
"""
    This Module contains a script that starts a Flask web application
    Routes:
        home
        route
        c: a dynamic route that gets the text for the url
        python: a dynamic route that gets the text for the url, If
        none is passed text ="is magic"

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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(debug=True)
