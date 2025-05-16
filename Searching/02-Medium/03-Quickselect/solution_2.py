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


import random


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
            raise Exception("This should never happen.")

        # Choose a random pivot and swap it to the start
        pivot_idx = random.randint(start_idx, end_idx)
        swap(start_idx, pivot_idx, array)

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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

The `quick_select` algorithm is a selection algorithm to find the k-th smallest element in an unordered list.
It's based on the QuickSort algorithm but only recurses into one partition.

1. **Best Case**:  
   - The best case occurs when the randomly chosen pivot is the k-th element.  
   - This results in a single partitioning step, giving a time complexity of **O(n)**.

2. **Average Case**:  
   - On average, the pivot will divide the array into two roughly equal parts.  
   - The recurrence relation is:  
     
    T(n) = T(n/2) + O(n)
    
   - Solving this using the Master Theorem gives **O(n)** time complexity.

3. **Worst Case**:  
   - The worst case occurs when the pivot is always the smallest or largest element (e.g., if the array is already sorted and
   we pick the first/last element as the pivot).  
   - The recurrence relation becomes:  
    
    T(n) = T(n-1) + O(n)
    
   - This results in **O(n²)** time complexity.  
   - However, since we are using **randomized pivot selection**, the probability of worst-case behavior is extremely low.

### Space Complexity:

- The algorithm is **iterative** (using a `while True` loop instead of recursion), so it does not use additional call stack space.  
- All operations are performed **in-place** (only constant extra space is used for variables like `pivot_idx`, `left_idx`, `right_idx`, etc.).  
- Thus, the space complexity is **O(1)** (constant space).

### Summary:

| Case      | Time Complexity | Space Complexity  |
|-----------|-----------------|-------------------|
| Best      | O(n)            | O(1)              |
| Average   | O(n)            | O(1)              |
| Worst     | O(n²)           | O(1)              |

The randomized pivot selection ensures that the **average case O(n)** is the expected runtime, making this an efficient algorithm
for selection problems.

"""
