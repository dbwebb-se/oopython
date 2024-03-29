#!/usr/bin/env python3
"""
Example of inheritance
"""

# pylint: disable=unused-private-member
class Video():
    """
    Class representing a video
    """

    def __init__(self, title, length, revenue):
        self.title = title
        self.length = length
        self._revenue = revenue

    def to_string(self):
        """
        Return object as string
        """
        return  f"{self.title} is {self.length} minute(s) long"

    def print_info(self):
        """
        Print object as string
        """
        print(self.to_string())

    def must_override(self):
        """
        Example method for forcing implementation of method
        """
        raise NotImplementedError("Subclasses must implement this!")

    def __draw_tax(self, revenue):
        """
        Draw tax from new revenue
        """
        self._revenue += revenue * 0.7
        print(f"New revenue is: {self._revenue}")

    def add_revenue(self, money):
        """
        Add revenue
        """
        self.__draw_tax(money)


class Movie(Video):
    """
    Class representing a Movie, inherits from Video
    """
    def __init__(self, title, length, revenue, director, rating):
        super().__init__(title, length, revenue)

        self.director = director
        self.rating = rating

    def to_string(self):
        """
        Return object as string
        """
        return  f"{super().to_string()}, has the director {self.director}\
         and a rating of {self.rating}"

    def must_override(self):
        """
        Overriding abstract method from base class
        """
        print("Abstract method is overridden")

    def __draw_tax(self, revenue):
        """
        overrides from Video to change taxation.
        """
        self._revenue += revenue * 0.9
        print(f"Lowered taxes and new revenue is: {self._revenue}")


charlie = Video("Charlie bit my finger", 1, 10000)
dogs = Movie("Isle of Dogs", 101, 64241499, "Wes Anderson", 8.0)

charlie.print_info()
dogs.print_info()
charlie.add_revenue(10000)
dogs.add_revenue(1500000)

print(charlie._revenue)# pylint: disable=protected-access
print(dogs._revenue)# pylint: disable=protected-access
