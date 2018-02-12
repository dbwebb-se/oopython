#!/usr/bin/env python3
"""
Contains code for a function to be improved.
"""
import random
import math
import time

def func(numbers):
    """
    Analyze and run the code to discover what it does.
    Once you know what i does improve the code to lower the execution time.
    You are done when all the tests in test.py pass.
    """
    m_sum = 0
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            p_sum = 0

            for k in range(i, j+1):
                p_sum = p_sum + numbers[k]
            if p_sum > m_sum:
                m_sum = p_sum

    return m_sum





def generate_random(nums, seed=0):
    """
    Generate random numbers between -50 and 50.
    Use seed if sent.
    """
    numbers = []
    if seed:
        random.seed(seed)
    for _ in range(nums):
        numbers.append(math.ceil(random.uniform(-50, 50)))
    return numbers

if __name__ == "__main__":
    n = generate_random(200, 24)
    start = time.time()
    res = func(n)
    done = time.time() - start
    print(done)
    print(res)
