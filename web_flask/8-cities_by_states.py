#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_greetings():
    """ Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ C Text Replacing """
    return 'C ' + text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ display defined txt """
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display n is a number if type(n) == int"""
    if type(n) == int:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """ finds if even or odd """
    if n % 2 == 0:
        its = 'even'
    else:
        its = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           its=its)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states list"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def t1clozer(self):
    """ string to be returned """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_states():
    """ cities with states """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
