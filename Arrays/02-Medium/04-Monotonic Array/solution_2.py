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
    # Initialize two flags to track the array's monotonicity
    is_non_decreasing = True  # Assumes the array is non-decreasing initially
    is_non_increasing = True  # Assumes the array is non-increasing initially

    # Iterate through the array starting from the second element
    for i in range(1, len(array)):
        # Check if the current element is less than the previous element
        if array[i] < array[i - 1]:
            # If true, the array is not non-decreasing
            is_non_decreasing = False

        # Check if the current element is greater than the previous element
        if array[i] > array[i - 1]:
            # If true, the array is not non-increasing
            is_non_increasing = False

    # The array is monotonic if it is either non-decreasing or non-increasing
    return is_non_decreasing or is_non_increasing


# Test cases:

print(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
# Output: True

print(is_monotonic([2, 2, 2, 1, 4, 5]))
# Output: False

print(is_monotonic([]))
# Output: True

print(is_monotonic([7]))
# Output: True

# =========================================================================================================================== #
