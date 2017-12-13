#!/usr/bin/env python3
"""
Unittest file for Phone
"""

import unittest
from phone import Phone

class Testcase(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""
    # Create instances to use in the tests
    phone = Phone("Samsung", "Galaxy S8", "Android")
    phone_two = Phone("Apple", "iPhone 8", "iOS")

    # Tests if the objects are the same
    def test_A_equal_objects(self):
        """ Should return True, they are not the same """
        self.assertIsNot(self.phone, self.phone_two)

    # Tests if the objects are instances of Person
    def test_B_are_object_instance_of(self):
        """ Should return True, is is instance of Phone """
        self.assertIsInstance(self.phone, Phone)

    # Tests if owner returns correct when none is set
    def test_C_no_owner(self):
        """Should return 'No owner yet' if correct"""
        self.assertEqual(self.phone.get_owner(), "No owner yet")

    # Tests if owner returns corect when owner is set
    def test_D_set_owner(self):
        """Should return 'Pelle' if correct"""
        self.phone.change_owner("Pelle")
        self.assertEqual(self.phone.get_owner(), "Pelle")

    # Tests property: manufacturer
    def test_E_prop_manufacturer(self):
        """Should return 'Samsung' if correct"""
        self.assertEqual(self.phone.get_manufacturer(), "Samsung")

    # Tests property: model
    def test_F_prop_model(self):
        """Should return 'S8' if correct"""
        self.assertEqual(self.phone.get_model(), "Galaxy S8")

    # Tests property: os
    def test_G_prop_os(self):
        """Should return 'Android' if correct"""
        self.assertEqual(self.phone.get_os(), "Android")

    # Test if phonebook is empty
    def test_H_empty_phonebook(self):
        """Should return False if phonebook is empty"""
        self.assertFalse(self.phone.has_contacts())

    # Test if phonebook is not empty
    def test_I_not_empty_phonebook(self):
        """Should return True if phonebook has contacts"""
        self.phone.add_contact("Andreas", 12345)
        self.phone.add_contact("Emil", 67890)
        self.assertTrue(self.phone.has_contacts())

    # Test phonebook length
    def test_J_phonebook_length(self):
        """Should return the number 2"""
        self.assertEqual(self.phone.get_contacts_length(), 2)

    # Test get contact that not exists
    def test_K_faulty_contact(self):
        """Should return None"""
        self.assertIsNone(self.phone.get_contact("Kenneth"))

    # Test get contact that exists
    def test_L_get_contact(self):
        """Should return tuple with contact name and number"""
        self.assertEqual(self.phone.get_contact("Andreas"), ("Andreas", 12345))



if __name__ == '__main__':
    unittest.main()
