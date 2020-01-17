#!/usr/bin/env python3
"""A Car class"""
import json

class Car():

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

    @classmethod
    def create_from_json(cls, filename):
        """
        Read data from json file. Create objekt with data and return it.
        Called a factory method
        """
        data = json.load(open(filename))
        return cls(data["model"], data["year"], data["color"])
