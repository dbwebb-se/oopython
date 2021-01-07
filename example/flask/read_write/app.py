#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pylint: disable=import-outside-toplevel


"""
My first Flask app
"""

from flask import Flask, render_template, request
from handler import Handler

app = Flask(__name__)

handler = Handler()

@app.route("/", methods=["POST", "GET"])
def main():
    """ Company route """

    if request.method == "POST":
        handler.add_employee(request.form)
        handler.write_data()

    return render_template("company.html")

@app.route("/showemployees", methods=["GET"])
def showemployees():
    """ showshapes route """
    handler.read_data()
    return render_template("show.html", empls=handler.get_employees())

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True)
