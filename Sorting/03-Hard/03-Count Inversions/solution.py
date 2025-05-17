# Problem Description:

"""
                                                Count Inversions

Write a function that takes in an array of integers and returns the number of `inversions` in the array. An `inversion` occurs
if for any valid indices `i` and `j`, `i < j` and `array[i] > array[j]`.

For example, given `array = [3, 4, 1, 2]`, there are `4 inversions`. The following pairs of indices represent inversions:
`[0, 2], [0, 3], [1, 2], [1, 3]`.

Intuitively, the number of inversions is a measure of how unsorted the array is.


## Sample Input:
```
array = [2, 3, 3, 1, 9, 5, 6]
```

## Sample Output:
```
5

// The following pairs of indices represent inversions: [0, 3], [1, 3], [2, 3], [4, 5], [4, 6]
```

## Optimal Time & Space Complexity:
```
O(n log n) time | O(n) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n log n) time | O(n) space
def count_inversions(array):
    """Count the number of inversions in the given array.
    An inversion is a pair of indices (i, j) where i < j and array[i] > array[j].

    Args:
        array: The input array to count inversions in

    Returns:
        The total number of inversions in the array
    """
    # Start the recursive divide-and-conquer process on the entire array
    return count_sub_array_inversions(array, 0, len(array))


def count_sub_array_inversions(array, start, end):
    """Recursively count inversions in a subarray using divide-and-conquer approach.

    Args:
        array: The original array being processed
        start: Starting index of the subarray (inclusive)
        end: Ending index of the subarray (exclusive)

    Returns:
        The number of inversions in the subarray from start to end
    """
    # Base case: subarray has 0 or 1 elements - no inversions possible
    if end - start <= 1:
        return 0

    # Calculate middle point to divide the subarray
    middle = start + (end - start) // 2

    # Recursively count inversions in left and right halves
    left_inversions = count_sub_array_inversions(array, start, middle)
    right_inversions = count_sub_array_inversions(array, middle, end)

    # Count inversions found during merging and sort the subarray
    merged_array_inversions = merge_sort_and_count_inversions(array, start, middle, end)

    # Return total inversions (left + right + merge)
    return left_inversions + right_inversions + merged_array_inversions


def merge_sort_and_count_inversions(array, start, middle, end):
    """Merge two sorted subarrays while counting split inversions.

    Args:
        array: The original array being processed
        start: Start index of left subarray
        middle: Start index of right subarray (end of left subarray)
        end: End index of right subarray

    Returns:
        The number of split inversions found during merging
    """
    sorted_array = []  # Temporary storage for merged result
    left = start  # Pointer for left subarray
    right = middle  # Pointer for right subarray
    inversions = 0  # Count of split inversions found during merge

    # Merge the two subarrays while counting inversions
    while left < middle and right < end:
        if array[left] <= array[right]:
            # No inversion - left element is smaller
            sorted_array.append(array[left])
            left += 1
        else:
            # When right element is smaller than left, it's smaller than all
            # remaining elements in left subarray (since left subarray is sorted)
            inversions += middle - left
            sorted_array.append(array[right])
            right += 1

    # Append any remaining elements from either subarray
    sorted_array += array[left:middle] + array[right:end]

    # Copy the merged result back into the original array
    for idx, num in enumerate(sorted_array):
        array[start + idx] = num

    return inversions


# Test Cases:

print(count_inversions([2, 3, 3, 1, 9, 5, 6]))
# Output: 5

print(count_inversions([5, -1, 2, -4, 3, 4, 19, 87, 762, -8, 0]))
# Output: 23

print(count_inversions([]))
# Output: 0
