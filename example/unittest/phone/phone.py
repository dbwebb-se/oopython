#!/usr/bin/env python3

"""
Main object file
"""

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
        self._phonebook = []

    def has_contacts(self):
        """ Returns True if phonebook has contacts, else False """
        return bool(self._phonebook)

    def get_contacts_length(self):
        """ Returns amount of contacts """
        return len(self._phonebook)

    def add_contact(self, name, number):
        """ Add contact to phonebook """
        if self.validate_number(number):
            self._phonebook.append((name, number))
            return True

        return False

    @staticmethod
    def validate_number(number):
        """
        Validate phonenumber
        """
        if len(number) == 13 and number[3] + number[7] + number[10] == "-  ":
            n = number[4:].replace(" ", "")
            for c in n:
                if not c.isdigit():
                    return False
            return True

        return False

    def get_contact(self, name):
        """ Returns tuple with name and number """
        for person in self._phonebook:
            if person[0] == name:
                return person
        raise ValueError(f"No contact with name {name}")
