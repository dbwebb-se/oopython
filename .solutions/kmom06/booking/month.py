#!/usr/bin/env python3

"""
Month class file
"""

from day import Day

class Month():
    """
    Class Month
    """
    def __init__(self, name):
        self.name = name
        self.days_in_month = []

    def fill_month(self, amount_of_days):
        """
        Fills month with days
        """
        for i in range(amount_of_days):
            self.days_in_month.append(Day(i+1))

    def get_day(self, day_nr):
        """
        Returns day object on day_nr in list
        """
        return self.days_in_month[day_nr-1]

    def get_nr_of_days(self):
        """
        Returns the number of days in the month
        """
        return len(self.days_in_month)

    def __str__(self):
        return self.name + ": " + str(len(self.days_in_month))
