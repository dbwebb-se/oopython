import treevizer
from random import randint

def bubble_sort(array):
    """
    O(n^2)
    """
    n = len(array)

    for i in range(n): # O(n)
        already_sorted = True

        for j in range(n - i - 1): # O((n-1)/2)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array
    # O(n) * O((n-1)/2) --> O(½n^2 - ½n)
    # ½n^2 - ½n --> n^2 - n
    # n^2 -n --> n^2








def insertion_sort(items):
    """
    O(n^2)
    """
    # O(n-1)
    for i in range(1, len(items)):
            j = i
            # 1, 2, 3, 4...n
            while j > 0 and items[j] < items[j-1]:
                    (items[j], items[j-1]) = (items[j-1], items[j])
                    j -= 1
    # O(n-1)*(n) --> O(n²)
    return items









# @treevizer.recursion_viz
def quicksort(array):
    """
    O(n log2n)
    """
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array: # O(n) + n/2 + n/2 + n/4 + n/4 ....
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)
    # O((n-1, -2, -3 ...)/2) + ? + O((n-1, -2, -3 ...)/2)
    #  --> (log n)
    #          2
    # O(n) * O(log n) -->  O(n log n).
    #             2               2

if __name__ == "__main__":
    print(quicksort([2,5,1,5,2,6,6,3,8]))
    treevizer.recursion_to_png("quicksort")