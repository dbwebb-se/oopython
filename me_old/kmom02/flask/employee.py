#!/usr/bin/env python3
"""
Class file for Employee
"""
import random

class Employee():
    """
    Class for Employee
    """

    def __init__(self, firstname, lastname, salary, id_number=None):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.id_number = id_number if id_number else random.sample(range(10), 4)

    def to_json(self):
        """
        Convert data from instance to dict
        """
        return {
            "fname": self.firstname,
            "lname": self.lastname,
            "salary": self.salary,
            "id": self.id_number,
        }
    # factory method
    @classmethod
    def from_json(cls, json):
        """
        Create instance from dict
        """
        return cls(json["fname"], json["lname"], json["salary"], json["id"])

    def get_salary(self):
        """
        Returns the salary
        """
        return self.salary

    def get_id(self):
        """
        Returns the employement id
        """
        return "".join(map(str, self.id_number))

    def get_name(self):
        """
        Returns name
        """
        return self.firstname + " " + self.lastname
