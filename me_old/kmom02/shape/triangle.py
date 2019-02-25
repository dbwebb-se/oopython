#!/usr/bin/env python3
"""
Class file for Triangle subclass
"""

from shape import Shape

class Triangle(Shape):
    """
    Class Triangle
    """
    def __init__(self, width, height, pos_left, pos_top, color):
        """
        init method
        """
        super(Triangle, self).__init__(width, height, pos_left, pos_top, color)

    def get_tri_width(self):
        """
        Returns width, overloaded from Shape
        """
        new_width = float(self.width) / 2
        return str(new_width) + "px"

    def get_area(self):
        """
        Overloaded from base, returns area
        """
        area = (float(self.width) * float(self.height)) / 2
        return area

    def validate(self):
        """
        Overloaded from base, returns True if valid, else False
        """
        return True
