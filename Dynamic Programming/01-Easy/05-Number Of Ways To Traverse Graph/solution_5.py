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

import math


# O(w + h) time | O(1) space
# Combinatorial Optimization (Mathematical Formula)
def number_of_ways_to_traverse_graph(width, height):
    """
    Calculate the number of unique paths from top-left to bottom-right in a grid,
    moving only right or down.

    This is a combinatorial problem that can be solved using binomial coefficients.
    In a grid of size (width x height), the number of unique paths is equal to
    the number of combinations of (width + height - 2) moves taken (width - 1) at a time
    (or equivalently (height - 1) at a time).

    Args:
        width (int): The width of the grid (number of columns)
        height (int): The height of the grid (number of rows)

    Returns:
        int: The number of unique paths from top-left to bottom-right
    """
    return math.comb(width + height - 2, width - 1)
    # math.comb(n, k) calculates the binomial coefficient "n choose k"
    # which is equal to n! / (k! * (n - k)!)

    # Explanation of parameters:
    # width + height - 2: Total moves needed (right + down)
    # width - 1: Number of right moves needed (could also use height - 1 for down moves)
    #
    # For example, in a 3x4 grid:
    # Total moves = (3 + 4 - 2) = 5
    # Right moves = (3 - 1) = 2
    # The calculation becomes "5 choose 2" = 10 unique paths


# Test Cases:

print(number_of_ways_to_traverse_graph(4, 3))
# Output: 10

print(number_of_ways_to_traverse_graph(3, 2))
# Output: 3

print(number_of_ways_to_traverse_graph(2, 2))
# Output: 2
