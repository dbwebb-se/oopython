#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application, including useful error handlers.
"""
# pylint: skip-file
from datetime import date, timedelta
from flask import Flask, render_template, request
from account_manager import AccountManager

app = Flask(__name__)
bank = AccountManager()

@app.route("/")
def main():
    """
    Home route
    Shows a table of all accounts and their information.
    """
    return render_template("index.html", accounts=bank.accounts)



@app.route("/transfer", methods=["POST", "GET"])
def transfer():
    """
    Transaction route
    Displays a form where you can transfer balance.
    """
    message = None
    if request.method == "POST":
        bank.transfer(request.form)
        bank.save_data()
        message = "Moved ${amount} from account #{from_} to #{to}".format(
            amount=request.form["amount"],
            from_=request.form["from_account"],
            to=request.form["to_account"],
        )

    return render_template(
        "transfer.html",
        accounts=bank.accounts,
        message=message
    )

@app.route('/account/<int:account_id>', methods=["POST", "GET"])
def account(account_id):
    """
    Account route
    Takes an account id and displays its "own" page.
    """
    interests = None
    current_account = bank.get_account_by_id(account_id)
    date_ = date.today() + timedelta(days=1)

    if request.method == "POST":
        date_ = request.form["calculation_date"]
        interests = bank.calculate_interest_rate(current_account, date_)

    return render_template(
        "account.html",
        account=current_account,
        time=date_,
        interests=interests
    )

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
    #pylint: disable=unused-argument,import-outside-toplevel
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run(debug=True)
