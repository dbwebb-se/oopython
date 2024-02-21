"""
https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
"""
import matplotlib.pyplot as plt

def plot(x, y, title):
    plt.plot(x, y, 'b')
    plt.xlabel('Number of inputs')
    plt.ylabel('Number of steps')
    plt.title(title)
    plt.show()


# def constant_algo(items):
#     """
#     Finds the square of the first item in the list and then prints it on the screen.
#     O(1)
#     """
#     result = items[0] * items[0]
#     print(result)

# constant_algo([4, 5, 6, 8])
# x = [2, 4, 6, 8, 10, 12]
# y = [2, 2, 2, 2, 2, 2]
# plot(x, y, 'Constant Complexity')








# def linear_algo(items):
#     """
#     Displays all items in the list to the console.
#     O(n)
#     """
#     for item in items:
#         print(item)

# linear_algo([4, 5, 6, 8])
# x = [2, 4, 6, 8, 10, 12]
# y = [2, 4, 6, 8, 10, 12]
# plot(x, y, 'Linear Complexity')









def linear_algo2(items):
    """
    Print all items in input twice
    O(2n)
    But when n is infinity, 2*n doesn't matter and we count it as 
    O(n)
    """
    for item in items:
        print(item)

    for item in items:
        print(item)
    # O(n) + O(n) --> O(2n) --> O(n)

# linear_algo2([4, 5, 6, 8])
# x = [2, 4, 6, 8, 10, 12]
# y = [4, 8, 12, 16, 20, 24]
# plot(x, y, 'Linear Complexity2')










def quadratic_algo(items):
    """
    Nestled loops
    O(n^2)
    """
    for item in items:
        for item2 in items:
            print(item, ' ' ,item)
    # O(n) * O(n) --> O(n^2)

# quadratic_algo([4, 5, 6, 8])
# x = [2, 4, 6, 8, 10, 12]
# y = [4, 16, 36, 64, 100, 144]
# plot(x, y, 'Quardratic Complexity')










def logarithmic_algo(items):
    """
    Prints part of list
    O(log(n))
    """
    counter = 1
    while counter < (len(items)):
        print(items[counter]);
        counter *= 2
# logarithmic_algo([4, 5, 6, 8, 10, 12])
# x = [2, 4, 6, 8, 10, 12, 20]
# y = [1, 2, 3, 3, 3, 3, 4]
# plot(x, y, 'Logarithmic Complexity')











def complex_algo(items):
    """
    Print a bunch of stuff
    O(8) + O(2n) --> O(2n) --> O(n)
    For extremely large numbers, the constans become irrelevant
    """
    # O(5) Five constant steps
    for i in range(5):
        print ("Python is awesome")

    # O(n) 
    for item in items:
        print(item)

    # O(n)
    for item in items:
        print(item)

    # O(3)
    print("Big O")
    print("Big O")
    print("Big O")

    # O(5) + O(n) + O(n) + O(3)
    # O(8) + O(2n) --> O(2n)
    # O(n)

# complex_algo([4, 5, 6, 8])
# x = [2, 4, 6, 8, 10, 12]
# y = [4*2+8, 8*2+8, 12*2+8, 16*2+8, 20*2+8, 24*2+8]
# plot(x, y, 'Complex Complexity (O(n))')









def search_algo(num, items):
    """
    Find a value in list.
    Wors vs. best case scenario
    O(1) vs. O(n)
    """
    for item in items: #O(n)
        if item == num: 
            return True #O(?)
    return False # O(n)
nums = [2, 4, 6, 8, 10]

print(search_algo(2, nums))
