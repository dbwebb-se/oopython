#!/usr/bin/env python3
"""
Controller class
"""
from registry import Registry
from book import Book

class Controller:
    """
    Controlls the registry
    """
    def __init__(self):
        self.registry = Registry()

    def main(self):
        """
        starts everything
        """
        self.register_books(self.registry)

    def register_books(self, registry):
        """
        Registers books to the registry
        """
        books = [Book("'The Wheel of time'", "Robert Jordan"),
                 Book("'The painted man'", "Peter V. Brett"),
                 Book("'The name of the wind'", "Patrick Rothfuss"),
                 Book("'Off to Be the Wizard'", "Scott Meyer"),
                 Book("'Half a King'", "Joe Abercrombie "),
                 Book("'The Way of Shadows'", "Brent Weeks"),
                 Book("'Fool's Assassin'", "Robin Hobb"),
                 Book("'The Golem and the Jinni'", "Helene Wecker"),
                 Book("'The Way of Kings'", "Brandon Sanderson"),
                 Book("'1984'", "George Orwell"),
                 Book("'The Count of Monte Cristo'", "Alexandre Dumas"),
                 Book("'Brott och straff'", "Fyodor Dostoyevsky")]

        for book in books:
            registry.register_book(book)
        self.registry.print_books()

if __name__ == '__main__':
    controller = Controller()
    controller.main()
