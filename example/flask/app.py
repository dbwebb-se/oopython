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
def main():
    return render_template("index.html", test444=test)

@app.route('/about')
def show_about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run()
