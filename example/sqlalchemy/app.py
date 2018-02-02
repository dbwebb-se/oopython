#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
A Flask app using SQLAlchemy to read a SQLite database.
"""

from flask import Flask, render_template
import functions


app = Flask(__name__)

# functions.add_to_db("Svenne", 67)
persons = functions.get_all_as_list()


@app.route("/")
def main():
    """ Main route """
    return render_template("index.html", persons=persons)


@app.errorhandler(500)
def internal_server_error(_):
    """
    Handler for internal server error 500
    """
    import traceback
    return "<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
