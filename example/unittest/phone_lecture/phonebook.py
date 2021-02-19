"""
Class for phonebook file
"""
class PhoneBook():
    """
    Phonebook class
    """
    def __init__(self):
        self._contacts = []

    @property
    def contacts(self):
        """
        property for contacts
        """
        return self._contacts

    def has_contacts(self):
        """ Returns True if phonebook has contacts, else False """
        return bool(self._contacts)

    def get_contacts_length(self):
        """ Returns amount of contacts """
        return len(self._contacts)


    def add_contact(self, name, number):
        """ Add contact to phonebook """
        if self.validate_number(number):
            self._contacts.append((name, number))
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
        for person in self._contacts:
            if person[0] == name:
                return person
        raise ValueError("No contact with name {}".format(name))
