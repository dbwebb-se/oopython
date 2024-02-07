#!/usr/bin/env python3
"""
Class for testing the Owner class with mock
"""
import unittest
from unittest import mock

from src.owner import Owner
from src.empty_list_exception import EmptyAccountListException
from src.account import Account

class TestOwnerMagicMock(unittest.TestCase):
    """ 
    Test class. Testcases with Magic mock.
    """

    def test_owner1_ssn_ok(self):
        """ Test that account number is set """
        m = mock.MagicMock()
        m.get_ssn.return_value = "933838339"
        self.assertEqual(m.get_ssn(), "933838339", "Ssn should be 933838339")

    def test_owner1_number_of_accounts_ok(self):
        """ Test that account number is set """
        m = mock.MagicMock()
        a = mock.MagicMock()
        m.get_accounts.return_value = [a, a, a, a, a, a]
        self.assertEqual(len(m.get_accounts()), 6, "Should be 6 accounts")

    def test_owner1_account_numbers_magic_ok(self):
        """ Test that account number is set """
        owner1 = Owner("Andreas", "933838339", "BTH")
        a1 = mock.MagicMock(number=7133616)
        a2 = mock.MagicMock(number=7777777)
        owner1.accounts.extend([a1, a2])
        self.assertEqual(owner1.get_accounts()[0].number, 7133616)
        self.assertEqual(owner1.get_accounts()[1].number, 7777777)

    def test_owner2_magic_EmptyAccountListException(self):
        """ Test that account number is set """
        m = mock.MagicMock()
        m.get_accounts.side_effect = EmptyAccountListException
        with self.assertRaises(EmptyAccountListException) as _:
            m.get_accounts()
            