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


# O(log(n)) time | O(log(n)) space
def search_for_range(array, target):
    """
    Finds the starting and ending positions of a target value in a sorted array.

    Args:
        array: A sorted list of integers.
        target: The integer value to search for in the array.

    Returns:
        A list containing the first and last indices of the target value.
        Returns [-1, -1] if the target is not found.
    """
    # Initialize the result range with [-1, -1] in case target is not found
    final_range = [-1, -1]

    # First search to find the left boundary (start index) of the target
    altered_binary_search(array, target, 0, len(array) - 1, final_range, True)
    # Second search to find the right boundary (end index) of the target
    altered_binary_search(array, target, 0, len(array) - 1, final_range, False)

    return final_range


def altered_binary_search(array, target, left, right, final_range, go_left):
    """
    A modified binary search that searches for the boundaries of a target value.

    Args:
        array: The sorted list to search in.
        target: The value to search for.
        left: The left boundary of the current search range.
        right: The right boundary of the current search range.
        final_range: The result array that stores the start and end indices.
        go_left: Boolean flag indicating whether we're searching for the left boundary (True)
                 or right boundary (False) of the target range.
    """
    # Base case: stop when left pointer exceeds right pointer
    if left > right:
        return

    # Calculate middle index
    middle = (left + right) // 2

    if array[middle] < target:
        # Target is in the right half
        altered_binary_search(array, target, middle + 1, right, final_range, go_left)
    elif array[middle] > target:
        # Target is in the left half
        altered_binary_search(array, target, left, middle - 1, final_range, go_left)
    else:
        # Found the target value
        if go_left:
            # We're searching for the left boundary
            if middle == 0 or array[middle - 1] != target:
                # Found the left boundary (either at start of array or previous element is different)
                final_range[0] = middle
            else:
                # Continue searching left to find the earliest occurrence
                altered_binary_search(
                    array, target, left, middle - 1, final_range, go_left
                )
        else:
            # We're searching for the right boundary
            if middle == len(array) - 1 or array[middle + 1] != target:
                # Found the right boundary (either at end of array or next element is different)
                final_range[1] = middle
            else:
                # Continue searching right to find the last occurrence
                altered_binary_search(
                    array, target, middle + 1, right, final_range, go_left
                )


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

Let's analyze the time and space complexity of the given `search_for_range` algorithm.

### **Time Complexity: O(log n)**

The algorithm performs two modified binary searches:
1. One to find the leftmost occurrence of the target (`go_left = True`).
2. One to find the rightmost occurrence of the target (`go_left = False`).

Each binary search runs in **O(log n)** time because, in the worst case, it halves the search space in each recursive call.
Since we perform **two independent binary searches**, the total time remains **O(log n)**.

#### **Why not O(2 log n)?**
- In Big-O notation, we drop constant factors, so **O(2 log n) = O(log n)**.

### **Space Complexity: O(log n) (due to recursion stack)**

The algorithm uses recursion, and the maximum depth of the recursion stack is determined by the number of times we split
the array in half:
- Each binary search has a recursion depth of **O(log n)**.
- Since the two searches are independent (not nested), the space complexity remains **O(log n)**.

### **Summary**

| Complexity  | Value                                             |
|-------------|---------------------------------------------------|
| **Time**    | O(log n)                                          |
| **Space**   | O(log n) (can be O(1) if implemented iteratively) |

#### **Can we optimize space to O(1)?**

Yes! If we rewrite the binary search iteratively instead of recursively, the space complexity reduces to **O(1)** because
we no longer use the call stack.

This algorithm efficiently finds the range of a target in a sorted array using a modified binary search approach.

"""
