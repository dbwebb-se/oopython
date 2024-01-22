"""
Main file for bank application
"""
import traceback
from flask import Flask, render_template
from src.owner import Owner
from src.account import Account

app = Flask(__name__)


@app.route("/")
def main():
    """
    Main route
    """
    return render_template("index.html")


@app.route("/bank")
def show_bank():
    """
    Show bank information
    """
    andreas = Owner("andreas", "7894789", "bth")
    a1 = Account(1000, "spar", andreas)
    a2 = Account(100022, "ränta", andreas)
    a3 = Account(10033330, "löning", andreas)
    andreas.accounts.extend([a1, a2, a3])

    return render_template("show_bank.html", owner=andreas)


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    # pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    # pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run(debug=True)
