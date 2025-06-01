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


# O(2^(n + m)) time | O(n + m) space
def number_of_ways_to_traverse_graph(width, height):
    """
    Calculate the number of unique ways to traverse a grid from top-left to bottom-right
    when you can only move right or down.

    Args:
        width (int): The width of the grid (number of columns)
        height (int): The height of the grid (number of rows)

    Returns:
        int: The number of unique paths from top-left to bottom-right

    Approach:
        This uses a recursive solution with base case and recurrence relation:
        - Base case: If grid is 1x1 (single cell) or a single row/column, there's only 1 way
        - Recursive case: Paths to current cell = paths from above + paths from left
    """

    # Base case: if grid is single row or single column, only one path exists
    if width == 1 or height == 1:
        return 1

    # Recursive case:
    # Number of ways to reach current cell equals:
    #   ways to reach cell above (same column, row-1) +
    #   ways to reach cell to left (column-1, same row)
    return number_of_ways_to_traverse_graph(
        width - 1, height
    ) + number_of_ways_to_traverse_graph(width, height - 1)


# Test Cases:

print(number_of_ways_to_traverse_graph(4, 3))
# Output: 10

print(number_of_ways_to_traverse_graph(3, 2))
# Output: 3

print(number_of_ways_to_traverse_graph(2, 2))
# Output: 2
