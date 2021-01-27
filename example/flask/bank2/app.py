#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Example for bank 2.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/add/<string:what>", methods=["POST", "GET"])
def add(what):
    """
    Route to add accounts or persons
    - /add/person  returns a create form for the class Person
    - /add/account returns a create form for the Account classes
    """

    return render_template(
        "add.html",
        what=what
    )

@app.route("/connect", methods=["POST", "GET"])
def connect():
    """
    Route to connect a person to an account
    """

    return render_template("connect.html")
