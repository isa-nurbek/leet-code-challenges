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
def powerset_iterative(array):
    result = [[]]  # start with the empty subset

    for elem in array:
        # For each element, add it to all existing subsets
        new_subsets = [subset + [elem] for subset in result]
        result.extend(new_subsets)

    return result


# Test Cases:

print(powerset_iterative([1, 2, 3]))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

print(powerset_iterative([]))
# Output: [[]]
