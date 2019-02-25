import unittest
from classes import BankAccount, CheckingAccount

class BankAccountTest(unittest.TestCase):
    
    def test_withdraw(self):
        ba = BankAccount("Bert", 100)

        ba.withdraw(50)
        self.assertEqual(ba.get_balance(), 50)


class CheckingAccountTest(unittest.TestCase):
    
    def test_withdraw(self):
        ca = CheckingAccount("Bert", 100)

        ca.withdraw(50)
        self.assertEqual(ca.get_balance(), 50)


if __name__ == "__main__":
    unittest.main(verbosity=3)