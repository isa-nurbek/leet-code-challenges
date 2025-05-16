# Problem Description:

"""
                                               Three Number Sort

You're given an array of integers and another array of three distinct integers. The first array is guaranteed to only contain
integers that are in the second array, and the second array represents a desired order for the integers in the first array. For
example, a second array of `[x, y, z]` represents a desired order of `[x, x, ..., x, y, y, ..., y, z, z, ..., z]` in the first array.

Write a function that sorts the first array according to the desired order in the second array.

The function should perform this in place (i.e., it should mutate the input array), and it shouldn't use any auxiliary space
(i.e., it should run with constant space: `O(1)` space).

> Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily contain all
three integers found in the second array—it might only contain one or two.


## Sample Input:
```
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
```

## Sample Output:
```
[0, 0, 0, 1, 1, 1, -1, -1]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def three_number_sort(array, order):
    # Initialize a list to keep count of how many times each number in 'order' appears
    value_counts = [0, 0, 0]

    # Count occurrences of each value in the array based on their order in 'order'
    for element in array:
        # Find the index of the current element in the 'order' list
        order_idx = order.index(element)
        # Increment the count for that index
        value_counts[order_idx] += 1

    # Reconstruct the array in the desired order
    for i in range(3):
        # Get the value that should appear in this position of the sorted array
        value = order[i]
        # Get how many times this value appears in the original array
        count = value_counts[i]

        # Calculate where this block of values should start in the array
        # It's the sum of counts of all previous values in the order
        num_elements_before = sum(value_counts[:i])

        # Fill the appropriate positions in the array with the current value
        for n in range(count):
            # Calculate the current index to fill
            current_idx = num_elements_before + n
            # Assign the value to its correct position
            array[current_idx] = value

    return array


# Test Cases:

print(three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
# Output: [0, 0, 0, 1, 1, 1, -1, -1]

print(three_number_sort([7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9], [8, 7, 9]))
# Output: [8, 8, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9]

print(three_number_sort([], [0, 7, 9]))
# Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity:**

1. **Counting Occurrences:**
   - The first loop iterates through each element in the `array` (length `N`).
   - For each element, it calls `order.index(element)`, which in the worst case takes `O(3)` = `O(1)` time (since `order` has
   only 3 elements).
   - Thus, this part takes `O(N * 3)` = `O(N)` time.

2. **Reconstructing the Sorted Array:**
   - The outer loop runs 3 times (for each unique value in `order`).
   - The inner loop runs `count` times (where `count` is the number of occurrences of the current value in `order`).
   - The total number of assignments in the inner loop is `N` (since we're reconstructing the entire array).
   - The `sum(value_counts[:i])` is `O(3)` = `O(1)` since `i` is at most 2.
   - Thus, this part also takes `O(N)` time.

**Total Time Complexity:** `O(N) + O(N)` = `O(N)`.

### **Space Complexity:**

- The only additional space used is `value_counts`, which is of fixed size `3` (since `order` has only 3 unique values).
- No other significant extra space is used (the input array is modified in-place).

**Total Space Complexity:** `O(1)` (constant extra space).

### **Summary:**
- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

This is an efficient in-place sorting algorithm for this constrained problem (where the array only contains 3 distinct values
in a known order). It works similarly to the "Dutch National Flag" problem solution.

"""
