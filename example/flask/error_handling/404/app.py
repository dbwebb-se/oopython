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
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    return render_template("404.html")


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    import traceback
    return "<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
