#!/usr/bin/env python3

""" My sorting algorithms """

def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(items.size()):
        for j in range(items.size()-1-i):
            if items.get(j) > items.get(j+1):
                temp = items.get(j)
                items.set(j, items.get(j+1))
                items.set(j+1, temp)
    # return items
