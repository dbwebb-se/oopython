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


    def assertEqual(self, question, answer, hint=False):
        """
        Check if the answer is correct or not, present a hint if asked for.
        """

        status = None
        noanswer = "Replace this text with the variable holding the answer."

        if answer == noanswer:
            status = question + " NOT YET DONE."
            self.notDone += 1
        
        elif answer == self.answers["answers"][question]:
            status = question + " CORRECT. Well done!\n" + json.dumps(answer)
            self.correct += 1
        
        else:
            status = question + " FAIL.\nYou said:\n" + json.dumps(answer)
            status += "\nHint:\n" + json.dumps(self.answers["answers"][question]) if hint else ""
            self.failed += 1

        return status
        

    def exitWithSummary(self):
        """
        Print a exit message with the result of all tests. Exit with status 0 if all
        tasks are solved, else exit with status 1.
        """
        msg = "Done with status {}/{}/{}/{} (Total/Correct/Failed/Not done)."
        total = len(self.answers["answers"])

        print(msg.format(total, self.correct, self.failed, self.notDone))

        if total == self.correct: 
            sys.exit(0)
        else:
            sys.exit(1)
