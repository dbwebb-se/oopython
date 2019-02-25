#!/usr/bin/env python3
"""
ska bestå av enhetstester för klassen Hand.
Alla medlemsvariabler och metoder ska testas.
Spara den i mappen war.
"""
import unittest
from main import Hand

class TestHand(unittest.TestCase):
    """docstring for TestHand."""
    hand = Hand()
    card = ""
    hand_two = Hand()
     # Tests if the objects are the same
    def test_a_equal_objects(self):
        """ Should return True, they are not the same """
        self.assertIsNot(self.hand, self.hand_two)
    # Tests if the objects are instances of Person
    def test_b_are_object_instance_of(self):
        """ Should return True, is instance of Hand """
        self.assertIsInstance(self.hand, Hand)
    #test if hand starts out empty
    def test_c_is_object_empty(self):
        """check if hand is empty"""
        self.assertEqual(len(self.hand.cards), 0)
    #Test if hand can make full deck.
    def test_d_fill_deck(self):
        """test to fill the hand"""
        self.hand.fill_deck()
        self.assertEqual(len(self.hand.cards), 52)
    #Test if Hand can draw card and that hand loose one card when done
    def test_e_draw_card(self):
        """test if draw card works and returns the bottom card"""
        self.card = str(self.hand.draw_card())
        self.assertEqual("King of Hearts", self.card)
        self.assertEqual(len(self.hand.cards), 51)
    def test_f_add_card(self):
        """test if add card returns the removed card from earlier"""
        self.hand.add_card(self.card)
        self.assertEqual(len(self.hand.cards), 52)


if __name__ == "__main__":
    unittest.main()
