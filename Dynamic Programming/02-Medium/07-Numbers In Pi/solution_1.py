# Problem Description:

"""
                                            Numbers In Pi

Given a string representation of the first `n` digits of `Pi` and a list of positive integers (all in string format), write a
function that returns the smallest number of spaces that can be added to the `n` digits of `Pi` such that all resulting numbers
are found in the list of integers.

> Note that a single number can appear multiple times in the resulting numbers.

For example, if `Pi` is `"3141"` and the numbers are `["1", "3", "4"]`, the number `"1"` is allowed to appear twice in the list
of resulting numbers after three spaces are added: `"3 | 1 | 4 | 1"`.

If no number of spaces to be added exists such that all resulting numbers are found in the list of integers, the function should
return `-1`.


## Sample Input:
```
pi = "3141592653589793238462643383279",
numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
```

## Sample Output:
```
2

// "314159265 | 35897932384626433832 | 79"
```

## Optimal Time & Space Complexity:
```
O(n³ + m) time | O(n + m) space - where `n` is the number of digits in `Pi` and `m` is the number of favorite numbers.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n³ + m) time | O(n + m) space
def numbersInPi(pi, numbers):
    numbersTable = {number for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, 0, {})

    return minSpaces if minSpaces != float("inf") else -1


def getMinSpaces(pi, numbersTable, idx, cache):
    if idx == len(pi):
        return -1

    if idx in cache:
        return cache[idx]

    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx : i + 1]

        if prefix in numbersTable:
            spacesInSuffix = getMinSpaces(pi, numbersTable, i + 1, cache)
            minSpaces = min(minSpaces, spacesInSuffix + 1)

    cache[idx] = minSpaces

    return minSpaces


# Test Case:

pi = "3141592653589793238462643383279"
numbers = [
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79",
]

print(numbersInPi(pi, numbers))
# Output: 2
