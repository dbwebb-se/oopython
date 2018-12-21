#!/usr/bin/env python3

""" Vehicle class """

from abc import ABCMeta, abstractmethod
class Vehicle():
    """
    A vehicle base class. Can be made into more classes, wheels, \
        engine and so on.


    Attributes:
        wheels: Number of wheels.
        miles:  Number of miles have traveled.
        make:   Company that made the vehicle.
        model:  The vehicle model.
        year:   The year the vehicle was built.
    """

    _metaclass_ = ABCMeta

    wheels = 0
    vehicleType = ""
    startPrice = 0

    def __init__(self, miles, make, model, year):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def price(self):
        """
        Return the price calculated with start price, year and miles
        """

    @abstractmethod
    def get_vehicle_type(self):
        """
        Return the type of the vehicle
        """
