#!/usr/bin/env python3

"""Unit test class"""

import unittest
import main

class Testcase(unittest.TestCase):
    """Class Testcase"""

    def test_return(self):
        """test on function returnName"""
        self.assertEqual(main.return_name("Kalle"), "Hello Kalle")

    def test_add(self):
        """test on function addNumbers"""
        self.assertEqual(main.add_numbers(14, 6), 20)

    def test_upper(self):
        """test uppercase"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """test if uppercase (boolean)"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """test split"""
        str1 = 'hello world'
        self.assertEqual(str1.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            str1.split(2)

if __name__ == '__main__':
    unittest.main()
