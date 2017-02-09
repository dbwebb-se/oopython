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
        # Här gäller det att sätta nodens data till 'newdata' på rätt
        # index-position.

    def get(self, index):
        """
        Returns node data based on index
        """
        # Likt 'set()' gäller det att traversera listan men här ska du
        # returnera datan för värdet på rätt index-plats

    def search(self, item):
        """
        Returns True if item found, else return False
        """
        # Här ska du returnera en bool (True/False)
        # beroende på om 'item' finns i listan

    def print_list(self):
        """
        Prints each item in list
        """
        # Traversera listan och gör en print() på varje element

    def remove(self, item):
        """
        Removes item from list
        """
        # Traversera listan och håll koll på föregående nod
        # och nästa nod. Om nuvarande 'data' är samma som 'item'
        # gäller det att koppla ihop föregående med nästa.
