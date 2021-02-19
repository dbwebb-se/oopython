"""
Tests a Binary Search Tree
"""
import unittest
from unittest.mock import patch
from io import StringIO
import utils
#pylint: disable=no-name-in-module,import-error
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
        seq = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]
        utils.list_to_bst(seq, self.bst)
        self.assertTrue(utils.is_bst(self.bst.root))



    def test_get(self):
        """ Test that get returns correct values """
        seq = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]
        utils.list_to_bst(seq, self.bst)
        (seq[5], seq[8]) = (seq[8], seq[5])
        self.bst.insert(seq[5], 5)
        self.bst.insert(seq[8], 8)
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
        seq = [1, 5, 2, 4, 3, 0, 9, 7, 8, 6]
        utils.list_to_bst(seq, self.bst)
        remove_seq = [5, 0, 2, 3, 4, 1, 6, 7, 8, 9]

        for k in remove_seq:
            v = seq.index(k)
            self.assertEqual(v, self.bst.remove(k))
            with self.assertRaises(KeyError):
                self.bst.get(k)
            self.assertTrue(utils.is_bst(self.bst.root))




    def test_del_error(self):
        """ Test that remove raise KeyError """
        with self.assertRaises(KeyError):
            self.bst.remove(3)
        seq = [1, 5, 2, 4, 3, 0, 9, 7, 8, 6]
        utils.list_to_bst(seq, self.bst)

        with self.assertRaises(KeyError):
            self.bst.remove(-1)
        with self.assertRaises(KeyError):
            self.bst.remove(len(seq)+1)
        self.assertTrue(utils.is_bst(self.bst.root))



    def test_inorder_traversal(self):
        """ Test the inorder traversal print"""
        seq = [3, 10, 4, 14, 1, 8, 2, 9, 12, 18, 16, 7, 0, 11, 17, 5, 13, 6, 19, 15]
        utils.list_to_bst(seq, self.bst)

        seq_dict = utils.list_to_dict(seq)# Done to get index for each value.
        sorted_keys = sorted(seq_dict.keys())# Get keys in order, values from seq list
        # use sorted keys to get values for they keys in order
        res = [str(seq_dict[i]) for i in sorted_keys]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.bst.inorder_traversal_print()
            printed_values = fake_out.getvalue().strip("\n")
            list_data = printed_values.split("\n")
            self.assertEqual(list_data, res)

if __name__ == '__main__':
    unittest.main(verbosity=3)
