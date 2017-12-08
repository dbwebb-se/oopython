#!/usr/bin/env python3

""" Example on recursion, Towers of Hanoi """

def move_tower(height, from_pole, to_pole, with_pole):
    """ Recursive function to move disks from poles """
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)

def move_disk(fp, tp):
    """ Print method, prints usage """
    print("moving disk from", fp, "to", tp)


move_tower(3, "A", "B", "C")
