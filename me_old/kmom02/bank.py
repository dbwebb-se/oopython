
class BankAccount():
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

class CheckingAccount(BankAccount):
    NUM_FREE = 3
    TRANS_FREE = 50
    
    def __init__(self, name, starting_balance):
        super().__init__(name, starting_balance)
        self._transaction_count = 0
    def withdraw(self, amount):
        self._transaction_count += 1
        if self._transaction_count > self.NUM_FREE:
            self._balance -= self.TRANS_FREE
        super().withdraw(amount)
            

class Bank():
    def __init__(self, name):
        self._accounts = []
        self.name = name

    def start_bank(self):
        print("Välkommen till {}".format(self.name))
        while True:
            alt = input("""
                  1. Lägg till konto
                  2. Ta ut pengar
                  2. Sätt in pengar
                  """)
            if alt == 1:
                self.create_account()

    def create_account(self):
        info = input("Enter name and balance").split(" ")
        
if __name__ == "__main__":
    my_bank = Bank("Andreas lagliga bank")
    my_bank.start_bank()