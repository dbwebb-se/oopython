#!/usr/bin/env python3

# pylint: disable=wildcard-import, method-hidden
# pylint: disable=line-too-long
# pylint: disable=C0103

"""
Flask test in python
"""

from flask import Flask, render_template, request
from my_data import Data
from person import Person
import functions as func

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

@app.route('/cars', methods=["POST", "GET"])
def show_cars():
    if request.method == "POST":
        func.showCars()

    if request.method == "GET":
        delThisCar = request.args.get("del")
        if delThisCar != None:
            func.removeCar(delThisCar)

    return render_template('cars.html', data=data, car_table=func.fixCarTable())



if __name__ == "__main__":
    app.run()