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
    """
    Finds the minimum area rectangle that can be formed from a given set of points.
    The rectangle must be axis-aligned (sides parallel to x and y axes).

    Args:
        points: List of [x, y] coordinate points

    Returns:
        The area of the smallest rectangle that can be formed, or 0 if no rectangle exists
    """

    # Group points by their x-coordinate (creates vertical columns of points)
    columns = initialize_columns(points)

    # Initialize minimum area to infinity (so any found rectangle will be smaller)
    min_area_found = float("inf")

    # Dictionary to store pairs of y-coordinates we've seen before (as "y1:y2" strings)
    # and the x-coordinate where we last saw them
    edges_parallel_to_y_axis = {}

    # Process columns in order from left to right
    sorted_columns = sorted(columns.keys())

    for x in sorted_columns:
        # Get all y-coordinates in the current x-column and sort them
        y_values_in_current_column = columns[x]
        y_values_in_current_column.sort()

        # Compare all pairs of y-values in this column
        for current_idx, y2 in enumerate(y_values_in_current_column):
            for previous_idx in range(current_idx):
                y1 = y_values_in_current_column[previous_idx]

                # Create a string key representing this vertical edge
                point_string = str(y1) + ":" + str(y2)

                # If we've seen this y-pair before, we can form a rectangle
                if point_string in edges_parallel_to_y_axis:
                    # Calculate area: width * height
                    # width = current x - previous x where we saw this y-pair
                    # height = y2 - y1
                    current_area = (x - edges_parallel_to_y_axis[point_string]) * (
                        y2 - y1
                    )

                    # Update minimum area if this is smaller
                    min_area_found = min(min_area_found, current_area)

                # Record that we saw this y-pair at the current x-coordinate
                edges_parallel_to_y_axis[point_string] = x

    # Return the minimum area found, or 0 if no rectangle exists
    return min_area_found if min_area_found != float("inf") else 0


def initialize_columns(points):
    """
    Helper function to organize points into columns by their x-coordinate.

    Args:
        points: List of [x, y] coordinate points

    Returns:
        A dictionary mapping x-coordinates to lists of their y-coordinates
    """
    columns = {}

    for point in points:
        x, y = point

        # Create a new list for this x-coordinate if we haven't seen it before
        if x not in columns:
            columns[x] = []

        # Add the y-coordinate to this x-column
        columns[x].append(y)

    return columns


# Test Cases:

points = [[1, 5], [5, 1], [4, 2], [2, 4], [2, 2], [1, 2], [4, 5], [2, 5], [-1, -2]]
print(minimum_area_rectangle(points))  # Output: 3

points_2 = [[-4, 4], [4, 4], [4, -2], [-4, -2], [0, -2], [4, 2], [0, 2]]
print(minimum_area_rectangle(points_2))  # Output: 16
