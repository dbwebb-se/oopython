from flask import Flask, render_template
from classes import BankAccount
app = Flask(__name__)

account = BankAccount(1000000, "Aktier")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/bankaccount")
def show_bank_account():
    return render_template("bank_account.html", acc=account)

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
