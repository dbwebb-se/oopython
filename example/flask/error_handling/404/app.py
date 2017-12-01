#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    """ Main route """
    test1 = 2 + "3" #Raises Internal server error 500
    return render_template("index.html", test=test1)



@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    return render_template("404.html")



if __name__ == "__main__":
    app.run()
