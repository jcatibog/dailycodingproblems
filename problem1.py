"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def sum_exists(list_nums, k):
    exists = False
    for i, v in enumerate(list_nums):
        if k-v > 0:
            j = k - v
            if j in list_nums[i:]:
                exists = True

    return exists


test_list = [10, 15, 3, 7, 1]
k = 17

print(sum_exists(test_list, k))
