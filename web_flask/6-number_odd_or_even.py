#!/usr/bin/python3
#!/usr/bin/python3
'''
Module to run the Flask web app on 0.0.0.0:5000
'''
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ returns `Hello HBNB` """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns `HBNB` """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def print_c(text=None):
    if text:
        return f"C {escape(text.replace('_', ' '))}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_python(text='is cool'):
    ''' returns a message when /python is called '''
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    ''' display n is a number if it is integer '''
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def render_odd_or_even(n):
    """
    display a HTML page only if n is an integer and\
        indicate whether it is odd or even
    """
    if n % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           odd_or_even=odd_or_even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
