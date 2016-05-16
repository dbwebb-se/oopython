"""
Contains the register class
"""

class Registry:
    """
    Contains all the registered books
    """
    def __init__(self):
        self.books = []
        self.trash = []

    def register_book(self, book):
        """
        Registers books
        """
        if book.should_register():
            self.add_book(book)
        else:
            self.trash_book(book)

    def add_book(self, book):
        """
        Adds book to the list
        """
        self.books.append(book)

    def trash_book(self, book):
        """
        Add book to trashlist
        """
        self.trash.append(book)

    def print_books(self):
        """
        Print all registered books
        """
        print(self.books)
