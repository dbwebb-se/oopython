#!/usr/bin/env python3

"""
Main file for testing
"""

# Imports
import unittest
from my_bubblesort import bubble_sort
from unorderedlist import UnorderedList



class TestList(unittest.TestCase):
    """ Test Class """

    studlist = UnorderedList()

    def test_a_empty_list(self):
        """ Test is_empty() """
        self.assertEqual(self.studlist.is_empty(), True)

    def test_b_nr_of_elements(self):
        """ Test size() and add() """
        self.studlist.add(30)
        self.studlist.add(55)
        self.studlist.add(10)
        self.studlist.add(25)
        self.studlist.add(40)

        self.assertEqual(self.studlist.size(), 5)

    def test_c_set_data(self):
        """ Test set() and get()"""
        self.studlist.set(3, 999)
        self.assertEqual(self.studlist.get(3), 999)

    def test_d_search(self):
        """ Test search() """
        self.assertTrue(self.studlist.search(25))
        self.assertFalse(self.studlist.search(888))

    def test_e_remove(self):
        """ Test remove() """
        current_size = self.studlist.size()
        self.assertTrue(self.studlist.search(30))
        self.studlist.remove(30)
        self.assertFalse(self.studlist.search(30))
        self.assertNotEqual(current_size, self.studlist.size())

    def test_f_sort(self):
        """ Test sort() """
        bubble_sort(self.studlist)
        self.assertEqual(self.studlist.get(0), 10)
        self.assertEqual(self.studlist.get(1), 25)
        self.assertEqual(self.studlist.get(2), 40)
        self.assertEqual(self.studlist.get(3), 999)


if __name__ == '__main__':
    unittest.main()
