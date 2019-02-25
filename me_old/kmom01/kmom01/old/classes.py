
class BankAccount():

    interest = 0.02

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        return self.balance
    def deposit(self, amount):
        self.balance += amount

    @staticmethod
    def test_interest(amount):
        return BankAccount.interest * amount

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        else:
            return self.balance + other

    def __iadd__(self, other):
        if isinstance(other, BankAccount):
            self.balance += other.balance
        else:
            self.balance += other
        return self
