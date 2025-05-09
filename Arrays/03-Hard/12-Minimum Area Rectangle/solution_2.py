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
