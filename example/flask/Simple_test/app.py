#!/usr/bin/env python3
"""
Flask test in python
"""

from flask import Flask, render_template
from car import Car

app = Flask(__name__)

volvo = Car("volvo", 1998, "green")
test = volvo.make_sound()


@app.route("/")
def home():
    """ Home route """
    return render_template("index.html", test444=test)


@app.route('/about')
def about():
    """ About route """
    return render_template('about.html')


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    import traceback
    return "<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
