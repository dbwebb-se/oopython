"""
Show code for a bank account based on UML diagram in an article.
"""

class BankAccount:
    """
    A bank account
    """
    bank_name = "Andreas Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance


    def deposit(self, amount):
        """
        Deposit amount to balance
        """
        pass

    def withdraw(self, amount):
        """
        Withdraw amount from balance
        """
        pass
