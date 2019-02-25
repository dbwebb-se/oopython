#!/usr/bin/env python3
"""
basklass, Shape, och skapa subklasserna Square, Circle och Triangle.
get_area() och validate()
"""
import math

class Shape(object):
    """docstring for Shape."""
    def __init__(self, form):
        self.form = form
        self.height = form.get("height")
        self.width = form.get("width")
        self.left = form.get("left")
        self.top = form.get("top")
        self.color = form.get("colors")
        self.shape_type = form.get("shapes")
        self.border_top = 0
        self.border_right = 0

    def get_area(self):
        """must be implemented in Subclasses"""
        raise NotImplementedError("Subclasses should implement this!")
    def validate(self):
        """must be implemented"""
        raise NotImplementedError("Subclasses should implement this!")



class Square(Shape):
    """docstring for Square."""
    def get_area(self):
        return int(self.height)*int(self.width)
    def validate(self):
        return bool(self.height == self.width)

class Circle(Shape):
    """docstring for Circle."""
    def get_area(self):
        return round((int(self.height)/2)*(int(self.height)/2)*math.pi, 4)
    def validate(self):
        return bool(self.height == self.width)


class Triangle(Shape):
    """docstring for Triangle."""
    def get_area(self):
        return (int(self.height)*int(self.width))/2
    def validate(self):
        return True
