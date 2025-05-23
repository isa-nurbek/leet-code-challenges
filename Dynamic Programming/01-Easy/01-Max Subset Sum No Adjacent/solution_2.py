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
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]

    second_prev = array[0]
    first_prev = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(first_prev, second_prev + array[i])
        second_prev, first_prev = first_prev, current

    return first_prev


# Test Cases:

print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))
# Output: 330

print(max_subset_sum_no_adjacent([]))
# Output: 0

print(max_subset_sum_no_adjacent([30, 25, 50, 55, 100]))
# Output: 180
