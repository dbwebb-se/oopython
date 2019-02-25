from classes import BankAccount, CheckingAccount
class Bank():
    def __init__(self):
        self.accounts = []
        self.add_default_accounts()

    def read_session(self, session):
        self.accounts = []
        if session.get("accounts"):
            for acc in session["accounts"]:
                self.add_account(self.create_account(acc))

    def write_session(self, session):
        session["accounts"] = []
        for acc in self.accounts:
            session["accounts"].append(acc.to_dict())
    
    def reset(self):
        self.accounts = []
        self.add_default_accounts()
    
    @staticmethod
    def create_account(form):
        if form.get("type") == "bank":
            return BankAccount(form.get("name"), form.get("balance"))

        return CheckingAccount(form.get("name"), form.get("balance"))

    def add_account(self, account):
        self.accounts.append(account)

    def add_default_accounts(self):
        self.accounts.append(BankAccount("Aktiespar", 100000))
        self.accounts.append(CheckingAccount("Matkonto", 3000))
        self.accounts.append(BankAccount("Pensionskonto", 200000))
        self.accounts.append(CheckingAccount("Teknink", 50000))