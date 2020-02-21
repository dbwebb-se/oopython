#!/usr/bin/env python3
"""
Contains the handler/manager class for the questions.
"""

class QuestionManager():
    """
    Manages all questions
    """

    def __init__(self):
        self._points = 0
        self._quest_count = 0




    def read_session(self, session):
        """
        Read current score and current quest number from session
        """
        self._points = session.get("points", 0)
        self._quest_count = session.get("quest_count", 0)

    def write_session(self, session):
        """
        Write current score and quest number to session
        """
        session["points"] = self._points
        session["quest_count"] = self._quest_count

    def reset(self):
        """
        Reset score and quest number to 0
        """
        self._quest_count = 0
        self._points = 0
