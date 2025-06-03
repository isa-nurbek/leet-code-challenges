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
    # Convert the list of numbers into a set for O(1) lookups
    numbersTable = {number for number in numbers}

    # Start the recursive process from index 0 with an empty cache
    minSpaces = getMinSpaces(pi, numbersTable, 0, {})

    # Return the result (or -1 if no valid split was found)
    return minSpaces if minSpaces != float("inf") else -1


def getMinSpaces(pi, numbersTable, idx, cache):
    # Base case: if we've reached the end of the string, return -1
    # (we'll add 1 to this later, making it 0 spaces for the last number)
    if idx == len(pi):
        return -1

    # If we've already computed the result for this index, return it
    if idx in cache:
        return cache[idx]

    # Initialize minimum spaces to infinity (indicating no valid split found yet)
    minSpaces = float("inf")

    # Try all possible prefixes starting at current index
    for i in range(idx, len(pi)):
        prefix = pi[idx : i + 1]  # Get the substring from idx to i

        # If this prefix is one of our target numbers
        if prefix in numbersTable:
            # Recursively find the minimum spaces for the remaining string
            spacesInSuffix = getMinSpaces(pi, numbersTable, i + 1, cache)

            # Update the minimum spaces if this split leads to a better solution
            # We add 1 because each split adds one space between numbers
            minSpaces = min(minSpaces, spacesInSuffix + 1)

    # Store the computed result in cache before returning
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
