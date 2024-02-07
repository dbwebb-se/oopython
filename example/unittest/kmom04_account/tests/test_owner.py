#!/usr/bin/env python3
"""
Class for testing the Owner class
"""
import unittest

from src.owner import Owner
from src.empty_list_exception import EmptyAccountListException
from src.account import Account

class TestOwner(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        # Owner 1 with 2 accounts
        self.owner1 = Owner("Andreas", "933838339", "BTH") # Arrange
        a1 = Account(100, "räntor", self.owner1) # Arrange
        a2 = Account(35, "aktier", self.owner1) # Arrange
        self.owner1.accounts.extend([a1, a2]) # Arrange
        # Owner 2 with 0 accounts
        self.owner2 = Owner("Marie", "999888777", "BTH") # Arrange
    
    def test_owner1_ok(self):
        """ Test owner 1, that the data is correct """
        self.assertEqual(self.owner1.name, "Andreas", "Name should be Andreas") # Assert
        self.assertEqual(self.owner1.get_ssn(), "933838339", "SSN should be 933838339") # Assert
        self.assertEqual(self.owner1.address, "BTH", "Address should be BTH") # Assert
        self.assertEqual(len(self.owner1.accounts), 2, "No of accounts should be 2") # Assert

    def test_owner2_no_accounts_ok(self):
        """ Test owner 2, number of accounts should be 0 """
        self.assertEqual(len(self.owner2.accounts), 0, "No of accounts should be 0") # Assert

    def test_owner2_EmptyAccountListException(self):
        """ Test that owner2 gets EmptyAccountListException since no accounts """
        with self.assertRaises(EmptyAccountListException) as _:
            self.owner2.get_accounts()

    def test_owner1_get_accounts_ok(self):
        """ Test that owner1 gets 2 and not EmptyAccountListException """
        self.assertEqual(len(self.owner1.get_accounts()), 2, "No of accounts should be 2") # Assert

    @unittest.skip
    def test_owner1_accounts_balance_ok(self):
        """ Test that account number is set """
        self.skipTest("Another way to skip this test")
        accounts = self.owner1.get_accounts()
        self.assertEqual(accounts[0]._balance, 100, "Number should be 100") # Assert
        self.assertEqual(accounts[1]._balance, 35, "Number should be 35") # Assert