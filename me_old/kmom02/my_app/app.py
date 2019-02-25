import os
import re
from flask import Flask, request, render_template, session, redirect, url_for
from bank import Bank
app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

bank = Bank()

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/bankaccounts")
def show_bank_account():
    bank.read_session(session)
    return render_template("show_bank_accounts.html", accounts=bank.accounts)

@app.route("/add_account",  methods=["POST", "GET"])
def add_account():
    if request.method == "POST":
        bank.add_account(bank.create_account(request.form))
        bank.write_session(session)

    return render_template("add_account.html")

@app.route("/reset")
def reset():
    """ Reset questions """
    bank.reset()
    bank.write_session(session)
    return redirect(url_for('main'))

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
    app.run(debug=True)
