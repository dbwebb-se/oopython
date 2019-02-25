#!/usr/bin/env python3
"""
Handler file
"""
from shapes import Square, Circle, Triangle

shapes = []

def add_shape(form):
    """ lägg till shape"""
    if form.get("shapes") == "triangle":
        new_shape = Triangle(form)
        if new_shape.validate():
            new_shape.border_top = str(new_shape.height) +\
                                 "px solid " + new_shape.color
            new_shape.border_right = str(new_shape.width) +\
                                     "px solid transparent"
            new_shape.color = "transparent"
            shapes.append(new_shape)
            return True
        return False

    elif form.get("shapes") == "square":
        new_shape = Square(form)
        if new_shape.validate():
            shapes.append(new_shape)
            return True
        return False

    elif form.get("shapes") == "circle":
        new_shape = Circle(form)
        if new_shape.validate():
            shapes.append(new_shape)
            return True
        return False

def get_shapes():
    """returnera alla shapes"""
    return shapes
