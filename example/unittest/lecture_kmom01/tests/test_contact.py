import unittest
import random
from src.contact import Contact

class TestContactCreate(unittest.TestCase):
    def setUp(self):
        print("hejhej")
        random.seed("lecture")


    def test_create_valid_number(self):
        c = Contact("andreas", "234-123 23 12")
        self.assertEqual("andreas", c.name)
        self.assertEqual("234-123 23 12", c.number)

    def test_create_no_number(self):
        c = Contact("andreas")
        self.assertEqual("andreas", c.name)
        self.assertEqual("267-751 82 74", c.number)

    def test_create_invalid_number(self):
        c = Contact("marie", "ijiolkj")
        self.assertEqual("marie", c.name)
        self.assertEqual("267-751 82 74", c.number)

        c1 = Contact("emil", "dasd")
        self.assertEqual("emil", c1.name)
        self.assertEqual("793-424 76 85", c1.number)
