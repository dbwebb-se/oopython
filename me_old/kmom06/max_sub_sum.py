#!/usr/bin/env python3
import random
import math
import time

def max_sub_sum1(l):
    max_sum = 0
    for i in range(len(l)):# 0 - len
        for j in range(i,len(l)): # 0 - len | 1 - len
            part_sum = 0

            for k in range(i, j+1): # 0 - 0+1 | 0 - 1+1
                part_sum = part_sum + l[k]                
            if part_sum > max_sum:
                max_sum = part_sum
                
    return max_sum

def max_sub_sum2(l):
    max_sum = 0
    for i in range(len(l)):# 0 - len
        part_sum = 0
        for j in range(i,len(l)): # 0 - len | 1 - len
            part_sum = part_sum + l[j]

            if part_sum > max_sum:
                max_sum = part_sum
                
    return max_sum
    
def max_sub_sum3(l):
    max_sum = part_sum = 0
    for i in range(len(l)):# 0 - len
        part_sum += l[i]
        if part_sum > max_sum:
            max_sum = part_sum
        elif part_sum < 0:
            part_sum = 0
                
    return max_sum


def max_sub_sum_max(l):
    max_ending_here = max_so_far = l[0]
    
    for x in l[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def generate_random(nums, seed=0):
    numbers = []
    if seed:
        random.seed(seed)
    for i in range(nums):
        numbers.append(math.ceil(random.uniform(-50, 50)))
    return numbers

if __name__ == "__main__":
    numbers = generate_random(15000, 24)
    # start = time.time()
    # res = max_sub_sum1(numbers)
    # done = time.time() - start
    # print(done)
    # print(res)
    start = time.time()
    res = max_sub_sum2(numbers)
    done = time.time() - start
    print(done)
    print(res)
    start = time.time()
    res = max_sub_sum3(numbers)
    done = time.time() - start
    print(done)
    print(res)
    start = time.time()
    res = max_sub_sum_max(numbers)
    done = time.time() - start
    print(done)
    print(res)