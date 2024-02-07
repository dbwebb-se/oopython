#!/usr/bin/env python3
"""
Owner class
"""

from src.empty_list_exception import EmptyAccountListException

class Owner:
    """
    Represents an owner of a bank account
    """
    def __init__(self, name, ssn, address):
        self.name = name
        self._ssn = ssn
        self.address = address
        self.accounts = []

    def get_ssn(self):
        """Return private attribute """
        return self._ssn

    def get_accounts(self):
        """" Return the list of accounts, raises an exception if no accounts """
        if not self.accounts:
            raise EmptyAccountListException
        return self.accounts