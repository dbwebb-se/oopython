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
die = import_module(REPO_PATH, 'src/die')
hand = import_module(REPO_PATH, 'src/hand')


class Test2Hand(ExamTestCase):
    """
    Testing the class Hand.
    """
    def setUp(self):
        random.seed("yahtzee")
        self.hand = hand.Hand()

    @tags("hand")
    def test_to_create_a_hand(self):
        """
        Testar att skapa en hand som innehåller 5 tärningar med slumpade värden.
        Förväntar att attributet dice är en lista med 5 tärningar:
        {correct}
        Innehöll följande:
        {student}
        """
        student_dice_value = [self.hand.dice[0]._value, self.hand.dice[1]._value, self.hand.dice[2]._value, self.hand.dice[3]._value, self.hand.dice[4]._value]
        self.assertEqual(student_dice_value, [2, 4, 6, 2, 1])

    @tags("hand")
    def test_to_create_a_hand_with_dice(self):
        """
        Testar att skapa en hand som innehåller 5 tärningar med värden.
        Skapar handen med listan:
        [6, 6, 6, 6, 6]
        Förväntar att attributet dice är en lista med 5 tärningar:
        {correct}
        Innehöll följande:
        {student}
        """
        new_hand = hand.Hand([6, 6, 6, 6, 6])
        student_dice_value = [new_hand.dice[0]._value, new_hand.dice[1]._value, new_hand.dice[2]._value, new_hand.dice[3]._value, new_hand.dice[4]._value]
        self.assertEqual(student_dice_value, [6, 6, 6, 6, 6])

    @tags("hand")
    def test_to_roll_hand_specific_dice(self):
        """
        Testar att slå om specifika tärningarna i handen, med roll() metoden.
        Använder följande som argument:
        {arguments}
        Förväntar att attributet dice innehåller följande värden på sina tärningar:
        {correct}
        Innehöll följande:
        {student}
        """
        new_hand = self.hand
        self._argument = [0, 3, 4]
        new_hand.roll([0, 3, 4])
        student_dice_value = [new_hand.dice[0]._value, new_hand.dice[1]._value, new_hand.dice[2]._value, new_hand.dice[3]._value, new_hand.dice[4]._value]
        self.assertEqual(student_dice_value, [4, 4, 6, 1, 2])

    # @tags("hand")
    # def test_to_roll_hand_specific_dice_out_of_index(self):
    #     """
    #     Testar att slå om vissa av tärningarna i handen.
    #     Förväntar att attributet dice har fått följande värden:
    #     {correct}
    #     Innehöll följande:
    #     {student}
    #     """
    #     with self.assertRaises(IndexError):
    #         self.hand.roll([0, 6])


    @tags("hand")
    def test_magical_method_str(self):
        """
        Testar att den magiska funktionen __str__ funkar med str().
        Skapar en Hand med slumpade tärningar,
        Förväntar att följande sträng returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.assertEqual(str(self.hand), "2, 4, 6, 2, 1")

    @tags("hand")
    def test_to_list_random(self):
        """
        Testar att funktionen to_list funkar.
        Skapar en Hand med slumpade tärningar.
        Förväntar att följande lista returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.assertEqual(self.hand.to_list(), [2, 4, 6, 2, 1])

    @tags("hand")
    def test_to_list_med_inparametrar(self):
        """
        Testar att funktionen to_list funkar.
        Skapar Hane med följande list:
        [6, 6, 6, 6, 6]
        Förväntar att följande lista returneras:
        {correct}
        Fick följande:
        {student}
        """
        new_hand = hand.Hand([6, 6, 6, 6, 6])
        self.assertEqual(new_hand.to_list(), [6, 6, 6, 6, 6])


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
