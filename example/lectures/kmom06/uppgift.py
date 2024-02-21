import random
import time


def get_k(items, k):
    return sorted(items, reverse=True)[k-1]


def quick_select(arr, n):
    # 0(log n)
    pivot = arr[0]
    below = [x for x in arr if x < pivot] # Alla element som är mindre än pivot
    above = [x for x in arr if x > pivot] # Alla element som är större än pivot

    num_less = len(below) # Hur många är mindre
    num_above_or_eq = len(arr) - len(above) # Hur många är större eller lika med

    if n < num_less: # Om värdet vi letar efter är mindre än antalet som är mindre
        return quick_select(below, n)
    elif n >= num_above_or_eq: # Om värdet är större än antalet element som är större än 
        return quick_select(above, n-num_above_or_eq)
    else:
        return pivot # Eller om det är pivot värdet vi letar efter


if __name__ == "__main__":
    n = 10000
    # n = 1000000
    random_list = random.sample(range(n * 10), n)
    # print("Hej")
    k = 5000
    # k = 50000
    start = time.time()
    median = get_k(random_list, k)
    end = time.time()
    print(median)
    print(end-start)

    # start = time.time()
    # median = quick_select(random_list, k)
    # end = time.time()
    # print(median)
    # print(end-start)
