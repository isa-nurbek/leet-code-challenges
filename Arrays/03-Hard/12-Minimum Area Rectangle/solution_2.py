# Problem Description:

"""

                                            Minimum Area Rectangle

You're given an array of points plotted on a `2D graph (the x,y-plane)`. Write a function that returns the minimum area of any
rectangle that can be formed using any `4` of these points such that the rectangle's sides are parallel to the `x` and `y` axes
(i.e., only rectangles with horizontal and vertical sides should be considered no rectangles with diagonal sides). If no rectangle
can be formed, your function should return `0`.

The input array will contain points represented by arrays of two integers `[x, y]`. The input array will never contain `duplicate
points`.


## Sample Input
```
points =
[
  [1, 5],
  [5, 1],
  [4, 2],
  [2, 4],
  [2, 2],
  [1, 2],
  [4, 5],
  [2, 5],
  [-1, -2],
]
```

## Sample Output
```
3

// The rectangle with corners [1, 5], [2, 5], [1, 2], and [2, 2] has the minimum area: 3
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(n) space - where `n` is the number of points.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n²) time | O(n) space
def minimum_area_rectangle(points):
    point_set = set(map(tuple, points))
    columns = {}

    for x, y in points:
        if x not in columns:
            columns[x] = []
        columns[x].append(y)

    min_area = float("inf")
    processed_columns = {}

    for x in sorted(columns):
        column = columns[x]
        column.sort()

        # Skip if fewer than 2 points in the column
        if len(column) < 2:
            continue

        # Compare with previously processed columns
        for prev_x in processed_columns:
            prev_column = processed_columns[prev_x]
            i = j = 0
            common_ys = []

            # Find common y-values between current and previous column
            while i < len(column) and j < len(prev_column):
                if column[i] == prev_column[j]:
                    common_ys.append(column[i])
                    i += 1
                    j += 1
                elif column[i] < prev_column[j]:
                    i += 1
                else:
                    j += 1

            # If at least 2 common y-values, compute area
            if len(common_ys) >= 2:
                width = x - prev_x
                height = min(
                    common_ys[k + 1] - common_ys[k] for k in range(len(common_ys) - 1)
                )
                current_area = width * height
                if current_area == 1:
                    return 1  # Early termination
                min_area = min(min_area, current_area)

        # Store the current column for future comparisons
        processed_columns[x] = column

    return min_area if min_area != float("inf") else 0


# Test Cases:

points = [[1, 5], [5, 1], [4, 2], [2, 4], [2, 2], [1, 2], [4, 5], [2, 5], [-1, -2]]
print(minimum_area_rectangle(points))  # Output: 3

points_2 = [[-4, 4], [4, 4], [4, -2], [-4, -2], [0, -2], [4, 2], [0, 2]]
print(minimum_area_rectangle(points_2))  # Output: 16

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

- **Building `point_set` and `columns`:** O(n).

- **Sorting each column:** O(k * m log m), where `k` is the number of columns and `m` is the average number of points per column.
In the worst case, this is O(n log n).

- **Finding common y-values:** For each pair of columns, this is O(m + n) in the worst case (using a two-pointer approach).
If there are `k` columns, this becomes O(k² * m).

- **Overall:** O(n + k² * m + n log n). In the worst case (all points in one column), this is O(n²).
In the average case, it's closer to O(n log n + k² * m).

### Space Complexity:

- `point_set`: O(n).
- `columns`: O(n).
- `processed_columns`: O(k * m) in the worst case, where `k` is the number of columns and `m` is the average number of points
per column.

- **Overall:** O(n).

### Summary:
- **Time Complexity:** O(n²) in the worst case, O(n log n + k² * m) in the average case.
- **Space Complexity:** O(n)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Here's a **detailed explanation** of how your `minimum_area_rectangle` function works and what it's doing at each step.

## 🎯 **Goal of the Function**

Given a list of 2D points, the function returns the **minimum area** of an **axis-aligned rectangle** that can be formed using 
any **four points** from the list.

* Axis-aligned rectangle: The sides are parallel to the x and y axes.
* You return the smallest such area; if no rectangle can be formed, return 0.

---

## 📦 Step-by-Step Breakdown

### 🧩 Step 1: Convert Points to Set

```
point_set = set(map(tuple, points))
```

* You convert the list of points into a set of tuples so you can quickly check if a point exists using constant-time lookup (`O(1)`).

---

### 🏗 Step 2: Group Y-values by X-coordinate

```
columns = {}

for x, y in points:
    if x not in columns:
        columns[x] = []
    columns[x].append(y)
```

* You group all points by their x-coordinate.
* `columns[x]` will contain a **list of all y-values** that share the same x.
  👉 So each `columns[x]` represents a **vertical column** of points.

Example:

```
points = [[1, 2], [1, 5], [2, 2], [2, 5]]
columns = {
    1: [2, 5],
    2: [2, 5]
}
```

---

### ⚙ Step 3: Process Each Column in Order

```
min_area = float('inf')
processed_columns = {}

for x in sorted(columns):
    ...
```

* Sort x-values (columns) to process from left to right.
* `processed_columns` keeps track of all columns we've already seen to compare with future columns.

---

### 🔍 Step 4: Compare Column with Previous Columns

#### ➕ Common y-values (horizontal alignment)

```
for prev_x in processed_columns:
    prev_column = processed_columns[prev_x]
    ...
    while i < len(column) and j < len(prev_column):
        ...
```

* You're comparing current column `x` with each previous column `prev_x`.
* Use two pointers to **find common y-values** between the two columns (i.e., rows that can form a rectangle side).
* These common y-values represent potential **horizontal sides** of rectangles.

---

### 📐 Step 5: Compute Area for All Rectangles

```
if len(common_ys) >= 2:
    width = x - prev_x
    height = min(common_ys[k+1] - common_ys[k] for k in range(len(common_ys)-1))
    current_area = width * height
```

* If you have **2 or more** common y-values between columns `x` and `prev_x`, you can form **rectangles** between each pair
of consecutive common y-values.
* Compute the area of the rectangle with the **minimum height** to potentially minimize area.
* Update `min_area`.

**Early return:** If area = 1, return immediately.

---

### 🗃 Step 6: Store Current Column

```
processed_columns[x] = column
```

* Save the current column so future columns can compare with it.

---

### 🏁 Step 7: Return Result

```
return min_area if min_area != float('inf') else 0
```

* If no rectangles were found, return `0`.
* Otherwise, return the smallest area found.

---

## ✅ Example Walkthrough

```
points = [[1, 5], [5, 1], [4, 2], [2, 4], [2, 2], [1, 2], [4, 5], [2, 5], [-1, -2]]
```

* Consider columns:

```
{
    -1: [-2],
     1: [5, 2],
     2: [4, 2, 5],
     4: [2, 5],
     5: [1]
}
```

* At `x=1` and `x=2`, common y-values = \[2, 5]
  → Two horizontal lines → rectangle of width 1, height = 3 → area = 3

---

Here’s an **ASCII visualization** to help you understand how axis-aligned rectangles are formed by matching vertical columns
with common y-values.

---

### 🎯 Example Points:

```
points = [[1, 5], [1, 2], [2, 5], [2, 2]]
```

These form two vertical columns:

* Column at `x = 1`: y = 5, 2
* Column at `x = 2`: y = 5, 2

---

### 🧱 Grid Representation (Y-axis top to bottom)

```plaintext
y=6 |                   
y=5 |   *           *     ← (1,5) and (2,5)
y=4 |
y=3 |
y=2 |   *           *     ← (1,2) and (2,2)
y=1 |
     +---+---+---+---+ 
        x=1 x=2
```

---

### 🧾 What’s Happening?

* Both x=1 and x=2 have **y=2** and **y=5** ⇒ two matching rows.
* You can connect these 4 points to form a **rectangle**:

  ```
  Top:    (1,5) ────── (2,5)
  Bottom: (1,2) ────── (2,2)
  ```
* **Width** = 2 - 1 = 1
* **Height** = 5 - 2 = 3
* **Area** = 3

---

### 🧊 Another Example

```
points = [[0, 1], [0, 3], [3, 1], [3, 3]]
```

ASCII:

```plaintext
y=4 |        
y=3 |  *           *   ← (0,3), (3,3)
y=2 |
y=1 |  *           *   ← (0,1), (3,1)
     +---+---+---+---+
        x=0     x=3
```

* Common y-values: 1 and 3
* Width = 3
* Height = 2
* Area = 6

"""
