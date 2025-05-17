# Problem Description:

"""
                                               Heap Sort

Write a function that takes in an array of integers and returns a `sorted version` of that array. Use the `Heap Sort` algorithm
to sort the array.

You can make 2 versions:

- Max-Heap Version (Ascending Order Sort)
- Min-Heap Version (Descending Order Sort)


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
Best: O(n log(n)) time | O(1) space - where n is the length of the input array.
Average: O(n log(n)) time | O(1) space - where n is the length of the input array.
Worst: O(n log(n)) time | O(1) space - where n is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n log(n)) time | O(1) space
# Average: O(n log(n)) time | O(1) space
# Worst: O(n log(n)) time | O(1) space


# Min-Heap Version (Descending Order Sort)
def min_heapify(arr, n, i):
    """
    Converts an array into a min-heap structure starting from index i.
    A min-heap is a binary tree where each parent node is smaller than its children.

    Args:
        arr: The array to be heapified
        n: Size of the heap (can be smaller than array length)
        i: Index of the root node to start heapification from
    """
    smallest = i  # Initialize smallest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child exists and is smaller than current smallest
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # If right child exists and is smaller than current smallest
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If smallest is not the root, swap and continue heapifying
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
        min_heapify(arr, n, smallest)  # Recursively heapify the affected subtree


def heap_sort_descending(arr):
    """
    Sorts an array in descending order using a min-heap approach.
    The process involves:
    1. Building a min-heap from the array
    2. Repeatedly extracting the smallest element and rebuilding the heap

    Args:
        arr: The array to be sorted

    Returns:
        The sorted array in descending order
    """
    n = len(arr)

    # Build the min-heap (rearrange array)
    # Start from the last non-leaf node (n//2 - 1) and work up to the root
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (smallest) to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap (size i)
        min_heapify(arr, i, 0)

    return arr


# Test Cases:

print(heap_sort_descending([8, 5, 2, 9, 5, 6, 3]))
# Output: [9, 8, 6, 5, 5, 3, 2]

print(
    heap_sort_descending(
        [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]
    )
)
# Output: [10, 8, 6, 5, 5, 3, 1, -1, -2, -4, -4, -4, -5, -5, -6, -7, -10]

print(heap_sort_descending([2, 1]))
# Output: [2, 1]
