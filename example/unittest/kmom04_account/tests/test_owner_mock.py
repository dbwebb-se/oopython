#!/usr/bin/env python3
"""
Class for testing the Owner class with mock
"""
import unittest
from unittest import mock

from src.owner import Owner
from src.empty_list_exception import EmptyAccountListException
from src.account import Account

class TestOwnerMock(unittest.TestCase):
    """ 
    Test class. Testcases with Mock, use self.owner1 and self.owner2 in setup.
    """

    def setUp(self):
        self.owner1 = mock.Mock()
        self.owner1.name = "Andreas"
        self.owner1.address = "BTH"
        self.owner1.side_effect = ["933838339", 2] # SSN and number of accounts
        self.owner2 = mock.Mock()
        self.owner2.name = "Marie"
        self.owner2.address = "BTH"
        self.owner2.get_accounts = self.raise_exception 
    
    def test_owner1_ok(self):
        """ Test owner 1, that the data is correct """
        self.assertEqual(self.owner1.name, "Andreas", "Name should be Andreas") # Assert
        self.assertEqual(self.owner1(), "933838339", "SSN should be 933838339") # Assert
        self.assertEqual(self.owner1.address, "BTH", "Address should be BTH") # Assert
        self.assertEqual(self.owner1(), 2, "No of accounts should be 2") # Assert

    def test_owner2_name_address_ok(self):
        """ Test owner 2, that the data is correct """
        self.assertEqual(self.owner2.name, "Marie", "Name should be Marie") # Assert
        self.assertEqual(self.owner1.address, "BTH", "Address should be BTH") # Assert

    def test_owner2_EmptyAccountListException(self):
        """ Test that owner2 gets EmptyAccountListException since no accounts """
        with self.assertRaises(EmptyAccountListException) as _:
            self.owner2.get_accounts()