from flask import Flask, render_template, request

app = Flask(__name__)
bank = AccountManager()

@app.route("/add/<string:what>", methods=["POST", "GET"])
def add(what):
    """
    Route to add accounts or persons
    """

    return render_template(
        "add.html",
        what=what,
        account_types=[{}]
    )

@app.route("/connect", methods=["POST", "GET"])
def connect():
    """
    Route to connect a person to an account
    """

    return render_template("connect.html")
