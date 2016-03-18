#!/usr/bin/python3
from car import Car
from truck import Truck

car = Car(4000, "Volvo", "X90", 2015)
print(car.price())

truck = Truck(5000, "Scania", "XBC", 2014)
print(truck.price())
