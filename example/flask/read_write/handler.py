#!/usr/bin/env python3
"""
Handler file
"""

import json
from employee import Employee

class Handler:
    """
    Handler class
    """
    filename = "data.json"

    def __init__(self):
        """ Constructor
        Populates list with data from file
        """
        self.employees = []
        self.read_data()

    def add_employee(self, form):
        """
        Create and add Employee object from form
        """
        self.employees.append(Employee(form["firstname"],
                                       form["lastname"], form["salary"]))

    def get_employees(self):
        """
        Return employees
        """
        return self.employees

    def read_data(self):
        """Read data from json file to init handler"""
        with open(Handler.filename, "r") as f:
            data = json.load(f)
        self.employees = []

        if data:
            for empl in data:
                self.employees.append(Employee(empl["fname"],
                                               empl["lname"], empl["salary"],
                                               empl["iid"]))

    def write_data(self):
        """Transform all data to json object and write to file"""
        data = []
        for empl in self.employees:
            data.append(empl.to_dict())

        with open(Handler.filename, "w") as f:
            json.dump(data, f)
