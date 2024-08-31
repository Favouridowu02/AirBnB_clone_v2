#!/usr/bin/python3
"""
    This Module contains a script that starts a Flask web application
    Routes:
        home
        route
        c: a dynamic route that gets the text for the url
        python: a dynamic route that gets the text for the url, If
        none is passed text ="is magic"
        number: a dynamix route that only collect numbers
        number_template: a dynamic route that renders am html template
        number_odd_or_even: a dynamic route that renders an html template

    Option: strict_slashes=False
"""
from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    num = 'odd'
    if n % 2 == 0:
        num = 'even'

    return render_template('6-number_odd_or_even.html', n=n, num=num)


if __name__ == "__main__":
    app.run(debug=True)
