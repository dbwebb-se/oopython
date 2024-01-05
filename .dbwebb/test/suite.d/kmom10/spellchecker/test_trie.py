#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
from io import StringIO
import os
import sys
from unittest.mock import patch
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

Trie = import_module(REPO_PATH, 'src/trie').Trie

class Test1Trie(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    link_to_assignment = "https://dbwebb.se/kurser/oopython-v3/kmom10"

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)



    @tags("1")
    def test_a_prefix(self):
        """
        Testar kolla att prefix_search returnerar rätt lista.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns i listan:
        {correct}
        Innehöll:
        {student}
        """
        self._argument  = ["mos"]
        words = [
            "most",
            "mostly",
            "moss",
            "mosque",
            "mosquitoes",
            "mosquito",
            "mosaic",
            "mosquitos"
        ]
        trie = Trie.create_from_file()
        respons = trie.prefix_search("mos")
        for word in words:
            if self.find_index(word, respons) == -1:
                self.assertIn(word, respons)
        self.assertEqual(len(respons), len(words), ["Förväntar att antalet ord i listan är:", "Det fanns:"])


    @tags("1")
    def test_a_prefix_no_match(self):
        """
        Testar kolla att prefix_search tom lista när prefixet inte finns.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns i listan:
        {correct}
        Innehöll:
        {student}
        """
        self._argument  = ["xyz"]
        words = []
        trie = Trie.create_from_file()
        respons = trie.prefix_search("xyz")
        self.assertEqual(respons, words)


    @tags("1")
    def test_a_prefix_is_word(self):
        """
        Testar kolla att prefix_search returnerar rätt lista när prefixet också är ett ord.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns i listan:
        {correct}
        Innehöll:
        {student}
        """
        self._argument  = ["mos"]
        words = [
            'them',
            'themselves',
            'theme',
            'themes',
            'themis',
            'thematic',
        ]
        trie = Trie.create_from_file()
        respons = trie.prefix_search("them")
        for word in words:
            if self.find_index(word, respons) == -1:
                self.assertIn(word, respons)
        self.assertEqual(len(respons), len(words), ["Förväntar att antalet ord i listan är:", "Det fanns:"])



    @staticmethod
    def find_index(word, container):
        for index, element in enumerate(container):
            if isinstance(element, str):
                if word == element:
                    return index
            elif word in element:
                return index
        return -1


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)