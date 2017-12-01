#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """ Home route """
    return("<h1>Hello World of Flask</h1><p>Rockn Roll...")


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    import traceback
    return "<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
