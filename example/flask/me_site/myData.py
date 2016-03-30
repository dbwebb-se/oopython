#!/usr/bin/env python3

"""
Main object
"""

class Data:
    """
    Data class
    """
    title = ""
    owner = "Kenneth"
    images = ["static/monkey.png"]
    links = [
        ("Hem", "/"),
        ("Redovisning", "/reports"),
        ("Om", "/about")
    ]

    def __init__(self, title):
        self.title = title
