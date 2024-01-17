"""
Example code for functional programming.
"""
employees = [
    ["Bob", 100000.0],
    ["Jane", 125000.0]
]

def change_salaries(_employees, amt):
    """
    Change salary of all employees
    """
    new_list = []
    for emp in _employees:
        new_list.append(change_salary(emp, amt))
    return new_list

def change_salary(employee, amt):
    """
    Change set salary for an employee
    """
    employee[1] += amt
    return employee

if __name__ == "__main__":
    happier_employees = change_salaries(employees, 10000)
    for _emp in happier_employees:
        print(f"{_emp[0]} makes {_emp[1]}")
