from abc import ABCMeta, abstractmethod
from vehicle import Vehicle

class Truck(Vehicle):
    """
    A car
    """
    startPrice = 200000
    wheels = 6
    vehicleType = "truck"

    def getVehicleType(self):
        """
        Return the price calculated with start price, year and miles
        """
        return self.vehicleType

    def price(self):
        """
        Return the type of the vehicle
        """
        return self.startPrice - self.wheels * (0.1 * self.miles)
