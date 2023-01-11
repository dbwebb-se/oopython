#!/usr/bin/env python3
""" Module for testing the class Car """

import unittest
from src.car import Car

class TestCar(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """
    def test_no_of_wheels_ok(self):
        """ Test if number of wheels is 4 """
        my_car = Car("Volvo", 50000) # Act
        self.assertEqual(my_car.wheels, 4)# Assert

    def test_present_car_ok(self):
        """ Test if the string is correct from present_car """
        my_car = Car("Volvo", 50000) # Act
        self.assertEqual(my_car.present_car(),
            "This car is of model Volvo and costs 50000$.")# Assert
