#!/usr/bin/env python3

"""
Main object
"""

class Data:
    """
    Data class
    """
    title = ""
    owner = "OOPython"
    images = ["static/snake.png"]
    links = [
        ("Hem", "/"),
        ("Redovisning", "/reports"),
        ("Om", "/about"),
        ("Cars", "/cars")
    ]

    def __init__(self, title):
        self.title = title
