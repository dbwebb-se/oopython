#!/usr/bin/env python3
"""
Owner class
"""

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
