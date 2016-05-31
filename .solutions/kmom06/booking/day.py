#!/usr/bin/env python3

"""
Day class file
"""

class Day():
    """
    Class Day
    """
    def __init__(self, number):
        self.booked = False
        self.number = number
        self.match = object()

    def is_booked(self):
        """
        Returns self.booked boolean
        """
        return self.booked

    def book(self, new_match):
        """
        Mark day as booked
        """
        self.booked = True
        self.match = new_match

    def unbook(self):
        """
        Unmark day as booked
        """
        self.booked = False
        self.match = object()

    def __str__(self):
        printed_day = str(self.number) + ". Booked: " + str(self.booked)

        if self.booked:
            printed_day += "\nMatch: " + str(self.match)

        return printed_day
