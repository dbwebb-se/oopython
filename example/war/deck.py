#!/usr/bin/env python3

"""
Class file for Deck
"""

import random
from card import Card

class Deck():
    """
    Represents a card deck
    """
    counter = 0

    def __init__(self, cards=None):
        """
        Initialize deck with 52 Cards
        """
        self.cards = cards if cards else []

    def shuffle(self):
        """
        Shuffle card deck
        """
        random.shuffle(self.cards)

    def __str__(self):
        """
        overrider str to print all cards in the deck
        """
        return "\n".join(str(x) for x in self.cards)

    def take_card(self):
        """
        Takes bottom card
        """
        return self.cards.pop()

    def add_card(self, card):
        """
        Adds card to deck
        """
        self.cards.append(card)

    def reset_cards(self):
        """
        Resets deck to original state
        """
        self.cards = []
        for suit in range(4):
            for value in range(1, 14):
                self.cards.append(Card(value, suit))
