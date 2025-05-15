# Problem Description:

"""
                                             Binary Search

Write a function that takes in a `sorted array` of integers as well as a `target integer`. The function should use the `Binary
Search` algorithm to determine if the target integer is contained in the array and should return its `index` if it is, otherwise `-1`.


## Sample Input:
```
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
```

## Sample Output:
```
3
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(n)) time | O(1) space
def binary_search(array, target):
    """
    Performs binary search on a sorted array to find the target value.

    Args:
        array: A sorted list of elements to search through
        target: The value to search for in the array

    Returns:
        int: The index of the target in the array, or -1 if not found
    """
    # Start the search with the full range of the array
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(array, target, left, right):
    """
    Helper function that performs the actual binary search recursively.

    Args:
        array: The sorted list to search through
        target: The value to search for
        left: The leftmost index of the current search range
        right: The rightmost index of the current search range

    Returns:
        int: Index of the target if found, -1 otherwise
    """
    # Continue searching while the search range is valid (left hasn't passed right)
    while left <= right:
        # Calculate the middle index of the current search range
        middle = (left + right) // 2
        potential_match = array[middle]

        # Check if we've found the target
        if target == potential_match:
            return middle  # Target found, return its index
        # If target is smaller, search the left half
        elif target < potential_match:
            right = middle - 1
        # If target is larger, search the right half
        else:
            left = middle + 1

    # If we exit the loop, the target wasn't found
    return -1


# Test Cases:

print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
# Output: 3

print(binary_search([1, 5, 23, 111], 5))
# Output: 1

print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0))
# Output: 0
