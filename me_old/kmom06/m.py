def balance(nums):
    left = 0
    right = sum(nums) #summa
    for i, n in enumerate(nums):
        right -= n
        if left == right:
            yield i
        left += n

num = [0, -3, 5, -4, -2, 3, 1, 0]
for i in balance(num):
    print(i)
# print(num)