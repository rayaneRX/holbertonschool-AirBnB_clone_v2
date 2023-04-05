#!/usr/bin/python3
"""Flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def all_states():
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_handle(app):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
