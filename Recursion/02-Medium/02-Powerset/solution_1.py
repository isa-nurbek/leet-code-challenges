# Problem Description:

"""

                                            Powerset

Write a function that takes in an array of unique integers and returns its powerset.

The powerset `P(X)` of a set `X` is the set of all subsets of `X`. For example, the powerset of `[1, 2]` is `[[], [1], [2], [1,2]]`.

> Note that the sets in the powerset do not need to be in any particular order.


## Sample Input
```
array = [1, 2, 3]
```

## Sample Output
```
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

## Optimal Time & Space Complexity:
```
O(n * 2ⁿ) time | O(n * 2ⁿ) space - where `n` is the length of the input array.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n * 2ⁿ) time | O(n * 2ⁿ) space
def powerset(array, idx=None):
    # Handle initial call (no index provided)
    if idx is None:
        # Start with the last index of the array
        idx = len(array) - 1

    # Base case: when we've gone past the first element
    if idx < 0:
        # Return a list containing just the empty subset
        return [[]]

    # Get the current element we're processing
    elem = array[idx]

    # Recursively get all subsets without the current element
    subsets = powerset(array, idx - 1)

    # Return:
    # 1. All subsets that don't include the current element
    # 2. All subsets that do include the current element (created by adding
    #    the current element to each existing subset)
    return subsets + [subset + [elem] for subset in subsets]


# Test Cases:

print(powerset([1, 2, 3]))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

print(powerset([]))
# Output: [[]]
