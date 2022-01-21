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
rules = import_module(REPO_PATH, 'src/rules')

class Test3Rule(ExamTestCase):
    """
    Testing the class Rule.
    """
    @tags("rules")
    def test_rule_is_abc(self):
        """
        Testar att Rule är en abstrakt klass.
        Förväntar att pass eftersom metoden är tom:
        {correct}
        Innehöll följande:
        {student}
        """
        pass
        # self.assertTrue(issubclass(rules.Rule, ABC))

    # @tags("rules")
    # @patch("rules.Rules.__abstractmethods__", set())
    # def test_rule_has_points(self):
    #     """
    #     Testar att Rule har en abstrakt metod som heter points.
    #     Förväntar att True returneras:
    #     {correct}
    #     Innehöll följande:
    #     {student}
    #     """
    #     rule = rule.Rule()
    #     self.assertTrue(rules.Rule.points)


class Test4SameValueRule(ExamTestCase):
    """
    Testing the class SameValueRule.
    """
    def setUp(self):
        random.seed("yahtzee")
        self.hand = hand.Hand()

    @tags("rules")
    def test_points(self):
        """
        Testar att point returnerar rätt värde.
        Förväntar att 2 från (1*2):
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.SameValueRule(1, "1")
        self.hand.dice = [1, 3, 1, 4, 6]
        self.assertEqual(rule.points(self.hand), 1*2)

    @tags("rules")
    def test_points_missing_value(self):
        """
        Testar att point returnerar rätt värde när tärningar saknas.
        Förväntar att 0 (2*0):
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.SameValueRule(2, "2")
        self.hand.dice = [1, 3, 1, 4, 6]
        self.assertEqual(rule.points(self.hand), 2*0)

class Test5Ones(ExamTestCase):
    """
    Testing the class Ones.
    """
    @tags("rules")
    def test_ones_points(self):
        """
        Testar att Ones ger ifrån sig rätt antal poäng.
        Förväntar att 13 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.ones = rules.Ones()
        self.hand = hand.Hand([1, 3, 1, 4, 6])
        self.assertEqual(self.ones.points(self.hand), 1*2)

    @tags("rules")
    def test_ones_points_missing_value(self):
     """
     Testar att Ones ger ifrån sig rätt antal poäng när 1:or saknas.
     Förväntar att 0 (1*0) returneras:
     {correct}
     Innehöll följande:
     {student}
     """
     self.ones = rules.Ones()
     self.hand = hand.Hand([1, 3, 1, 4, 6])
     self.assertEqual(self.ones.points(self.hand), 1*2)

class Test5Twos(ExamTestCase):
    """
    Testing the class Twos.
    """
    @tags("rules")
    def test_twos_points(self):
        """
        Testar att Twos ger ifrån sig rätt antal poäng.
        Förväntar att 6 (2*3) returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.twos = rules.Twos()
        self.hand = hand.Hand([1, 2, 1, 2, 2])
        self.assertEqual(self.twos.points(self.hand), 2*3)

class Test5Threes(ExamTestCase):
    """
    Testing the class Threes.
    """
    @tags("rules")
    def test_threes_points(self):
        """
        Testar att Threes ger ifrån sig rätt antal poäng.
        Förväntar att 2 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.threes = rules.Threes()
        self.hand = hand.Hand([1, 3, 1, 4, 6])
        self.assertEqual(self.threes.points(self.hand), 3*1)


class Test5Fours(ExamTestCase):
    """
    Testing the class Fours.
    """
    @tags("rules")
    def test_fours_points(self):
        """
        Testar att Fours ger ifrån sig rätt antal poäng.
        Förväntar att 4 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.fours = rules.Fours()
        self.hand = hand.Hand([1, 3, 1, 4, 6])
        self.assertEqual(self.fours.points(self.hand), 4*1)

class Test5Fives(ExamTestCase):
    """
    Testing the class Fives.
    """
    @tags("rules")
    def test_fives_points(self):
        """
        Testar att Fives ger ifrån sig rätt antal poäng.
        Förväntar att 10 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.fives = rules.Fives()
        self.hand = hand.Hand([5, 5, 1, 4, 6])
        self.assertEqual(self.fives.points(self.hand), 5*2)

class Test5Sixes(ExamTestCase):
    """
    Testing the class Sixes.
    """
    @tags("rules")
    def test_sixes_points(self):
        """
        Testar att Sixes ger ifrån sig rätt antal poäng.
        Förväntar att 18 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.sixes = rules.Sixes()
        self.hand = hand.Hand([1, 3, 6, 6, 6])
        self.assertEqual(self.sixes.points(self.hand), 6*3)

class Test6ThreeOfAKind(ExamTestCase):
    """
    Testing the class TestThreeOfAKind.
    """
    @tags("rules")
    def test_three_of_a_kind_points(self):
        """
        Testar att ThreeOfAKind ger ifrån sig rätt antal poäng.
        Förväntar att 18 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.ThreeOfAKind()
        self.hand = hand.Hand([1, 3, 6, 6, 6])
        self.assertEqual(self.a_rule.points(self.hand), 6*3)

    @tags("rules")
    def test_three_of_a_kind_points_all_the_same(self):
        """
        Testar att ThreeOfAKind ger ifrån sig rätt antal poäng även om det är 5 6:or.
        Förväntar att 18 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.ThreeOfAKind()
        self.hand = hand.Hand([6, 6, 6, 6, 6])
        self.assertEqual(self.a_rule.points(self.hand), 6*3)

class Test6FourOfAKind(ExamTestCase):
    """
    Testing the class TestFourOfAKind.
    """
    @tags("rules")
    def test_four_of_a_kind_points(self):
        """
        Testar att FourOfAKind ger ifrån sig rätt antal poäng.
        Förväntar att 18 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.FourOfAKind()
        self.hand = hand.Hand([1, 6, 6, 6, 6])
        self.assertEqual(self.a_rule.points(self.hand), 6*4)

    @tags("rules")
    def test_four_of_a_kind_points_all_the_same(self):
        """
        Testar att FourOfAKind ger ifrån sig rätt antal poäng även om det är 5 6:or.
        Förväntar att 18 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.FourOfAKind()
        self.hand = hand.Hand([6, 6, 6, 6, 6])
        self.assertEqual(self.a_rule.points(self.hand), 6*4)

class Test7FullHouse(ExamTestCase):
    """
    Testing the class FullHouse.
    """
    @tags("rules")
    def test_full_house_points(self):
        """
        Testar att FullHouse ger ifrån sig rätt antal poäng.
        Förväntar att 25 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.FullHouse()
        self.hand = hand.Hand([1, 1, 6, 6, 6])
        self.assertEqual(self.a_rule.points(self.hand), 25)

    @tags("rules")
    def test_full_house_points_none(self):
        """
        Testar att FullHouse ger ifrån sig rätt antal poäng när det inte är full hus.
        Förväntar att 0 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.FullHouse()
        self.hand = hand.Hand([1, 1, 5, 6, 6])
        self.assertEqual(self.a_rule.points(self.hand), 0)

class Test7Yahtzee(ExamTestCase):
    """
    Testing the class Yahtzee.
    """
    @tags("rules")
    def test_yahtzee_points(self):
        """
        Testar att Yahtzee ger ifrån sig rätt antal poäng.
        Förväntar att 50 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.Yahtzee()
        self.hand = hand.Hand([1, 1, 1, 1, 1])
        self.assertEqual(self.a_rule.points(self.hand), 50)

    @tags("rules")
    def test_yahtzee_points_none(self):
        """
        Testar att Yahtzee ger ifrån sig rätt antal poäng när inte regeln uppfylls.
        Förväntar att 0 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.Yahtzee()
        self.hand = hand.Hand([1, 1, 1, 1, 6])
        self.assertEqual(self.a_rule.points(self.hand), 0)

class Test7Chance(ExamTestCase):
    """
    Testing the class Chance.
    """
    @tags("rules")
    def test_chance_points(self):
        """
        Testar att Chance ger ifrån sig rätt antal poäng.
        Förväntar att 17 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.Chance()
        self.hand = hand.Hand([1, 4, 1, 6, 5])
        self.assertEqual(self.a_rule.points(self.hand), 17)

class Test8SmallStraight(ExamTestCase):
    """
    Testing the class SmallStraight.
    """
    @tags("rules")
    def test_small_straight_points_end(self):
        """
        Testar att SmallStraight ger ifrån sig rätt antal poäng med 6 högst.
        Förväntar att 30 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.SmallStraight()
        self.hand = hand.Hand([1, 3, 6, 4, 5])
        self.assertEqual(self.a_rule.points(self.hand), 30)


    @tags("rules")
    def test_small_straight_points_beginning(self):
        """
        Testar att SmallStraight ger ifrån sig rätt antal poäng med 1 lägst.
        Förväntar att 30 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.SmallStraight()
        self.hand = hand.Hand([1, 3, 2, 2, 4])
        self.assertEqual(self.a_rule.points(self.hand), 30)

    @tags("rules")
    def test_small_straight_points_missing_values(self):
        """
        Testar att SmallStraight ger ifrån sig rätt antal poäng med värden som saknas i mitten.
        Förväntar att 0 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.SmallStraight()
        self.hand = hand.Hand([1, 3, 6, 6, 5])
        self.assertEqual(self.a_rule.points(self.hand), 0)

class Test9LargeStraight(ExamTestCase):
    """
    Testing the class LargeStraight.
    """
    @tags("rules")
    def test_large_straight_points_end(self):
        """
        Testar att LargeStraight ger ifrån sig rätt antal poäng med 6 högst.
        Förväntar att 40 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.LargeStraight()
        self.hand = hand.Hand([2, 3, 6, 4, 5])
        self.assertEqual(self.a_rule.points(self.hand), 40)


    @tags("rules")
    def test_large_straight_points_beginning(self):
        """
        Testar att LargeStraight ger ifrån sig rätt antal poäng med 1 lägst.
        Förväntar att 40 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.LargeStraight()
        self.hand = hand.Hand([1, 3, 2, 5, 4])
        self.assertEqual(self.a_rule.points(self.hand), 40)

    @tags("rules")
    def test_large_straight_points_missing_values(self):
        """
        Testar att LargeStraight ger ifrån sig rätt antal poäng med värden som saknas i mitten.
        Förväntar att 0 returneras:
        {correct}
        Innehöll följande:
        {student}
        """
        self.a_rule = rules.LargeStraight()
        self.hand = hand.Hand([1, 3, 6, 6, 5])
        self.assertEqual(self.a_rule.points(self.hand), 0)


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
