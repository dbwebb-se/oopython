from random import randint
from timing import run_sorting_algorithm
from algos import bubble_sort, insertion_sort, quicksort

ARRAY_LENGTH = 20000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="sorted", array=array[::])
    
    # run_sorting_algorithm(algorithm="bubble_sort", array=array[::])
    # run_sorting_algorithm(algorithm="insertion_sort", array=array[::])
    run_sorting_algorithm(algorithm="quicksort", array=array[::])
