# Problem Description:

"""
                                             Index Equals Value

You're given `two sorted arrays` of integers `array_one` and `array_two`. Write a function that returns the `median` of these arrays.

You can assume both arrays have at least one value. However, they could be of different lengths. If the `median` is a decimal value,
it should not be rounded (beyond the inevitable rounding of floating point math).


## Sample Input:
```
array_one = [1, 3, 4, 5]
array_two = [2, 3, 6, 7]
```

## Sample Output:
```
3.5

// The combined array is [1, 2, 3, 3, 4, 5, 6, 7]
```

## Optimal Time & Space Complexity:
```
O(log(min(n, m)) time | O(1) space - where `n` is the length of `array_one` and `m` is the length of `array_two`.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(min(n, m))) time | O(1) space
def median_of_two_sorted_arrays(array_one, array_two):
    # Ensure array_one is the smaller array to reduce binary search range
    if len(array_one) > len(array_two):
        array_one, array_two = array_two, array_one

    n, m = len(array_one), len(array_two)
    total = n + m
    half = (total + 1) // 2  # This works for both even and odd total lengths

    # Initialize binary search bounds for the smaller array
    left, right = 0, n

    while left <= right:
        # Partition position in array_one
        mid = (left + right) // 2
        # Corresponding partition position in array_two
        remaining = half - mid

        # Handle edge cases where partition might be at the beginning or end
        # of either array by using +/- infinity as appropriate
        max_left_one = float("-inf") if mid == 0 else array_one[mid - 1]
        min_right_one = float("inf") if mid == n else array_one[mid]
        max_left_two = float("-inf") if remaining == 0 else array_two[remaining - 1]
        min_right_two = float("inf") if remaining == m else array_two[remaining]

        # Check if we've found the correct partition
        if max_left_one <= min_right_two and max_left_two <= min_right_one:
            # If total length is odd, median is the max of left partitions
            if total % 2 == 1:
                return max(max_left_one, max_left_two)
            else:
                # If even, median is average of max left and min right partitions
                return (
                    max(max_left_one, max_left_two) + min(min_right_one, min_right_two)
                ) / 2
        # If array_one's left partition is too big, move partition left
        elif max_left_one > min_right_two:
            right = mid - 1
        # Otherwise, move partition right
        else:
            left = mid + 1

    # This should theoretically never be reached with valid sorted input
    raise ValueError("Input arrays are not sorted or invalid.")


# Test Cases:

print(median_of_two_sorted_arrays([1, 3, 4, 5], [2, 3, 6, 7]))
# Output: 3.5

print(median_of_two_sorted_arrays([2, 2, 2, 2, 2], [3, 3, 3, 3]))
# Output: 2
