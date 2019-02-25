#!/usr/bin/env python3
"""
My first Flask app
"""

# Importera relevanta moduler
import os
import re
from flask import Flask, render_template, request, session
from handler import Handler

app = Flask(__name__)
app.secret_key = re.sub("[^a-z\d]", "", os.path.realpath(__file__))

handler = Handler()

my_name = "Kenneth Lewenhagen"
my_course = "OOPython"


@app.route("/")
def main():
    """ Main route """
    handler.read_session(session)
    return render_template("index.html", people=handler.get_people())

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html", name=my_name, course=my_course)

@app.route("/company", methods=["POST", "GET"])
def company():
    """ Company route """

    if request.method == "POST":
        handler.add_employee(request.form)
        handler.write_session(session)
        

    return render_template("company.html", persons=handler.get_people())

@app.route("/reset")
def reset():
    """ Route for reset session """
    session.clear()
    return render_template("index.html", people=handler.get_people())

@app.route("/shape", methods=["POST", "GET"])
def shape():
    """ Shape route """
    message = ""
    if request.method == "POST":
        message = handler.add_shape(request.form)

    return render_template("shape.html", message=message)


@app.route("/display")
def display():
    """ Display route """

    return render_template("display.html", shapes=handler.get_shapes())

if __name__ == "__main__":
    app.run(debug=True)
    
