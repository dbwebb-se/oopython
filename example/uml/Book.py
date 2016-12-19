#!/usr/bin/env python3
"""
Book class
"""
from random import randint

class Book:
    """
    Represents a book
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def should_register(self):
        """
        Returns wheter it is OK or not to add Book to the registry
        """
        okToRegister = randint(0, 1)

        return okToRegister
        
    def __str__(self):
        """
        Overriding str function for class
        """
        return "{} written by {}".format(self.title, self.author)
