#!/usr/bin/env python3

"""
Calendar class file
"""

from month import Month

class Calendar():
    """
    Calendar class
    """
    def __init__(self):
        self.year = 2016
        self.months = []

        months = [
            ("January", 31),
            ("February", 30),
            ("March", 31),
            ("April", 30),
            ("May", 31),
            ("June", 30),
            ("July", 31),
            ("August", 31),
            ("September", 30),
            ("October", 31),
            ("November", 30),
            ("December", 31)]

        for mon in months:
            holder = Month(mon[0])
            holder.fill_month(mon[1])
            self.months.append(holder)

    def get_month(self, get_month):
        """
        Returns the month based on integer
        """
        try:
            return self.months[get_month-1]
        except IndexError:
            print("Not in list")

    def __str__(self):
        """
        Prints all months and nr of days
        """
        month_to_string = ""
        counter = 1
        for mon in self.months:
            month_to_string += str(counter) + ". " + str(mon) + "\n"
            counter += 1
        return month_to_string

    # def empty(self):
    #     """
    #     Clears calendar
    #     """
    #     self.months = []
