#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application
"""

import traceback
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    """ Main route """
    #pylint: disable=unused-variable
    test1 = 2 + "3" #Raises Internal server error 500
    return "<h1>Hello World of Flask</h1><p>Rockn Roll..."


@app.errorhandler(500)
def internal_server_error(_):
    """
    Handler for internal server error 500
    """
    return "<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
