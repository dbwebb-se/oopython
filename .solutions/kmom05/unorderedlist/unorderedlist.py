#!/usr/bin/env python3

"""
Unordered list class
"""

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
        Sets data in list
        """
        current = self.head
        count = 0
        while current != None:
            if count == index:
                current.set_data(newdata)
                break
            count = count + 1
            current = current.get_next()

    def get(self, index):
        """
        Returns item based on index
        """
        current = self.head
        count = 0
        while current != None:
            if count == index:
                return current.get_data()

            count = count + 1
            current = current.get_next()


    def search(self, item):
        """
        Returns True if item found, else return False
        """
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def print_list(self):
        """
        Prints the list
        """
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()

    def remove(self, item):
        """
        Removes item from list
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
