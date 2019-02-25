#!/usr/bin/env python3
"""
Handler file
"""

from employee import Employee

class Handler():
    """
    Manager class, connection ebtween app and employee
    """
    def __init__(self):
        self.people = []
        self.add_predefined_employees()

    def write_session(self, session):
        """
        Add all employee objects to session
        """
        session["employees"] = [e.to_json() for e in self.people]

    def read_session(self, session):
        """
        Add all employee objects from session
        """
        if session.get("employees", []):
            self.people = [Employee.from_json(e) for e in session["employees"]]

    def get_people(self):
        """
        Return list with all employee objects
        """
        return self.people

    def add_employee(self, form):
        """
        Create an employee from form
        """
        empl = Employee(
            form["firstname"],
            form["lastname"],
            form["salary"]
        )
        self.people.append(empl)

    def add_predefined_employees(self):
        """
        Add default employees
        """
        emil = Employee("Emil", "Folino", 30000)
        mikael = Employee("Mikael", "Roos", 31000)
        kenneth = Employee("Kenneth", "Lewenhagen", 75000)
        andreas = Employee("Andreas", "Arnesson", 12000)

        self.people.append(emil)
        self.people.append(mikael)
        self.people.append(kenneth)
        self.people.append(andreas)
