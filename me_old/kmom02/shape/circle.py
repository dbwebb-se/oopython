#!/usr/bin/env python3
"""
Class file for circle subclass
"""

import math
from shape import Shape

class Circle(Shape):
    """
    Class Circle
    """
    def __init__(self, width, height, pos_left, pos_top, bgcolor):
        """
        init method
        """
        super(Circle, self).__init__(width, height, pos_left, pos_top, bgcolor)


    def get_area(self):
        """
        Overloaded from base, returns area
        """
        radius = int(self.width) / 2
        return round(radius**2 * math.pi, 2)

    def validate(self):
        """
        Overloaded from base, returns True if valid, else False
        """
        return self.width == self.height
