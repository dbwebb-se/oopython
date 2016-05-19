#!/usr/bin/env python3

"""
Unordered list class
"""

# Imports
from node import Node

class UnorderedList:
    """
    Unordered list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Checks if list is empty
        """
        return self.head is None

    def add(self, item):
        """
        Add item to list
        """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """
        Return size of list
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def set(self, index, newdata):
        """
        Set node-data in list at specific index
        """
        # insert method

    def get(self, index):
        """
        Returns node data based on index
        """
        # insert method

    def search(self, item):
        """
        Returns True if item found, else return False
        """
        # insert method

    def print_list(self):
        """
        Prints each item in list
        """
        # insert method

    def remove(self, item):
        """
        Removes item from list
        """
        # insert method
