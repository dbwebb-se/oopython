#!/usr/bin/env python3
"""
Deck, Hand och Card. Hand ska ärva från Deck som ska bestå av 52 stycken Card.
"""
import random

class Card:
    """docstring for Card."""
    ranks = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
             "Queen", "King"]
    suits = ["Club", "Diamond", "Spade", "Heart"]
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return "{} of {}s"\
        .format(self.ranks[self.value], self.suits[self.suit])

class Deck:
    """docstring for Deck."""
    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        """fyll deck med 52 cards"""
        self.cards = []
        for suit in range(4):
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def shuffle(self):
        """blanda leken"""
        random.shuffle(self.cards)

    def draw_card(self):
        """dra kort"""
        return self.cards.pop()

    def add_card(self, card):
        """lägg till kort"""
        self.cards.insert(0, card)

class Hand(Deck):
    """docstring for Hand."""
    def __init__(self):
        super().__init__()
        self.cards = []

class War:
    """docstring for War."""

    deck = Deck()
    deck.shuffle()
    stack = []
    counter = 0
    player1 = Hand()
    player2 = Hand()
    test1 = ""
    test2 = ""
    def start_war(self):
        """starta spelet"""
        self.create_hands()
        self.first_turn()
        input("Press enter to continue...")


        while self.player1.cards and self.player2.cards:
            self.stack.append(self.player2.draw_card())
            print("Player2: ", self.stack[self.counter])
            self.test2 = self.stack[self.counter]
            self.counter += 1
            self.test_cards(self.test1, self.test2)
            input("Press enter to continue...")
            self.stack.append(self.player1.draw_card())
            print("Player1: ", self.stack[self.counter])
            self.test1 = self.stack[self.counter]
            self.counter += 1
            self.test_cards(self.test1, self.test2)
            input("Press enter to continue...")
        if self.player1.cards:
            print("Player1 win")
        else:
            print("Player2 win")
    def test_cards(self, value1, value2):
        """Testa om samma suit och isf kolla vem som har högst kort"""
        if value1.suit == value2.suit:
            print("Same suit")
            if value1.value > value2.value:
                print("Player1 wins stack")
                for value in self.stack:
                    self.player1.add_card(value)
                print("""
                            Standings

                        Player1: {} cards
                        Player2: {} cards

                        """\
                    .format(len(self.player1.cards), len(self.player2.cards)))
            else:
                print("Player2 wins stack")
                for value in self.stack:
                    self.player2.add_card(value)
                print("""
                            Standings

                        Player1: {} cards
                        Player2: {} cards

                        """\
                    .format(len(self.player1.cards), len(self.player2.cards)))
            self.counter = 0
            self.stack = []
            input("Press enter to continue...")
            self.first_turn()


    def first_turn(self):
        """start omgången i spelet även efter någon vunnit en omgång"""
        self.stack.append(self.player1.draw_card())
        print("Player1: ", self.stack[self.counter])
        self.test1 = self.stack[self.counter]
        self.counter += 1

    def create_hands(self):
        """skapa spelar stacks"""
        for _ in range(26):
            self.player1.add_card(self.deck.draw_card())
            self.player2.add_card(self.deck.draw_card())



if __name__ == "__main__":
    war = War()
    war.start_war()
