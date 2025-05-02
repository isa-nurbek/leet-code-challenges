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

Let's analyze the time and space complexity of the given recursive solution for calculating the number of binary tree topologies.

### Time Complexity:
The function computes the number of binary tree topologies by considering all possible left and right subtree combinations for a given `n`. 

1. **Recursive Structure**: For each call with `n` nodes, it makes recursive calls for all possible left subtree sizes from `0` to `n-1` (with corresponding right subtree sizes from `n-1` to `0`). This leads to a lot of overlapping subproblems.

2. **Number of Subproblems**: The number of unique subproblems is `O(n)` (from `0` to `n`), but each subproblem `k` is computed by summing over all pairs of smaller subproblems.

3. **Repeated Work**: Without memoization, the same subproblems are recomputed many times. The time complexity is exponential, specifically it follows the Catalan number recurrence. The nth Catalan number is given by:
   \[
   C_n = \frac{1}{n+1} \binom{2n}{n}
   \]
   The Catalan numbers grow as \( C_n \approx \frac{4^n}{n^{3/2} \sqrt{\pi}} \), so the time complexity is \( O(4^n / n^{3/2}) \).

4. **Overall Time Complexity**: The time complexity is \( O(4^n / n^{3/2}) \), which is exponential in `n`.

### Space Complexity:
1. **Recursion Stack**: The maximum depth of the recursion stack is `O(n)` because each recursive call reduces the problem size by at least `1` (from `n` down to `0`).
2. **No Additional Storage**: The function does not use any additional data structures to store intermediate results (like memoization), so the space complexity is just the recursion stack.

   - **Overall Space Complexity**: \( O(n) \).

### Optimizing with Memoization:
If you memoize the results of subproblems (i.e., store the result of `number_of_binary_tree_topologies(k)` once computed and reuse it), you can drastically improve the time complexity:
- **Time Complexity with Memoization**: \( O(n^2) \), because there are \( O(n) \) unique subproblems, and each subproblem takes \( O(n) \) time to compute (due to the loop).
- **Space Complexity with Memoization**: \( O(n) \) to store the memoization table and \( O(n) \) for the recursion stack, so \( O(n) \) total.

### Final Answer:
- **Time Complexity**: \( O(4^n / n^{3/2}) \) (exponential, without memoization).
- **Space Complexity**: \( O(n) \) (due to recursion stack).

For practical purposes, you should use memoization to bring the time complexity down to \( O(n^2) \). The recursive solution without memoization is very inefficient for larger `n`.

"""
