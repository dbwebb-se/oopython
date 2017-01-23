#!/usr/bin/env python3

"""
Python dbwebb module for asserting and auto correcting labs.

It reads the answers from a json-file and use it
for checking with assert_equal().
"""

import json
import sys


class Dbwebb():
    """
    Class for autocorrecting labs.
    """

    # Texts
    _text = {
        "prompt": ">>> ",

        "ready": "{prompt} Ready to begin.",

        "default": "Replace this text with the variable holding the answer.",

        "no_answer": "{prompt} {question} NOT YET DONE.",

        "correct": """{prompt} {question} CORRECT. Well done!
{answer}""",

        "fail": """{prompt} {question} FAIL.
{prompt} You said:
{answer} {type}
{prompt}""",

        "hint": """Hint:
{answer} {type}""",

        # pylint: disable=line-too-long
        "done": """{prompt} Done with status {total}/{correct}/{failed}/{not_done} (Total/Correct/Failed/Not done).""",  # noqa
        # pylint: enable=line-too-long

        "pass": "\033[92m{prompt}Grade: PASS! :-)\033[0m",

        "no_pass": "\033[93m{prompt}Grade: Thou Did Not Pass. :-|\033[0m"
    }

    def __init__(self, answersFileName="answer.json"):
        """
        Init by reading json-file with answers.
        """
        self.answers = json.load(open(answersFileName))
        self.correct = 0
        self.failed = 0
        self.not_done = 0
        self.prompt = self._text["prompt"]

    def ready_to_begin(self):
        """
        Called before everything starts.
        """
        print(self._text["ready"].format(prompt=self.prompt))

    def assert_equal(self, question, answer, hint=False):
        """
        Check if the answer is correct or not, present a hint if asked for.
        """
        status = None

        if answer == self._text["no_answer"]:
            status = self._text["no_answer"].format(
                promtp=self.prompt,
                question=question
            )
            self.not_done += 1

        elif answer == self.answers["answers"][question]:
            status = self._text["correct"].format(
                prompt=self.prompt,
                question=question,
                answer=json.dumps(answer)
            )
            self.correct += 1

        else:
            status = self._text["fail"].format(
                prompt=self.prompt,
                question=question,
                answer=json.dumps(answer),
                type=str(type(answer))
            )

            if hint:
                status += self._text["hint"].format(
                    answer=self.answers["answers"][question],
                    type=str(type(self.answers["answers"][question]))
                )

            self.failed += 1

        return status

    def exit_with_summary(self):
        """
        Print a exit message with the result of all tests.
        Exit with status 0 if all tasks are solved, else exit with status 1.
        """
        total = len(self.answers["answers"])
        print(self._text["done"].format(
            prompt=self.prompt,
            total=total,
            correct=self.correct,
            failed=self.failed,
            not_done=self.not_done
        ))

        # Grading
        if total == self.correct:
            print(self._text["pass"].format(prompt=self.prompt))
            sys.exit(0)
        else:
            print(self._text["no_pass"].format(prompt=self.prompt))
            sys.exit(42)
