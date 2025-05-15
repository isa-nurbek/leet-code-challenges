# Problem Description:

"""
                                             Shifted Binary Search

Write a function that takes in a sorted array of distinct integers as well as a target integer. The caveat is that the integers in
the array have been shifted by some amount; in other words, they've been moved to the left or to the right by one or more positions.
For example, `[1, 2, 3, 4]` might have turned into `[3, 4, 1, 2]`.

The function should use a variation of the `Binary Search` algorithm to determine if the target integer is contained in the array
and should return its `index` if it is, otherwise `-1`.


## Sample Input:
```
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
```

## Sample Output:
```
8
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(n)) time | O(log(n)) space
def shifted_binary_search(array, target):
    """Performs a binary search on a shifted sorted array.

    Args:
        array: A sorted array that has been shifted (rotated) by some unknown offset.
        target: The value to search for in the array.

    Returns:
        The index of the target if found, otherwise -1.
    """
    return shifted_binary_search_helper(array, target, 0, len(array) - 1)


def shifted_binary_search_helper(array, target, left, right):
    """Helper function that performs the actual shifted binary search recursively.

    Args:
        array: The input array.
        target: The value to search for.
        left: The left boundary of the current search range.
        right: The right boundary of the current search range.

    Returns:
        The index of the target if found, otherwise -1.
    """
    # Base case: target not found in current search range
    if left > right:
        return -1

    middle = (left + right) // 2
    potential_match = array[middle]

    # These are used to determine which side is properly ordered
    left_num = array[left]
    right_num = array[right]

    # Target found at middle index
    if target == potential_match:
        return middle

    # Case 1: Left half is properly ordered (left_num <= potential_match)
    elif left_num <= potential_match:
        # If target is in the left ordered half, search there
        if target < potential_match and target >= left_num:
            return shifted_binary_search_helper(array, target, left, middle - 1)
        # Otherwise search the right half (which might be shifted)
        else:
            return shifted_binary_search_helper(array, target, middle + 1, right)

    # Case 2: Right half is properly ordered (left_num > potential_match)
    else:
        # If target is in the right ordered half, search there
        if target > potential_match and target <= right_num:
            return shifted_binary_search_helper(array, target, middle + 1, right)
        # Otherwise search the left half (which might contain the shift point)
        else:
            return shifted_binary_search_helper(array, target, left, middle - 1)


# Test Cases:

print(shifted_binary_search([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33))
# Output: 8

print(shifted_binary_search([0, 1, 21, 33, 37, 45, 61, 71, 72, 73], 38))
# Output: -1

print(shifted_binary_search([111, 1, 5, 23], 5))
# Output: 2
