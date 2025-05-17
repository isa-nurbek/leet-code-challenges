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
    Main merge sort function that initiates the sorting process.
    Creates a temporary array once to be used for all merging operations.

    Args:
        arr: The array to be sorted

    Returns:
        The sorted array
    """
    # Create a temporary array for merging once (to avoid repeated allocations)
    temp = [0] * len(arr)
    # Start the recursive sorting process
    _merge_sort(arr, temp, 0, len(arr) - 1)

    return arr


def _merge_sort(arr, temp, left, right):
    """
    Recursive helper function that divides the array into halves and sorts them.

    Args:
        arr: The array being sorted
        temp: Temporary array for merging
        left: Left index of the current subarray
        right: Right index of the current subarray
    """
    # Only proceed if there's more than one element in the subarray
    if left < right:
        # Find the middle point to divide the array into two halves
        mid = (left + right) // 2
        # Recursively sort the left half
        _merge_sort(arr, temp, left, mid)
        # Recursively sort the right half
        _merge_sort(arr, temp, mid + 1, right)
        # Merge the two sorted halves
        merge(arr, temp, left, mid, right)


def merge(arr, temp, left, mid, right):
    """
    Merges two sorted subarrays into one sorted subarray.
    The subarrays are arr[left..mid] and arr[mid+1..right].

    Args:
        arr: The main array being sorted
        temp: Temporary array used for merging
        left: Left index of the first subarray
        mid: End index of the first subarray
        right: End index of the second subarray
    """
    i = left  # Pointer for left subarray (starts at beginning)
    j = mid + 1  # Pointer for right subarray (starts at middle + 1)
    k = left  # Pointer for temp array (starts at beginning of current range)

    # Traverse both subarrays and copy the smaller element to temp
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]  # Left element is smaller or equal
            i += 1
        else:
            temp[k] = arr[j]  # Right element is smaller
            j += 1
        k += 1

    # Copy any remaining elements from left subarray
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy any remaining elements from right subarray
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy the merged elements from temp back to the original array
    for k in range(left, right + 1):
        arr[k] = temp[k]


# Test Cases:

print(merge_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# Output: [3, 9, 10, 27, 38, 43, 82]

print(merge_sort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]))
# Output: [-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]
