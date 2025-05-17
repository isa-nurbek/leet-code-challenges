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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of this iterative merge sort implementation.

### Time Complexity:

The iterative merge sort follows the same divide-and-conquer approach as recursive merge sort, just implemented differently.

1. **Outer while loop**: Runs until `size` grows from 1 to n (or larger). Since `size` doubles each iteration (size *= 2),
this loop runs O(log n) times.

2. **Inner for loop**: For each `size`, it processes all elements in the array with O(n) total work per `size` (since each
element is part of exactly one merge operation at each size level).

3. **merge() function**: For each merge operation of two subarrays of size `size`, it takes O(size) time, and across all merges
at a given level, this sums to O(n) time.

Since we have O(log n) levels/doublings of `size`, and each level does O(n) work, the total time complexity is O(n log n).

### Space Complexity:

1. The algorithm uses a temporary array `temp` of size n, which is its dominant space usage.
2. Other variables use constant space.

Thus, the space complexity is O(n) (for the `temp` array).

### Summary:
- **Time Complexity**: O(n log n) in all cases (best, average, worst) because merge sort always divides the array in half and
merges in linear time.
- **Space Complexity**: O(n) due to the auxiliary `temp` array.

This matches the complexity of the standard recursive merge sort, just implemented iteratively to avoid recursion stack overhead.
The iterative approach is generally more space-efficient in practice (though both are O(n) space) because it avoids recursive
call stack space.

"""
