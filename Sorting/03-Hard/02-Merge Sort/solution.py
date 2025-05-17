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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The space complexity of Merge Sort is determined by the additional space used during the sorting process:

1. **Divide Step**: The array is divided into two halves recursively until each subarray has only one element.
This division process takes O(log n) steps because the array is halved at each level of recursion.

2. **Merge Step**: At each level of recursion, merging two sorted subarrays takes O(n) time, where `n` is the total number of
elements being merged. This is because each element is compared and placed in the merged array exactly once.

3. **Total Levels**: Since the array is divided into halves at each level, there are `log n` levels of recursion.

4. **Total Time**: At each level, the total work done is O(n) (for merging all subarrays at that level).
Since there are `log n` levels, the total time complexity is: O(n log n)

   This holds for the best, average, and worst cases because the algorithm always divides the array in half and merges it back
   together, regardless of the initial order of the elements.

### Space Complexity Analysis:

The space complexity of Merge Sort is determined by the additional space used during the sorting process:

1. **Recursive Calls**: The recursion depth is O(log n), which contributes to the space used on the call stack.

2. **Temporary Arrays**: During the merge process, temporary arrays are created to store the left and right halves of the subarrays.
At any given time, the maximum additional space used is O(n) because the algorithm needs to store the entire array being sorted
at the top level of recursion (though smaller subarrays are used at lower levels).

3. **Total Space**: The dominant factor is the temporary storage used for merging, so the space complexity is: O(n)

   This is because the algorithm requires additional space proportional to the size of the input array to store the merged subarrays.

### Summary:

- **Time Complexity**: O(n log n) in all cases (best, average, worst).
- **Space Complexity**: O(n) due to the additional space required for merging.

Merge Sort is a stable, comparison-based sorting algorithm with consistent performance, but it does require additional space,
which may be a consideration for very large datasets.

"""
