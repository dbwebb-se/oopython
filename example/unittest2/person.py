#!/usr/bin/env python3

"""
Main object to make tests on
"""

class Person:
    """
    Person class
    """
    race = "human"
    alive = True

    def __init__(self, name, born, age):
        self.name = name
        self.born = born
        self.age = age
        self.interests = []

    def add_interest(self, interest):
        """ adds interests """
        self.interests.append(interest)

    def get_interests(self):
        """ returns interests as a list """
        return self.interests

    def get_interests_as_string(self):
        """ returns interests as a comma separated string """
        return ", ".join(self.interests)

    def presentation(self):
        """ returns a presentation """
        return "My name is {name}. I am born in {b}, {age} years ago" \
                ".".format(name=self.name, b=self.born, age=self.age)

    def is_alive(self):
        return self.alive
