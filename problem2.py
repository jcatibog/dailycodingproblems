"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was[1, 2, 3, 4, 5], the expected output would be[120, 60, 40, 30, 24]. If our input was[3, 2, 1], the expected output would be[2, 3, 6].

Follow-up: what if you can't use division?
"""


def list_products(ints):
    sums = []

    for index, _ in enumerate(ints):
        sums.insert(index, product(
            [element for key, element in enumerate(ints) if key != index]
        ))

    return sums


def product(l):
    prod = 0

    for x in l:
        if prod == 0:
            prod = x
        else:
            prod = prod * x

    return prod


test_inputs = [
    [1, 2, 3, 4, 5],
    [3, 2, 1]
]

expected_outputs = [
    [120, 60, 40, 30, 24],
    [2, 3, 6]
]


for i, list_in in enumerate(test_inputs):
    result = list_products(list_in)

    print(result)
    print(result == expected_outputs[i])
