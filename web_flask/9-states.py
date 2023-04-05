#!/usr/bin/python3
"""Flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", defaults={'id' : None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def all_states(id):
    states = storage.all(State)
    if id:
        id = 'State.' + id
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown_handle(app):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)