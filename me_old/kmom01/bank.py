
class BankAccount():
    interest = 0.02

    def __init__(self, name, starting_balance):
        self.name = name
        self.balance = starting_balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def deposit(self, amount):
        self.balance += amount

    @staticmethod
    def test_interest(amount):
        return amount + (amount * BankAccount.interest)
    
    def add_interest(self):
        self.balance = self.test_interest(self.balance)
    
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

def main():
    my_account = BankAccount("My savings", 10000)
    other_account = BankAccount("Pension fund", 50000)
    
    my_account += other_account
    # my_account = my_account.__iadd__(other_account)
    print(type(my_account))
    print(my_account.balance)
    # 
    # print(my_account.name)
    # print(my_account.balance)
    # print(my_account.interest)
    # 
    # print(other_account.name)
    # print(other_account.balance)
    # print(other_account.interest)




if __name__ == "__main__":
    main()