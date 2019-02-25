#!/usr/bin/env python3
"""
Class file for base class shape
"""

class Shape():
    """
    Class Shape
    """
    def __init__(self, width, height, pos_left, pos_top, bgcolor):
        """
        init method
        """
        self.width = width
        self.height = height
        self.pos_left = pos_left
        self.pos_top = pos_top
        self.bgcolor = bgcolor

    def get_pos(self):
        """
        Returns tuple with x, y position
        """
        return (self.pos_left, self.pos_top)

    def get_width(self):
        """
        Returns width
        """
        return str(self.width) + "px"

    def get_height(self):
        """
        Returns height
        """
        return str(self.height) + "px"

    def get_bgcolor(self):
        """
        Returns bgcolor
        """
        return self.bgcolor

    def get_area(self):
        """
        Should be overloaded
        """
        raise NotImplementedError("Subclasses should implement this!")

    def validate(self):
        """
        Should be overloaded
        """
        raise NotImplementedError("Subclasses should implement this!")
