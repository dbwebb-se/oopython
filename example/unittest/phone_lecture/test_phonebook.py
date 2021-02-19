import unittest
from unittest import mock
from phonebook import PhoneBook
# pylint: skip-file

class TestPhoneBook(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Create object for all tests """
        # Arrange
        self.phonebook = PhoneBook()

    def tearDown(self):
        """ Remove dependencies after test """
        self.phonebook = None

    def test_empty_phonebook(self):
        """Test that has_contacts return False when phonebook is empty"""
        self.assertFalse(self.phonebook.has_contacts()) # Assert

    def test_has_contact_true(self):
        """Test that has_contacts return True when phonebook is has a contact"""
        self.phonebook._contacts.append("070-354 78 00") # Arrange
        self.assertTrue(self.phonebook.has_contacts()) # Assert

    def test_validate_valid_number(self):
        """Test validating valid number"""
        self.assertTrue(self.phonebook.validate_number("070-354 78 00"))
        
    def test_validate_number_with_letter(self):
        """Test validating number with a letter init"""
        self.assertFalse(self.phonebook.validate_number("070-35b 78 00"))

    def test_valid_number_with_missing_space(self):
        """Test validating number with a space missing"""
        self.assertFalse(self.phonebook.validate_number("070-354 7800"))

    def test_get_contact_empty(self):
        """
        Test that error is raised when list is empty
        """
        with self.assertRaises(ValueError) as _:
            self.phonebook.get_contact("Missing")

    def test_get_contact_fail(self):
        """
        Test that correct value is returned
        when getting contact that does not exist or is empty
        """
        self.phonebook.add_contact("Andreas", "079-244 07 80")
        with self.assertRaises(ValueError) as _:
            self.phonebook.get_contact("Zeldah")
            

    def test_add_contact_success(self):
        """
        Test we can add contat. Mock validation method.
        """
        # Arrange
        contact = ("Andreas", "079-244 07 80")
        with mock.patch.object(self.phonebook, 'validate_number') as validate_mock:
            validate_mock.return_value = True

            # Act
            result = self.phonebook.add_contact(*contact)

            # Assert
            validate_mock.assert_called_once_with(contact[1])
            self.assertTrue(result)
            self.assertEqual(len(self.phonebook._contacts), 1)
            self.assertEqual(self.phonebook._contacts[0], contact)