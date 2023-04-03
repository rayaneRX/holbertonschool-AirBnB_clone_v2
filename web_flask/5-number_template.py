#!/usr/bin/python3
"""Flask"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def C_text(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route("/python/<text>")
def python_text(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
