#!/usr/bin/env python3

"""
Class file for Card
"""

class Card():
    """
    Represents card in a deck
    """

    names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

    def __init__(self, value, suit):
        """
        Value = 1-13
        suit = 0-3
        """
        self.value = value
        self.suit = suit

    def get_suit(self):
        """returns the suit"""
        return Card.suits[self.suit]

    def get_value(self):
        """returns the value"""
        return self.value

    def __str__(self):
        """
        Override str to return card name and suit
        """
        return "{} of {}".format(Card.names[self.value], Card.suits[self.suit])
