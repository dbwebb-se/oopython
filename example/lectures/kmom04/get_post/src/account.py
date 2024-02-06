"""
Contain Account class
"""
import random

class Account:
    """
    Represents a bank account
    """
    interest = 1.12

    def __init__(self, amount, name, owner):
        self._balance = amount
        self.name = name
        self.owner = owner
        self.number = random.randint(1000000, 20000000)

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            data["balance"],
            data["name"],
            data["owner"]
        )
        obj.number = int(data["number"])
        return obj

    def to_dict(self):
        return {
            "balance": self._balance,
            "name": self.name,
            "owner": self.owner,
            "number": self.number
        }

    def withdraw(self, amount):
        """
        Withdraws money
        """
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def deposit(self, amount):
        """
        Deposits money
        """
        if amount > 0:
            self._balance += amount
            return True
        return False

    def transfer(self, amount, other_account):
        """
        Transfer money between accounts
        """
        if self.withdraw(amount):
            if other_account.deposit(amount):
                return True
            self.deposit(amount)
            return False
        return False

    @staticmethod
    def calc_interest(amount):
        """
        Calculate interest for amount
        """
        return Account.interest * amount

    def get_balance(self):
        """
        return balance
        """
        return self._balance

    def __add__(self, other):
        if isinstance(other, str):
            return self.name + other
        if isinstance(other, int):
            return self._balance + other
        return self._balance + other.get_balance()

    def __sub__(self, other):
        if isinstance(other, Account):
            return self._balance - other.get_balance()
        if isinstance(other, int):
            return self._balance - other
        return None

    def __iadd__(self, other):
        self._balance += other.get_balance()
        return self

if __name__ == "__main__":
    acc1 = Account(1000, "löning", "Andreas")
    acc2 = Account(100, "löning", "Kenneth")
    acc2 += acc1
    var1  = 100
    var2 = 20
    var1 += var2
    print(var1)
