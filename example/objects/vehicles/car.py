#!/usr/bin/env python3

""" Car class """

from vehicle import Vehicle

class Car(Vehicle):
    """
    A car
    """
    startPrice = 100000
    wheels = 4
    vehicleType = "car"

    def get_vehicle_type(self):
        """
        Return the price calculated with start price, year and miles
        """
        return self.vehicleType

    def price(self):
        """
        Return the type of the vehicle
        """
        return self.startPrice - self.wheels * (0.1 * self.miles)
