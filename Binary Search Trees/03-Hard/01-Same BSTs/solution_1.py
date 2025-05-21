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


# O(n) time | O(n) space
def same_bsts(array_one, array_two):
    if len(array_one) != len(array_two):
        return False

    if len(array_one) == 0 and len(array_two) == 0:
        return True

    if array_one[0] != array_two[0]:
        return False

    left_one = get_smaller(array_one)
    left_two = get_smaller(array_two)

    right_one = get_bigger_or_equal(array_one)
    right_two = get_bigger_or_equal(array_two)

    return same_bsts(left_one, left_two) and same_bsts(right_one, right_two)


def get_smaller(array):
    smaller = []

    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])

    return smaller


def get_bigger_or_equal(array):
    bigger_or_equal = []

    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger_or_equal.append(array[i])

    return bigger_or_equal


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
