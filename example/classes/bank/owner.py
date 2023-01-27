#!/usr/bin/env python3
"""
Owner class
"""

class Owner:
    """
    Represents an owner of a bank account
    """
    def __init__(self, name, ssn, adress):
        self.name = name
        self._ssn = ssn
        self.adress = adress
        self.accounts = []

    def get_ssn(self):
        """Return private attribute """
        return self._ssn
