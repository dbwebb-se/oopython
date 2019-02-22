"""
Tests a Binary Search Tree
"""
import unittest
from unittest.mock import patch
from io import StringIO
import utils
from bst import BinarySearchTree as Bst


class TestBst(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Setup test """
        self.bst = Bst()

    def tearDown(self):
        """ teardown test """
        self.bst = None

    def test_insert(self):
        """ Test that insert creates binary search tree """
        size = 100
        seq = utils.random_seq(size)
        utils.list_to_bst(seq, self.bst)
        self.assertTrue(utils.is_bst(self.bst.root))

    def test_get(self):
        """ Test that get returns correct values """
        size = 20
        seq = utils.random_seq(size)
        utils.list_to_bst(seq, self.bst)
        (seq[5], seq[16]) = (seq[16], seq[5])
        self.bst.insert(seq[5], 5)
        self.bst.insert(seq[16], 16)
        for v, k in enumerate(seq):
            self.assertEqual(v, self.bst.get(k))

    def test_get_error(self):
        """ Test that get raises KeyError """
        with self.assertRaises(KeyError):
            self.bst.get(0)
        self.bst.insert(3, 16)
        with self.assertRaises(KeyError):
            self.bst.get(2)

    def test_del(self):
        """ Test that remove maintain correct structure in tree """
        size = 10
        seq = utils.random_seq(size)
        utils.list_to_bst(seq, self.bst)
        r_seq = utils.random_seq_from_list(seq)

        for k in r_seq:
            v = seq.index(k)
            self.assertEqual(v, self.bst.remove(k))
            self.assertTrue(utils.is_bst(self.bst.root))

    def test_del_error(self):
        """ Test that remove raise KeyError """
        with self.assertRaises(KeyError):
            self.bst.remove(3)
        size = 10
        seq = utils.random_seq(size)
        utils.list_to_bst(seq, self.bst)
        with self.assertRaises(KeyError):
            self.bst.remove(-1)
        with self.assertRaises(KeyError):
            self.bst.remove(size+1)
        self.assertTrue(utils.is_bst(self.bst.root))

    def test_inorder_traversal(self):
        """ Test the inorder traversal print"""
        size = 20
        seq = utils.random_seq(size)
        utils.list_to_bst(seq, self.bst)
        seq_dict = utils.list_to_dict(seq)
        sorted_keys = sorted(seq_dict.keys())
        res = [str(seq_dict[i]) for i in sorted_keys]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.bst.inorder_traversal_print()
            printed_values = fake_out.getvalue().strip("\n")
            list_data = printed_values.split("\n")
            self.assertEqual(list_data, res)

if __name__ == '__main__':
    unittest.main(verbosity=3)
