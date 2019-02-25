#!/usr/bin/env python3
class Video():

    def __init__(self, title, length, revenue):
        self.title = title
        self.length = length
        self._revenue = revenue

    def to_string(self):
        return  "{title} is {length} minute(s) long".format(
                title=self.title,
                length=self.length,
        )

    def print_info(self):
        print(self.to_string())

    def mustOverride(self):
        raise NotImplementedError("Subclasses must implement this!")

    def __draw_tax(self, revenue):
        self._revenue += revenue * 0.7
        print("New revenue is: {}".format(self._revenue))

    def add_revenue(self, money):
        self.__draw_tax(money)


class Movie(Video):

    def __init__(self, title, length, revenue, director, rating):
        super().__init__(title, length, revenue)

        self.director = director
        self.rating = rating

    def to_string(self):
        return  "{base_msg}, has the director {dir} and a rating of {rating}".format(
            base_msg=super().to_string(),
            dir=self.director,
            rating=self.rating
        )
    
    def __draw_tax(self, revenue):
        self._revenue += revenue * 0.9
        print("Lowered taxes and new revenue is: {}".format(self._revenue))


charlie = Video("Charlie bit my finger", 1, 10000)
dogs = Movie("Isle of Dogs", 101, 64241499, "Wes Anderson", 8.0)

charlie.print_info()
dogs.print_info()
charlie.add_revenue(10000)
dogs.add_revenue(1500000)

print(charlie._revenue)
print(dogs._revenue)

class Date():

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return "{year}-{month}-{day}".format(year=self.year, month=self.month, day=self.day)
        
class Person:

    def __init__(self, name, year, month, day):
        self.name = name
        self.date_of_birth = Date(year, month, day)

    def __repr__(self):
        return "My name is {name} and my date of birth is {date}".format(name=self.name, date=self.date_of_birth)

pers = Person("James", 1993, 5, 14)
print(pers)
print(pers.date_of_birth)
person2 = Person("Klara", 2010, 3, 15)
print(person2)
print(person2.date_of_birth)

