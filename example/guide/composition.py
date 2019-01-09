#!/usr/bin/env python3
"""
Example of composition
"""
class Date():
    """
    Class representing a Date
    """
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return "{year}-{month}-{day}".format(
            year=self.year,
            month=self.month,
            day=self.day,
        )

class Person:
    """
    Class representing a Person
    """
    def __init__(self, name, year, month, day):
        self.name = name
        self.date_of_birth = Date(year, month, day)

    def __repr__(self):
        return "My name is {name} and my date of birth is {date}".format(
            name=self.name,
            date=self.date_of_birth,
        )

pers = Person("James", 1993, 5, 14)
print(pers)
print(pers.date_of_birth)
person2 = Person("Klara", 2010, 3, 15)
print(person2)
print(person2.date_of_birth)
