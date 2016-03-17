#!/usr/bin/env python3

"""Unit test class"""

import unittest
import main

class testingMyFunction(unittest.TestCase):

    def test_return(self):
        self.assertEqual(main.returnName("Kalle"), "Hello Kalle")

    def test_add(self):
        self.assertEqual(main.addNumbers(14, 6), 20)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
