# Problem Description:

"""
                                                Merge Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Merge Sort` algorithm
to sort the array.


## Sample Input:
```
array = [8, 5, 2, 9, 5, 6, 3]
```

## Sample Output:
```
[2, 3, 5, 5, 6, 8, 9]
```

## Optimal Time & Space Complexity:
```
Best: O(n log(n)) time | O(n) space - where `n` is the length of the input array.
Average: O(n log(n)) time | O(n) space - where `n` is the length of the input array.
Worst: O(n log(n)) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n log(n)) time | O(n) space
# Average: O(n log(n)) time | O(n) space
# Worst: O(n log(n)) time | O(n) space
def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm (divide and conquer approach).

    Args:
        arr: The input list to be sorted

    Returns:
        A new sorted list containing all elements from the input
    """
    # Base case: if array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2

    # Divide the array into left and right halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves and return
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left: First sorted array
        right: Second sorted array

    Returns:
        A new merged sorted array containing all elements from both inputs
    """
    merged = []
    left_index = 0
    right_index = 0

    # Traverse both arrays and compare elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            # If left element is smaller, add it to the result
            merged.append(left[left_index])
            left_index += 1
        else:
            # If right element is smaller or equal, add it to the result
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from left or right array
    # (one of these will be empty, the other will have sorted elements)
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Test Cases:

print(merge_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# Output: [3, 9, 10, 27, 38, 43, 82]

print(merge_sort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]))
# Output: [-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]
