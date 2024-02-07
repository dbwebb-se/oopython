#!/usr/bin/env python3
"""
Class for testing the Owner class with mock
"""
import unittest
from unittest import mock

from src.owner import Owner
from src.empty_list_exception import EmptyAccountListException
from src.account import Account

class TestOwnerMock2(unittest.TestCase):
    """ 
    Test class. Testcases with Mock, create owners within the testcases
    """

    def test_owner1_1_account_number_ok(self):
        """ Test that account number is set """
        owner1 = Owner("Andreas", "933838339", "BTH")# Arrange
        with mock.patch.object(random, 'randint') as rand_mock:
            rand_mock.return_value = 7133616
            a1 = Account(100, "räntor", self.owner1) # Arrange
            a2 = Account(35, "aktier", self.owner1) # Arrange
            owner1.accounts.extend([a1, a2]) # Arrange
        accounts = owner1.get_accounts()
        self.assertEqual(accounts[0].number, 7133616)
        self.assertEqual(accounts[1].number, 7133616)
        
    def test_owner1_2_account_number_ok(self):
        """ Test that account number is set """
        owner1 = Owner("Andreas", "933838339", "BTH")# Arrange
        with mock.patch.object(random, 'randint') as rand_mock:
            rand_mock.side_effect = [7133616, 7777777]
            a1 = Account(100, "räntor", self.owner1) # Arrange
            a2 = Account(35, "aktier", self.owner1) # Arrange
            owner1.accounts.extend([a1, a2]) # Arrange
        accounts = owner1.get_accounts()
        self.assertEqual(accounts[0].number, 7133616)
        self.assertNotEqual(accounts[1].number, 7133616)
        self.assertEqual(accounts[1].number, 7777777)

