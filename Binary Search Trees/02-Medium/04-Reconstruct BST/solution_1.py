# Problem Description:

"""
                                                Reconstruct BST

The pre-order traversal of a Binary Tree is a traversal technique that starts at the tree's root node and visits nodes in the
following order:

1. Current node
2. Left subtree
3. Right subtree

Given a `non-empty` array of integers representing the `pre-order traversal` of a `Binary Search Tree (BST)`, write a function that
creates the relevant BST and returns its root node.

The input array will contain the values of BST nodes in the order in which these nodes would be visited with a pre-order traversal.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
pre_order_traversal_values = [10, 4, 2, 1, 5, 17, 19, 18]
```

## Sample Output:
```
        10 
      /    \
     4      17
   /   \      \
  2     5     19
 /           /
1           18 
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array.
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


# O(n²) time | O(n) space
def reconstruct_bst(pre_order_traversal_values):
    if not pre_order_traversal_values:
        return None

    current_value = pre_order_traversal_values[0]
    right_subtree_root_idx = len(pre_order_traversal_values)

    for idx in range(1, len(pre_order_traversal_values)):
        value = pre_order_traversal_values[idx]
        if value >= current_value:
            right_subtree_root_idx = idx
            break  # This break is correct; we want the first occurrence

    left_subtree = reconstruct_bst(pre_order_traversal_values[1:right_subtree_root_idx])
    right_subtree = reconstruct_bst(pre_order_traversal_values[right_subtree_root_idx:])

    return BST(current_value, left_subtree, right_subtree)


# Helper function to print the tree in-order for testing
def in_order_traversal(tree):
    if tree is not None:
        in_order_traversal(tree.left)
        print(tree.value, end=" ")
        in_order_traversal(tree.right)


# Test Case:

pre_order = [10, 4, 2, 1, 5, 17, 19, 18]
tree = reconstruct_bst(pre_order)

in_order_traversal(tree)

#  Output: 1 2 4 5 10 17 18 19

#         10
#        /  \
#       4    17
#      / \    \
#     2   5    19
#    /        /
#   1        18
