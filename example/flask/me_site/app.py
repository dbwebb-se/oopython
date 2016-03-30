#!/usr/bin/env python3
"""
Flask test in python
"""

from flask import Flask, render_template
from myData import Data
from person import Person

app = Flask(__name__)

me = Person("Kenneth Lewenhagen", "Karlskrona", 32)
data = Data("Min me-sida")

@app.route("/")
def main():
    return render_template("index.html", data=data)

@app.route('/about')
def show_about():
    return render_template('about.html', me=me, data=data)

@app.route('/reports')
def show_reports():
    return render_template('reports.html', data=data)

if __name__ == "__main__":
    app.run()
