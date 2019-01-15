#!/usr/bin/env python3

"""
Main program for flights
"""
import random
from plane import Plane
from flight import Flight



class FlightControll():
    """
    FlightControll class for handling flights and planes
    """
    def __init__(self):
        """
        init method
        """
        self.planes = []
        self.flights = []

        self.create_flights()
        self.create_planes()

    def find_available_plane(self):
        """
        Find an available plane from existing planes
        """
        plane_indexes = list(range(len(self.planes)))
        random.shuffle(plane_indexes)
        for index in plane_indexes:
            if not self.planes[index].booked:
                return self.planes[index]
        return False

    def schedule_flights(self):
        """
        Find a plane for each flight
        """
        for flight in self.flights:
            plane = self.find_available_plane()
            flight.assigne_plane(plane)

    def create_flights(self):
        """
        Create flights
        """
        self.flights.append(Flight(1200, 10500, "Arlanda", "Berlin"))
        self.flights.append(Flight(2230, 18630, "Kastrup", "Arlanda"))
        self.flights.append(Flight(1725, 16123, "Kastrup", "London"))

    def create_planes(self):
        """
        Create airplanes
        """
        self.planes.append(Plane("Boeing 777", 600, 17395))
        self.planes.append(Plane("Airbus A380", 643, 16670))
        self.planes.append(Plane("Boeing 787", 710, 15750))
        self.planes.append(Plane(" Boeing 747-8i", 850, 13750))

    def display_flights(self):
        """
        Print all scheduled flights
        """
        for flight in self.flights:
            print(flight)

if __name__ == "__main__":
    fc = FlightControll()
    fc.schedule_flights()
    fc.display_flights()
