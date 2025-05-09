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
    max_number_of_points_on_line = 1
    for idx1, p1 in enumerate(points):
        slopes = {}

        for idx2 in range(idx1 + 1, len(points)):
            p2 = points[idx2]
            rise, run = get_slope_of_line_between_points(p1, p2)
            slope_key = create_hashable_key_for_rational(rise, run)

            if slope_key not in slopes:
                slopes[slope_key] = 1

            slopes[slope_key] += 1

        max_number_of_points_on_line = max(
            max_number_of_points_on_line, max(slopes.values(), default=0)
        )

    return max_number_of_points_on_line


def get_slope_of_line_between_points(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    slope = [1, 0]

    if p1x != p2x:
        x_diff = p1x - p2x
        y_diff = p1y - p2y

        gcd = get_greatest_common_divisor(abs(x_diff), abs(y_diff))

        x_diff = x_diff // gcd
        y_diff = y_diff // gcd

        if x_diff < 0:
            x_diff *= -1
            y_diff *= -1

        slope = [y_diff, x_diff]

    return slope


def create_hashable_key_for_rational(numerator, denominator):
    return str(numerator) + ":" + str(denominator)


def get_greatest_common_divisor(num1, num2):
    a = num1
    b = num2

    while True:
        if a == 0:
            return b

        if b == 0:
            return a

        a, b = b, a % b


# Test Cases:

points = [[1, 1], [2, 2], [3, 3], [0, 4], [-2, 6], [4, 0], [2, 1]]
print(line_through_points(points))  # Output: 4

points_2 = [[3, 3], [0, 4], [-2, 6], [4, 0], [2, 1], [3, 4], [5, 6], [0, 0]]
print(line_through_points(points_2))  # Output: 3
