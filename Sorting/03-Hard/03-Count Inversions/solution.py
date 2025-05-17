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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The given code counts the number of inversions in an array using a modified merge sort algorithm.
Here's the breakdown of the time complexity:

1. **Divide Step**: The array is recursively divided into two halves until the base case (subarrays of size 1 or 0) is reached.
This division takes O(log n) time because the array is halved at each recursive call.

2. **Conquer Step**: The inversions are counted in the left half, the right half, and during the merge step. The work done at each
level of recursion is O(n) for the merge step (explained below), and there are O(log n) levels of recursion.

3. **Merge Step**: The `merge_sort_and_count_inversions` function merges two sorted subarrays and counts the inversions across them.
This is done in O(n) time per merge, where `n` is the total number of elements in the two subarrays being merged. The key operation
is counting inversions when an element from the right subarray is placed before elements in the left subarray, which is done in
constant time per such occurrence.

Thus, the overall time complexity is O(n log n), which is the same as the standard merge sort. This is because the additional work
for counting inversions during the merge step does not increase the asymptotic complexity.

### Space Complexity Analysis:

1. **Recursive Calls**: The recursion depth is O(log n), but this does not contribute significantly to space complexity beyond the
stack space.

2. **Temporary Array**: The `merge_sort_and_count_inversions` function uses a temporary array (`sorted_array`) to store the merged
result before copying it back to the original array. The size of this temporary array is proportional to the number of elements
being merged, which is O(n) in the worst case.

Thus, the space complexity is O(n) due to the additional space used for merging. The algorithm is not purely in-place because of
this temporary storage.

### Summary:
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n) (due to the temporary array used in merging)

"""
