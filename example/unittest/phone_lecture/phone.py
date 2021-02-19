#!/usr/bin/env python3

"""
Main object file
"""
from phonebook import PhoneBook
class Phone:
    """
    Phone class
    """
    def __init__(self, manufacturer, model, os):
        """
        init method
        """
        self.manufacturer = manufacturer
        self.model = model
        self.os = os
        self.owner = "No owner yet"
        self._phonebook = PhoneBook()


    def call(self):
        """
        Decide who to call
        """
        print(self._phonebook.contacts)
        contact_name = input("Enter contactname: ")
        self._make_call(contact_name)

    def _make_call(self, name):
        """
        Pretend to make an actual phonecall
        """
        contact = self._phonebook.get_contact(name)
        print("Calling number", contact, "...")
