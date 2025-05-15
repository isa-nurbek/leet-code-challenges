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


# O(log(n)) time | O(log(n)) space
def binary_search(array, target):
    """Performs binary search on a sorted array to find the target value.

    Args:
        array: A sorted list of elements to search through
        target: The value to search for in the array

    Returns:
        The index of the target in the array, or -1 if not found
    """
    # Start the search with the full range of the array
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(array, target, left, right):
    """Helper function that performs binary search recursively on a subarray.

    Args:
        array: The sorted list to search through
        target: The value to search for
        left: The left boundary of the current search range
        right: The right boundary of the current search range

    Returns:
        The index of the target in the array, or -1 if not found
    """
    # Base case: search range is invalid (target not found)
    if left > right:
        return -1

    # Calculate the middle point of the current search range
    middle = (left + right) // 2
    potential_match = array[middle]

    # Check if we've found the target
    if target == potential_match:
        return middle
    # If target is smaller, search the left half
    elif target < potential_match:
        return binary_search_helper(array, target, left, middle - 1)
    # If target is larger, search the right half
    else:
        return binary_search_helper(array, target, middle + 1, right)


# Test Cases:

print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
# Output: 3

print(binary_search([1, 5, 23, 111], 5))
# Output: 1

print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0))
# Output: 0

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

Binary search works by repeatedly dividing the search interval in half. At each step, the algorithm compares the middle element
of the current interval with the target value and eliminates half of the remaining elements from consideration.

- **Best Case**: O(1) - when the target is the middle element of the array.
- **Worst Case**: O(log n) - when the target is at one of the ends or not present in the array.
- **Average Case**: O(log n)

Each recursive call processes half of the remaining elements, leading to a logarithmic number of operations with respect to the
input size.

### Space Complexity:

This is a recursive implementation, so we need to consider the call stack:
- In each recursive call, we only pass constant space (the array reference and a few indices).
- The maximum depth of the recursion is the number of times we can divide the array in half, which is log₂n.

Therefore:
- **Space Complexity**: O(log n) for the recursive call stack.

### Summary:
- Time Complexity: O(log n)
- Space Complexity: O(log n) (due to recursion)

### Comparison with Iterative Binary Search:
An iterative implementation would have O(1) space complexity since it doesn't use the call stack. This recursive version uses
more space (O(log n)) due to the recursive calls, but both have the same O(log n) time complexity.

"""
