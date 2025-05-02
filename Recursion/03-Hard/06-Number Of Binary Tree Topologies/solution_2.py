# Problem Description:

"""

                                            Number Of Binary Tree Topologies

Write a function that takes in a non-negative integer `n` and returns the number of possible Binary Tree topologies that can be
created with exactly `n` nodes.

A Binary Tree topology is defined as any Binary Tree configuration, irrespective of node values. For instance, there exist only
two Binary Tree topologies when `n` is equal to `2`: a root node with a left node, and a root node with a right node.

> Note that when `n` is equal to `0`, there's one topology that can be created: the `None` node.


## Sample Input
```
n = 3
```

## Sample Output
```
5
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(n) space - where `n` is the input number.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n²) time | O(n) space
def number_of_binary_tree_topologies(n, memo=None):
    """
    Calculate the number of possible binary tree topologies with 'n' nodes.
    Uses memoization to optimize recursive calculations.

    Args:
        n (int): Number of nodes in the binary tree.
        memo (dict): Dictionary to store previously computed results (used for memoization).

    Returns:
        int: Number of distinct binary tree topologies for 'n' nodes.
    """

    # Initialize the memoization dictionary if not provided
    if memo is None:
        memo = {0: 1}  # Base case: an empty tree has one topology (the empty tree)

    # If we've already computed the result for 'n', return it
    if n in memo:
        return memo[n]

    # Initialize counter for total number of trees
    number_of_trees = 0

    # Iterate through all possible left subtree sizes
    for left_tree_size in range(n):
        # The right subtree size is computed as:
        # Total nodes - 1 (for root) - left_tree_size
        right_tree_size = n - 1 - left_tree_size

        # Recursively compute the number of topologies for left and right subtrees
        number_of_left_trees = number_of_binary_tree_topologies(left_tree_size, memo)
        number_of_right_trees = number_of_binary_tree_topologies(right_tree_size, memo)

        # The total number of trees for this split is the product of left and right possibilities
        number_of_trees += number_of_left_trees * number_of_right_trees

    # Store the computed result in memo before returning
    memo[n] = number_of_trees

    return number_of_trees


# Test Cases:

print(number_of_binary_tree_topologies(3))  # Output: 5
print(number_of_binary_tree_topologies(0))  # Output: 1
print(number_of_binary_tree_topologies(5))  # Output: 42
