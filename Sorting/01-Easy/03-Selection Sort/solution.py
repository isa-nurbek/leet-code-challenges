# Problem Description:

"""
                                               Selection Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Selection Sort` algorithm
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
Best: O(n²) time | O(1) space - where `n` is the length of the input array.
Average: O(n²) time | O(1) space - where `n` is the length of the input array.
Worst: O(n²) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n²) time | O(1) space
# Average: O(n²) time | O(1)
# Worst: O(n²) time | O(1) space
def selection_sort(array):
    current_idx = 0

    while current_idx < len(array) - 1:
        smallest_idx = current_idx

        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i

        swap(current_idx, smallest_idx, array)
        current_idx += 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# Test Cases:

print(selection_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(selection_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(selection_sort([2, 1]))
# Output: [1, 2]
