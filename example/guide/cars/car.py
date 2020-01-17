"""
Contains a class that represent a grafical car
"""
import random

class Car():
    """
    Represent a car
    """
    model1 = """
{pos}.-'--`-._
{pos}'-O---O--'
"""
    model2 = r"""
{pos}   __
{pos} _| =\__
{pos}/o____o_\
"""
    model3 = r"""
{pos}  ______
{pos} /|_||_\`.__
{pos}(   _    _ _\
{pos}=`-(_)--(_)-'
"""
    model4 = """
{pos}     .--.
{pos}.----'   '--.
{pos}'-()-----()-'
"""

    wheels = 4
    car_count = 0

    def __init__(self, model, price, driver):
        """
        Constructor for class
        Assign random value for speed
        """
        self.model = model
        self.driver = driver
        self._price = price

        self._speed = random.uniform(0.5, 2)
        self._position = 0

        Car.car_count += 1

    def get_model(self):
        """
        Return ascii picture with spaces as position
        """
        spaces = " " * round(self._position)
        return getattr(self, self.model).format(pos=spaces)

    def move(self):
        """
        Move position forward with speed and another random value
        """
        self._position += random.uniform(0.5, 2.5) + self._speed

    def get_pos(self):
        """
        Return private value position
        """
        return self._position

    def get_price(self):
        """
        Return private value attribute price
        """
        return self._price

    def set_price(self, new_price):
        """
        Check that new price for car is not less more than 30%
        """
        if float(new_price) / float(self._price) > 0.7:
            self._price = new_price
            return "New price is " + str(self._price)

        return "New price is too low. You can max lower it with 30%."

    def present_car(self):
        """
        Return string that represent a car object.
        """
        return "{d} with the car {m}. The car costs {p}$.".format(
            m=self.model, p=self._price, d=self.driver
        )

    def __add__(self, other):
        """
        overload +, for two car objects
        """
        return self._price + other.get_price()

    def __iadd__(self, other):
        """
        overload +=, for two car objects
        """
        self._price += other.get_price()
        return self

    @classmethod
    def wheel_message(cls):
        """
        Print the static variable wheels
        """
        print("A car normally have {nr} wheels".format(nr=cls.wheels))


if __name__ == "__main__":
    car = Car("volvo v40", 40000, "Zeldah")
    print(car.get_price())
    print(car.set_price(35000))
    print(car.set_price(20000))

    print(car.present_car())
