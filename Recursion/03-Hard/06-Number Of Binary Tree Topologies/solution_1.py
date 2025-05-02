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


# Upper Bound: O(n*(2n)!)/(n!(n+1)!) time | O(n) space
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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The time complexity can be analyzed by considering how many subproblems are solved and how much work is done for each subproblem.

1. **Number of Subproblems**: For each `n`, the function makes recursive calls for all possible left subtree sizes from `0` to
`n-1`. This means the number of unique subproblems is `n` (one for each possible value of `k` from `0` to `n-1`).

2. **Work per Subproblem**: For each subproblem of size `n`, the function performs `O(n)` work (due to the loop iterating over
`left_tree_size` from `0` to `n-1`), and each iteration involves two recursive calls and some constant-time operations.

However, the recursive calls lead to overlapping subproblems, and the total number of unique subproblems is `O(n)`. If we were to
memoize the results (i.e., use dynamic programming), the time complexity would be `O(n^2)` because for each `i` from `1` to `n`,
we do `O(i)` work (summing over `i` from `1` to `n` gives `O(n^2)`).

But in the current implementation (without memoization), the time complexity is exponential because the same subproblems are
recomputed many times. Specifically, the time complexity is given by the Catalan number recurrence, which grows as `O(4^n / n^(3/2))
` (the nth Catalan number is `C(n) = (2n choose n) / (n+1)`, and the sum of all Catalan numbers up to `n` is also exponential).

### Space Complexity:
1. **Recursion Stack**: The maximum depth of the recursion stack is `O(n)` (when the left or right subtree is as large as possible,
e.g., left subtree size `n-1`, then `n-2`, etc., down to `0`).
2. **No Additional Space**: The current implementation does not use any additional space for memoization, so the space complexity
is `O(n)` due to the recursion stack.

### Summary:
- **Time Complexity (current recursive implementation)**: Exponential, `O(4^n / n^(3/2))` (nth Catalan number).
- **Space Complexity (current recursive implementation)**: `O(n)` (due to recursion stack).

### Optimized Approach (Dynamic Programming):
If you memoize the results of subproblems (i.e., store the results of `number_of_binary_tree_topologies(k)` for `k` from `0` to
`n`), the time complexity becomes `O(n^2)` (since you compute `n` subproblems, each taking `O(n)` time), and the space complexity
becomes `O(n)` (to store the results).

"""
