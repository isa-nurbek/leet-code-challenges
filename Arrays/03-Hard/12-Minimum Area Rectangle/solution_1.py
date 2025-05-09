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
    columns = initialize_columns(points)
    min_area_found = float("inf")
    edges_parallel_to_y_axis = {}

    sorted_columns = sorted(columns.keys())

    for x in sorted_columns:
        y_values_in_current_column = columns[x]
        y_values_in_current_column.sort()

        for current_idx, y2 in enumerate(y_values_in_current_column):
            for previous_idx in range(current_idx):
                y1 = y_values_in_current_column[previous_idx]
                point_string = str(y1) + ":" + str(y2)

                if point_string in edges_parallel_to_y_axis:
                    current_area = (x - edges_parallel_to_y_axis[point_string]) * (
                        y2 - y1
                    )
                    min_area_found = min(min_area_found, current_area)

                edges_parallel_to_y_axis[point_string] = x

    return min_area_found if min_area_found != float("inf") else 0


def initialize_columns(points):
    columns = {}

    for point in points:
        x, y = point

        if x not in columns:
            columns[x] = []

        columns[x].append(y)

    return columns


# Test Cases:

points = [[1, 5], [5, 1], [4, 2], [2, 4], [2, 2], [1, 2], [4, 5], [2, 5], [-1, -2]]
print(minimum_area_rectangle(points))  # Output: 3

points_2 = [[-4, 4], [4, 4], [4, -2], [-4, -2], [0, -2], [4, 2], [0, 2]]
print(minimum_area_rectangle(points_2))  # Output: 16
