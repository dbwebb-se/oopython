#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pylint: disable=import-outside-toplevel

"""
Minimal Flask application, including useful error handlers.
"""

import traceback
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """ Home route """
    return "<h1>Hello World of Flask</h1><p>Rockn Roll..."


@app.errorhandler(404)
def page_not_found(_):
    """
    Handler for page not found 404
    """
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(_):
    """
    Handler for internal server error 500
    """
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
