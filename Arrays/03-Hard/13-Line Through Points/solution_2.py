# Problem Description:

"""

                                            Line Through Points

You're given an array of points plotted on a `2D graph` (the `x,y-plane`). Write a function that returns the maximum number of
points that a single line (or potentially multiple lines) on the graph passes through.

The input array will contain points represented by an array of two integers `[x, y]`. The input array will never contain duplicate
points and will always contain at least one point.


## Sample Input
```
points = [
  [1, 1],
  [2, 2],
  [3, 3],
  [0, 4],
  [-2, 6],
  [4, 0],
  [2, 1],
]
```

## Sample Output
```
4

// A line passes through points: [-2, 6], [0, 4], [2, 2], [4, 0]
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(n) space - where `n` is the number of points.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n²) time | O(n) space
def line_through_points(points):
    # Initialize the maximum number of points on a line to 1
    # (a single point always forms a "line" with itself)
    max_points = 1

    # Iterate through each point as the reference point
    for i in range(len(points)):
        x1, y1 = points[i]
        # Dictionary to store slopes and their point counts
        slopes = {}

        # Compare with all other points
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            dx = x2 - x1  # Difference in x-coordinates
            dy = y2 - y1  # Difference in y-coordinates

            # Handle vertical line case (undefined/infinite slope)
            if dx == 0:
                # Use (0,1) as a special representation for vertical lines
                slope = (0, 1)
            # Handle horizontal line case (zero slope)
            elif dy == 0:
                # Use (1,0) as a special representation for horizontal lines
                slope = (1, 0)
            else:
                # Calculate greatest common divisor (GCD) to reduce the slope to simplest form
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a

                # Reduce the slope fraction to its simplest form
                common_divisor = gcd(abs(dx), abs(dy))
                reduced_dx = dx // common_divisor
                reduced_dy = dy // common_divisor

                # Ensure consistent representation of slopes
                # For example, make (-2,-4) become (1,2) instead of (-1,-2)
                if reduced_dx < 0:
                    reduced_dx *= -1
                    reduced_dy *= -1

                slope = (
                    reduced_dy,
                    reduced_dx,
                )  # Store slope as (numerator, denominator)

            # Update the count of points for this slope
            if slope not in slopes:
                slopes[slope] = 1  # Start with 1 (the current reference point)
            slopes[slope] += 1  # Add the current point being compared

        # After processing all points for this reference point,
        # update the global maximum if we found a line with more points
        if slopes:
            current_max = max(slopes.values())
            max_points = max(max_points, current_max)

    return max_points


# Test Cases:

points = [[1, 1], [2, 2], [3, 3], [0, 4], [-2, 6], [4, 0], [2, 1]]
print(line_through_points(points))  # Output: 4

points_2 = [[3, 3], [0, 4], [-2, 6], [4, 0], [2, 1], [3, 4], [5, 6], [0, 0]]
print(line_through_points(points_2))  # Output: 3

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

1. **Outer Loop**: The outer loop runs `n` times, where `n` is the number of points.
2. **Inner Loop**: For each iteration of the outer loop, the inner loop runs `n - i - 1` times (where `i` is the current index of
the outer loop). In the worst case, this is roughly `n` times.
3. **GCD Calculation**: Inside the inner loop, the GCD is calculated for each pair of points. The GCD calculation using Euclid's
algorithm has a time complexity of `O(log(min(abs(dx), abs(dy))))`. In the worst case, this can be considered `O(log(max_coordinate))
`, where `max_coordinate` is the maximum value of the coordinates.
4. **Slope Calculation and Dictionary Operations**: The rest of the operations (slope calculation, dictionary insertion/update)
are `O(1)`.

Thus, the total time complexity is:
- Worst case: `O(n² * log(max_coordinate))`
- Best case: `O(n²)` (if all points are the same or GCD calculation is negligible)

### Space Complexity:

1. **Slopes Dictionary**: For each outer loop iteration, a new `slopes` dictionary is created. In the worst case, this dictionary
can hold up to `n` unique slopes (if all lines through the current point are unique).
2. **Other Variables**: The other variables use constant space (`O(1)`).

Thus, the total space complexity is:
- Worst case: `O(n)` (due to the `slopes` dictionary in each iteration, but since it's recreated for each outer loop, the maximum
space at any point is `O(n)`).
- Best case: `O(1)` (if all points are the same or collinear).

### Summary:
- **Time Complexity**: `O(n² * log(max_coordinate))` (worst case), `O(n²)` (best case).
- **Space Complexity**: `O(n)` (worst case), `O(1)` (best case).

This is because the function checks all pairs of points to determine the maximum number of collinear points by comparing slopes.
The GCD calculation adds a logarithmic factor to the time complexity. The space is dominated by the dictionary storing the slopes
for each point.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break down the `line_through_points` function step by step and explain how it determines the **maximum number of points
that lie on the same straight line**.

---

## ✅ **Objective**

Given a list of 2D points, the goal is to find the **maximum number of points** that lie on a **single straight line**.

---

## 📘 **Key Idea**

* Two points define a line.
* Any other point on the same line must share the same **slope** with respect to those two points.
* So, for each point, compute slopes to every other point, and track how many share the same slope (i.e., lie on the same line).

---

## 🔍 **Detailed Explanation**

```
def line_through_points(points):
    max_points = 1
```

* We initialize `max_points = 1` because at the very least, a single point forms a trivial line by itself.

---

```
for i in range(len(points)):
    slopes = {}
    x1, y1 = points[i]
```

* For every point `i`, consider it as the **starting point**.
* Create a dictionary `slopes` to track how many other points share the same slope with `points[i]`.

---

```
for j in range(i + 1, len(points)):
    x2, y2 = points[j]
    dx = x2 - x1
    dy = y2 - y1
```

* Compare point `i` to every subsequent point `j`, calculating the differences in `x` and `y`.

---

### ⚠️ Special Case Handling

```
if dx == 0:
    slope = (0, 1)  # Vertical line
elif dy == 0:
    slope = (1, 0)  # Horizontal line
```

* Vertical lines (infinite slope) are represented as `(0,1)`.
* Horizontal lines (zero slope) are represented as `(1,0)`.

---

### 🧮 Reducing Slopes to Simplest Form

```
else:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common_divisor = gcd(abs(dx), abs(dy))
    reduced_dx = dx // common_divisor
    reduced_dy = dy // common_divisor

    if reduced_dx < 0:
        reduced_dx *= -1
        reduced_dy *= -1

    slope = (reduced_dy, reduced_dx)
```

* For non-vertical/horizontal lines, the slope is `dy/dx`.
* Use `gcd` to reduce `(dy, dx)` to its simplest form.
* Normalize the sign so the same slope doesn't appear with opposite signs.

> Example: `(2, 4)` becomes `(1, 2)`, and `(-2, -4)` also becomes `(1, 2)`.

---

### 📊 Storing Slopes

```
if slope not in slopes:
    slopes[slope] = 1  # Start with 1 (the current point)
slopes[slope] += 1
```

* If we encounter this slope for the first time, initialize its count as `1`.
* Then increment it — this counts how many points share the same slope (line) with `points[i]`.

---

```
if slopes:
    current_max = max(slopes.values())
    max_points = max(max_points, current_max)
```

* After processing all points from `i` to the end, take the highest count of any slope from point `i`.
* Update `max_points` accordingly.

---

```
return max_points
```

* Finally, return the **maximum number of points** found that lie on a single line.

---

## ✅ **Test Case Example**

### Input:

```
points = [[1, 1], [2, 2], [3, 3], [0, 4], [-2, 6], [4, 0], [2, 1]]
```

* Points `[1,1], [2,2], [3,3], [-2,6]` lie on the line `y = x`, so output is `4`.

---

## 💡 Efficiency

* Time Complexity: **O(n²)** — for each point, compare with all others.
* Space Complexity: **O(n)** — to store slope counts per point.

"""
