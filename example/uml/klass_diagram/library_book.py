#!/usr/bin/env python3
"""
Registering book"""

class Library:
    """
    Represents a Library
    """
    def __init__(self):
        self.book_register = BookRegister()

    def register_book(self, isbn):
        """
        Register a book in BookRegister
        """
        self.book_register.register_book(isbn)

class BookRegister:
    """
    Holds books for a library
    """
    def __init__(self):
        self.books = []

    def register_book(self, isbn):
        """
        Register book
        """
        return self.books.append(isbn)
