#!/usr/bin/env python3

"""
Python dbwebb module for asserting and auto correcting labs.

It reads the answers from a json-file and use it
for checking with assert_equal().
"""

import json
import sys
import os


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

        "correct": """{prompt} {question} CORRECT. Well done!""",

        "fail": """{prompt} {question} FAIL.
{prompt} You said:
{answer} {type}
{prompt}""",

        "hint": """Hint:
{answer} {type}""",

        # pylint: disable=line-too-long
        "done": """{prompt} Done with status {total}/{correct}/{failed}/{not_done} (Total/Correct/Failed/Not done).""",  # noqa

        "pointspass": """{prompt} Points earned: {points}p of {total}p (PASS=>{passval}p).""",  # noqa

        "pointspassdistinct": """{prompt} Points earned: {points}p of {total}p (PASS=>{passval}p PASS W DISTINCTION=>{passdistinct}p).""",  # noqa

        "passdistinct": "\033[96m{prompt}Grade: PASS WITH DISTINCTION!!! :-D\033[0m",
        "pass": "\033[92m{prompt}Grade: PASS! :-)\033[0m",

        # pylint: enable=line-too-long
        "no_pass": "\033[93m{prompt}Grade: Thou Did Not Pass. :-|\033[0m"
    }

    def __init__(self, answersFileName=".answer.json"):
        """
        Init by reading json-file with answers.
        """
        location = os.path.realpath(
            os.path.join(
                os.getcwd(),
                os.path.dirname(__file__)
            )
        )
        self.answers = json.load(open(os.path.join(location, answersFileName)))
        self.correct = 0
        self.failed = 0
        self.not_done = 0
        self.points = 0
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

        if answer == self._text["default"]:
            status = self._text["no_answer"].format(
                prompt=self.prompt,
                question=question
            )
            self.not_done += 1

        elif answer == self.answers["answers"][question]:
            status = self._text["correct"].format(
                prompt=self.prompt,
                question=question
            )
            self.correct += 1
            self.points += self.answers["points"][question]

        else:
            status = self._text["fail"].format(
                prompt=self.prompt,
                question=question,
                answer=answer,
                type=str(type(answer))
            )

            if hint:
                status += self._text["hint"].format(
                    answer=self.answers["answers"][question],
                    type=str(type(self.answers["answers"][question]))
                )

            self.failed += 1

        print(status)

    def exit_with_summary(self):
        """
        Print a exit message with the result of all tests.
        Exit with status 0 if all tasks are solved, else exit with status 1.
        """
        questions = self.answers["summary"]["questions"]
        points = self.answers["summary"]["points"]
        pass_val = self.answers["summary"]["pass"]
        pass_distinct = self.answers["summary"]["passdistinct"]

        print(self._text["done"].format(
            prompt=self.prompt,
            total=questions,
            correct=self.correct,
            failed=self.failed,
            not_done=self.not_done
        ))

        if pass_distinct:
            print(self._text["pointspassdistinct"].format(
                prompt=self.prompt,
                points=self.points,
                total=points,
                passval=pass_val,
                passdistinct=pass_distinct
            ))
        elif pass_val:
            print(self._text["pointspass"].format(
                prompt=self.prompt,
                points=points,
                total=questions,
                passval=pass_val
            ))


        # Grading
        did_pass = self.correct == questions
        if pass_val:
            did_pass = self.points >= pass_val

        did_pass_distinct = None
        if pass_distinct:
            did_pass_distinct = self.points >= pass_distinct

        if did_pass_distinct:
            print(self._text["passdistinct"].format(prompt=self.prompt))
            sys.exit(0)
        elif did_pass:
            print(self._text["pass"].format(prompt=self.prompt))
            sys.exit(0)
        else:
            print(self._text["no_pass"].format(prompt=self.prompt))
            sys.exit(42)
