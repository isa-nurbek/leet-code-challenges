# Problem Description:

"""
                                                Min Height BST

Write a function that takes in a `non-empty sorted array` of distinct integers, constructs a BST from the integers, and returns
the root of the BST.

The function should minimize the height of the BST.

You've been provided with a `BST` class that you'll have to use to construct the BST.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or `None`.

A `BST` is valid if and only if all of its nodes are valid `BST` nodes.

> Note that the `BST` class already has an `insert` method which you can use if you want.


## Sample Input:
```
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
```

## Sample Output:
```
         10
       /     \
      2      14
    /   \   /   \
   1     5 13   15
          \       \
           7      22

// This is one example of a BST with min height that you could create from the input array.
// You could create other BSTs with min height from the same array; for example:

         10
       /     \
      5      15
    /   \   /   \
   2     7 13   22
 /           \
1            14
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value):
        # Initialize a BST node with a given value
        # Left and right children are initialized to None
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def min_height_bst(array):
    # Main function to construct a minimum-height BST from a sorted array
    # It calls the helper function with the full array range (start to end indices)
    return construct_min_height_bst(array, 0, len(array) - 1)


def construct_min_height_bst(array, start_idx, end_idx):
    # Helper function to recursively construct the BST
    # Base case: when start index exceeds end index, return None (no node)
    if end_idx < start_idx:
        return None

    # Find the middle index to make it the root of current subtree
    # This ensures the tree will be balanced (minimum height)
    middle_idx = (start_idx + end_idx) // 2

    # Create a new BST node with the middle value
    bst = BST(array[middle_idx])

    # Recursively construct the left subtree using the left half of the array
    bst.left = construct_min_height_bst(array, start_idx, middle_idx - 1)
    # Recursively construct the right subtree using the right half of the array
    bst.right = construct_min_height_bst(array, middle_idx + 1, end_idx)

    # Return the constructed node
    return bst


# Helper function to print the tree in-order for testing
def in_order_traversal(tree):
    # Perform in-order traversal (left, root, right) to print values in sorted order
    if tree is not None:
        in_order_traversal(tree.left)
        print(tree.value, end=" ")
        in_order_traversal(tree.right)


# Test Cases:

tree1 = min_height_bst([1, 2, 5, 7, 10, 13, 14, 15, 22])
in_order_traversal(tree1)
print()

#  Output: 1 2 5 7 10 13 14 15 22

#     10
#    /  \
#   2    14
#  / \   / \
# 1   5 13 15
#      \     \
#       7    22


tree2 = min_height_bst([1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36])
in_order_traversal(tree2)
print()

# Output: 1 2 5 7 10 13 14 15 22 28 32 36

#           13
#         /    \
#        5      28
#      /  \    /  \
#     2   10  15  32
#    /    / \   \   \
#   1    7  14  22  36
