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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function calculates the **number of unique ways to traverse a grid** (or graph) from the **top-left corner to the bottom-right
corner**, where you can only move **right** or **down** at each step.

---

### 🧠 **Understanding the Problem**

Given a grid of size `width x height`:

* Start at the top-left cell `(1, 1)`.
* Your goal is to reach the bottom-right cell `(width, height)`.
* You can only move:

  * **Right** (→)
  * **Down** (↓)

This is a classic **Dynamic Programming** problem that counts the number of unique paths in a grid.

---

### 🔍 **Breakdown of the Code**

```
def number_of_ways_to_traverse_graph(width, height):
    dp = [[0 for _ in range(height + 1)] for _ in range(width + 1)]
```

* We initialize a 2D list `dp` of size `(width + 1) x (height + 1)` filled with zeros.
* `dp[w][h]` will store the **number of ways to reach cell (w, h)** from (1,1).

Why `+1`?

> To make the grid 1-indexed. This avoids dealing with index 0, making the logic cleaner.

---

```
    for w in range(1, width + 1):
        for h in range(1, height + 1):
```

* Iterate through every cell in the grid from `(1,1)` to `(width, height)`.

```
    if w == 1 or h == 1:
        dp[w][h] = 1
```

* If we're on the **first row** or **first column**, there's only **1 way** to reach that cell:

  * Move right all the way (if on row 1)
  * Move down all the way (if on column 1)

```
    else:
        dp[w][h] = dp[w - 1][h] + dp[w][h - 1]
```

* For other cells:

  * Number of ways to get to `(w, h)` = **from the left cell** `(w-1, h)` **+ from the top cell** `(w, h-1)`

This is the key dynamic programming idea:
**Each cell's solution is built using smaller sub-problems.**

---

### 🔁 **How It Works With Example**

#### `number_of_ways_to_traverse_graph(3, 2)`

Grid size: 3 (width) x 2 (height)
Grid cells:

```
(1,1) (1,2)
(2,1) (2,2)
(3,1) (3,2)
```

We fill the `dp` table like this:

| w\h | 1 | 2 |
| --- | - | - |
| 1   | 1 | 1 |
| 2   | 1 | 2 |
| 3   | 1 | 3 |

→ **Answer = 3**

---

### ✅ **Test Case Outputs**

```
print(number_of_ways_to_traverse_graph(4, 3))  # Output: 10
```

10 unique paths in a 4x3 grid.

```
print(number_of_ways_to_traverse_graph(3, 2))  # Output: 3
```

3 unique paths in a 3x2 grid.

```
print(number_of_ways_to_traverse_graph(2, 2))  # Output: 2
```

2 unique paths in a 2x2 grid.

---

### ⏱️ **Time & Space Complexity**

* **Time Complexity:** `O(width * height)`
* **Space Complexity:** `O(width * height)` for the 2D `dp` array

We could optimize space to `O(min(width, height))` using a 1D array if needed.

---

### 🧮 **Alternative (Mathematical) Solution**

The number of unique paths is a **combinatorics problem**:

> To move from (1,1) to (W,H), you need `(W-1)` right moves and `(H-1)` down moves
> So total moves = `(W-1 + H-1)`
> Choose `(W-1)` or `(H-1)` from that:

Paths} = (width + height - 2)}{(width - 1)}

This approach is faster for large grids and uses constant space.

---

Let's visualize the path traversal in an ASCII grid.

We'll use:

* `S` = Start (top-left)
* `E` = End (bottom-right)
* `.` = Open cell
* Arrows (`→`, `↓`) to represent possible movements

We'll take `width = 4`, `height = 3` as an example. The grid is 4 columns wide and 3 rows high.

---

### 📦 Grid Layout (4 × 3)

```
S  .  .  .
↓  ↓  ↓  ↓
.  .  .  .
↓  ↓  ↓  ↓
.  .  .  E
```

---

### 🧠 Idea

You can move only:

* **Right (`→`)**
* **Down (`↓`)**

To get from `S` to `E`, you need:

* 3 right moves (to go from column 1 to 4)
* 2 down moves (to go from row 1 to 3)

So any path is a sequence of 3 R's and 2 D's.

---

### 📋 Possible Paths Count (Width = 4, Height = 3)

* Total moves = 3 (right) + 2 (down) = 5 moves
* Choose 2 downs (or 3 rights) from 5 steps:

{5}{2} = 10 { unique paths}

---

### 🛤️ A Few Path Examples (R = Right, D = Down):

1. `→ → → ↓ ↓`
2. `→ → ↓ → ↓`
3. `→ ↓ → → ↓`
4. `→ ↓ → ↓ →`
5. `↓ → → → ↓`
6. `↓ → → ↓ →`
7. `↓ → ↓ → →`
8. `→ ↓ ↓ → →`
9. `↓ ↓ → → →`
10. `→ ↓ ↓ → →`

Each one represents a different sequence to reach the end.

"""
