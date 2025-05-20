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
        self.value = value
        self.left = None
        self.right = None


def min_height_bst(array):
    return construct_min_height_bst(array, 0, len(array) - 1)


def construct_min_height_bst(array, start_idx, end_idx):
    if end_idx < start_idx:
        return None

    middle_idx = (start_idx + end_idx) // 2
    bst = BST(array[middle_idx])

    bst.left = construct_min_height_bst(array, start_idx, middle_idx - 1)
    bst.right = construct_min_height_bst(array, middle_idx + 1, end_idx)

    return bst


# Helper function to print the tree in-order for testing
def in_order_traversal(tree):
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
