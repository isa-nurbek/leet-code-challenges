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


# O(n) time | O(n) space
def max_subset_sum_no_adjacent(array):
    # Handle edge cases:
    # If array is empty, maximum sum is 0
    if not len(array):
        return 0
    # If array has only one element, that's the maximum sum
    elif len(array) == 1:
        return array[0]

    # Create a copy of the array to store maximum sums at each position
    max_sums = array[:]

    # For the second element, the maximum sum is either:
    # - the first element (if we skip this one), or
    # - the second element itself (if we take it and skip the first)
    max_sums[1] = max(array[0], array[1])

    # Iterate through the rest of the array starting from index 2
    for i in range(2, len(array)):
        # At each position, the maximum sum is either:
        # 1. The maximum sum up to the previous position (we don't take current element)
        # OR
        # 2. The maximum sum up to two positions back plus current element (we take current)
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])

    # The last element in max_sums contains the maximum sum for the entire array
    return max_sums[-1]


# Test Cases:

print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))
# Output: 330

print(max_subset_sum_no_adjacent([]))
# Output: 0

print(max_subset_sum_no_adjacent([30, 25, 50, 55, 100]))
# Output: 180
