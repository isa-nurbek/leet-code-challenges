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
    if memo is None:
        memo = {0: 1}

    if n in memo:
        return memo[n]

    number_of_trees = 0
    for left_tree_size in range(n):
        right_tree_size = n - 1 - left_tree_size

        number_of_left_trees = number_of_binary_tree_topologies(left_tree_size, memo)
        number_of_right_trees = number_of_binary_tree_topologies(right_tree_size, memo)
        number_of_trees += number_of_left_trees * number_of_right_trees

    memo[n] = number_of_trees

    return number_of_trees


# Test Cases:

print(number_of_binary_tree_topologies(3))  # Output: 5
print(number_of_binary_tree_topologies(0))  # Output: 1
print(number_of_binary_tree_topologies(5))  # Output: 42
