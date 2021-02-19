#!/usr/bin/env python3
""" Module for unittests """
# pylint: skip-file
import unittest
from queue import Queue
from node import Node
from errors import EmptyQueueException


class TestQueue(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    first_node_value = "value"
    second_node_value = "value_two"

    def setUp(self):
        """ Create object for all tests """
        # Arrange
        self.queue = Queue()

    def tearDown(self):
        """ Remove dependencies after test """
        self.queue = None

    def test_enqueue(self):
        """
        Test that one can add a node to the queue.
        """
        self.queue.enqueue(TestQueue.first_node_value)
        self.queue.enqueue(TestQueue.second_node_value)
        self.assertIsInstance(self.queue.head, Node)
        self.assertEqual(self.queue.head.data, TestQueue.first_node_value)

    def test_peek(self):
        """
        Test if the peek method returns the first node's data.
        """
        self.queue.enqueue(TestQueue.first_node_value)
        self.queue.enqueue(TestQueue.second_node_value)
        self.assertEqual(self.queue.peek(), TestQueue.first_node_value)

    def test_is_empty(self):
        """
        Tests if the is_empty method returns the correct boolean.
        """
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.enqueue(TestQueue.first_node_value)
        self.assertEqual(self.queue.is_empty(), False)

    def test_size(self):
        """
        Tests if the size method should return the correct size.
        """
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(TestQueue.first_node_value)
        self.queue.enqueue(TestQueue.second_node_value)
        self.assertEqual(self.queue.size(), 2)

    def test_dequeue(self):
        """
        Tests if dequeue removes the node and returns its data.
        """
        self.queue.enqueue(TestQueue.first_node_value)
        self.queue.enqueue(TestQueue.second_node_value)
        self.assertEqual(self.queue.dequeue(), TestQueue.first_node_value)
        self.assertEqual(self.queue.peek(), TestQueue.second_node_value)
        self.assertEqual(self.queue.size(), 1)

    def test_dequeue_empty(self):
        """
        An EmptyQueueException should be raised when one tries to remove a node
        from an empty queue.
        """
        with self.assertRaises(EmptyQueueException) as _:
            self.queue.dequeue()

    def test_peek_empty(self):
        """
        An EmptyQueueException should be raised when one tries to peek at the first node
        from an empty queue.
        """
        with self.assertRaises(EmptyQueueException) as _:
            self.queue.peek()


if __name__ == "__main__":
    unittest.main(verbosity=3)
