#!/usr/bin/env python3
"""
Class for testing the Account class
"""
import unittest
import random

from src.account import Account

class TestAccount(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        random.seed("account")
    
    def test_create_account_owner_ok(self):
        """ Test owner """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        test_owner = my_account.owner # Act
        self.assertEqual(test_owner, "Marie", "Owner should be Marie") # Assert

    def test_create_account_ok(self):
        """ Test that instance is Account """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        self.assertIsInstance(my_account, Account, "Instance should be Account") # Assert

    def test_create_account_number_ok(self):
        """ Test that account number is set """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        self.assertNotEqual(my_account.number, 0, "Number should not be 0") # Assert
        self.assertEqual(my_account.number, 7133616, "Number should be 7133616") # Assert

    def test_create_2_accounts_number_ok(self):
        """ Test that second account number not is the same as first """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        my_charity = Account(500, "välgörenhet", "Marie") # Arrange
        self.assertNotEqual(my_charity.number, 7133616, "Number should not be 7133616") # Assert

    def test_account_balance_ok(self):
        """ Test that account balance is set """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        self.assertEqual(my_account.get_balance(), 10000, "Balance should be 10000") # Assert

    def test_account_withdraw_ok(self):
        """ Test that withdraw works """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        res = my_account.withdraw(500)
        self.assertTrue(res, "Withdraw is ok, res should be true")
        self.assertEqual(my_account.get_balance(), 9500, "Balance should be 9500") # Assert

    def test_account_withdraw_not_ok(self):
        """ Test that withdraw not works, not enough on account """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        res = my_account.withdraw(50000) # Act
        self.assertFalse(res, "Withdraw is not ok, res should be false")
        self.assertEqual(my_account.get_balance(), 10000, "Balance should be 10000") # Assert
