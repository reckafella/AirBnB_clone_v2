#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models.state import State
from models import storage
from os import environ
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """display states and cities in alphabetical order"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)

    cities_in_state = []
    for state in states:
        cities_in_state.append([state,
            sorted(state.cities, key=lambda k: k.name)])

    return render_template('8-cities_by_states.html',
            states=cities_in_state, H_1="States")


@app.teardown_appcontext
def close_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
