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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break down the function `number_of_ways_to_traverse_graph(width, height)` in detail.

---

## ❓ Problem Statement

Given a grid of size `width` x `height`, you are asked to find how many **unique paths** exist from the **top-left corner** to the
**bottom-right corner**, if you can only move **right** or **down** at any point.

This is a classic **combinatorics problem** often called the **grid traversal** or **unique paths** problem.

---

## ✅ High-Level Idea

To go from the top-left to bottom-right, you must:

* Take `(width - 1)` steps **right**
* Take `(height - 1)` steps **down**

So the total number of moves = `(width - 1) + (height - 1) = width + height - 2`.

The number of ways to arrange these steps is a **combination**:

Number of ways} = {width + height - 2}{width - 1}

But this function uses **Dynamic Programming** instead of the combinatorics formula.

---

## 🔍 Code Explanation

```
def number_of_ways_to_traverse_graph(width, height):
    dp = [1] * (height + 1)
```

* `dp` is a 1D array of length `height + 1`, initialized to all `1`s.
* This represents the number of ways to reach each cell in the first column (when `width = 1`), which is always 1 because
you can only move **down**.

---

### 🧮 Dynamic Programming Transition

```
    for w in range(2, width + 1):
        for h in range(2, height + 1):
            dp[h] += dp[h - 1]
```

We loop from `width = 2` to `width`, and for each column:

* For each cell at height `h`, we update the number of ways to get there by:

  dp[h] = dp[h] + dp[h - 1]

Why?

* `dp[h]` already stores the number of ways to get to the current row at the previous column.
* `dp[h - 1]` stores the number of ways to get from the **above cell** (from the same column).

So you're effectively simulating a 2D DP table but with **optimized space**, using only a 1D array.

---

### 📥 Return Result

```
    return dp[height]
```

After processing all columns, `dp[height]` contains the total number of ways to reach the bottom-right corner.

---

## 🧪 Test Cases Breakdown

### Test 1: `number_of_ways_to_traverse_graph(4, 3)`

* Grid: 4 columns (width), 3 rows (height)
* Moves: 3 right, 2 down → total ways = `C(5, 2) = 10`
  ✅ Output: **10**

### Test 2: `number_of_ways_to_traverse_graph(3, 2)`

* Moves: 2 right, 1 down → `C(3, 1) = 3`
  ✅ Output: **3**

### Test 3: `number_of_ways_to_traverse_graph(2, 2)`

* Moves: 1 right, 1 down → `C(2, 1) = 2`
  ✅ Output: **2**

---

## ✅ Summary

* The code uses dynamic programming with 1D space optimization.
* `dp[h]` holds the number of ways to get to row `h` at the current column.
* Time Complexity: **O(width × height)**
* Space Complexity: **O(height)**

---

Here's a visual **ASCII diagram** showing how the dynamic programming (DP) table evolves as the function runs.
Let's walk through the example:

---

## 🧪 Example: `number_of_ways_to_traverse_graph(4, 3)`

This means:

* `width = 4` → 4 columns
* `height = 3` → 3 rows
  So we're working on a 3 (rows) × 4 (columns) grid:

```
Start at (0,0), move only right → or down ↓
Goal is at (3,4)
```

---

## 🗺 Grid Coordinates:

```
(0,0)  (0,1)  (0,2)  (0,3)
(1,0)  (1,1)  (1,2)  (1,3)
(2,0)  (2,1)  (2,2)  (2,3)
(3,0)  (3,1)  (3,2)  (3,3)
```

---

### ✅ Dynamic Programming Table

We’ll fill a 2D grid using DP, where each cell `(i, j)` contains the number of ways to reach it.

Start with 1s along the top row and leftmost column, because you can only reach them by going straight right or straight down.

```
Step 0 (initial DP table):
[1, 1, 1, 1]
[1, 0, 0, 0]
[1, 0, 0, 0]
[1, 0, 0, 0]
```

Now we fill in the rest using:

dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

---

### Step-by-step filling:

```
Step 1:
[1, 1, 1, 1]
[1, 2, 3, 4]
[1, 0, 0, 0]
[1, 0, 0, 0]

Step 2:
[1, 1, 1, 1]
[1, 2, 3, 4]
[1, 3, 6,10]
[1, 0, 0, 0]

Step 3:
[1, 1, 1, 1]
[1, 2, 3, 4]
[1, 3, 6,10]
[1, 4,10,20]
```

---

### 🎯 Final Result:

Bottom-right corner `(3,3)` = **20** ways

Wait! That means our original input must be:

```
number_of_ways_to_traverse_graph(4, 4)
```

So let's revise:

---

## For `number_of_ways_to_traverse_graph(4, 3)`:

Grid: 4 columns, 3 rows → meaning grid size is **3×4**

So dimensions:

```
[1, 1, 1, 1]
[1, 2, 3, 4]
[1, 3, 6,10]
```

Final answer = bottom-right = `10`

✅ Matches output: `10`

---

## ✅ Conclusion:

This shows how the number of paths build up using `dp[i][j] = dp[i - 1][j] + dp[i][j - 1]`.

"""
