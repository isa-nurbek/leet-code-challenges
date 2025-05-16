# Problem Description:

"""
                                               Quick Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Quick Sort` algorithm
to sort the array.

To avoid `O(n²)` worst-case time complexity you can:

- Choose a `random pivot` or `median-of-three pivot`.
- Use an `in-place partitioning` scheme to reduce space usage.

1. **Avoiding O(n²) worst-case**: Quick Sort can degrade to `O(n²)` time complexity if poorly chosen pivots (e.g., always picking
the `first/last` element in an already sorted array) lead to highly unbalanced partitions. The suggestions address this:
   - **Random pivot**: Randomization makes worst-case behavior unlikely.
   - **Median-of-three pivot**: Choosing the median of the first, middle, and last elements helps avoid bad pivots.

2. **In-place partitioning**: This reduces space complexity from O(log n) (due to recursion stack) to O(1) auxiliary space
(excluding the stack), making it more memory-efficient.


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

import random  # Import the random module for selecting random pivot


# Best: O(n log(n)) time | O(log(n)) space
# Average: O(n log(n)) time | O(log(n)) space
# Worst: O(n²) time | O(n) space
def randomized_quick_sort(arr):
    """
    Sorts an array using the randomized quicksort algorithm.
    This version creates new lists for partitions rather than sorting in-place.

    Args:
        arr: List of comparable elements to be sorted

    Returns:
        A new list containing all elements from arr in sorted order
    """

    # Base case: arrays of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr.copy()  # Return a copy to maintain consistency in return types

    # Randomly select a pivot index to help avoid worst-case O(n^2) performance
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]

    # Partition the array into three parts:
    # - left: elements smaller than pivot
    # - middle: elements equal to pivot (handles duplicate values)
    # - right: elements larger than pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right partitions, then combine with middle
    # Note: middle doesn't need sorting as all elements are equal
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


# Test Cases:

print(randomized_quick_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(
    randomized_quick_sort(
        [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]
    )
)
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(randomized_quick_sort([2, 1]))
# Output: [1, 2]
