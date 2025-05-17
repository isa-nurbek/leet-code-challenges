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
def merge_sort_iterative(arr):
    """
    Iterative implementation of merge sort algorithm.
    Args:
        arr: List to be sorted
    Returns:
        Sorted list
    """
    n = len(arr)
    # Temporary array for merging
    temp = [0] * n
    # Start with smallest subarray size of 1, then double each time
    size = 1

    # Continue until the subarray size covers the entire array
    while size < n:
        # Traverse through the array with current subarray size
        for left_start in range(0, n, size * 2):
            # Calculate mid point (end of left subarray)
            mid = min(left_start + size - 1, n - 1)
            # Calculate end of right subarray
            right_end = min(left_start + 2 * size - 1, n - 1)

            # Only merge if right subarray exists (mid < right_end)
            if mid < right_end:
                merge(arr, temp, left_start, mid, right_end)

        # Double the subarray size for next iteration
        size *= 2

    return arr


def merge(arr, temp, left, mid, right):
    """
    Merges two sorted subarrays into one sorted subarray.
    Args:
        arr: Original array being sorted
        temp: Temporary array for merging
        left: Start index of left subarray
        mid: End index of left subarray
        right: End index of right subarray
    """
    i = left  # Pointer for left subarray
    j = mid + 1  # Pointer for right subarray
    k = left  # Pointer for temp array

    # Merge while both subarrays have elements
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # Copy remaining elements from left subarray if any
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements from right subarray if any
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy merged elements back to original array
    for k in range(left, right + 1):
        arr[k] = temp[k]


# Test Cases:

print(merge_sort_iterative([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(merge_sort_iterative([38, 27, 43, 3, 9, 82, 10]))
# Output: [3, 9, 10, 27, 38, 43, 82]

print(merge_sort_iterative([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]))
# Output: [-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]
