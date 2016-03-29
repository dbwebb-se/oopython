#!/usr/bin/env python3
"""
Unittest version 2
"""

import unittest
from person import Person

class Testcase(unittest.TestCase):
    """Class Testcase"""

    test = Person("Test Testsson", "Testvillage", 42)
    test2 = Person("Andreas Arnesson", "Karlskrona", 25)

    # Tests if the objects are the same
    def test_equal_objects(self):
        """ Should return True, they are not the same """
        self.assertIsNot(self.test, self.test2)

    # Tests if the objects are instances of Person
    def test_are_object_instance_of(self):
        """ Should return True, is is instance of Person """
        self.assertIsInstance(self.test, Person)

    # Tests the firstName of the object
    def test_name(self):
        """Should return Test if correct"""
        self.assertEqual(self.test.name, "Test Testsson")

    # Tests the born of the object
    def test_born(self):
        """Should return Testvillage if correct"""
        self.assertEqual(self.test.born, "Testvillage")

    # Tests the age of the object
    def test_age(self):
        """Should return 42 if correct"""
        self.assertEqual(self.test.age, 42)

    # Tests the interest of the object
    def test_interest(self):
        """Should return empy list if correct"""
        self.assertEqual(self.test.get_interests(), [])

    # Tests the interests of the object, when added programming and testing
    def test_interest_again(self):
        """Should return [programming, testing] if correct"""
        # add some interests
        self.test.add_interest("programming")
        self.test.add_interest("testing")
        self.assertEqual(self.test.get_interests(), ["programming", "testing"])

    # Tests the interest as string
    def test_interest_as_string(self):
        """Should return programming, testing if correct"""
        self.assertEqual(self.test.get_interests_as_string(), "programming, testing")

    # Tests if the person is alive or not
    def test_is_alive(self):
        """ Returns True if person is alive """
        self.assertTrue(self.test.is_alive())


if __name__ == '__main__':
    unittest.main()
