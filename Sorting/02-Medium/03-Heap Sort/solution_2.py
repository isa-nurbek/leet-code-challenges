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
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


def heap_sort_descending(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
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
