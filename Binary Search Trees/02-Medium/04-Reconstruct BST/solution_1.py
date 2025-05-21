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
    """
    Reconstructs a BST from its pre-order traversal values.

    Pre-order traversal visits nodes in the order: root -> left -> right.
    The first element is always the root, followed by left subtree nodes (all < root),
    then right subtree nodes (all >= root).

    Args:
        pre_order_traversal_values: List of values in pre-order traversal order

    Returns:
        The root node of the reconstructed BST
    """
    # Base case: empty list means we've reached a leaf node's child
    if not pre_order_traversal_values:
        return None

    # The first value in pre-order is always the root of current subtree
    current_value = pre_order_traversal_values[0]

    # Initialize the right subtree start index as end of list (case where no right subtree exists)
    right_subtree_root_idx = len(pre_order_traversal_values)

    # Find the first value >= current_value (marks start of right subtree)
    for idx in range(1, len(pre_order_traversal_values)):
        value = pre_order_traversal_values[idx]
        if value >= current_value:
            right_subtree_root_idx = idx
            break  # Found the divider between left and right subtrees

    # Recursively reconstruct left subtree (values between current root and right subtree start)
    left_subtree = reconstruct_bst(pre_order_traversal_values[1:right_subtree_root_idx])
    # Recursively reconstruct right subtree (remaining values after left subtree ends)
    right_subtree = reconstruct_bst(pre_order_traversal_values[right_subtree_root_idx:])

    # Create and return current node with its left and right subtrees
    return BST(current_value, left_subtree, right_subtree)


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
