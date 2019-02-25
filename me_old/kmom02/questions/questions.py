"""
Contains all classes for the different types of questions
"""
class Question():
    """
    Base type question, free text
    """
    type = "text"

    def __init__(self, answer, text):
        self._answer = answer
        self._text = text

    @classmethod
    def get_type(cls):
        return cls.type

    def check_answer(self, respons):
        """
        Check if answer is correct
        """
        return self._answer.lower() == respons[0].lower()

    def get_text(self):
        """
        Return text of question
        """
        return self._text

class RadiobuttonQuestion(Question):
    """
    Gör denna klass efter checkboxes..
    Hur gör man här? Multipla arv för att få _alternatives och
    answer som string?
    Lösa med trait? Ta upp på en föreläsning efter veckan
    """
    type = "radiobutton"

    def __init__(self, answer, text, *alternatives):
        super().__init__(answer, text)
        self._alternatives = alternatives

    def get_alternatives(self):
        """
        Return all the question alternatives
        """
        return self._alternatives

class CheckboxQuestion(Question):
    """
    Class for checkbox type question
    """
    type = "checkbox"

    def __init__(self, answer, text, *alternatives):
        super().__init__(answer, text)
        self._alternatives = alternatives

    def get_alternatives(self):
        """
        Return all the question alternatives
        """
        return self._alternatives

    def check_answer(self, respons):
        """
        Extrauppgift, ge poäng för varje rätt istället för
         ett poäng för alla rätt.
        """
        if len(respons) == len(self._answer):
            for cor  in self._answer:
                if cor not in respons:
                    return False
            return True
        return False
