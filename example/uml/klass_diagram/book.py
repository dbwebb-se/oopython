#!/usr/bin/env python3
"""
Book and Chapter class
"""

class Book:
    """
    Represents a book
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.chapters = []

    def to_string(self):
        """
        Return string with details about book
        """

    def number_of_pages(self):
        """
        Return number of pages
        """

    def create_chapter(self, title, number, nr_pages):
        """
        Create a chapter for the book
        """

class Chapter:
    """
    Represents a chapter
    """
    def __init__(self, title, number_of_pages, chapter_number):
        self.title = title
        self.number_of_pages = number_of_pages
        self.chapter_number = chapter_number
