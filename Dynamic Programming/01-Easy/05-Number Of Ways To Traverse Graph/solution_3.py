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
