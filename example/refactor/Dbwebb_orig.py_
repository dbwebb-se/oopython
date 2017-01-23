#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
Python dbwebb module for asserting and auto correcting labs.

It reads the answers from a json-file and use it
for checking with assertEqual().

"""

import json
import sys


class Dbwebb():
    """
    Class for autocorrecting labs.
    """

    def __init__(self, answersFileName="answer.json"):
        """
        Init by reading json-file with answers.
        """
        self.answers = json.load(open(answersFileName))
        self.correct = 0
        self.failed = 0
        self.notDone = 0
        self.prompt = ">>> "


    def assertEqual(self, question, answer, hint=False):
        """
        Check if the answer is correct or not, present a hint if asked for.
        """

        status = None
        noanswer = "Replace this text with the variable holding the answer."

        if answer == noanswer:
            status = self.prompt + question + " NOT YET DONE."
            self.notDone += 1
        
        elif answer == self.answers["answers"][question]:
            status = self.prompt + question + " CORRECT. Well done!\n" + json.dumps(answer)
            self.correct += 1
        
        else:
            status = self.prompt + question + " FAIL.\n"
            status += self.prompt + "You said:\n" + json.dumps(answer) + " "
            status += str(type(answer))
            status += "\n" + self.prompt
            if hint:
                status += "Hint:\n"
                status += json.dumps(self.answers["answers"][question]) + " "
                status += str(type(self.answers["answers"][question]))
            self.failed += 1

        return status
        

    def exitWithSummary(self):
        """
        Print a exit message with the result of all tests. Exit with status 0 if all
        tasks are solved, else exit with status 1.
        """
        msg = self.prompt + "Done with status {}/{}/{}/{} (Total/Correct/Failed/Not done)."
        total = len(self.answers["answers"])

        print(msg.format(total, self.correct, self.failed, self.notDone))

        # Grading

        if total == self.correct: 
            print("\033[92m{}Grade: PASS! :-)\033[0m".format(self.prompt))
            sys.exit(0)
        else:
            print("\033[93m{}Grade: Thou Did Not Pass. :-|\033[0m".format(self.prompt))
            sys.exit(42)
