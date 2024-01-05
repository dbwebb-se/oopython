#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
import os
import random
import sys
from io import StringIO
from unittest.mock import patch
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
list = import_module(REPO_PATH, 'src/unorderedlist')
node = import_module(REPO_PATH, 'src/node')
from src.errors import MissingIndex, MissingValue

class Test3ListExtra(ExamTestCase):
    """
    Testing the class List.
    """
    def setUp(self):
        self.list = list.UnorderedList()

    @tags("list_extra")
    def test_len(self):
        """
        Testar att lägga till 2 noder i listan.
        Förväntar att listans längd med len() är:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        self.list.append("two")
        try:
            list_len = len(self.list)
            self.assertEqual(list_len, 2)
        except:
            self.assertEqual("Class is missing __len__", 2)


    @tags("list_extra")
    def test_str(self):
        """
        Testar att lägga till 1 nod ("one") i listan.
        Förväntar att noden innehåller:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        try:
            node_str = str(self.list)
            self.assertIn("one", node_str)
        except:
            self.assertEqual("Class is missing __str__", "one")
        node_str = str(self.list)


    @tags("list_extra")
    def test_getitem(self):
        """
        Testar att lägga till 1 nod ("one") i listan.
        Förväntar att list[0] är:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        try:
            data = self.list[0]
            self.assertEqual(data, "one")
        except:
            self.assertEqual("Class is missing __getitem__", "one")

    @tags("list_extra")
    def test_getitem_exception(self):
        """
        Testar att lägga till 1 nod ("one") i listan.
        Förväntar att list[3] kastar MissingIndex:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        try:
            with self.assertRaises(MissingIndex):
                self.list[3]
        except:
            self.assertEqual("Class is missing __getitem__", "one")


    @tags("list_extra")
    def test_setitem(self):
        """
        Testar att lägga till 1 nod ("one") i listan. Sätter om till "new".
        Förväntar att list[0] = "new" returnerar:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        try:
            self.list[0] = "new"
            self.assertEqual(self.list[0], "new")
        except:
            self.assertEqual("Class is missing __setitem__", "one")


    @tags("list_extra")
    def test_setitem_exception(self):
        """
        Testar att lägga till 1 nod ("one") i listan. Sätter om till "new" på en
        node som inte finns.
        Förväntar att list[3] = "new" kastar MissingIndex:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        try:
            with self.assertRaises(MissingIndex):
                self.list[3] = "new"
        except:
            self.assertEqual("Class is missing __setitem__", "one")


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)