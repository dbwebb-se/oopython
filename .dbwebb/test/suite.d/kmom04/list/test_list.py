#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import io
import unittest
import unittest.mock
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

class Test2List(ExamTestCase):
    """
    Testing the class List.
    """
    def setUp(self):
        self.list = list.UnorderedList()

    @tags("list")
    def test_if_list_is_empty(self):
        """
        Testar att listan som skapas är tom med metoden is_empty().
        Förväntar att self.list.is_empty() returnerar True:
        {correct}
        Innehöll följande:
        {student}
        """
        self.assertEqual(self.list.is_empty(), True)

    @tags("list")
    def test_append(self):
        """
        Testar att lägga till 1 nod med innehåll "one" i listan.
        Förväntar att listans huvud innehåller "one":
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        self.assertEqual(self.list.head.data, "one")

    @tags("list")
    def test_set_ok(self):
        """
        Testar att lägga till 2 noder "one" och "two" med append(). Ändrar data i listan
        på första noden med set() till "new_one".
        Förväntar att listans första node innehåller "new_one":
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        self.list.append("two")
        self.list.set(0, "new_one")
        self.assertEqual(self.list.head.data, "new_one")

    @tags("list")
    def test_set_exception(self):
        """
        Testar att lägga till 2 noder "one" och "two" i listan med append(). Testar använda set() för att
        ändra på node med index 3.
        Förväntar att ett MissingIndex exception skickas:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        self.list.append("two")
        with self.assertRaises(MissingIndex):
            self.list.set(3, "three")

    @tags("list")
    def test_size(self):
        """
        Testar att lägga till 2 noder i listan med append.
        Förväntar att listans längd med size() är:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        self.list.append("two")
        self.assertEqual(self.list.size(), 2)

    @tags("list")
    def test_size_0(self):
        """
        Testar att storleken på en tom lista är 0.
        Förväntar att listans längd med size() är:
        {correct}
        Innehöll följande:
        {student}
        """
        self.assertEqual(self.list.size(), 0)

    @tags("list")
    def test_get_ok(self):
        """
        Testar att lägga till 2 noder i listan med append() och sen hämta dem med get().
        Förväntar att listan ska innehålla:
        {correct}
        Innehöll följande:
        {student}
        """
        input = ["one",  "two"]
        self.list.append(input[0])
        self.list.append(input[1])
        result = [ self.list.get(0), self.list.get(1)]
        self.assertEqual(result, input)

    @tags("list")
    def test_get_exception(self):
        """
        Testar att lägga till 1 nod i listan och hämtar tredje noden med get(), som inte finns.
        Förväntar att MissingIndex ska kastas:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        with self.assertRaises(MissingIndex) as e:
            self.list.get(3)

    @tags("list")
    def test_index_of_ok(self):
        """
        Testar att lägga till 2 noder ("one" och "two") i listan med append() och kollar att index_of()
        returnerar rätt värde för "two".
        Förväntar att indexet till node "two" är:
        {correct}
        Innehöll följande:
        {student}
        """
        input = ["one",  "two"]
        self.list.append(input[0])
        self.list.append(input[1])
        self.assertEqual(self.list.index_of("two"), 1)

    @tags("list")
    def test_index_of_exception(self):
        """
        Testar att lägga till värdet "one" i listan med append() och använder index_of() för
        att hämta index för värde om inte finns, "two".
        Förväntar att MissingValue ska kastas:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        with self.assertRaises(MissingValue):
            self.list.index_of("two")

    @tags("list")
    def test_remove_middle_node_ok(self):
        """
        Testar att lägga till 3 noder ("one", "two" och "three") i listan med append() och tar
        bort "two" med remove().
        Förväntar att listans innehåller:
        {correct}
        Innehöll följande:
        {student}
        """
        input = ["one", "two", "three"]
        result = ["one", "three"]
        self.list.append(input[0])
        self.list.append(input[1])
        self.list.append(input[2])
        self.list.remove("two")
        new_list = [self.list.get(i) for i in range(self.list.size())]
        self.assertEqual(new_list, result)

    @tags("list")
    def test_remove_first_node_ok(self):
        """
        Testar att lägga till 3 noder ("one", "two" och "three") i listan med append() och tar
        bort "one" med remove().
        Förväntar att listans innehåller:
        {correct}
        Innehöll följande:
        {student}
        """
        input = ["one", "two", "three"]
        result = ["two", "three"]
        self.list.append(input[0])
        self.list.append(input[1])
        self.list.append(input[2])
        self.list.remove("one")
        new_list = [self.list.get(i) for i in range(self.list.size())]
        self.assertEqual(new_list, result)

    @tags("list")
    def test_remove_last_node_ok(self):
        """
        Testar att lägga till 3 noder ("one", "two" och "three") i listan med append() och tar
        bort "three" med remove().
        Förväntar att listans innehåller:
        {correct}
        Innehöll följande:
        {student}
        """
        input = ["one", "two", "three"]
        result = ["one", "two"]
        self.list.append(input[0])
        self.list.append(input[1])
        self.list.append(input[2])
        self.list.remove("three")
        new_list = [self.list.get(i) for i in range(self.list.size())]
        self.assertEqual(new_list, result)

    @tags("list")
    def test_remove_exception(self):
        """
        Testar att lägga till 1 nod "one" i listan med append() och tar bort "two" som inte finns
        med remove(). 
        Förväntar att MissingValue ska kastas:
        {correct}
        Innehöll följande:
        {student}
        """
        self.list.append("one")
        with self.assertRaises(MissingValue):
            self.list.remove("two")

    @tags("list")
    def test_print_list(self):
        """
        Testar att lägga till 2 noder ("one" och "two") i listan och skriver ut den.
        Förväntar att listans vid print_list() innehåller:
        {correct}
        Innehöll följande:
        {student}
        """
        input = ["one",  "two"]
        self.list.append(input[0])
        self.list.append(input[1])
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.list.print_list()
            text = fake_out.getvalue()
        for value in input:
            self.assertIn(value, text)


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
