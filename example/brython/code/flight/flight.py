#!/usr/bin/env python3

"""
Contains the Flight class
"""
import random

class Flight():
    """
    Flight class
    """
    def __init__(self, departure_time, distance, departing_from, destination):
        self.departure_time = departure_time
        self.distance = distance
        self.departing_from = departing_from
        self.destination = destination

        self.assigned_plane = None
        self.arriving_time = 0
        self.duration = 0
        self.flight_number = random.randint(1000, 9999)

    def assigne_plane(self, plane):
        """
        Assign a plane to flight and calculate arrive time and flight duration
        """
        plane.booked = True
        self.assigned_plane = plane

        self.duration = plane.calc_flight_duration(self.distance)
        self.arriving_time = self.departure_time + self.duration

    def __repr__(self):
        return (
            f"{self.departing_from} - {self.destination}\n"
            f"Departure: {self.departure_time} Arrival: {self.arriving_time}\n"
            f"Duration: {self.duration}\n"
            f"Plane: {self.assigned_plane}"
        )
