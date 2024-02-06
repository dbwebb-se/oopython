"""
Main file for bank application
"""
import re
import os
import traceback
from flask import Flask, render_template, request, redirect, url_for, session
from src.owner import Owner
from src.account import Account
from src.bank import Bank

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))


@app.route("/")
def main():
    """
    Main route
    """
    return render_template("index.html")

@app.route("/init")
def initialize():
    """
    Main route
    """
    andreas = Owner("andreas", "7894789", "bth")
    a1 = Account(1000, "spar", andreas.get_ssn())
    a2 = Account(100022, "ränta", andreas.get_ssn())
    a3 = Account(10033330, "löning", andreas.get_ssn())
    andreas.accounts.extend([a1, a2, a3])

    bank = Bank({
        "accounts": [a1.to_dict(), a2.to_dict(), a3.to_dict()],
        "owners": [andreas.to_dict()]
    })

    session["bank"] = bank.to_dict()

    return redirect(url_for("show_bank"))

@app.route("/bank")
def show_bank():
    """
    Show bank information
    """
    bank = Bank(session["bank"])
    print(bank)

    return render_template("show_bank.html", bank=bank)

@app.route("/add-owner", methods=["POST"])
def add_owner():
    print(request.form)

    bank = Bank(session["bank"])
    bank.owners.append(Owner(
        request.form["name"], request.form["ssn"], request.form["adress"])
    )

    session["bank"] = bank.to_dict()
    return redirect(url_for("show_bank"))


@app.route("/add-account", methods=["POST"])
def add_account():
    bank = Bank(session["bank"])
    account = Account(float(request.form["amount"]), request.form["name"], request.form["owner"])

    bank.accounts.append(account)

    session["bank"] = bank.to_dict()
    return redirect(url_for("show_bank"))

@app.route("/reset")
def reset():
    """ Route for reset session """
    _ = [session.pop(key) for key in list(session.keys())]

    return redirect(url_for('main'))

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
