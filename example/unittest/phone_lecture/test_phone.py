import unittest
from io import StringIO
from unittest import mock
from phone import Phone
from phonebook import PhoneBook
# pylint: skip-file

class TestPhone(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Create object for all tests """
        # Arrange
        self.phone = Phone("Samsung", "Galaxy S8", "Android")

    def tearDown(self):
        """ Remove dependencies after test """
        self.phone = None

    def test_init(self):
        """Test that init works as expected"""
        # Assert
        self.assertEqual(self.phone.owner, "No owner yet")
        self.assertEqual(self.phone.manufacturer, "Samsung")
        self.assertEqual(self.phone.model, "Galaxy S8")
        self.assertEqual(self.phone.os, "Android")
        self.assertTrue(isinstance(self.phone._phonebook, PhoneBook))


    def test_call(self):
        inp = ["andreas"]
        with mock.patch('builtins.input', side_effect=inp):
            pass

    def test_make_call(self):
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            with mock.patch.object(self.phone._phonebook, "get_contact") as get_mock:
                get_mock.return_value = "070-354 78 00"

                self.phone._make_call("andreas")

                content = fake_out.getvalue().rstrip()
                self.assertEqual(content, "Calling number 070-354 78 00 ...")
