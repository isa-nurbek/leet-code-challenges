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

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

## **Time Complexity**

- **Binomial Coefficient Calculation**: The `math.comb` function in Python computes the binomial coefficient efficiently.
The time complexity of calculating `C(n, k)` is `O(n)` due to the multiplicative approach used to compute the factorials or
using multiplicative formula for combinations.
  - Here, `n = width + height - 2`, so the time complexity is `O(width + height)`.

### **Space Complexity**

- **Auxiliary Space**: The calculation of the binomial coefficient does not require additional space proportional to the input size.
It uses a constant amount of space for intermediate calculations. Thus, the space complexity is `O(1)`.

### **Summary**
- **Time Complexity**: `O(width + height)`
- **Space Complexity**: `O(1)`

This approach efficiently leverages combinatorial mathematics to solve the problem with optimal time and space complexity.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break this code down and explain in detail how it works.

---

### 📌 **Problem Context**

You want to calculate the **number of unique paths** from the **top-left corner** to the **bottom-right corner** of a grid with
a given `width` and `height`.

You are only allowed to move:

* **Right** or
* **Down**

---

### 🧠 **Concept Behind the Code**

This is a classic **combinatorics** problem. You are trying to find how many different **sequences of moves** can get you from
the start to the end of the grid.

If your grid has:

* `width = w`
* `height = h`

Then, to go from the top-left to the bottom-right:

* You need to move **right** exactly `w - 1` times
* You need to move **down** exactly `h - 1` times

So, the **total number of moves** is:

```
(w - 1) + (h - 1) = w + h - 2
```

You are choosing **when to go right** (or down) among the total steps.

### 🧮 **Combinatorial Formula Used**

The number of unique sequences is:

```
C(w + h - 2, w - 1)
```

Which reads as:

> Choose `w - 1` right-moves from a total of `w + h - 2` moves.

This is what `math.comb()` calculates in Python.

---

### ✅ **Code Explanation**

```
import math  # We need math.comb to compute combinations
```

```
def number_of_ways_to_traverse_graph(width, height):
    return math.comb(width + height - 2, width - 1)
```

* **`width + height - 2`** = total number of moves needed
* **`width - 1`** = number of right moves (alternatively you can choose down moves)
* **`math.comb(n, k)`** returns the number of combinations (`n` choose `k`)

```
# Test Cases
print(number_of_ways_to_traverse_graph(4, 3))  # Output: 10
```

* Grid: 4 columns × 3 rows
* Moves: 3 right, 2 down → total 5
* Ways: C(5, 3) = 10

```
print(number_of_ways_to_traverse_graph(3, 2))  # Output: 3
```

* 2 right, 1 down → total 3
* Ways: C(3, 2) = 3

```
print(number_of_ways_to_traverse_graph(2, 2))  # Output: 2
```

* 1 right, 1 down → total 2
* Ways: C(2, 1) = 2

---

### ⏱️ **Time and Space Complexity**

* **Time Complexity:** `O(w + h)` because `math.comb()` calculates factorials under the hood, but Python uses efficient
algorithms for this.
* **Space Complexity:** `O(1)` — just constant space.

---

### 📌 Summary

We're using a combinatorics formula to calculate the number of unique paths in a grid, avoiding brute-force traversal.
This makes the solution **very efficient**, even for large grids.

---

Let’s visualize the paths in a grid using **ASCII art**. We’ll use a small grid so that the visualization is clear.

---

## 🔲 Example: `width = 3`, `height = 2` (3 columns × 2 rows)

You must move:

* **Right (R)**: `3 - 1 = 2` times
* **Down (D)**: `2 - 1 = 1` time

Total moves = `2 + 1 = 3`
We are choosing positions for 2 R's in a sequence of 3 moves: `C(3, 2) = 3` paths

### ASCII Grid:

```
Start → ──┬──→
         │
         ↓
        End
```

### All Paths:

Here are all 3 unique ways (using `R` for right and `D` for down):

```
Path 1: R R D   (→ → ↓)
Path 2: R D R   (→ ↓ →)
Path 3: D R R   (↓ → →)
```

### Grid with example path (R R D):

```
[S] → [ ] → [ ]
              ↓
            [E]
```

---

## 🔲 Example: `width = 4`, `height = 3` (4 columns × 3 rows)

* **Right moves = 3**
* **Down moves = 2**
* Total moves = 5 → C(5, 3) = 10 paths

We won’t draw all 10 paths, but here’s how the grid looks:

```
[S] → [ ] → [ ] → [ ]
  ↓     ↓     ↓     ↓
[ ] → [ ] → [ ] → [ ]
  ↓     ↓     ↓     ↓
[ ] → [ ] → [ ] → [E]
```

Each path is a combination of 3 R’s and 2 D’s in some order.

Examples of a few paths:

```
Path 1: R R R D D
Path 2: R R D R D
Path 3: R D R R D
Path 4: D R R R D
Path 5: D D R R R
...
Total: 10 unique paths
```

"""
