#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
import os
import random
import sys
from io import StringIO
from unittest.mock import patch
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
queue = import_module(REPO_PATH, 'src/queue')
node = import_module(REPO_PATH, 'src/node')
from src.errors import EmptyQueueException

class Test1Queue(ExamTestCase):
    """
    Testing the class Queue.
    """
    def setUp(self):
        """ Create object for all tests """
        # Arrange
        self.queue = queue.Queue()
        self.first_node_value = "value"
        self.second_node_value = "value_two"

    def tearDown(self):
        """ Remove dependencies after test """
        self.queue = None

    def test_is_empty_true(self):
        """
        Testar att skapa en kö och att den är tom.
        Förväntar att is_empty() returnerar True:
        {correct}
        Innehöll följande:
        {student}
        """
        self.assertEqual(self.queue.is_empty(), True)

    def test_is_empty_false(self):
        """
        Testar att skapa en kö och lägga till noder i kön.
        Förväntar att is_empty() returnerar False:
        {correct}
        Innehöll följande:
        {student}
        """
        self.queue.enqueue(self.first_node_value)
        self.assertEqual(self.queue.is_empty(), False)

    def test_enqueue_node(self):
        """
        Testar att skapa en kö och lägga till 1 nod i kön.
        Förväntar att queue.head.data innehåller "value":
        {correct}
        Innehöll följande:
        {student}
        """
        self.queue.enqueue(self.first_node_value)
        self.assertEqual(self.queue.head.data, self.first_node_value)

    def test_enqueue_2_nodes(self):
        """
        Testar att skapa en kö och lägga till 2 noder i kön. Första noden innehåller
        "value" och andra noden "value_two". Andra noden ska läggas sist i kön.
        Förväntar att queue.head.data returnerar "value":
        {correct}
        Innehöll följande:
        {student}
        """
        self.queue.enqueue(self.first_node_value)
        self.queue.enqueue(self.second_node_value)
        self.assertEqual(self.queue.head.data, self.first_node_value)

    def test_peek(self):
        """
        Testar att skapa en kö och lägga till 2 noder i kön. Titta på första noden.
        Förväntar att peek() returnerar "value":
        {correct}
        Innehöll följande:
        {student}
        """
        self.queue.enqueue(self.first_node_value)
        self.queue.enqueue(self.second_node_value)
        self.assertEqual(self.queue.peek(), self.first_node_value)

    def test_size(self):
        """
        Testar att skapa en kö och lägga till 2 noder i kön.
        Förväntar att size() returnerar 2:
        {correct}
        Innehöll följande:
        {student}
        """
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(self.first_node_value)
        self.queue.enqueue(self.second_node_value)
        self.assertEqual(self.queue.size(), 2)

    def test_dequeue(self):
        """
        Testar att attributet är privat och heter _value.
        Förväntar att attributet heter _value:
        {correct}
        Innehöll följande:
        {student}
        """
        self.queue.enqueue(self.first_node_value)
        self.queue.enqueue(self.second_node_value)
        self.assertEqual(self.queue.dequeue(), self.first_node_value)
        self.assertEqual(self.queue.peek(), self.second_node_value)
        self.assertEqual(self.queue.size(), 1)

    def test_dequeue_empty(self):
        """
        Testar att ett exception kastas då dequeue() anropas på en tom queue.
        Förväntar att EmptyQueueException kastas:
        {correct}
        Innehöll följande:
        {student}
        """
        with self.assertRaises(EmptyQueueException):
            self.queue.dequeue()

    def test_peek_empty(self):
        """
        Testar att ett exception kastas då peek() anropas på en tom queue.
        Förväntar att EmptyQueueException kastas:
        {correct}
        Innehöll följande:
        {student}
        """
        # with self.assertRaises(self.error) as e:
        with self.assertRaises(EmptyQueueException):
            self.queue.peek()


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
