# Problem Description:

"""

                                            Permutations

Write a function that takes in an array of unique integers and returns an array of all `permutations` of those integers in
no particular order.

If the input array is empty, the function should return an empty array.


## Sample Input
```
array = [1, 2, 3]
```

## Sample Output
```
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Optimal Time & Space Complexity:
```
O(n * n!) time | O(n * n!) space - where `n` is the length of the input array.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n * n!) time | O(n * n!) space
def get_permutations(array):
    permutations = []
    permutations_helper(0, array, permutations)
    return permutations


def permutations_helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutations_helper(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# Test Cases:

print(get_permutations([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

print(get_permutations([1]))
# Output: [[1]]

print(get_permutations([]))
# Output: []
