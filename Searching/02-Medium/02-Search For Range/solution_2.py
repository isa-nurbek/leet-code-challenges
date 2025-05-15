# Problem Description:

"""
                                             Search For Range

Write a function that takes in a `sorted array` of integers as well as a `target integer`. The function should use a variation of
the `Binary Search` algorithm to find a range of indices in between which the target number is contained in the array and should
return this range in the form of an array.

The first number in the output array should represent the first index at which the target number is located, while the second number
should represent the last index at which the target number is located. The function should return `[-1, -1]` if the integer isn't
contained in the array.


## Sample Input:
```
array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
```

## Sample Output:
```
[4, 9]
```

## Optimal Time & Space Complexity:
```
O(log(n)) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(log(n)) time | O(1) space
def search_for_range(array, target):
    # Initialize the final range with [-1, -1] in case target is not found
    final_range = [-1, -1]

    # First search to find the leftmost index of target (go_left = True)
    altered_binary_search(array, target, 0, len(array) - 1, final_range, True)
    # Second search to find the rightmost index of target (go_left = False)
    altered_binary_search(array, target, 0, len(array) - 1, final_range, False)

    return final_range


def altered_binary_search(array, target, left, right, final_range, go_left):
    """
    A modified binary search that searches for the leftmost or rightmost
    occurrence of target in array and updates final_range accordingly.

    Args:
        array: The sorted array to search in
        target: The value to search for
        left: Left boundary of current search range
        right: Right boundary of current search range
        final_range: The result array to store start/end indices
        go_left: Boolean indicating whether we're searching for leftmost (True)
                 or rightmost (False) occurrence
    """
    while left <= right:
        middle = (left + right) // 2

        if array[middle] < target:
            # Target is in right half
            left = middle + 1
        elif array[middle] > target:
            # Target is in left half
            right = middle - 1
        else:
            # Found target value at middle index
            if go_left:
                # We're searching for left boundary
                if middle == 0 or array[middle - 1] != target:
                    # Found left boundary (either at start of array or previous
                    # element isn't target)
                    final_range[0] = middle
                    return
                else:
                    # Continue searching left half for earlier occurrences
                    right = middle - 1
            else:
                # We're searching for right boundary
                if middle == len(array) - 1 or array[middle + 1] != target:
                    # Found right boundary (either at end of array or next
                    # element isn't target)
                    final_range[1] = middle
                    return
                else:
                    # Continue searching right half for later occurrences
                    left = middle + 1


# Test Cases:

print(search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45))
# Output: [4, 9]

print(search_for_range([5, 7, 7, 8, 8, 10], 5))
# Output: [0, 0]

print(search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], -1))
# Output: [-1, -1]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `search_for_range` function and its helper `altered_binary_search`.

### Time Complexity:

1. **Binary Search Variant**: The `altered_binary_search` function is a modified binary search. In the worst case, it will run
in O(log n) time, where n is the number of elements in the array. This is because, like standard binary search, it halves the
search space in each iteration.

2. **Two Binary Searches**: The `search_for_range` function calls `altered_binary_search` twice—once to find the left boundary
(`go_left=True`) and once to find the right boundary (`go_left=False`). Each of these calls is O(log n).

3. **Total Time Complexity**: Since we perform two O(log n) operations, the total time complexity remains **O(log n)**.
The constants (2 in this case) are dropped in Big-O notation.

### Space Complexity:

1. **Recursive vs. Iterative**: The `altered_binary_search` function is implemented iteratively (using a `while` loop), so it does
not use additional space on the call stack. This is in contrast to a recursive binary search, which would use O(log n) space due
to the call stack.

2. **Variables**: The function uses a constant amount of extra space (variables like `left`, `right`, `middle`, etc.), and the
`final_range` array is passed by reference and has a fixed size of 2.

3. **Total Space Complexity**: The space complexity is **O(1)** (constant space), as no additional space is used that scales with
the input size.

### Summary:
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

This is an efficient solution for finding the range of a target value in a sorted array. The two-pass binary search approach
ensures we correctly identify the boundaries of the target range.

"""
