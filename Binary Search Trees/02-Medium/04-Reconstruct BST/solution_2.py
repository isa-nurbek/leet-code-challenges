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

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of this algorithm is **O(N)**, where **N** is the number of nodes in the BST.

Here's why:

1. **Each node is visited exactly once**: The algorithm processes each element in the `pre_order_traversal_values` array exactly
once. The `idx` variable ensures that no element is revisited after it's processed.

2. **Constant work per node**: For each node, the algorithm performs a constant amount of work (checking bounds, incrementing `idx`,
and making recursive calls).

3. **No redundant work**: The bounds (`lower_bound` and `upper_bound`) ensure that the algorithm does not explore invalid paths,
making the traversal efficient.

Thus, the total time complexity is linear in the number of nodes.

---

### Space Complexity Analysis

The space complexity is **O(N)** in the worst case and **O(H)** in the average case (where **H** is the height of the BST).

Here's why:

1. **Recursion stack space**: The algorithm uses recursion, so the maximum depth of the call stack determines the space complexity.
   - In the **worst case** (a skewed tree, e.g., a linked list), the recursion depth is **O(N)**.
   - In the **average case** (a balanced BST), the recursion depth is **O(log N)** (since the height of a balanced BST is logarithmic in the number of nodes).
2. **Output space**: The space required to store the reconstructed BST is **O(N)**, but this is typically considered separate
from the auxiliary space used by the algorithm.

Thus:
- **Worst-case space complexity (skewed tree)**: **O(N)** (due to recursion stack).
- **Average-case space complexity (balanced BST)**: **O(log N)**.

If we consider the space required for the output BST, then it is always **O(N)** (since we need to store all nodes), but this is
usually considered separate from the algorithm's auxiliary space.

---

### Summary
- **Time Complexity**: **O(N)** (linear time, each node processed once).
- **Space Complexity**:
  - **Worst case (skewed tree)**: **O(N)** (recursion stack).
  - **Best/average case (balanced BST)**: **O(log N)** (recursion stack proportional to tree height).

"""
