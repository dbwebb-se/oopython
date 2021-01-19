#!/usr/bin/env python3
"""
Class file for Employee
"""
import random
from datetime import date

class Employee():
    """
    Class for Employee
    """

    def __init__(self, firstname, lastname, salary, hired, iid=False):
        """
        init method
        """
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.hired = hired
        self.iid = iid if iid else random.sample(range(10), 4)

    def to_dict(self):
        """Transform data to a dict for saving in json file"""
        return {"fname": self.firstname, "lname": self.lastname,
                "salary": self.salary, "hired": self.hired, "iid": self.iid}

    def get_salary(self):
        """
        Returns the salary
        """
        return self.salary

    def get_id(self):
        """
        Returns the employement iid
        """
        return "".join(map(str, self.iid))

    def get_name(self):
        """
        Returns name
        """
        return self.firstname + " " + self.lastname
    
    def get_days_hired(self):
        """
        Returns the number of days an Employee
        has been hired.
        """
        today = date.today()
        hired_date_list = [int(x) for x in self.hired.split('-')]
        hired_date = date(*hired_date_list)

        difference = today - hired_date
        return difference.days
