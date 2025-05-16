# Problem Description:

"""
                                             Quickselect

Write a function that takes in an array of distinct integers as well as an integer `k` and that returns the `k`th smallest integer
in that array.

The function should do this in `linear time`, on average.


## Sample Input:
```
array = [8, 5, 2, 9, 7, 6, 3]
k = 3
```

## Sample Output:
```
5
```

## Optimal Time & Space Complexity:
```
Best: O(n) time | O(1) space - where `n` is the length of the input array.
Average: O(n) time | O(1) space - where `n` is the length of the input array.
Worst: O(n²) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n) time | O(1) space
# Average: O(n) time | O(1) space
# Worst: O(n²) time | O(1)
def quick_select(array, k):
    """
    Finds the kth smallest element in an unsorted array using QuickSelect algorithm.

    Args:
        array: The unsorted list of elements
        k: The position of the element to find (1-based index)

    Returns:
        The kth smallest element in the array

    Note:
        This is a wrapper function that sets up the initial parameters for the helper function.
    """
    position = k - 1  # Convert to 0-based index

    return quick_select_helper(array, 0, len(array) - 1, position)


def quick_select_helper(array, start_idx, end_idx, position):
    """
    Helper function that performs the actual QuickSelect algorithm recursively (using iteration).

    Args:
        array: The unsorted list of elements
        start_idx: The starting index of the current subarray
        end_idx: The ending index of the current subarray
        position: The target position (0-based) we're searching for

    Returns:
        The element at the target position when the array would be sorted

    Note:
        Uses a while loop with tail recursion elimination for better performance.
    """
    while True:
        # Base case that should theoretically never be reached if inputs are valid
        if start_idx > end_idx:
            raise Exception("Your algorithm should never arrive here!")

        # Initialize pointers for partitioning
        pivot_idx = start_idx  # Choose first element as pivot
        left_idx = start_idx + 1
        right_idx = end_idx

        # Partitioning step (similar to QuickSort)
        while left_idx <= right_idx:
            # If left element is greater than pivot and right is smaller, swap them
            if (
                array[left_idx] > array[pivot_idx]
                and array[right_idx] < array[pivot_idx]
            ):
                swap(left_idx, right_idx, array)

            # Move left pointer if element is <= pivot
            if array[left_idx] <= array[pivot_idx]:
                left_idx += 1

            # Move right pointer if element is >= pivot
            if array[right_idx] >= array[pivot_idx]:
                right_idx -= 1

        # After partitioning, swap pivot with right_idx (final pivot position)
        swap(pivot_idx, right_idx, array)

        # Check if we've found our target element
        if right_idx == position:
            return array[right_idx]
        # If pivot is left of target, search right subarray
        elif right_idx < position:
            start_idx = right_idx + 1
        # If pivot is right of target, search left subarray
        else:
            end_idx = right_idx - 1


def swap(one, two, array):
    """
    Swaps two elements in an array.

    Args:
        one: Index of first element
        two: Index of second element
        array: The array containing the elements to swap
    """
    array[one], array[two] = array[two], array[one]


# Test Cases:

print(quick_select([8, 5, 2, 9, 7, 6, 3], 3))
# Output: 5

print(quick_select([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5))
# Output: 25

print(quick_select([43, 24, 37], 2))
# Output: 37
