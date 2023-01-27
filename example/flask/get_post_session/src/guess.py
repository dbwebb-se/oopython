"""
Contains a Guess class
"""
class Guess:
    """
    Represents a guess in a guessing game
    """
    def __init__(self, value, attempt, correct=False):
        self.value = value
        self.attempt = attempt
        self.correct = correct

    def __str__(self):
        return f"Guessed {self.value} on attempt {self.attempt}, it was {self.correct}"
