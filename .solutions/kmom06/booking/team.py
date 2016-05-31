#!/usr/bin/env python3

"""
Team class file
"""

class Team(): # pylint: disable=too-few-public-methods
    """
    Class Team
    """
    def __init__(self, name):
        self.name = name

    def get_team_name(self):
        """
        Returns team name
        """
        return self.name

    def __str__(self):
        """
        Prints team name
        """
        return self.name
