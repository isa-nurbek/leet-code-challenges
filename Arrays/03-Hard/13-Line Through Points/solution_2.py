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
    max_points = 1

    for i in range(len(points)):
        slopes = {}
        x1, y1 = points[i]

        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1

            # Handle vertical line case
            if dx == 0:
                slope = (0, 1)  # Using (0,1) to represent vertical
            # Handle horizontal line case
            elif dy == 0:
                slope = (1, 0)  # Using (1,0) to represent horizontal
            else:
                # Calculate GCD to reduce fraction to simplest form
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a

                common_divisor = gcd(abs(dx), abs(dy))
                reduced_dx = dx // common_divisor
                reduced_dy = dy // common_divisor

                # Ensure consistent representation
                if reduced_dx < 0:
                    reduced_dx *= -1
                    reduced_dy *= -1

                slope = (reduced_dy, reduced_dx)

            # Use slope as dictionary key
            if slope not in slopes:
                slopes[slope] = 1  # Start with 1 (the current point)
            slopes[slope] += 1

        if slopes:
            current_max = max(slopes.values())
            max_points = max(max_points, current_max)

    return max_points


# Test Cases:

points = [[1, 1], [2, 2], [3, 3], [0, 4], [-2, 6], [4, 0], [2, 1]]
print(line_through_points(points))  # Output: 4

points_2 = [[3, 3], [0, 4], [-2, 6], [4, 0], [2, 1], [3, 4], [5, 6], [0, 0]]
print(line_through_points(points_2))  # Output: 3
