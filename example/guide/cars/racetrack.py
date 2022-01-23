"""
Conatins a RaceTrack class that use car objects to race to a finishline
"""
import time
import json
from car import Car



class RaceTrack():
    """
    RaceTrack class
    """
    def __init__(self, finishline, sleep):
        """
        Constructor
        """
        self.finishline = finishline
        self.sleep = sleep

        self.cars = []
        self.create_cars()



    def create_cars(self):
        """
        Read card data from file and create Car objects
        """
        with open("cars.json", encoding="utf-8") as fd:
            json_cars = json.load(fd)
        for car in json_cars:
            self.cars.append(Car.create_from_json(car))



    def race(self):
        """
        Main loop of program, represent a race between cars
        Run as long as no one has finished
        """
        finished = []
        while not finished:
            self.clear_console()
            self.print_finishline()
            self.move_cars()

            finished = self.get_finished_cars()

            time.sleep(self.sleep)

        self.print_winners(finished)



    def move_cars(self):
        """
        Move each car another step forward
        """
        for car in self.cars:
            car.move()
            print(car.get_model())
            self.print_finishline()



    def get_finished_cars(self):
        """
        Use list comprehension to find finished cars and add to list
        """
        return [car for car in self.cars if car.get_pos() >= self.finishline]



    @staticmethod
    def print_winners(finished):
        """
        Staticmethod that prints the winners of the race
        """
        print("Winner is!")
        for car in finished:
            msg = "{} finished first out of {} cars!"
            print(msg.format(car.present_car(), Car.car_count))


    def print_finishline(self):
        """
        Print a finishline
        """
        print(" " * self.finishline + "|")

    @staticmethod
    def clear_console():
        """
        Clear the console of old text
        """
        print(chr(27) + "[2J" + chr(27) + "[;H")



if __name__ == "__main__":
    rt = RaceTrack(50, 0.2)
    rt.race()
