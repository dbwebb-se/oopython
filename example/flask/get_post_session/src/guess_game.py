"""
Main class for the guessing game
"""
import random
from src.guess import Guess

class GuessGame:
    """
    Holds info for playing a guessing game
    """
    def __init__(self, correct_value=None, guesses=None):
        if correct_value is not None:
            self._correct_value = correct_value
        else:
            self._correct_value = random.randint(0, 15)
        self.guesses = [Guess(v, a, c) for v, a, c in guesses] if guesses is not None else []
        self.guess_attempts = len(self.guesses)


    def make_guess(self, guess_value):
        """
        Makes a new guess and adds to list
        """
        self.guess_attempts += 1
        if guess_value == self._correct_value:
            self.guesses.append(Guess(guess_value, self.guess_attempts, True))
            return True
        self.guesses.append(Guess(guess_value, self.guess_attempts))
        return False


    def get_correct_value(self):
        """ Return private attribute """
        return self._correct_value

    def get_if_guessed_correct(self):
        """ return if last guess was correct or not """
        return self.guesses[-1].correct if self.guesses else False

    def to_list(self):
        """ Turn old guesses to a list """
        return [(g.value, g.attempt, g.correct) for g in self.guesses]
