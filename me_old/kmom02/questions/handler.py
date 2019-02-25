#!/usr/bin/env python3
"""
Contains the handler/manager class for the questions.
"""
from questions import Question, CheckboxQuestion, RadiobuttonQuestion

class QuestionManager():
    """
    Manages all questions
    """

    def __init__(self):
        self._questions = []
        self._points = 0
        self.quest_count = 0
        self._add_questions()

    def get_score(self):
        return self._points

    def get_max_score(self):
        return len(self._questions)

    def has_next(self):
        return self.quest_count < len(self._questions)

    def get_next(self):
        return self._questions[self.quest_count]
    
    def get_quest_count(self):
        return self.quest_count

    def correct_answer(self, form):
        current_question = self.get_next()
        if current_question.check_answer(form.getlist("answer")):
            self._points += 1
        self.quest_count += 1

    def read_session(self, session):
        self._points = session.get("points", 0)
        self.quest_count = session.get("quest_count", 0)

    def write_session(self, session):
        session["points"] = self._points
        session["quest_count"] = self.quest_count

    def reset(self):
        self.quest_count = 0
        self._points = 0

    def _add_questions(self):
        #pylint: disable=line-too-long
        self._questions.append(Question("Andreas", "Vem är bäst?"))
        self._questions.append(Question("Mikael", "Vad heter mos i förnamn?"))
        self._questions.append(Question("Kenneth", "Vem i lärarteamet har ägt en bar?"))

        self._questions.append(CheckboxQuestion(["Andreas", "Emil"], "Vilka började jobba på BTH 2016?", "Andreas", "Emil", "Kenneth"))
        self._questions.append(CheckboxQuestion(["Hund", "Katt"], "Vilka typer av husdjur har lärarteamet?", "Hund", "Undelat", "Katt", "Orm", "Ödla", "Fiskar"))
        self._questions.append(CheckboxQuestion(["Andreas", "Kenneth"], "Vilkar två har bott längst i Karlskrona?", "Andreas", "Emil", "Kenneth", "Mikael"))

        self._questions.append(RadiobuttonQuestion("Emil", "Vem är dansk?", "Andreas", "Emil", "Kenneth", "Mikael"))
        self._questions.append(RadiobuttonQuestion("15", "Hur många år har Mikael innan han får en guldklocka?", "17", "15", "13", "11", "10"))
        self._questions.append(RadiobuttonQuestion("Emil", "Vem har åkt Wasaloppet?", "Andreas", "Emil", "Kenneth"))
