#!/usr/bin/env python3
"""A Car class"""

class Car(object):

    """Car class"""

    wheels = 4 # Class attribute, all cars have 4 wheels (almost)

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    @staticmethod
    def make_sound():
        """Print a car sound"""
        return "Wrooom, wroom"
