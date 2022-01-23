#!/usr/bin/env python3
"""
Flask test in python
"""
import traceback
from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    """ Home route """
    return render_template("index.html")

@app.route("/execute/<path:path>")
def execute(path):
    """ Route for showing interpreter """
    return render_template("execute.html", code_path=path)

@app.route('/code/<path:path>')
def code(path):
    """
    Route for returning python files that brython looks for when import is done in interpreter
    """
    print(path)
    return send_from_directory('code', path)




@app.errorhandler(500)
def internal_server_error(_):
    """
    Handler for internal server error 500
    """
    return "<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
