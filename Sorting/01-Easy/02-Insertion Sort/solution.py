# Problem Description:

"""
                                             Insertion Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Insertion Sort` algorithm
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
Best: O(n) time | O(1) space - where `n` is the length of the input array.
Average: O(n²) time | O(1) space - where `n` is the length of the input array.
Worst: O(n²) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n) time | O(1) space
# Average: O(n²) time | O(1)
# Worst: O(n²) time | O(1) space
def insertion_sort(array):
    """
    Sorts an array in ascending order using the Insertion Sort algorithm.

    Insertion Sort works by building a sorted portion of the array one element at a time.
    It takes each element from the unsorted portion and inserts it into its correct position
    in the sorted portion.

    Args:
        array: The list to be sorted

    Returns:
        The sorted list in ascending order
    """
    # Start from the second element (index 1) since the first element is trivially sorted
    for i in range(1, len(array)):
        j = i  # j is the current index of the element we're inserting

        # While we haven't reached the start of the array and the current element
        # is smaller than its left neighbor
        while j > 0 and array[j] < array[j - 1]:
            # Swap the current element with its left neighbor
            swap(j, j - 1, array)
            # Move left one position to check the next pair
            j -= 1

    return array


def swap(i, j, array):
    """
    Helper function to swap two elements in an array.

    Args:
        i: Index of first element
        j: Index of second element
        array: The array containing the elements to swap
    """
    array[i], array[j] = array[j], array[i]


# Test Cases:

print(insertion_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(insertion_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(insertion_sort([2, 1]))
# Output: [1, 2]
