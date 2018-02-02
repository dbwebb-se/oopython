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
        self.phonebook = []

    def get_manufacturer(self):
        """ Returns the manufacturer """
        return self.manufacturer

    def get_model(self):
        """ Returns the model """
        return self.model

    def get_os(self):
        """ Returns the os """
        return self.os

    def get_owner(self):
        """ Returns the owner """
        return self.owner

    def change_owner(self, new_owner):
        """ Changes the owner of the phone """
        self.owner = new_owner

    def has_contacts(self):
        """ Returns True if phonebook has contacts, else False """
        return True if self.phonebook else False

    def get_contacts_length(self):
        """ Returns amount of contacts """
        return len(self.phonebook)

    def add_contact(self, name, number):
        """ Add contact to phonebook """
        self.phonebook.append((name, number))

    def get_contact(self, name):
        """ Returns tuple with name and number """
        for person in self.phonebook:
            if person[0] == name:
                return person
        return False
