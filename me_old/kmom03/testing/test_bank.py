import unittest
from bank import Bank

class BankTest(unittest.TestCase):

    def test_bank(self):
        ba = Bank()
        acc = ba.create_account({"type": "bank", "name": "andreas", "balance": "1000"})
        self.assertEqual(acc.name, "andreas")

if __name__ == "__main__":
    unittest.main(verbosity=3)