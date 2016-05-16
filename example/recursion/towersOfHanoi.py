#!/usr/bin/env python3

""" Example on recursion, Towers of Hanoi """

def moveTower(height, fromPole, toPole, withPole):
    """ Recursive function to move disks from poles """
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    """ Print method, prints usage """
    print("moving disk from", fp, "to", tp)


moveTower(3, "A", "B", "C")
