#!/usr/bin/env python3
"""
Class file for Square subclass
"""

from shape import Shape

class Square(Shape):
    """
    Class Aquare
    """
    def __init__(self, width, height, pos_left, pos_top, bgcolor):
        """
        init method
        """
        super(Square, self).__init__(width, height, pos_left, pos_top, bgcolor)


    def get_area(self):
        """
        Overloaded from base, returns area
        """
        return float(self.width) * float(self.height)

    # def get_h_w(self):
    #     """
    #     Overloaded from base, returns height and width
    #     """
    #     return "height: "

    def validate(self):
        """
        Overloaded from base, returns True if valid, else False
        """
        return self.width == self.height
