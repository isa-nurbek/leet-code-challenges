# Problem Description:

"""

                                        # Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing
elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.


## Sample Input:
```
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
```

## Sample Output:
```
True
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space - where `n` is the length of the array
def is_monotonic(array):
    # If the array has 2 or fewer elements, it is always monotonic
    if len(array) <= 2:
        return True

    # Calculate the initial direction of the array (increasing or decreasing)
    direction = array[1] - array[0]

    # Iterate through the array starting from the third element
    for i in range(2, len(array)):
        # If the direction is still undetermined (i.e., direction == 0),
        # update the direction based on the current and previous elements
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue

        # Check if the current element breaks the previously determined direction
        if breaks_direction(direction, array[i - 1], array[i]):
            return False

    # If no elements break the direction, the array is monotonic
    return True


def breaks_direction(direction, previous_int, current_int):
    # Calculate the difference between the current and previous elements
    difference = current_int - previous_int

    # If the initial direction was increasing, check if the current difference is decreasing
    if direction > 0:
        return difference < 0

    # If the initial direction was decreasing, check if the current difference is increasing
    return difference > 0


# Test cases:

print(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
# Output: True

print(is_monotonic([2, 2, 2, 1, 4, 5]))
# Output: False

print(is_monotonic([]))
# Output: True

# =========================================================================================================================== #
