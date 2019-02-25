from classes import BankAccount, CheckingAccount
class Bank():
    def __init__(self):
        self.accounts = []
        self.add_default_accounts()

    @staticmethod
    def create_account(form):
        if form["type"] == "bank":
            return BankAccount(form["name"], form["balance"])

        return CheckingAccount(form["name"], form["balance"])

    def add_account(self, account):
        self.accounts.append(account)

    def add_default_accounts(self):
        self.accounts.append(BankAccount("Aktiespar", 100000))
        self.accounts.append(CheckingAccount("Matkonto", 3000))
        self.accounts.append(BankAccount("Pensionskonto", 200000))
        self.accounts.append(CheckingAccount("Teknink", 50000))