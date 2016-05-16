"""
Controller class
"""
from Registry import Registry
from Book import Book

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
        books = [Book("The Wheel of time", "Robert Jordan"),
                 Book("The name of the wind", "Patrick Rothfuss"),
                 Book("The painted man", "Peter V. Brett")]

        for book in books:
            registry.register_book(book)
        self.registry.print_books()

if __name__ == '__main__':
    controller = Controller()
    controller.main()
