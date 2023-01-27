#!/usr/bin/env python3

"""
Contains the Plane class
"""
import random
from math import floor

class Plane():
    """
    Plane class
    """
    def __init__(self, p_type, max_speed, max_distance):
        self.type = p_type
        self.max_speed = max_speed # km/h
        self.max_distance = max_distance
        self.id = random.randint(1000, 9999)
        self.booked = False

    def calc_flight_duration(self, distance):
        """
        Calculate flight duration for distance with max_speed
        """
        duration = (distance / self.max_speed) * 0.95
        return floor(duration * 100)

    def get_flight_duration(self, distance):
        """
        Get flight duration for distance
        """
        if distance > self.max_distance:
            first_flight = self.max_distance
            second_flight = distance - self.max_distance

            duration = self.calc_flight_duration(first_flight)
            duration += 2 # Add two duration for filling up tank
            duration += self.calc_flight_duration(second_flight)
            return duration

        return self.calc_flight_duration(distance)

    def __repr__(self):
        return f"{self.id}|{self.type}"
