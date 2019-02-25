from flask import Flask, render_template
from classes import BankAccount
app = Flask(__name__)

my_account = BankAccount(100000, "Aktier")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/bankaccount")
def bank_account():
    return render_template("bank_account.html", account=my_account)

if __name__ == "__main__":
    app.run(debug=True)
