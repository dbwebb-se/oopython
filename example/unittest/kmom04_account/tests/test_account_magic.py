#!/usr/bin/env python3
"""
Class for testing the Account class
"""
import unittest

from src.account import Account

class TestAccountMagic(unittest.TestCase):
    """ Test class"""

    def test_add_with_string_ok(self):
        """ Test that account name is extended with vt23 """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        new_name = my_account + " vt23" # Act
        self.assertEqual(new_name, "studiemedel vt23") # Assert
        self.assertIn("vt23", new_name)

    def test_add_with_integer_ok(self):
        """ Test that account balance is increased 500 """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        new_balance = my_account + 500 # Act
        self.assertEqual(new_balance, 10500) # Assert

    def test_add_with_object_ok(self):
        """ Test that account balance is increased 500 """
        my_account = Account(10000, "studiemedel", "Marie") # Arrange
        bonus = Account(500, "bonus", "Marie") # Arrange
        new_balance = my_account + bonus # Act
        self.assertEqual(new_balance, 10500) # Assert