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


def number_of_binary_tree_topologies(n):
    """Returns the number of possible binary tree topologies with n nodes.

    A binary tree topology is defined by the arrangement of nodes, without considering
    specific node values. This function uses a recursive approach to count all possible
    unique structures.

    Args:
        n: The number of nodes in the binary tree (non-negative integer)

    Returns:
        The number of distinct binary tree topologies possible with n nodes
    """

    # Base case: an empty tree (0 nodes) has exactly 1 topology (the empty tree)
    if n == 0:
        return 1

    # Initialize counter for total number of trees
    number_of_trees = 0

    # Iterate through all possible left subtree sizes
    # For n nodes, the root uses 1 node, remaining n-1 nodes are split between left/right
    for left_tree_size in range(n):
        # Calculate corresponding right subtree size
        right_tree_size = n - 1 - left_tree_size

        # Recursively compute number of topologies for left and right subtrees
        number_of_left_trees = number_of_binary_tree_topologies(left_tree_size)
        number_of_right_trees = number_of_binary_tree_topologies(right_tree_size)

        # The total for this split is the product of left and right possibilities
        number_of_trees += number_of_left_trees * number_of_right_trees

    return number_of_trees


# Test Cases:

print(number_of_binary_tree_topologies(3))  # Output: 5
print(number_of_binary_tree_topologies(0))  # Output: 1
print(number_of_binary_tree_topologies(5))  # Output: 42
