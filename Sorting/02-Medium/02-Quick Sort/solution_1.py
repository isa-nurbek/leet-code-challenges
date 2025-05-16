# Problem Description:

"""
                                               Quick Sort

Write a function that takes in an array of integers and returns a `sorted` version of that array. Use the `Quick Sort` algorithm
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
Best: O(n log(n)) time | O(log(n)) space - where n is the length of the input array.
Average: O(n log(n)) time | O(log(n)) space - where n is the length of the input array.
Worst: O(n²) time | O(log(n)) space - where n is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Best: O(n log(n)) time | O(log(n)) space
# Average: O(n log(n)) time | O(log(n)) space
# Worst: O(n²) time | O(n) space
def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm (recursive implementation).
    Returns a new sorted array (does not modify the original array).

    Quick Sort works by:
    1. Selecting a 'pivot' element from the array
    2. Partitioning the other elements into two sub-arrays:
       - Elements less than or equal to the pivot
       - Elements greater than the pivot
    3. Recursively sorting the sub-arrays
    4. Combining the results

    Args:
        arr: List of comparable elements to be sorted

    Returns:
        A new list containing all elements from arr in sorted order
    """

    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr.copy()  # Return a copy to maintain immutability of original

    # Choose the last element as the pivot (common simple strategy)
    pivot = arr[-1]

    # Partition the array (excluding the pivot) into two sub-arrays:
    # - left contains elements <= pivot
    # - right contains elements > pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively sort both sub-arrays and combine the results:
    # sorted_left + pivot + sorted_right
    return quick_sort(left) + [pivot] + quick_sort(right)


# Test Cases:

print(quick_sort([8, 5, 2, 9, 5, 6, 3]))
# Output: [2, 3, 5, 5, 6, 8, 9]

print(quick_sort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7]))
# Output: [-10, -7, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 10]

print(quick_sort([2, 1]))
# Output: [1, 2]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

1. **Best Case**: O(n log n) - When the pivot always divides the array into two nearly equal parts. This leads to `log n`
recursive calls, each doing O(n) work for partitioning.

2. **Average Case**: O(n log n) - On average, with random input, the pivot will divide the array reasonably well.

3. **Worst Case**: O(n²) - When the pivot is always the smallest or largest element (e.g., already sorted array with this
implementation). This leads to n recursive calls, each doing O(n) work.

**Why worst case is O(n²) for this implementation**:
- The code always chooses the last element as the pivot (`pivot = arr[-1]`).
- For an already sorted array, this means each partition creates:
  - `left` with n-1 elements
  - `right` with 0 elements
- This leads to n recursive calls, each doing O(n) work for partitioning.

### Space Complexity:

1. **Worst Case**: O(n) - Due to recursion stack space in the worst case (unbalanced partitions).
   - In the worst case (sorted array), there are n recursive calls on the stack.
   - Each recursive call creates new `left` and `right` lists, but these are not simultaneously alive on the stack (space gets
   reclaimed after each call returns).

2. **Best/Average Case**: O(log n) - Space for recursion stack in balanced cases.

### Summary:

- **Time Complexity**:

    Best Case: O(n log(n)) 
    Average Case: O(n log(n)) 
    Worst Case: O(n²) 

- **Space Complexity**: 

    Best Case: O(log(n)) 
    Average Case: O(log(n)) 
    Worst Case: O(n)

---

**Additional Notes**:

- This implementation is not in-place (it creates new lists in each recursive call).
- The space for the new lists is not counted in the space complexity above because it's temporary and doesn't accumulate (Python
garbage collection reclaims it).
- If we counted the auxiliary space for the new lists, it would be O(n) in all cases (but this is typically not how space complexity
is analyzed for recursive algorithms unless it's persistent space).

### Improvements:

To avoid O(n²) worst-case time complexity:
1. Choose a random pivot or median-of-three pivot.
2. Use an in-place partitioning scheme to reduce space usage.

"""
