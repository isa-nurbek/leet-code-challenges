# Problem Description:

"""
                                                Same BSTs

An array of integers is said to represent the `Binary Search Tree (BST)` obtained by inserting each integer in the array, from left
to right, into the `BST`.

Write a function that takes in two arrays of integers and determines whether these arrays represent the same `BST`.

Note that you're not allowed to construct any `BST`s in your code.

A `BST` is a `Binary Tree` that consists only of `BST` nodes. A node is said to be a valid `BST` node if and only if it satisfies
the `BST` property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the
values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
```

## Sample Output:
```
True 
// Both arrays represent the BST below

          10
       /     \
      8      15
    /       /   \
   5      12    94
 /       /     /
2       11    81
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(d) space - where `n` is the number of nodes in each array, respectively, and `d` is the depth
of the BST that they represent.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n²) time | O(d) space
def same_bsts(array_one, array_two):
    if len(array_one) != len(array_two):
        return False
    return _same_bsts_helper(array_one, array_two, 0, 0, float("-inf"), float("inf"))


def _same_bsts_helper(
    array_one, array_two, root_idx_one, root_idx_two, min_val, max_val
):

    if root_idx_one == -1 and root_idx_two == -1:
        return True

    if (root_idx_one == -1) != (root_idx_two == -1):
        return False

    if array_one[root_idx_one] != array_two[root_idx_two]:
        return False

    left_root_one = _find_next_smaller(array_one, root_idx_one, min_val)
    left_root_two = _find_next_smaller(array_two, root_idx_two, min_val)

    right_root_one = _find_next_larger_or_equal(array_one, root_idx_one, max_val)
    right_root_two = _find_next_larger_or_equal(array_two, root_idx_two, max_val)

    return _same_bsts_helper(
        array_one,
        array_two,
        left_root_one,
        left_root_two,
        min_val,
        array_one[root_idx_one],
    ) and _same_bsts_helper(
        array_one,
        array_two,
        right_root_one,
        right_root_two,
        array_one[root_idx_one],
        max_val,
    )


def _find_next_smaller(array, start_idx, min_val):
    for i in range(start_idx + 1, len(array)):
        if array[i] < array[start_idx] and array[i] >= min_val:
            return i
    return -1


def _find_next_larger_or_equal(array, start_idx, max_val):
    for i in range(start_idx + 1, len(array)):
        if array[i] >= array[start_idx] and array[i] <= max_val:
            return i
    return -1


# Test Case:

array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]

print(same_bsts(array_one, array_two))  # Output: True

# Both arrays represent the BST below
#           10
#        /     \
#       8      15
#     /       /   \
#    5      12    94
#  /       /     /
# 2       11    81
