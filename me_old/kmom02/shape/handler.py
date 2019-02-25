#!/usr/bin/env python3
"""
Handler class file
"""

from employee import Employee
from square import Square
from circle import Circle
from triangle import Triangle




class Handler():
    """
    Handler class
    """
    def __init__(self):
        """
        init method
        """
        self.people = []
        self.add_predefined_employees()

        self.shapes = {
            "squares": [],
            "circles": [],
            "triangles": []
        }

    def add_employee(self, form):
        """
        Add Employee to people
        """
        f_name = form["firstname"]
        l_name = form["lastname"]
        salary = form["salary"]
        self.people.append(Employee(f_name, l_name, salary))

    def get_people(self):
        """
        Returns people list
        """
        return self.people
    
    def write_session(self, session):
        session["employees"] = [e.to_json() for e in self.people]
        print(session["employees"])
    
    def read_session(self, session):
        if session.get("employees", []):
            print(session["employees"])
            
            self.people = [Employee.from_json(e) for e in session["employees"]]

    def add_predefined_employees(self):
        emil = Employee("Emil", "Folino", 30000)
        mikael = Employee("Mikael", "Roos", 31000)
        kenneth = Employee("Kenneth", "Lewenhagen", 75000)
        andreas = Employee("Andreas", "Arnesson", 12000)

        self.people.append(emil)
        self.people.append(mikael)
        self.people.append(kenneth)
        self.people.append(andreas)


    def add_shape(self, form):
        """
        Adds shape to shapes dict
        """
        width = form["width"]
        height = form["height"]
        left = form["pos_left"]
        top = form["pos_top"]
        color = form["bgcolor"]
        validation = ""
        if form["shape_type"] == "square":
            square = Square(width, height, left, top, color)
            if square.validate():
                self.shapes["squares"].append(square)
                validation = "Added square."
            else:
                print("Not a valid square.")
                validation = "A square has equal height and width."

        if form["shape_type"] == "circle":
            circle = Circle(width, height, left, top, color)
            if circle.validate():
                self.shapes["circles"].append(circle)
                validation = "Added circle."
            else:
                validation = "A circle has equal height and width."

        if form["shape_type"] == "triangle":
            triangle = Triangle(width, height, left, top, color)
            if triangle.validate():
                self.shapes["triangles"].append(triangle)
                validation = "Added triangle."
            else:
                validation = "???"

        return validation

    def get_shapes(self):
        """
        Returns list of shapes
        """
        return self.shapes
