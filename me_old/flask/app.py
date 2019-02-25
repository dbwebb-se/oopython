#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template, request
from person import Person
import handler
app = Flask(__name__)
me_objekt = Person("Christofer", "Wikman", 32, "snake.png")

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html", christofer=me_objekt)

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html")

@app.route("/redovisning")
def redovisning():
    """ Redovisning route """
    return render_template("redovisning.html")

@app.route("/createshape")
def createshape():
    """ createshape route """
    return render_template("createshape.html", badresult="")

@app.route("/showshapes", methods=["POST", "GET"])
def showshapes():
    """ showshapes route """
    if request.method == "POST":
        handler.add_shape(request.form)
    return render_template("showshapes.html", test=handler.get_shapes())
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
    app.run()
