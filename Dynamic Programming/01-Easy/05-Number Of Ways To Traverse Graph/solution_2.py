# Problem Description:

"""
                                               Number Of Ways To Traverse Graph

You're given two positive integers representing the `width` and `height` of a grid-shaped, rectangular graph. Write a function that
returns the number of ways to reach the bottom right corner of the graph when starting at the top left corner. Each move you take
must either go down or right. In other words, you can never move up or left in the graph.

For example, given the graph illustrated below, with `width = 2` and `height = 3`, there are three ways to reach the bottom right
corner when starting at the top left corner:

```
 _ _
|_|_|
|_|_|
|_|_|

```

1. Down, Down, Right
2. Right, Down, Down
3. Down, Right, Down

> Note: you may assume that `width * height >= 2`. In other words, the graph will never be a `1x1 grid`.


## Sample Input:
```
width = 4
height = 3
```

## Sample Output:
```
10
```

## Optimal Time & Space Complexity:
```
O(n + m) time | O(1) space - where `n` is the width of the graph and `m` is the height.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * m) time | O(n * m) space
# Memoization (Top-Down DP)
def number_of_ways_to_traverse_graph(width, height):
    """
    Calculates the number of unique ways to traverse a grid from top-left to bottom-right
    when you can only move right or down.

    Args:
        width (int): The width of the grid (number of columns)
        height (int): The height of the grid (number of rows)

    Returns:
        int: The number of unique paths from top-left to bottom-right
    """

    # Create a memoization table initialized with -1
    # The table has dimensions (width+1) x (height+1) to account for all subproblems
    memo = [[-1 for _ in range(height + 1)] for _ in range(width + 1)]

    # Call the helper function with the memo table
    return helper(width, height, memo)


def helper(w, h, memo):
    """
    Recursive helper function that uses memoization to count paths efficiently.

    Args:
        w (int): Current width (subproblem width)
        h (int): Current height (subproblem height)
        memo (list): Memoization table to store computed results

    Returns:
        int: Number of paths for the given w x h grid
    """

    # Base case: If grid is single row or single column, there's only 1 path
    if w == 1 or h == 1:
        return 1

    # If we've already computed this subproblem, return the stored result
    if memo[w][h] != -1:
        return memo[w][h]

    # Recursive case:
    # Number of paths to (w,h) = paths coming from left (w-1,h) + paths coming from above (w,h-1)
    memo[w][h] = helper(w - 1, h, memo) + helper(w, h - 1, memo)

    # Return the computed and stored result
    return memo[w][h]


# Test Cases:

print(number_of_ways_to_traverse_graph(4, 3))
# Output: 10

print(number_of_ways_to_traverse_graph(3, 2))
# Output: 3

print(number_of_ways_to_traverse_graph(2, 2))
# Output: 2

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

## **Time Complexity Analysis**

- **Without Memoization**: The naive recursive approach would have an exponential time complexity of O(2^(w+h)) because each
call branches into two subproblems.
- **With Memoization**: Each subproblem `(w, h)` is computed only once. There are O(w * h) unique subproblems.
  - Each subproblem computation involves a constant amount of work (addition and memo lookups).
  - Thus, the time complexity is O(w * h).

## **Space Complexity Analysis**

- **Memoization Table**: The `memo` table has dimensions `(w+1) x (h+1)`, leading to O(w * h) space.
- **Recursion Stack**: In the worst case, the recursion depth is O(w + h) (e.g., when computing `(w, h)`, the stack goes
up to `(1, 1)`).
- **Total Space Complexity**: O(w * h + w + h) = O(w * h) (since (w * h) dominates).


### **Final Answer**
- **Time Complexity**: O(w * h).
- **Space Complexity**: O(w * h).

The DP with memoization approach efficiently computes the result by avoiding redundant calculations, leading to polynomial
time and space complexity.

"""
