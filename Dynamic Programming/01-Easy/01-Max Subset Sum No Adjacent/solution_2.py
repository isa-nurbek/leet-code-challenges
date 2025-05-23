# Problem Description:

"""
                                                Max Subset Sum No Adjacent

Write a function that takes in an array of `positive integers` and returns the `maximum sum of non-adjacent elements` in the array.

If the input array is empty, the function should return `0`.


## Sample Input:
```
array = [75, 105, 120, 75, 90, 135]
```

## Sample Output:
```
330

// 75 + 120 + 135
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def max_subset_sum_no_adjacent(array):
    """
    Calculate the maximum sum of a subset of non-adjacent elements in the array.

    Args:
    array: List of numbers to process

    Returns:
    Maximum sum of non-adjacent elements
    """

    # Handle edge cases
    if not len(array):
        return 0  # Empty array has sum 0
    elif len(array) == 1:
        return array[0]  # Only one element, so it's the max

    # Initialize variables to keep track of maximum sums:
    # second_prev represents max sum up to i-2
    # first_prev represents max sum up to i-1
    second_prev = array[0]  # Max sum for first element
    first_prev = max(array[0], array[1])  # Max sum for first two elements

    # Iterate through remaining elements starting from index 2
    for i in range(2, len(array)):
        # Current max is either:
        # 1. The max sum up to previous element (don't take current element)
        # 2. The max sum up to second previous element plus current element
        current = max(first_prev, second_prev + array[i])

        # Update the tracking variables for next iteration:
        # second_prev becomes the old first_prev
        # first_prev becomes the current max
        second_prev, first_prev = first_prev, current

    # After processing all elements, first_prev holds the maximum sum
    return first_prev


# Test Cases:

print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))
# Output: 330

print(max_subset_sum_no_adjacent([]))
# Output: 0

print(max_subset_sum_no_adjacent([30, 25, 50, 55, 100]))
# Output: 180
