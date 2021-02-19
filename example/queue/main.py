#!/usr/bin/python3
""" Main file with Handler class """
# pylint: skip-file
import sys
import inspect
from queue import Queue
from errors import EmptyQueueException


class Handler:
    """ Handler class """

    _OPTIONS = {
        "1": "add_to_queue",
        "2": "remove_from_queue",
        "3": "get_first_item",
        "4": "get_queue_size",
        "5": "is_queue_empty",
        "q": "quit"
    }

    def __init__(self):
        """ Initialize class """
        self.queue = Queue()
        self.start()


    def _get_method(self, method_name):
        """
        Uses function getattr() to dynamically get value of an attribute.
        """
        return getattr(self, self._OPTIONS[method_name])


    def _print_menu(self):
        """
        Use docstring from methods to print options for the program.
        """
        menu = ""

        for key in sorted(self._OPTIONS):
            method = self._get_method(key)
            docstring = inspect.getdoc(method)

            menu += "{choice}: {explanation}\n".format(
                choice=key,
                explanation=docstring
            )

        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(menu)

    def add_to_queue(self):
        """ Adds a node to the queue. """
        value = input("\nAdd a value: \n>>> ")
        self.queue.enqueue(value)
        print(f"{value} has been added.")

    def remove_from_queue(self):
        """ Removes the first node from the queue. """
        try:
            print(f"{self.queue.dequeue()} has been removed.")
        except EmptyQueueException as e:
            print(f"Error: {e}")

    def get_first_item(self):
        """ Prints the value of the first queue node. """
        try:
            print(self.queue.peek())
        except EmptyQueueException as e:
            print(f"Error: {e}")

    def get_queue_size(self):
        """ Shows the queue length. """
        print(self.queue.size())

    def is_queue_empty(self):
        """ Shows if the queue is empty or not. """
        print(self.queue.is_empty())

    @staticmethod
    def quit():
        """ Quit the program """
        sys.exit()

    def start(self):
        """ Start method """
        while True:
            self._print_menu()
            choice = input("Enter menu selection:\n-> ")

            try:
                self._get_method(choice.lower())()
            except KeyError:
                print("Invalid choice!")

            input("\nPress any key to continue ...")

if __name__ == "__main__":
    Handler()
