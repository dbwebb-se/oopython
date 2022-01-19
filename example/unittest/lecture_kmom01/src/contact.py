"""
Contain class for a contact
"""
import random

class Contact():
    """
    A phone contact
    """
    def __init__(self, name, number=None):
        """
        Constructor
        """
        if number is None or not self.is_number_valid(number):
            self.number = self.create_number()
        else:
            self.number = number
        self.name = name


    @staticmethod
    def create_number():
        """
        Create number with format "xxx-xxx xx xx"
        """
        numbers = str(random.randint(1000000000, 9999999999))
        return f"{numbers[:3]}-{numbers[3:6]} {numbers[6:8]} {numbers[8:]}"


    @staticmethod
    def is_number_valid(number):
        """
        Validate phonenumber
        format "xxx-xxx xx xx"
        """
        if len(number) == 13 and number[3] + number[7] + number[10] == "-  ":
            n = number.replace(" ", "").replace("-", "")
            for c in n:
                if not c.isdigit():
                    return False
            return True
        return False

    def __str__(self):
        return f"Name: {self.name}\nNumber: {self.number}"
