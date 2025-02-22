#!/usr/bin/python3
'''
Module to run the Flask web app on 0.0.0.0:5000 and print "Hello HBNB!"
'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
