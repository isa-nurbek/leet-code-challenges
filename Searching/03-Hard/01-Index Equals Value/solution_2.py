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


# O(log(n)) time | O(log(n)) space
def index_equals_value(array):
    """
    Finds the first index in a sorted array where array[index] == index.
    Uses a helper function to perform binary search recursively.

    Args:
        array: A sorted list of integers where elements are distinct and in increasing order.

    Returns:
        The first index where array[index] == index, or -1 if no such index exists.
    """
    return index_equals_value_helper(array, 0, len(array) - 1)


def index_equals_value_helper(array, left_idx, right_idx):
    """
    Helper function that performs binary search to find the first index where array[index] == index.

    Args:
        array: The sorted list of integers to search
        left_idx: Left boundary of the current search range
        right_idx: Right boundary of the current search range

    Returns:
        The first matching index found, or -1 if none exists in the current range
    """

    # Base case: search range is invalid, meaning no match was found
    if left_idx > right_idx:
        return -1

    # Calculate middle index to split search range
    middle_idx = left_idx + (right_idx - left_idx) // 2
    middle_value = array[middle_idx]

    if middle_value < middle_idx:
        # If value is less than index, all elements to the left must also be smaller
        # because array is strictly increasing. So we search right half.
        return index_equals_value_helper(array, middle_idx + 1, right_idx)
    elif middle_value == middle_idx and middle_idx == 0:
        # Found match at index 0 (can't check left neighbor)
        return middle_idx
    elif middle_value == middle_idx and array[middle_idx - 1] < middle_idx - 1:
        # Found match where previous element doesn't match, so this is first occurrence
        return middle_idx
    else:
        # Either:
        # 1) Value > index, so we need to search left half, or
        # 2) Value == index but there might be earlier matches, so search left half
        return index_equals_value_helper(array, left_idx, middle_idx - 1)


# Test Cases:

print(index_equals_value([-5, -3, 0, 3, 4, 5, 9]))
# Output: 3

print(index_equals_value([-12, 1, 2, 3, 12]))
# Output: 1

print(index_equals_value([-5, -4, -3, -2, -1, 0, 1, 3, 5, 6, 7, 11, 12, 14, 19, 20]))
# Output: 11
