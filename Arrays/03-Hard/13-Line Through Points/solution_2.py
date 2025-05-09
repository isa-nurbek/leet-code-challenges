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
