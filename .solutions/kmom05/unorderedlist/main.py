#!/usr/bin/env python3

"""
Main file for testing
"""
# Imports
from my_bubblesort import bubble_sort
from unorderedlist import UnorderedList

# Create a new list
my_list = UnorderedList()

# Add 10 numbers to the list
my_list.add(56)
my_list.add(89)
my_list.add(34)
my_list.add(76)
my_list.add(78)
my_list.add(13)
my_list.add(32)
my_list.add(234)
my_list.add(2)
my_list.add(1)

# Checks that the list is unsorted in the beginning
my_list.print_list()

# Sort the list
bubble_sort(my_list)

# Checks the structure of the list
print(my_list)

# Print the sorted list
my_list.print_list()
