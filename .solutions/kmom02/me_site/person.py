#!/usr/bin/env python3

"""
Main object
"""

class Person:
    """
    Person class
    """
    race = "human"
    alive = True

    def __init__(self, name, live_in, age):
        self.name = name
        self.live_in = live_in
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
        return "Jag heter {name}. Jag bor i {b}, och är {age} år gammal" \
                ".".format(name=self.name, b=self.live_in, age=self.age)

    def is_alive(self):
        """ checks if the person is alive, testing boolean """
        return self.alive
