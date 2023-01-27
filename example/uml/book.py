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

    @staticmethod
    def should_register():
        """
        Returns wheter it is OK or not to add Book to the registry
        """
        ok_to_register = randint(0, 1)

        return ok_to_register

    def __str__(self):
        """
        Overriding str function for class
        """
        return f"{self.title} written by {self.author}"
