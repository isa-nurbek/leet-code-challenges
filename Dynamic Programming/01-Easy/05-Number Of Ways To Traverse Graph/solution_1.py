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

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### **Problem Understanding**

The given function `number_of_ways_to_traverse_graph(width, height)` calculates the number of unique paths from the top-left
corner to the bottom-right corner of a 2D grid with dimensions `width x height`. Movement is restricted to either right or
down at any point in the grid.

### **Base Case**

The base case is straightforward:
- If either `width` or `height` is 1, there's only **one way** to traverse the grid.
This is because:
  - If `width = 1`, the grid is a single column; you can only move down.
  - If `height = 1`, the grid is a single row; you can only move right.

### **Recursive Case**

For grids larger than 1x1, the number of ways to traverse is the sum of:
1. The number of ways to traverse a grid of `(width - 1) x height` (move right first).
2. The number of ways to traverse a grid of `width x (height - 1)` (move down first).

This mirrors the combinatorial approach where the total paths are the sum of paths from the two possible immediate next steps.

---

### **Time Complexity Analysis**

#### **Recursive Tree Structure**
The recursion forms a binary tree where each node represents a subproblem:
- Root: `(width, height)`
- Left child: `(width - 1, height)`
- Right child: `(width, height - 1)`
- Leaves: Nodes where either `width = 1` or `height = 1`.

#### **Tree Depth**
The maximum depth of the tree is `(width + height - 2)`, because:
- Each level reduces either `width` or `height` by 1.
- The base case is reached when either `width` or `height` becomes 1.

#### **Number of Nodes**
The recursion tree is a full binary tree (each node has 0 or 2 children) with:
- Total nodes = 2^(depth + 1) - 1.
- Since depth is `(width + height - 2)`, the number of nodes is O(2^(width + height)).

However, this is a loose upper bound because many subproblems are repeated (e.g., `(width-1, height-1)` is computed in both branches).

#### **Tight Bound Using Combinatorics**
The exact number of unique subproblems is (width * height), since the recursion can be memoized into a 2D table.
Without memoization, the time complexity is exponential due to redundant calculations.

The exact time complexity is O({w + h - 2} / {w - 1}), which is the number of paths in the recursion tree (equivalent to the
answer itself). This is because the recursion explores all possible paths, and the answer is the binomial coefficient
({w + h - 2} / {w - 1}).

But in Big-O terms, this is O(2^(w + h)), as the binomial coefficient grows exponentially.

---

### **Space Complexity Analysis**

#### **Recursion Call Stack**
The maximum depth of the call stack is O(width + height), as each recursive call reduces either `width` or `height` by 1.

#### **Auxiliary Space**
No additional data structures are used, so the space complexity is dominated by the call stack: O(width + height)

---

### **Final Answer**
- **Time Complexity (Current Implementation):** O(2^(w + h)) (exponential).
- **Space Complexity (Current Implementation):** O(width + height) (call stack depth).

---

### **Optimization with Memoization or DP**
The current implementation is inefficient due to repeated work.

Two optimizations are possible:

1. Memoization (Top-Down DP)
2. Combinatorial Formula

"""
