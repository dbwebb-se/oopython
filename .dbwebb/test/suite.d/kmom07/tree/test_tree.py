#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import io
import unittest
import unittest.mock
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
BST = import_module(REPO_PATH, 'bst').BinarySearchTree

class Test2BST(ExamTestCase):
    """
    Testing the class List.
    """
    @classmethod
    def setUpClass(cls):
        """
        Is needed it the students write and read to files.
        """
        os.chdir(REPO_PATH)
        
    @staticmethod
    def list_to_bst(seq, bst):
        """
        Take list and insert value in BST.
        """
        for v in seq:
            bst.insert(v, str(v))

    @staticmethod
    def is_bst(root, l=None, r=None, parent=None):
        """Check is a tree fullfiles Binary Search Tree rules"""
        # Base condition
        if root is None:
            return True
        # if left node exist then check it has
        # correct data or not i.e. left node's data
        # should be less than root's data
        if l is not None and root.key < l.key:
            raise KeyError(f"Node with key {root.key}'s left child is not lower, it is {l.key}")
        # if right node exist then check it has
        # correct key or not i.e. right node's key
        # should be greater than root's key
        if r is not None and root.key > r.key:
            raise KeyError(f"Node with key {root.key}'s right child is not higher, it is {r.key}")

        # if check that the parent is correct node
        if root.parent is not parent:
            raise KeyError((
                f"Expected Node with key {root.key} to have parent with key {parent.key}"
                f" but it is {root.parent.key}"
            ))

        # check recursively for every node.
        return Test2BST.is_bst(root.left, l, root, root) and \
            Test2BST.is_bst(root.right, root, r, root)




    @tags("insert")
    def test_a_insert_small(self):
        """
        insert().
        Testar att lägg till element från följande lista i ordning. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Förväntar strukturen ska vara ett giltigt BST:
        {correct}
        Strukturen på trädet är inte ett giltigt träd.:
        {student}
        """
        seq = [5, 2, 10]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)
        self.assertTrue(self.is_bst(bst.root))


    @tags("insert")
    def test_b_insert_big(self):
        """
        insert().
        Testar att lägg till element från följande lista i ordning. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Förväntar strukturen ska vara ett giltigt BST:
        {correct}
        Strukturen på trädet är inte ett giltigt träd.:
        {student}
        """
        seq = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)
        self.assertTrue(self.is_bst(bst.root))



    @tags("insert")
    def test_b_insert_change_value(self):
        """
        insert().
        Testar att lägg till element från följande lista i ordning. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Sen används insert(3, "ny") igen för att ändra värdet på nyckeln som finns. 
        Förväntar nyckel 3 har värdet:
        {correct}
        Hade värdet:
        {student}
        """
        seq = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)
        bst.insert(3, "ny")
        self.assertEqual(bst.root.value, "ny")

    @tags("get")
    def test_c_get(self):
        """
        get().
        Testar att hämta värden från BST.
        Trädet är skapat med följande element. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Förväntar att en nyckel som argument returnerar samma värde som en sträng:
        {correct}
        .get() returnerade istället:
        {student}
        """
        self.norepr = True
        seq = [5, 2, 10, 7]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)
        for key in seq:
            self.assertEqual(bst.get(key), str(key))

    @tags("get")
    def test_d_get_error(self):
        """
        get().
        Testar att KeyError lyfts när man försöker hämta värde med nyckel som inte finns.
        Trädet är skapat med följande element. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Förväntar att KeyError lyfts
        {correct}
        """
        self.norepr = True
        seq = [5, 2, 10, 7]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)
        with self.assertRaises(KeyError):
            bst.get(0)


    @tags("get")
    def test_e_get_error_empty(self):
        """
        get().
        Testar att KeyError lyfts när man försöker hämta värde i ett tomt träd.
        Förväntar att KeyError lyfts
        {correct}
        """
        bst = BST()
        with self.assertRaises(KeyError):
            bst.get(2)


    @tags("remove")
    def test_f_remove_leaf(self):
        """
        remove().
        Testar att ta bort ett löv från BST.
        Trädet är skapat med följande element. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Testet kollar att remove(7) returnerar korrekt värde.
        {correct}
        Fick istället:
        {student}
        """
        seq = [5, 2, 10, 7]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)

        self.assertEqual(bst.remove(7), "7")
        self.assertTrue(self.is_bst(bst.root), ["Testet kollar att trädet fortfarande uppfyller strukturen hos ett BST efter remove(7).", "Det uppfyller inte BST kraven efter remove(7)."])
        with self.assertRaises(KeyError, msg=["Testet förväntar att get(7) lyfter exception efter remove(7)", "Exception lyftes inte vilket betyder att 7 finns kvar i trädet efter remove(7)."]):
            bst.get(7)


    @tags("remove")
    def test_g_remove_exception(self):
        """
        remove().
        Testar att remove() lyfter KeyError om nyckel inte finns.
        Trädet är skapat med följande element. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Förväntar att KeyError lyfts
        {correct}
        Exceptions lyftes inte:
        {student}
        """
        seq = [5, 2, 10, 7]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)

        with self.assertRaises(KeyError):
            bst.get(0)

    @tags("remove")
    def test_h_remove_parent(self):
        """
        remove().
        Testar att ta bort en förälder nod från BST.
        Trädet är skapat med följande element. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Testet kollar att remove(10) returnerar korrekt värde:
        {correct}
        Fick istället:
        {student}
        """
        seq = [5, 2, 10, 7, 12, 11]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)

        self.assertEqual(bst.remove(10), "10")
        self.assertTrue(self.is_bst(bst.root), ["Testet kollar att trädet fortfarande uppfyller strukturen hos ett BST efter remove(10).", "Det uppfyller inte BST kraven efter remove(10)."])
        with self.assertRaises(KeyError, msg=["Testet förväntar att get(10) lyfter exception efter remove(10)", "Exception lyftes inte vilket betyder att 10 finns kvar i trädet efter remove(10)."]):
            bst.get(10)


    @tags("remove")
    def test_i_remove_root(self):
        """
        remove().
        Testar att ta bort root noden från BST.
        Trädet är skapat med följande element. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Testet kollar att remove(5) returnerar korrekt värde:.
        {correct}
        Fick istället:
        {student}
        """
        seq = [5, 2, 10, 7]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)

        self.assertEqual(bst.remove(5), "5")
        self.assertTrue(self.is_bst(bst.root), ["Testet kollar att trädet fortfarande uppfyller strukturen hos ett BST efter remove(5).", "Det uppfyller inte BST kraven efter remove(5)."])
        with self.assertRaises(KeyError, msg=["Testet förväntar att get(5) lyfter exception efter remove(5)", "Exception lyftes inte vilket betyder att 5 finns kvar i trädet efter remove(5)."]):
            bst.get(5)


    @tags("remove")
    def test_j_remove_every_node(self):
        """
        remove().
        Testar att ta bort alla noder i trädet.
        Noderna tas bort i följande ordning:
        [5, 0, 2, 3, 14, 16, 4, 15, 1, 6, 12, 10, 7, 11, 8, 9]
        Trädet är skapat med följande element. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Testet kollar att remove() returnerar korrekt värde:
        {correct}
        Fick istället:
        {student}
        """
        seq = [9, 5, 2, 15, 4, 3, 11, 12, 10, 0, 1, 14, 16, 7, 8, 6]
        remove_seq = [5, 0, 2, 3, 14, 16, 4, 15, 1, 6, 12, 10, 7, 11, 8, 9]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)

        success_elements = "Har lyckats ta bort: "
        for i, key in enumerate(remove_seq):
            tmp = f"{success_elements}\nTestet kollar att remove({key}) returnerar korrekt värde:"

            self.fail_msg.what_msgs_from_assert = [tmp, f"Fick istället:"] # if error occurs in remove. Then the comments from previous loop is used. Since error in remove occurs before we send new values to the assertEqual method.
            self.fail_msg.correct_answer = str(key)

            self.assertEqual(bst.remove(key), str(key), [
                tmp,
                f"Fick istället:"
            ])

            tmp = f"{success_elements}\nTestet kollar att trädet fortfarande uppfyller strukturen hos ett BST efter remove({key})."
            tmp2 = f"Det uppfyller inte BST kraven efter remove({key})."
            self.fail_msg.what_msgs_from_assert = [tmp, tmp2]
            self.fail_msg.correct_answer = True

            self.assertTrue(
                self.is_bst(bst.root), [
                    tmp,
                    tmp2
            ])

            tmp = f"{success_elements}\nTestet förväntar att get({key}) lyfter exception efter remove({key})"
            tmp2 = f"Exception lyftes inte vilket betyder att {key} finns kvar i trädet efter remove({key})."

            with self.assertRaises(
                KeyError,
                msg=[
                    tmp,
                    tmp2
            ]):
                bst.get(key)
            success_elements += f"{key}, "
        self.assertEqual(bst.root, None, [f"{success_elements}\nTestet kollar att bst.root är None efter att alla element har tagits bort:", f"bst.root innehöll:"])



    @tags("remove")
    def test_k_always_remove_root(self):
        """
        remove().
        Testar att ta bort alla noder i trädet, genom alltid ta bort root noden.
        Noderna tas bort i följande ordning:
        [3, 4, 5, 6, 7, 8, 9, 1, 2, 0]
        Trädet är skapat med följande element. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Testet kollar att remove() returnerar korrekt värde:
        {correct}
        Fick istället:
        {student}
        """
        seq = [3, 8, 5, 6, 1, 0, 2, 4, 9, 7]
        remove_seq = [3, 4, 5, 6, 7, 8, 9, 1, 2, 0]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)
        success_elements = "Har lyckats ta bort: "

        for i, key in enumerate(remove_seq):
            tmp = f"{success_elements}\nTestet kollar att remove({key}) returnerar korrekt värde:"

            self.fail_msg.what_msgs_from_assert = [tmp, f"Fick istället:"] # if error occurs in remove. Then the comments from previous loop is used. Since error in remove occurs before we send new values to the assertEqual method.
            self.fail_msg.correct_answer = str(key)

            self.assertEqual(bst.remove(key), str(key), [
                tmp,
                f"Fick istället:"
            ])

            tmp = f"{success_elements}\nTestet kollar att trädet fortfarande uppfyller strukturen hos ett BST efter remove({key})."
            tmp2 = f"Det uppfyller inte BST kraven efter remove({key})."
            self.fail_msg.what_msgs_from_assert = [tmp, tmp2]
            self.fail_msg.correct_answer = True

            self.assertTrue(
                self.is_bst(bst.root), [
                    tmp,
                    tmp2
            ])

            tmp = f"{success_elements}\nTestet förväntar att get({key}) lyfter exception efter remove({key})"
            tmp2 = f"Exception lyftes inte vilket betyder att {key} finns kvar i trädet efter remove({key})."
            with self.assertRaises(
                KeyError,
                msg=[
                    tmp,
                    tmp2
            ]):
                bst.get(key)
            success_elements += f"{key}, "

        self.assertEqual(bst.root, None, [f"Testet kollar att bst.root är None efter att alla element har tagits bort:", f"bst.root innehöll:"])


    @tags("print")
    def test_l_print(self):
        """
        inorder_traversal_print().
        Testar att skriva ut alla noder i trädet.
        Trädet är skapat med följande element. Elementet används som nyckel och görs till en sträng för värdet.
        {arguments}
        Förväntar att följande värden skrivs ut i följande ordning:
        {correct}
        Fick istället:
        {student}
        """
        seq = [3, 10, 4, 14, 1, 8, 2, 9, 12, 18, 16, 17, 5, 13, 6, 19, 15]
        self._argument = seq
        bst = BST()
        self.list_to_bst(seq, bst)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            bst.inorder_traversal_print()
            printed_values = fake_out.getvalue().strip("\n")
            list_data = printed_values.split("\n")
            self.assertEqual(list_data, ['1', '2', '3', '4', '5', '6', '8', '9', '10', '12', '13', '14', '15', '16', '17', '18', '19'])


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
