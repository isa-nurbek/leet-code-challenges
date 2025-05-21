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


# O(n) time | O(n) space
def reconstruct_bst(pre_order_traversal_values):
    """
    Reconstructs a Binary Search Tree (BST) from its pre-order traversal values.

    Args:
        pre_order_traversal_values: List of integers representing the pre-order traversal of a BST

    Returns:
        The root node of the reconstructed BST
    """

    def helper(lower_bound, upper_bound):
        """
        Helper function to recursively build the BST.

        Args:
            lower_bound: The minimum value a node in this subtree can have
            upper_bound: The maximum value a node in this subtree can have

        Returns:
            A BST node or None if no valid node can be created
        """
        nonlocal idx  # Use the idx variable from the outer function

        # If we've processed all values, return None (base case)
        if idx >= len(pre_order_traversal_values):
            return None

        current_value = pre_order_traversal_values[idx]

        # Check if current value is within valid BST bounds for this position
        if not (lower_bound <= current_value < upper_bound):
            return None  # Not a valid BST node here

        # Move to next value in pre-order list since we're using this one
        idx += 1

        # Recursively build left subtree with updated bounds:
        # - Left subtree values must be greater than lower_bound
        # - But less than current node's value
        left_subtree = helper(lower_bound, current_value)

        # Recursively build right subtree with updated bounds:
        # - Right subtree values must be greater than current node's value
        # - But less than upper_bound
        right_subtree = helper(current_value, upper_bound)

        # Create and return the current node with its subtrees
        return BST(current_value, left_subtree, right_subtree)

    # Initialize index to start of pre-order list
    idx = 0

    # Start the reconstruction with infinite bounds that will get refined
    return helper(float("-inf"), float("inf"))


def in_order_traversal(tree):
    """
    Performs in-order traversal (left -> root -> right) and prints node values.
    For a BST, this should print values in sorted order.
    """
    if tree is not None:
        in_order_traversal(tree.left)
        print(tree.value, end=" ")
        in_order_traversal(tree.right)


# Test Case:

pre_order = [10, 4, 2, 1, 5, 17, 19, 18]
tree = reconstruct_bst(pre_order)

in_order_traversal(tree)  # Output: 1 2 4 5 10 17 18 19

# Visual representation of the reconstructed tree:
#         10
#        /  \
#       4    17
#      / \    \
#     2   5    19
#    /        /
#   1        18
