
class BankAccount():
    acc_type = "bank"
    interest = 0.02

    def __init__(self, name, starting_balance):
        self.name = name
        self._balance = starting_balance

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds!")

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    @staticmethod
    def test_interest(amount):
        return amount + (amount * BankAccount.interest)
    
    def add_interest(self):
        self._balance = self.test_interest(self._balance)
    
    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self._balance + other.get_balance()
        else:
            return self._balance + other
    
    def __iadd__(self, other):
        if isinstance(other, BankAccount):
            self._balance += other.get_balance()
        else:
            self._balance += other
        return self
    
    def to_dict(self):
        return {
                "type": self.acc_type,
                "name": self.name,
                "balance": self._balance,
            }

class CheckingAccount(BankAccount):
    NUM_FREE = 3
    TRANS_FREE = 50
    acc_type = "checking"

    def __init__(self, name, starting_balance):
        super().__init__(name, starting_balance)
        self._transaction_count = 0
    def withdraw(self, amount):
        self._transaction_count += 1
        if self._transaction_count > self.NUM_FREE:
            self._balance -= self.TRANS_FREE
        super().withdraw(amount)
    def free_trans_left(self):
        return self.NUM_FREE - self._transaction_count
            