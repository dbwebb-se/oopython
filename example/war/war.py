#!/usr/bin/env python3
"""
War game file
"""

import sys
from deck import Deck
from hand import Hand

class War():
    """
    War class
    """

    players = []

    def __init__(self, players):
        """init method"""
        self.deck = Deck()

        for _player in range(players):
            self.players.append(Hand([]))

    def new_game(self):
        """inits a new game"""
        self.deck.reset_cards()
        self.deck.shuffle()

        for player in self.players:
            for _ in range(int(52/len(self.players))):
                player.add_card(self.deck.take_card())

    def check_cards(self):
        """Check if cards are same suit"""
        if self.players[0].peek().get_suit() == self.players[1].peek().get_suit():
            if self.players[0].peek().get_value() > self.players[1].peek().get_value():
                print("\nPlayer 1 wins the round and picks up all cards.")
                self.players[0].add_cards(self.players[0].get_base())
                self.players[0].add_cards(self.players[1].get_base())
                self.players[0].clear_base()
                self.players[1].clear_base()
            else:
                self.players[1].add_cards(self.players[0].get_base())
                self.players[1].add_cards(self.players[1].get_base())
                self.players[1].clear_base()
                self.players[0].clear_base()
                print("\nplayer 2 wins the round and picks up all cards.")

            print(
                "Status: \nPlayer 1: {} cards\nPlayer 2: {} cards".format(
                    self.players[0].count_cards(),
                    self.players[1].count_cards())
            )



    def start_game(self):
        """starts one round of War"""

        print("\nNew round!")
        while True:
            for index, player in enumerate(self.players):
                if player.count_cards() == 52:
                    print("Player " + str(index) + " won!")
                    sys.exit(0)
                elif player.count_cards() < 1:
                    print("Player " + str(index) + " lost!")
                    sys.exit()
                else:
                    drawn_card = player.take_card()
                    print("\nPlayer {} draws {}\n".format(index+1, drawn_card))
                    player.add_to_base(drawn_card)


                input("Press any key to continue...")

            self.check_cards()
