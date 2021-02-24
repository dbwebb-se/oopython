"""
Contains utility functions for testing a Binary Search Tree
"""
import random
random.seed("BST")

def random_seq(n):
    """Creat a list with random values from range"""
    return random.sample(range(n), n)

def random_seq_from_list(l):
    """Creat a list with random values from list"""
    return random.sample(l, len(l))

def shuffle(arr):
    """Shuffle an array"""
    random.shuffle(arr)

def is_bst(root, l=None, r=None, parent=None):
    """Check is a tree fullfilles Binary Search Tree rules"""
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
    return is_bst(root.left, l, root, root) and \
        is_bst(root.right, root, r, root)


def list_to_bst(seq, bst):
    """
    Take list and insert value in BST.
    Using values from list as keys and index from list as values in BST.
    """
    for v, k in enumerate(seq):
        bst.insert(k, v)

def list_to_dict(seq):
    """
    Take list and insert value in dict
    Using values from list as keys and index from list as values in BST.
    """
    d = {}
    for v, k in enumerate(seq):
        d[k] = v
    return d
