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
    """
    Finds the maximum number of points that lie on the same straight line.

    Args:
        points: List of (x, y) coordinate points

    Returns:
        Maximum number of collinear points
    """
    max_number_of_points_on_line = 1  # At least one point will always be on any line

    # For each point, check all possible lines through it and other points
    for idx1, p1 in enumerate(points):
        slopes = {}  # Dictionary to count points with same slope from p1

        # Compare with all points after current point to avoid duplicate checks
        for idx2 in range(idx1 + 1, len(points)):
            p2 = points[idx2]
            # Get the slope between p1 and p2 as a reduced fraction [rise, run]
            rise, run = get_slope_of_line_between_points(p1, p2)
            # Create a unique string key for the slope to use in dictionary
            slope_key = create_hashable_key_for_rational(rise, run)

            # Initialize count if slope not seen before
            if slope_key not in slopes:
                slopes[slope_key] = 1  # Start with 1 to count p1

            slopes[slope_key] += 1  # Add p2 to this slope count

        # Update global maximum with the maximum count for lines through p1
        max_number_of_points_on_line = max(
            max_number_of_points_on_line, max(slopes.values(), default=0)
        )

    return max_number_of_points_on_line


def get_slope_of_line_between_points(p1, p2):
    """
    Calculates the slope between two points as a reduced fraction [rise, run].
    Handles vertical lines and duplicate points.

    Args:
        p1: First point (x1, y1)
        p2: Second point (x2, y2)

    Returns:
        Slope as [numerator, denominator] in simplest form
    """
    p1x, p1y = p1
    p2x, p2y = p2
    slope = [1, 0]  # Default for vertical line (undefined slope)

    if p1x != p2x:  # If not vertical line
        x_diff = p1x - p2x
        y_diff = p1y - p2y

        # Reduce fraction to simplest form using GCD
        gcd = get_greatest_common_divisor(abs(x_diff), abs(y_diff))

        x_diff = x_diff // gcd
        y_diff = y_diff // gcd

        # Ensure denominator is positive for consistent representation
        if x_diff < 0:
            x_diff *= -1
            y_diff *= -1

        slope = [y_diff, x_diff]  # slope = rise/run = y_diff/x_diff

    return slope


def create_hashable_key_for_rational(numerator, denominator):
    """
    Creates a unique string representation of a fraction for use as dictionary key.

    Args:
        numerator: Numerator of the slope fraction
        denominator: Denominator of the slope fraction

    Returns:
        String in format "numerator:denominator"
    """
    return str(numerator) + ":" + str(denominator)


def get_greatest_common_divisor(num1, num2):
    """
    Calculates the greatest common divisor (GCD) of two numbers using Euclid's algorithm.

    Args:
        num1: First number
        num2: Second number

    Returns:
        GCD of num1 and num2
    """
    a = num1
    b = num2

    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        # Replace larger number with remainder of division
        a, b = b, a % b


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

2. **Inner Loop**: For each iteration of the outer loop, the inner loop runs `n - idx1 - 1` times (which is roughly `n`
in the worst case).

3. **Slope Calculation**: Inside the inner loop, `get_slope_of_line_between_points` is called, which involves:
   - A constant-time check for vertical lines (`p1x != p2x`).
   - If not vertical, it computes the GCD of the differences in x and y coordinates. The GCD computation using Euclid's algorithm
   is `O(log(min(num1, num2)))`, but since the differences are bounded by the maximum coordinate value (let's assume coordinates
   are small integers or that the GCD is effectively constant time for practical purposes), we can treat this as `O(1)`.
   - The rest of the operations are `O(1)`.
   
4. **Slope Dictionary Operations**: Inserting or updating the `slopes` dictionary is `O(1)` per operation (assuming a good hash function).

Thus, the total time complexity is:
- Outer loop: `O(n)`
- Inner loop: `O(n)` per outer iteration
- Inner operations: `O(1)`

Total: `O(n²)`.

### Space Complexity:

1. The `slopes` dictionary is recreated for each outer loop iteration. In the worst case, it can contain up to `n` unique
slopes (if all lines through `p1` have unique slopes).
2. The space for the `slopes` dictionary is `O(n)` per outer iteration, but since it is recreated each time, the peak space
is `O(n)` (not `O(n²)`).

Thus, the total space complexity is `O(n)` (for the `slopes` dictionary and a few other variables).

### Summary:
- **Time Complexity**: `O(n²)`
- **Space Complexity**: `O(n)`

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The function `line_through_points(points)` is designed to determine **the maximum number of points that lie on the same straight
line** from a given list of 2D points.

---

### 🧠 **High-Level Idea**

To find the maximum number of points that lie on the same line, we:

* Loop over each point.
* For that point, compute the **slope** between it and every other point.
* Count how many times each slope occurs.
* The maximum frequency for any slope from a given point indicates how many points lie on the same line through that point.
* Track the global maximum across all starting points.

---

## 🔍 Detailed Walkthrough

---

### `line_through_points(points)`

```
max_number_of_points_on_line = 1
```

We initialize a variable to keep track of the global maximum number of collinear points (at least one point always exists).

---

### Outer Loop – picking base point

```
for idx1, p1 in enumerate(points):
    slopes = {}
```

We iterate over each point `p1` in `points`. For each base point `p1`, we maintain a dictionary `slopes` to store counts of
different slopes between `p1` and the rest.

---

### Inner Loop – comparing with other points

```
for idx2 in range(idx1 + 1, len(points)):
    p2 = points[idx2]
```

For each pair `(p1, p2)` where `p2` comes after `p1`, compute the slope.

---

### Get the slope

```
rise, run = get_slope_of_line_between_points(p1, p2)
slope_key = create_hashable_key_for_rational(rise, run)
```

We get the reduced slope between `p1` and `p2` in the form `[rise, run]`, and then convert it to a hashable key for dictionary usage.

---

### Update dictionary with slope

```
if slope_key not in slopes:
    slopes[slope_key] = 1
slopes[slope_key] += 1
```

* We initialize the slope count to 1 if it doesn’t exist.
* Then increment it to reflect one more point found on that slope (so it becomes 2 for the first occurrence since we start with
the base point and `p2`).

---

### Update global maximum

```
max_number_of_points_on_line = max(
    max_number_of_points_on_line, max(slopes.values(), default=0)
)
```

Update the global maximum with the highest number of points on any line through `p1`.

---

### Final result

```
return max_number_of_points_on_line
```

Return the overall maximum number of collinear points.

---

## 🧮 Helper Functions

---

### `get_slope_of_line_between_points(p1, p2)`

```
def get_slope_of_line_between_points(p1, p2):
    ...
    if p1x != p2x:
        ...
        gcd = get_greatest_common_divisor(abs(x_diff), abs(y_diff))
        ...
        slope = [y_diff, x_diff]
```

* Calculates the slope `(rise, run)` between `p1` and `p2` in a **normalized rational form** to avoid floating point precision errors.
* Uses GCD to reduce slope.
* Ensures consistency in sign by making denominator positive.

If `p1x == p2x`, slope is vertical → represented as `[1, 0]`.

---

### `create_hashable_key_for_rational(numerator, denominator)`

```
return str(numerator) + ":" + str(denominator)
```

Convert a slope like `[2, 1]` to `"2:1"` so it can be used as a dictionary key.

---

### `get_greatest_common_divisor(num1, num2)`

```
while True:
    if a == 0:
        return b
    if b == 0:
        return a
    a, b = b, a % b
```

Standard Euclidean algorithm to compute GCD for reducing the slope.

---

## ✅ Example Input/Output

### Example 1:

```
points = [[1, 1], [2, 2], [3, 3], [0, 4], [-2, 6], [4, 0], [2, 1]]
```

* Points `[1,1], [2,2], [3,3], [-2,6]` lie on the same line (slope = 1).
* Result: `4`

### Example 2:

```
points = [[3, 3], [0, 4], [-2, 6], [4, 0], [2, 1], [3, 4], [5, 6], [0, 0]]
```

* Best line includes `[0,4], [-2,6], [3,3]` or similar.
* Result: `3`

---

## 🧪 Time Complexity

Let `n = number of points`:

* Outer loop: `O(n)`
* Inner loop: up to `O(n)`
* Slope calculation & hash: `O(1)`

**Overall: O(n²)** — which is efficient for up to \~10⁴ points.

---

Let's visualize the points and lines using ASCII.

We’ll take the first test case:

```
points = [[1, 1], [2, 2], [3, 3], [0, 4], [-2, 6], [4, 0], [2, 1]]
```

We’ll map these points roughly on a coordinate grid (Y increases upward, X to the right):

---

### 🗺️ ASCII Grid (approximate)

```
 6 |       *                   (-2,6)
 5 |                           
 4 | *                         (0,4)
 3 |         *                 (3,3)
 2 |     *                     (2,2)
 1 | *       *                 (1,1)  (2,1)
 0 |             *             (4,0)
   +--------------------------
     -2  -1   0   1   2   3   4   X
```

---

### 📈 Line of Best Fit

Let's find which points lie on the same straight line.

**Slope 1 (rise/run = 1):**

* From (1,1) to (2,2), (3,3), (-2,6)
* These all follow: `y = x`

```
Line: y = x
Points: (1,1), (2,2), (3,3), (-2,6)
```

So, visually:

```
 6 |       *                   (-2,6)
 5 |                           
 4 | *                         (0,4)
 3 |         *                 (3,3)   ← on line
 2 |     *                     (2,2)   ← on line
 1 | *       *                 (1,1)   ← on line, (2,1) is not
 0 |             *             (4,0)
   +--------------------------
     -2  -1   0   1   2   3   4   X
```

---

### 🧩 Other Lines:

You can also visualize other lines like:

* (0,4) → (-2,6) has slope = -1
* (2,1) → (4,0) has slope = -0.5

But none of them go through more than 2 or 3 points.

---

### ✅ Final Result:

The maximum number of points that lie on the same line is **4**, clearly visible as those aligned diagonally through slope `1`.

"""
