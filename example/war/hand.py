#!/usr/bin/env python3

"""
Class file for Hand
"""

from deck import Deck

class Hand(Deck):
    """
    Hand class
    """
    def __init__(self, cards):
        super().__init__(cards)
        self.base = []

    def reset_cards(self):
        """
        Resets deck to original state
        """
        self.cards = []

    def set_cards(self, cards):
        """
        Sets the cards
        """
        self.cards = cards

    def add_cards(self, cards):
        """
        Add a list of card to self
        """
        self.cards[:0] = cards

    def add_to_base(self, card):
        """
        Add card to base
        """
        self.base.append(card)

    def get_base(self):
        """
        Returns base
        """
        return self.base

    def peek(self):
        """
        peeks at the top card
        """
        return self.base[len(self.base)-1]

    def clear_base(self):
        """
        Clears base
        """
        self.base = []

    def count_cards(self):
        """Returns amount of cards"""
        return len(self.cards)
