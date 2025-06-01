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


# O(w * h) time | O(h) space
# Space-Optimized DP (Using 1D Array)
def number_of_ways_to_traverse_graph(width, height):
    # Initialize a dynamic programming (DP) array where each index represents a row
    # The initial value of 1 for all positions represents:
    # - For the first column (width=1), there's only 1 way to reach any cell (only moving down)
    dp = [1] * (height + 1)

    # Start from width = 2 since width=1 case is already handled by initialization
    for w in range(2, width + 1):
        # For each subsequent height starting from 2 (since height=1 is already handled)
        for h in range(2, height + 1):
            # Update the current cell's value by adding:
            # - The value from the left (which is dp[h] from previous iteration)
            # - The value from above (which is dp[h-1])
            # This works because we're reusing the same array to save space
            dp[h] += dp[h - 1]

    # The final value in our DP array represents the number of unique paths
    # from top-left to bottom-right in a grid of size width x height
    return dp[height]


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

- The outer loop runs from `w = 2` to `width`, which is `O(width)` iterations.
- The inner loop runs from `h = 2` to `height`, which is `O(height)` iterations per outer loop iteration.
- Thus, the total time complexity is `O(width * height)`.

## **Space Complexity Analysis**

- The `dp` array is of size `height + 1`, so the space complexity is `O(height)`.
- This is efficient compared to a 2D DP table which would require `O(width * height)` space.

### **Final Answer**
The given DP solution has:
- **Time Complexity**: `O(width * height)`.
- **Space Complexity**: `O(height)`. 

This is efficient for moderate grid sizes. For very large grids, the combinatorics approach would be more efficient.

---

### **Alternative Approach (Combinatorics)**

This problem can also be solved using combinatorics:
- To go from `(0,0)` to `(width-1, height-1)`, you need to make `(width-1)` right moves and `(height-1)` down moves.
- The total number of moves is `(width-1 + height-1) = (width + height - 2)`.
- The number of ways is the number of ways to choose `(width-1)` right moves (or equivalently `(height-1)` down moves)
out of these total moves.
- Thus, the answer is `C(width + height - 2, width - 1)` or `C(width + height - 2, height - 1)`.

For the example `width = 4`, `height = 3`:
- Total moves = `4 + 3 - 2 = 5`.
- Ways = `C(5, 3) = 10` or `C(5, 2) = 10`.

This approach has:
- Time complexity: `O(width + height)` (assuming binomial coefficient computation is optimized).
- Space complexity: `O(1)`.

"""
