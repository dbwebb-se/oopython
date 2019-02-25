#!/usr/bin/env python3

"""
5ec7342c71641abf1e030bbeaae20c9b
oopython
lab2
v2
chai17
2018-01-25 22:55:55
v2.3.9 (2017-12-28)

Generated 2018-01-25 23:55:55 by dbwebb lab-utility v2.3.9 (2017-12-28).
https://github.com/mosbth/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - oopython
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python documentation](https://docs.python.org/3/library/index.html).
# Here you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Class relationships
#
# Practice on creating classes and relationships between them in python.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (2 points)
#
# Create a new class named **Person**.  Give the class the instance
# attributes "name" and "ssn". Make "ssn" a private attribute. The values for
# the attributes should be sent to the constructor as arguments.
# Create a *get* method for both "name" and "ssn". Only Create a *set* method
# for "name".
#
# In the code below create a new variable called **per** and set it to a new
# instance of Person. Give it the name `Hugo` and ssn `578118-6946`.
#
#
# Answer with per\'s get method for ssn.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Person:
    """docstring for Person."""
    def __init__(self, name, ssn, adress=""):
        """Init"""
        self.name = name
        self._ssn = ssn
        self.adress = adress
    def get_name(self):
        """ret namn"""
        return self.name
    def set_name(self, name):
        """sätt namn"""
        self.name = name
    def get_ssn(self):
        """ret ssn"""
        return self._ssn
    def set_adress(self, adress):
        """se addr"""
        self.adress = adress
    def to_string(self):
        """skriv ut"""
        return "Name: " + self.name + " SSN: " + self._ssn + " " + \
        Adress.to_string(self.adress)

per = Person("Hugo", "578118-6946")


ANSWER = per.get_ssn()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (2 points)
#
# Create a new class named **Address**.  Give the class the instance
# attributes "city", "state" and "country". The values for the attributes
# should be sent to the constructor as arguments.
# Create a method, in Address, called **to_string**, it should return
# `"Address: <city> <state> <country>"` (replace the \<city\> with the value
# of the attribute city...).
#
# Add the instance attribute **address** to class Person. It's value should
# be sent as argument to constructor, give it a default value of and empty
# string, `""`.
# Create a set method for attribute "address".
# Create a method, in Person, called **to_string**, it should return `"Name:
# <name> SSN: <ssn> Address: <city> <state> <country>"`. Use Address'
# to_string method to get address data.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Katar`, the state `Withywoods` and the country
# `Commonwealth`.
# Use the set method in Person to add the newly create Address object to your
# **per** object.
#
# Answer with per's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Adress:
    """docstring for Adress."""
    def __init__(self, city, state, country):
        """init"""
        self.city = city
        self.state = state
        self.country = country
    def to_string(self):
        """skriv ut"""
        return"Address: " + self.city + " " + self.state + " " + self.country


perAdress = Adress("Katar", "Withywoods", "Commonwealth")
per.set_adress(perAdress)

ANSWER = per.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (2 points)
#
# Create a new class name **Teacher** make it inherit from class "Person". In
# the constructor add the instance attribute "courses" and initiate it to and
# empty list.
# Create the method **add_course**, it should take one argument and add it to
# the course list attribute.
# Create the method **remove_course**, it should take one argument and remove
# if from the course list attribute.
# Overload the **to_string** method from the base class. It should return the
# same as the original method and add the courses to the end of the string,
# `"Name: <name> SSN: <ssn> Address: <city> <state> <country> Courses:
# <course>, <course>, ..."`. The list of courses should be comma seperated
# without one at the end. Tip, use `super(Teacher, self)` to access base
# method.
#
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Renere`, the state `Smaland` and the country `Six Duchies`.
#
# Create a new instance of the class Teacher. Initiate it with the name
# `Goliat` and ssn `502075-3392` and the aforementioned Address object.
# Use the add_course method to add the following courses, `javascript1`,
# `oophp` and `webgl`.
#
#
# Answer with the Teacher object's "to_string" method.
#
# Write your code below and put the answer into the variable ANSWER.
#


class Teacher(Person):
    """docstring for Teacher."""
    def __init__(self, name, ssn, adress):
        """init"""
        super().__init__(name, ssn, adress)
        self.courses = []
    def add_course(self, course):
        """lägg till kurs"""
        self.courses.append(course)
    def remove_course(self, course):
        """ta bort kurs"""
        self.courses.remove(course)
    def to_string(self):
        """skriv ut"""
        courseString = ", ".join(self.courses)
        return super(Teacher, self).to_string() + " Courses: " + courseString

etttreAdress = Adress("Renere", "Smaland", "Six Duchies")
etttreTeacher = Teacher("Goliat", "502075-3392", etttreAdress)
etttreTeacher.add_course("javascript1")
etttreTeacher.add_course("oophp")
etttreTeacher.add_course("webgl")

ANSWER = etttreTeacher.to_string()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (2 points)
#
# Create a new class name **Student** make it inherit from class "Person". In
# the constructor add the instance attribute "courses_grades" and initiate it
# to and empty list.
# Create the method **add_course_grade**, it should take two arguments, one
# course and a grade. Create a tuple with the two arguments and add to the
# attribute "courses_grades".
# Create the method **average_grade**. Calculate and return the students
# average grade. Ignore grades with "-" in the calculation.
#
# In the code below Create a new instance of the class Address. Initiate it
# with the city `Katar`, the state `Gotland` and the country `Illian`.
# Create a new instance of the class Student. Initiate it with the name
# `Buster` and ssn `768244-4857` and the aforementioned Address object.
# Use the add_course_grade method to add the following courses, `webgl` with
# grade `4`, `javascript1` with grade `-` and `python` with grade `4`.
#
#
# Answer with the Student object's "average_grade" method.
#
# Write your code below and put the answer into the variable ANSWER.
#

class Student(Person):
    """docstring for Student."""
    def __init__(self, name, ssn, adress):
        """init"""
        super().__init__(name, ssn, adress)
        self.courses_grades = []
    def add_course_grade(self, course, grade):
        """sätt kurs med betyg"""
        self.courses_grades.append((course, grade))
    def average_grade(self):
        """ räkna ut medel betyg"""
        grades = []
        for items in self.courses_grades:
            if items[1] != "-":
                grades.append(int(items[1]))
        return sum(grades) / len(grades)



ettfyraAdress = Adress("Katar", "Gotland", "Illian")
ettfyraStudent = Student("Buster", "768244-4857", ettfyraAdress)
ettfyraStudent.add_course_grade("webgl", "4")
ettfyraStudent.add_course_grade("javascript1", "-")
ettfyraStudent.add_course_grade("python", "4")

ANSWER = ettfyraStudent.average_grade()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)


dbwebb.exit_with_summary()
