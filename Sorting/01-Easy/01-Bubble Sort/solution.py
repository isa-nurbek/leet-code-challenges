# Problem Description:

"""
                                             Bubble Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Bubble Sort` algorithm
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
def bubble_sort(array):
    # Initialize a flag to track if the array is sorted
    is_sorted = False
    # Initialize a counter to keep track of how many elements have been sorted
    counter = 0

    # Continue looping until the array is sorted
    while not is_sorted:
        # Assume the array is sorted unless we find elements to swap
        is_sorted = True

        # Iterate through the unsorted portion of the array
        # The sorted portion grows by 1 each iteration (hence len(array) - 1 - counter)
        for i in range(len(array) - 1 - counter):
            # If current element is greater than the next element
            if array[i] > array[i + 1]:
                # Swap the elements
                swap(i, i + 1, array)
                # Since we found elements to swap, array wasn't fully sorted
                is_sorted = False

        # Increment the counter as the largest element has bubbled to the end
        counter += 1

    # Return the sorted array
    return array


def swap(i, j, array):
    # Swap two elements in the array
    array[i], array[j] = array[j], array[i]


# Test Cases:

print(bubble_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(bubble_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(bubble_sort([2, 1]))
# Output: [1, 2]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The time complexity of the Bubble Sort algorithm can be analyzed as follows:

1. **Worst-case time complexity**: 
   - In the worst case (when the array is in reverse order), the algorithm will perform the maximum number of comparisons and swaps.
   - For each pass through the array, the largest unsorted element "bubbles up" to its correct position.
   - The number of comparisons in the first pass is `(n-1)`, then `(n-2)`, and so on, down to `1` in the last pass.
   - Total comparisons = `(n-1) + (n-2) + ... + 1 = n(n-1)/2`, which is `O(n²)`.

2. **Best-case time complexity**:
   - In the best case (when the array is already sorted), the algorithm will still perform `(n-1)` comparisons in the first pass
   but will not perform any swaps.
   - Due to the `is_sorted` flag, the algorithm will terminate after the first pass.
   - Thus, the best-case time complexity is `O(n)`.

3. **Average-case time complexity**:
   - On average, Bubble Sort performs `O(n²)` comparisons and swaps because it typically requires multiple passes through the array.

### Space Complexity Analysis:

1. **Space complexity**:
   - Bubble Sort is an in-place sorting algorithm, meaning it does not require additional space proportional to the input size.
   - The only extra space used is for variables like `is_sorted`, `counter`, `i`, and temporary variables in the `swap` function,
   which are all constant space O(1).
   - Thus, the space complexity is `O(1)`.

### Summary:

- **Time Complexity**:

  - Worst-case: `O(n²)`
  - Best-case: `O(n)` (with `is_sorted` optimization)
  - Average-case: `O(n²)`
  
- **Space Complexity**: `O(1)` (in-place sorting).

"""
