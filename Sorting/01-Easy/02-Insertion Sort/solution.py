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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

1. **Best Case**: When the array is already sorted, the inner `while` loop never executes (since `array[j] < array[j-1]` will
always be false). This results in only the outer loop running, giving us a time complexity of **O(n)**.

2. **Worst Case**: When the array is sorted in reverse order, the inner `while` loop executes maximally. For each element at index
`i`, we need to swap it all the way to the beginning of the array. This results in:
   - 1 swap for the 2nd element,
   - 2 swaps for the 3rd element,
   - ...
   - (n-1) swaps for the nth element.
   The total number of swaps is `1 + 2 + ... + (n-1) = n(n-1)/2`, which is **O(n²)**.

3. **Average Case**: On average, insertion sort also requires **O(n²)** time because, for randomly ordered arrays, each element
may need to be moved about halfway back through the already-sorted portion.

### Space Complexity:

- The algorithm sorts the array **in-place**, meaning it only uses a constant amount of additional space (for variables like `i`,
`j`, and temporary values during swapping). Thus, the space complexity is **O(1)** (constant space).

### Summary:

- **Time Complexity**:

  - Best Case: O(n) (already sorted)
  - Worst Case: O(n²) (reverse sorted)
  - Average Case: O(n²)
  
- **Space Complexity**: O(1) (in-place sorting).

This makes insertion sort efficient for small or nearly sorted datasets but inefficient for large, randomly ordered datasets.

"""
