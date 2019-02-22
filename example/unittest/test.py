#!/usr/bin/env python3
"""
Unittest file for Phone
"""

import unittest
from phone import Phone

class TestPhone(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Create object for all tests """
        self.phone = Phone("Samsung", "Galaxy S8", "Android")

    def tearDown(self):
        """ Remove dependencies after test """
        self.phone = None



    def test_default_owner(self):
        """Test that default value if correct for owner"""
        self.assertEqual(self.phone.get_owner(), "No owner yet")

    def test_set_owner(self):
        """Test changing owner of a Phone"""
        self.phone.change_owner("Pelle")
        self.assertEqual(self.phone.get_owner(), "Pelle")

    def test_empty_phonebook(self):
        """Test that contacts are empty"""
        self.assertFalse(self.phone.has_contacts())

    def test_validate_valid_numbers(self):
        """Test validating valid numbers"""
        valid = self.phone.validate_number("070-354 78 00")
        self.assertTrue(valid)

        valid = self.phone.validate_number("153-222 78 00")
        self.assertTrue(valid)

    def test_validate_non_valid_numbers(self):
        """Test validating non valid numbers"""
        not_valid = Phone.validate_number("xxx-xxx xx xx")
        self.assertFalse(not_valid)

        not_valid = Phone.validate_number("073456129-")
        self.assertFalse(not_valid)

        not_valid = Phone.validate_number("073-456 12 9a")
        self.assertFalse(not_valid)


    def test_add_contacts(self):
        """Test adding contacts"""
        self.phone.add_contact("Andreas", "070-354 78 00")
        self.phone.add_contact("Emil", "073-456 12 99")

        self.assertTrue(self.phone.has_contacts())
        self.assertEqual(self.phone.get_contacts_length(), 2)

    def test_get_contact(self):
        """Test that can get added contact"""
        self.phone.add_contact("Andreas", "079-244 07 80")
        self.assertEqual(self.phone.get_contact("Andreas"),
                         ("Andreas", "079-244 07 80"))

    def test_get_contact_fail(self):
        """
        Test that correct value is returned
        when getting contact that does not exist or is empty
        """
        with self.assertRaises(ValueError) as cm:
            self.phone.get_contact("Nothing")

        self.phone.add_contact("Andreas", "079-244 07 80")
        with self.assertRaises(ValueError) as cm:
            self.phone.get_contact("Zeldah")



if __name__ == '__main__':
    unittest.main()
