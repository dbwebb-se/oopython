#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)


class Test5Tests(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """


    @tags("struct", "tests")
    def test_a_tests_dir_exist(self):
        """
        Testerna hittar inte mappen 'tests' som ska innehålla test filer.
        """
        self.assertTrue(os.path.isdir(f"{REPO_PATH}/tests/"))

    @tags("struct", "tests")
    def test_b_tests_dir_contain_tests(self):
        """
        'tests' mappen innehåller inte några test filer.
        """
        self.assertTrue(os.listdir(f"{REPO_PATH}/tests/"))



if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)