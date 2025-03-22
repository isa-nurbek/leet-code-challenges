# Problem Description:

"""
                                            # Count Squares

Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates) and returns the number of squares
that can be formed by these coordinates.

A square must have its four corners amongst the coordinates in order to be counted. A single coordinate can be used as a corner
for multiple different squares.

You can also assume that no coordinate will be farther than 100 units from the origin.


## Sample Input:
```
points = [
  [1, 1],
  [0, 0],
  [-4, 2],
  [-2, -1],
  [0, 1],
  [1, 0],
  [-1, 4],
]
```

## Sample Output:
```
2  // [1, 1], [0, 0], [0, 1], and [1, 0] makes a square,
// as does [1, 1], [-4, 2], [-2, -1], and [-1, 4]
```

## Optimal Time & Space Complexity:
```
O(n²) time | O(n) space - where `n` is the number of points.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n²) time | O(n) space
def count_squares(points):
    # Create a set to store all points as strings for quick lookup
    points_set = set()

    # Convert each point to a string and add it to the set
    for point in points:
        points_set.add(point_to_string(point))

    # Initialize a counter to keep track of the number of squares found
    count = 0

    # Iterate over all pairs of points to find potential diagonals of squares
    for point_a in points:
        for point_b in points:
            # Skip if the points are the same
            if point_a == point_b:
                continue

            # Calculate the midpoint between point_a and point_b
            mid_point = [(point_a[0] + point_b[0]) / 2, (point_a[1] + point_b[1]) / 2]

            # Calculate the x and y distances from point_a to the midpoint
            x_distance_from_mid = point_a[0] - mid_point[0]
            y_distance_from_mid = point_a[1] - mid_point[1]

            # Calculate the coordinates of the other two points (point_c and point_d)
            # that would form a square with point_a and point_b
            point_c = [
                mid_point[0] + y_distance_from_mid,
                mid_point[1] - x_distance_from_mid,
            ]

            point_d = [
                mid_point[0] - y_distance_from_mid,
                mid_point[1] + x_distance_from_mid,
            ]

            # Check if both point_c and point_d exist in the set of points
            if (
                point_to_string(point_c) in points_set
                and point_to_string(point_d) in points_set
            ):
                # If they exist, increment the square count
                count += 1

    # Since each square is counted 4 times (once for each diagonal), divide by 4 to get the correct count
    return count / 4


def point_to_string(point):
    # If the coordinates are integers, convert them to integers for cleaner representation
    if point[0] % 1 == 0 and point[1] % 1 == 0:
        point = [int(coordinate) for coordinate in point]

    # Convert the point to a string in the format "x,y"
    return ",".join([str(coordinate) for coordinate in point])


# Test Cases:

points = [
    [1, 1],
    [0, 0],
    [-4, 2],
    [-2, -1],
    [0, 1],
    [1, 0],
    [-1, 4],
]

points_2 = [
    [1, 1],
    [0, 0],
    [0, 1],
    [1, 0],
]

points_3 = []

print(count_squares(points))
# Output: 2.0

print(count_squares(points_2))
# Output: 1.0

print(count_squares(points_3))
# Output: 0.0
