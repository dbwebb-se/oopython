"""
Contain class for a phonebook
"""
from src.contact import Contact

class Phonebook:
    """
    Phonebook class
    """
    def __init__(self):
        """
        init method
        """
        self._contacts = []

    def has_contacts(self):
        """ Returns True if phonebook has contacts, else False """
        return bool(self._contacts)


    def add_contact(self, name, number):
        """ Add contact to phonebook """
        self._contacts.append(Contact(name, number))


    def get_contact(self, name):
        """ Returns tuple with name and number """
        for person in self._contacts:
            if person.name == name:
                return person
        return None

    def get_contacts(self):
        """ return all contacts"""
        return self._contacts
