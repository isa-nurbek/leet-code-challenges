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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity Analysis

The function `number_of_binary_tree_topologies(n)` computes the number of possible binary tree topologies for a given number of
nodes `n` using memoization to avoid redundant calculations. 

1. **Recursive Breakdown**: For each call with `n`, the function iterates from `0` to `n-1` (i.e., `n` iterations), splitting the
problem into left and right subtrees. For each split, it makes two recursive calls:
   - `number_of_binary_tree_topologies(left_tree_size, memo)`
   - `number_of_binary_tree_topologies(right_tree_size, memo)`

2. **Memoization Impact**: With memoization, each unique subproblem (i.e., each unique value of `k` where `0 <= k <= n`) is computed
only once. After computing `number_of_binary_tree_topologies(k)`, the result is stored in `memo` and reused in subsequent calls.

3. **Total Subproblems**: The number of unique subproblems is `O(n)` (specifically, `n+1` subproblems for `k = 0` to `k = n`).

4. **Work per Subproblem**: For each subproblem `k`, the work done is `O(k)` (due to the loop from `0` to `k-1`). 

5. **Total Time Complexity**: The total time is the sum of the work for all subproblems: **O(n²)**.

### Space Complexity Analysis

1. **Memoization Storage**: The `memo` dictionary stores `n+1` entries (for `k = 0` to `k = n`), each requiring constant space. Thus, the space for `memo` is **O(n)**.

2. **Recursion Stack**: In the worst case, the recursion stack can go as deep as `n` (e.g., when computing `n`, then `n-1`, then
`n-2`, etc., down to `0`). Thus, the recursion stack space is **O(n)**.

3. **Total Space Complexity**: The dominant factors are the `memo` storage and the recursion stack, both of which are `O(n)`.
Thus, the total space complexity is **O(n)**.

### Summary
- **Time Complexity**: O(n²)
- **Space Complexity**: O(n)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""

### 🔍 **Step-by-Step Explanation of the Code**

```
def number_of_binary_tree_topologies(n, memo=None):
```

* This function calculates the number of binary tree topologies for `n` nodes using **memoization** to store already computed values.

---

```
if memo is None:
    memo = {0: 1}  
```

* Initializes the memoization dictionary.
* `memo[0] = 1` means there's **one topology** with **0 nodes** — the **empty tree**.

---

```
if n in memo:
    return memo[n]
```

* If the result for `n` is already computed, return it to avoid redundant computation.

---

```
number_of_trees = 0
for left_tree_size in range(n):
```

* Initialize the count.
* Loop over all possible sizes for the left subtree (`0` to `n-1`).

---

```
right_tree_size = n - 1 - left_tree_size
```

* The right subtree gets the remaining nodes after one root and the left subtree.

---

```
number_of_left_trees = number_of_binary_tree_topologies(left_tree_size, memo)
number_of_right_trees = number_of_binary_tree_topologies(right_tree_size, memo)
```

* Recursively calculate the number of binary tree topologies for the left and right subtrees.
* These calls will use memoized values when available.

---

```
number_of_trees += number_of_left_trees * number_of_right_trees
```

* Multiply left and right subtree counts because each combination creates a new topology.
* Sum over all such combinations.

---

```
memo[n] = number_of_trees
return number_of_trees
```

* Cache the result in `memo` and return it.

---

### 🧪 **Test Cases**

```
print(number_of_binary_tree_topologies(3))  # Output: 5
```

* Possible binary tree topologies with 3 nodes: 5.
* Matches Catalan number $C_3 = 5$

```
print(number_of_binary_tree_topologies(0))  # Output: 1
```

* 1 way to form an empty tree (base case).

```
print(number_of_binary_tree_topologies(5))  # Output: 42
```

* Catalan number $C_5 = 42$

---

### ✅ Summary

* This function uses **recursive dynamic programming** (top-down with memoization) to compute **Catalan numbers**.
* Time complexity with memoization is **O(n²)** due to the nested recursive calls and caching.
* Used for counting binary search trees, balanced parentheses, polygon triangulations, etc.

"""
