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


# O(w * h) time | O(w * h) space
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

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go through the code **step by step**, understand **how it works**, and explain the **logic behind it**.

---

## 🌟 Goal of the Function

We're trying to calculate the **number of ways to traverse a grid** (graph) of size `width x height`, moving **only right or
down** from the **top-left corner (1,1)** to the **bottom-right corner (width, height)**.

---

## 🔢 Example of Traversal

For a `3x2` grid (3 columns, 2 rows), starting from the top-left corner:

```
• → • → •
↓    ↓    ↓
•    •    •
```

You can only move:

* Right (`→`)
* Down (`↓`)

To get to the bottom-right, you need to take exactly:

* `(width - 1)` right moves
* `(height - 1)` down moves

For `3x2`, that’s:

* 2 right moves
* 1 down move

All combinations of those moves give you the number of unique paths.

---

## 🧠 Recursive Approach with Memoization

### ✅ Main Function

```
def number_of_ways_to_traverse_graph(width, height):
    memo = [[-1 for _ in range(height + 1)] for _ in range(width + 1)]
    return helper(width, height, memo)
```

* Creates a 2D `memo` array (cache) initialized with `-1`, to store the number of ways for each subproblem (to avoid recomputation).
* Calls the recursive `helper()` function.

---

### ✅ Recursive Helper Function

```
def helper(w, h, memo):
    if w == 1 or h == 1:
        return 1
```

* **Base Case**: If either the width or height is 1, there's only **one way** to traverse (only down or only right).

  * E.g., a 1x4 or 5x1 grid has exactly 1 path.

---

```
    if memo[w][h] != -1:
        return memo[w][h]
```

* **Memoization**: If the number of ways for `(w, h)` was already calculated, return it.

---

```
    memo[w][h] = helper(w - 1, h, memo) + helper(w, h - 1, memo)
```

* **Recursive Step**:

  * You can reach cell `(w, h)` either:

    * from the left → `(w-1, h)`
    * from above → `(w, h-1)`
  * So total number of ways to reach `(w, h)` is the sum of:

    * ways to reach `(w-1, h)`
    * ways to reach `(w, h-1)`

* Store the result in `memo[w][h]` to avoid recalculating.

---

```
    return memo[w][h]
```

* Finally, return the computed value.

---

## 🧪 Test Cases

### Test Case 1:

```
number_of_ways_to_traverse_graph(4, 3)
```

* You need 3 right moves and 2 down moves.
* Total moves: `4 + 3 - 2 = 5`
* Combinations: `C(5, 2)` = 10
  ✅ Output: `10`

---

### Test Case 2:

```
number_of_ways_to_traverse_graph(3, 2)
```

* Moves: 2 right, 1 down → total 3 moves.
* Combinations: `C(3, 1)` = 3
  ✅ Output: `3`

---

### Test Case 3:

```
number_of_ways_to_traverse_graph(2, 2)
```

* Moves: 1 right, 1 down → total 2 moves.
* Combinations: `C(2, 1)` = 2
  ✅ Output: `2`

---

## 📌 Summary

* This code solves the **grid traversal** problem using **recursion + memoization**.
* It avoids repeated computation by storing subproblem results.
* It’s efficient for medium-sized inputs and clearly demonstrates **dynamic programming**.

---

Let's visualize **how traversal works** in a grid using **ASCII diagrams** for clarity.

---

## 🧭 Grid Traversal Rules

* Start at **top-left** corner `(1,1)`
* Move only **right (→)** or **down (↓)**
* Goal is **bottom-right** corner `(width, height)`

---

## 🔢 Example 1: `width=3`, `height=2`

A `3 x 2` grid (3 columns, 2 rows):

### 📍 Grid Representation

```
(1,1) ──→ (2,1) ──→ (3,1)
  │        │        │
  ↓        ↓        ↓
(1,2) ──→ (2,2) ──→ (3,2)
```

### ✅ All Unique Paths (Right + Down only)

Paths from (1,1) to (3,2):
You must take **2 rights** and **1 down** (R, R, D), in different orders:

1. → → ↓
2. → ↓ →
3. ↓ → →

So, **3 total paths** ✅

---

## 🔢 Example 2: `width=4`, `height=3`

A `4 x 3` grid:

### 📍 Grid Representation

```
(1,1) → (2,1) → (3,1) → (4,1)
   ↓       ↓       ↓       ↓
(1,2) → (2,2) → (3,2) → (4,2)
   ↓       ↓       ↓       ↓
(1,3) → (2,3) → (3,3) → (4,3)
```

### ✅ Count Total Unique Paths

You need:

* 3 rights
* 2 downs

Total moves: **5**
Choose positions for either rights or downs → **C(5, 2)** = 10 paths

---

## 🔢 Example 3: `width=2`, `height=2`

A `2 x 2` grid:

```
(1,1) → (2,1)
   ↓       ↓
(1,2) → (2,2)
```

Paths:

1. → ↓
2. ↓ →

✅ Total: 2 paths

"""
