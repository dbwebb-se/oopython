#!/usr/bin/env python3
"""
Flask test in python
"""

from flask import Flask, render_template
from car import Car

app = Flask(__name__)

# Make it easier to debug
app.debug = True
app.config.update(
    PROPAGATE_EXCEPTIONS = True
)

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



if __name__ == "__main__":
    app.run()
