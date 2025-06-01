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
# Dynamic Programming (Bottom-Up DP)
def number_of_ways_to_traverse_graph(width, height):
    # Create a dynamic programming (DP) table with dimensions (width+1) x (height+1)
    # This table will store the number of ways to reach each position
    dp = [[0 for _ in range(height + 1)] for _ in range(width + 1)]

    # Iterate through each position in the grid
    for w in range(1, width + 1):
        for h in range(1, height + 1):
            # Base case: If we're in the first row or first column,
            # there's only 1 way to get there (all right moves or all down moves)
            if w == 1 or h == 1:
                dp[w][h] = 1
            else:
                # For any other position, the number of ways to reach it is the sum of:
                # 1. The number of ways to reach the position above it (coming from top)
                # 2. The number of ways to reach the position to its left (coming from left)
                dp[w][h] = dp[w - 1][h] + dp[w][h - 1]

    # The bottom-right corner will contain the total number of ways
    # to traverse the entire grid
    return dp[width][height]


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

## **Time Complexity**

- **Initialization**: 
  - The DP table is initialized in O((width + 1) * (height + 1)) = O(width * height) time.
- **Filling the DP Table**:
  - The nested loops iterate over each cell in the `width x height` grid.
  - Each cell's computation is O(1) (just a lookup and addition).
  - Thus, the total time is O(width * height).


## **Space Complexity**

- **DP Table Storage**:
  - The DP table consumes O(width * height) space.
- **No Additional Space**:
  - Only the DP table is used, and no extra data structures are needed.
  - Thus, the total space is O(width * height).

### **Final Answer**
- **Time Complexity**: O(width * height).
- **Space Complexity**: O(width * height).

### **Optimization (Space)**

If we observe, at any point, we only need the **current row and the previous row** (or current column and previous column) to
compute the next value. Thus, we can reduce the space complexity to O(min(width, height)) by using a 1D DP array and updating
it iteratively.

However, the given solution uses the full 2D DP table, so the space remains O(width * height).

### **Alternative Approach (Combinatorics)**

This problem can also be solved using combinatorics:
- To go from `(0, 0)` to `(width-1, height-1)`, you need to make exactly `(width - 1)` right moves and `(height - 1)` down moves.

"""
