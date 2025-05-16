# Problem Description:

"""
                                             Index Equals Value

Write a function that takes in a sorted array of distinct integers and returns the first index in the array that is equal to the
value at that index. In other words, your function should return the minimum index where `index == array[index]`.

If there is no such index, your function should return `-1`.


## Sample Input:
```
array = [-5, -3, 0, 3, 4, 5, 9]
```

## Sample Output:
```
3

// 3 == array[3]
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(n)) time | O(1) space
def index_equals_value(array):
    # Initialize left and right pointers for binary search
    left = 0
    right = len(array) - 1
    # Initialize result to -1 (no match found case)
    result = -1

    # Binary search loop
    while left <= right:
        # Calculate middle index to avoid potential overflow
        middle = left + (right - left) // 2
        middle_value = array[middle]

        if middle_value == middle:
            # Found a match, store the result
            result = middle
            # Continue searching left half to find a smaller matching index
            # since we want the smallest index where array[i] == i
            right = middle - 1
        elif middle_value < middle:
            # If value is less than index, all elements to the left must also be
            # smaller than their indices (since array is sorted)
            # So we search the right half
            left = middle + 1
        else:  # middle_value > middle
            # If value is greater than index, all elements to the right must also be
            # larger than their indices (since array is sorted)
            # So we search the left half
            right = middle - 1

    # Return the smallest found index where array[i] == i, or -1 if none exists
    return result


# Test Cases:

print(index_equals_value([-5, -3, 0, 3, 4, 5, 9]))
# Output: 3

print(index_equals_value([-12, 1, 2, 3, 12]))
# Output: 1

print(index_equals_value([-5, -4, -3, -2, -1, 0, 1, 3, 5, 6, 7, 11, 12, 14, 19, 20]))
# Output: 11
