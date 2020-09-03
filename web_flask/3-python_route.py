#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """returns a custom message at / route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """returns a custom message at /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    returns a string at /c/<text> route,
    expands the <text> variable
    """
    new = text.replace('_', ' ')
    return 'C %s' % new


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text):
    """
    returns a string at /python route, with a default text
    of 'is cool', or the expansion of <text>
    """
    new = text.replace('_', ' ')
    return 'Python %s' % new


if __name__ == '__main__':
    app.run(host='0.0.0.0')
