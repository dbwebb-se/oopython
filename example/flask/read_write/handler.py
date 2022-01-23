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
    filename = "static/data/data.json"

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
                                       form["lastname"], form["salary"],
                                       form["hired"]))

    def get_employees(self):
        """
        Return employees
        """
        return self.employees

    def read_data(self):
        """Read data from json file to init handler"""
        with open(Handler.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.employees = []

        if data:
            for empl in data["employees"]:
                self.employees.append(Employee(empl["fname"],
                                               empl["lname"], empl["salary"],
                                               empl["hired"], empl["iid"]))

    def write_data(self):
        """Transform all data to json object and write to file"""
        data = {"employees": []}
        for empl in self.employees:
            data["employees"].append(empl.to_dict())

        with open(Handler.filename, "w", encoding="utf-8") as f:
            json.dump(data, f)
