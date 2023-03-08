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

class Test2TrieExtra(ExamTestCase):
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


    @staticmethod
    def find_index(word, container):
        for index, element in enumerate(container):
            if word == element.split(" ")[0]:
                return index
        return -1

    @tags("4")
    def test_a_prefix_with_frequency_10(self):
        """
        Testar att anropa prefix_search() med argument där det finns 10 förslag.
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._argument  = "alo"
        trie = Trie.create_from_file()
        words = [
            ('alone', 272173.0),
            ('along', 251163.0),
            ('aloud', 32565.4),
            ('alongside', 10349.6),
            ('aloft', 10098.0),
            ('aloof', 6721.47),
            ('aloofness', 1044.29),
            ('aloe', 439.079),
            ('aloneness', 74.3666),
            ('alopecia', 15.8226)
        ]
        respons = trie.prefix_search("alo")
        self.assertEqual(respons, words)


    @tags("4")
    def test_a_prefix_with_frequency_more_10(self):
        """
        Testar att anropa prefix_search() med argument där det finns mer än 10 förslag.
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._argument  = "hel"
        trie = Trie.create_from_file()
        words = [
            ('help', 243712.0),
            ('held', 235474.0),
            ('helped', 40487.8),
            ('hell', 31770.3),
            ('helpless', 23213.4),
            ('helping', 14882.8),
            ('helm', 7541.09),
            ('helmet', 7365.46),
            ('helpful', 4989.68),
            ('helper', 2847.29)
        ]
        respons = trie.prefix_search("hel")
        self.assertEqual(respons, words)


    @tags("4")
    def test_a_prefix_no_match(self):
        """
        Testar att anropa prefix_search() med argument där prefix inte finns.
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._argument  = "xyz"
        trie = Trie.create_from_file()
        words = []
        respons = trie.prefix_search("xyz")
        self.assertEqual(respons, words)



    @tags("5")
    def test_b_correct_same_word(self):
        """
        Testar att correct_spelling returnerar korrekt när argumentet är ett befintligt ord.
        Trie objektet innehåller följande ord: [hej, hoj, haj, dej]
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        self._argument  = "hej"
        trie = Trie()
        trie.add_word("hej")
        trie.add_word("hoj")
        trie.add_word("haj")
        trie.add_word("dej")
        self.assertEqual(trie.correct_spelling("hej"), ["hej"])


    @tags("5")
    def test_b_correct_first_letter(self):
        """
        Testar att correct_spelling returnerar korrekt när argumentet har felstavad första bokstav.
        Trie objektet innehåller följande ord: [absent, obsent, absene, xbsnt]
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        self._argument  = "xbsent"
        trie = Trie()
        trie.add_word("absent")
        trie.add_word("obsent")
        trie.add_word("absene")
        trie.add_word("xbsnt")
        self.assertEqual(trie.correct_spelling("xbsent"), ['absent', 'obsent'])


    @tags("5")
    def test_b_correct_middle_letter(self):
        """
        Testar att correct_spelling returnerar korrekt när argumentet har felstavad bokstav mitt i.
        Trie objektet innehåller följande ord: [flare, flake, fxary, glare, xare]
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        self._argument  = "fxare"
        trie = Trie()
        trie.add_word("flare")
        trie.add_word("flake")
        trie.add_word("fxary")
        trie.add_word("glare")
        trie.add_word("xare")
        self.assertEqual(trie.correct_spelling("fxare"), ['flake', 'flare'])


    @tags("5")
    def test_b_correct_many_matches(self):
        """
        Testar att correct_spelling returnerar korrekt när argumentet har möjliga matchningar.
        Skapar Trie objektet med Trie.create_from_file().
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        self._argument  = "xlare"
        trie = Trie.create_from_file()
        self.assertEqual(trie.correct_spelling("xlare"), ['blade', 'blame', 'blate', 'blaze', 'flake', 'flame', 'flare', 'glade', 'glare', 'glaze', 'place', 'plane', 'plate', 'slate', 'slave'])


    @tags("5")
    def test_b_correct_no_matches(self):
        """
        Testar att correct_spelling returnerar korrekt när argumentet inte har några möjliga matchningar.
        Skapar Trie objektet med Trie.create_from_file().
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        self._argument  = "ntax"
        trie = Trie.create_from_file()
        self.assertEqual(trie.correct_spelling("ntax"), [])



    @tags("5")
    def test_b_correct_many_different_matches(self):
        """
        Testar att correct_spelling returnerar korrekt när argumentet har flera möjliga matchningar på olika sätt.
        Trie objektet innehåller följande ord: [frake, great, flore, glare, fnate, frami, fldre]
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        self._argument  = "flare"
        trie = Trie()
        trie.add_word("glare")
        trie.add_word("flore")
        trie.add_word("great")
        trie.add_word("frake")
        trie.add_word("fnate")
        trie.add_word("frami")
        trie.add_word("fldre")

        self.assertEqual(trie.correct_spelling("flare"), ['fldre', 'flore', 'fnate', 'frake', 'glare'])



    @tags("6")
    def test_c_suffix(self):
        """
        Testar att anropa suffix_search() med argument där ord matchar flera.
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._argument  = "alo"
        trie = Trie.create_from_file()
        words = [
            'buffalo',
            'cembalo',
            'halo'
        ]
        respons = trie.suffix_search("alo")
        self.assertEqual(respons, words)

    @tags("6")
    def test_c_suffix_is_a_word(self):
        """
        Testar att anropa suffix_search() med argument där suffixet också är ett ord.
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._argument  = "chief"
        trie = Trie.create_from_file()
        words = ['chief', 'handkerchief', 'kerchief', 'mischief']
        # respons = trie.suffix_search("shed")
        # respons = trie.suffix_search("appointed")
        # respons = trie.suffix_search("chief")
        respons = trie.suffix_search("chief")
        self.assertEqual(respons, words)



    @tags("6")
    def test_c_suffix_no_match(self):
        """
        Testar att anropa suffix_search() med argument där suffixet inte finns.
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._argument  = "xyz"
        trie = Trie.create_from_file()
        words = []
        respons = trie.suffix_search("xyz")
        self.assertEqual(respons, words)


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
