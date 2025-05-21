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
    """
    Determines if two arrays represent the same Binary Search Tree (BST).

    Args:
        array_one: First array representing BST nodes in insertion order
        array_two: Second array representing BST nodes in insertion order

    Returns:
        bool: True if both arrays represent the same BST, False otherwise
    """

    # First check: if arrays have different lengths, they can't represent same BST
    if len(array_one) != len(array_two):
        return False

    # Base case: empty arrays are considered same BSTs
    if len(array_one) == 0 and len(array_two) == 0:
        return True

    # Root values must be equal for BSTs to be same
    if array_one[0] != array_two[0]:
        return False

    # Get all elements less than root (left subtree) for both arrays
    left_one = get_smaller(array_one)
    left_two = get_smaller(array_two)

    # Get all elements greater than or equal to root (right subtree) for both arrays
    right_one = get_bigger_or_equal(array_one)
    right_two = get_bigger_or_equal(array_two)

    # Recursively check if both left and right subtrees are same BSTs
    return same_bsts(left_one, left_two) and same_bsts(right_one, right_two)


def get_smaller(array):
    """
    Helper function to get all elements smaller than the first element (root).

    Args:
        array: Input array representing a BST

    Returns:
        list: Elements smaller than root (left subtree elements)
    """
    smaller = []
    # Start from index 1 since index 0 is the root
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])

    return smaller


def get_bigger_or_equal(array):
    """
    Helper function to get all elements greater than or equal to the first element (root).

    Args:
        array: Input array representing a BST

    Returns:
        list: Elements greater than or equal to root (right subtree elements)
    """
    bigger_or_equal = []
    # Start from index 1 since index 0 is the root
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
