# Problem Description:

"""
                                               Quick Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Quick Sort` algorithm
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
Best: O(n log(n)) time | O(log(n)) space - where n is the length of the input array.
Average: O(n log(n)) time | O(log(n)) space - where n is the length of the input array.
Worst: O(n²) time | O(log(n)) space - where n is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n log(n)) time | O(log(n)) space
# Average: O(n log(n)) time | O(log(n)) space
# Worst: O(n²) time | O(log(n)) space
def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm (recursive implementation).
    Returns a new sorted array (does not modify the original array).

    Quick Sort works by:
    1. Selecting a 'pivot' element from the array
    2. Partitioning the other elements into two sub-arrays:
       - Elements less than or equal to the pivot
       - Elements greater than the pivot
    3. Recursively sorting the sub-arrays
    4. Combining the results

    Args:
        arr: List of comparable elements to be sorted

    Returns:
        A new list containing all elements from arr in sorted order
    """

    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr.copy()  # Return a copy to maintain immutability of original

    # Choose the last element as the pivot (common simple strategy)
    pivot = arr[-1]

    # Partition the array (excluding the pivot) into two sub-arrays:
    # - left contains elements <= pivot
    # - right contains elements > pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively sort both sub-arrays and combine the results:
    # sorted_left + pivot + sorted_right
    return quick_sort(left) + [pivot] + quick_sort(right)


# Test Cases:

print(quick_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(quick_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(quick_sort([2, 1]))
# Output: [1, 2]
