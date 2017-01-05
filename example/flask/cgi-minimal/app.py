#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application
"""

from flask import Flask

app = Flask(__name__)

# Make it easier to debug
app.debug = True
app.config.update(
    PROPAGATE_EXCEPTIONS = True
)

@app.route("/")
def home():
    """ Home route """
    return("<h1>Hello World of Flask</h1><p>Rockn Roll...")


if __name__ == "__main__":
    app.run()
