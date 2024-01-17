"""
Example of object oriented code
"""
class Employee():
    """
    Employee
    """
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def change_salary(self, amt):
        """
        Set salary for an employee
        """
        self._salary += amt

    def description(self):
        """
        Return string representing object
        """
        return f"{self.name} makes {self._salary}"

if __name__ == "__main__":
    employees = [
        Employee("Bob", 100000.0),
        Employee("Jane", 125000.0)
    ]

    for emp in employees:
        emp.change_salary(10000)

    for emp in employees:
        print(emp.description())
