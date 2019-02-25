import random
class Coin():

    def __init__(self, value):
        self.sideup = "Heads"
        self.value = value

    def __iadd__(self, other):
        return Coin(self.value + other.value)


    def __add__(self, other):
        return self.value + other.value

    def toss(self):
        side = random.randint(0, 1)
        if side == 0:
            self.sideup = "Tails"
        else:
            self.sideup = "Heads"

class Dog():
    counter = 0
    def __init__(self, name):
        self.name = name
        Dog.counter += 1

    @staticmethod
    def bark():
        print("voff voff")
