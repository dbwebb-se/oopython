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


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    import traceback
    return render_template("500.html", error=traceback.format_exc())


if __name__ == "__main__":
    app.run()
