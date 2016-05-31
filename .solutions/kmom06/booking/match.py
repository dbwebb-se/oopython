#!/usr/bin/env python3

"""
Match class file
"""

class Match(): # pylint: disable=too-few-public-methods
    """
    Class Match
    """
    def __init__(self, sport, teams):
        self.teams = teams
        self.sport = sport

    def __str__(self):
        """
        Prints match info
        """
        return "Sport: " + self.sport + "\nTeams: " + self.teams[0].get_team_name() \
+ " vs " + self.teams[1].get_team_name()
