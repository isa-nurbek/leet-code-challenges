# Problem Description:

"""

                                            # Longest Subarray With Sum

Write a function that takes in a non-empty array of non-negative integers and a non-negative integer representing a target sum.
The function should find the longest subarray where the values collectively sum up to equal the target sum. Return an array
containing the starting index and ending index of this subarray, both inclusive.

If there is no subarray that sums up to the target sum, the function should return an empty array. You can assume that the given
inputs will only ever have one answer.


## Sample Input:
```
array = [1, 2, 3, 4, 3, 3, 1, 2, 1, 2]
target_sum = 10
```

## Sample Output:
```
[4, 8]  // The longest subarray that sums to 10 starts at index 4 and ends at index 8
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def longest_subarray_with_sum(array, target_sum):
    # Initialize a list to store the starting and ending indices of the longest subarray
    indices = []

    # Initialize variables to keep track of the current subarray sum and its indices
    current_subarray_sum = 0
    starting_index = 0
    ending_index = 0

    # Loop through the array using the ending_index as the moving pointer
    while ending_index < len(array):
        # Add the current element to the current_subarray_sum
        current_subarray_sum += array[ending_index]

        # If the current_subarray_sum exceeds the target_sum, move the starting_index forward
        # and subtract the element at starting_index from current_subarray_sum
        while starting_index < ending_index and current_subarray_sum > target_sum:
            current_subarray_sum -= array[starting_index]
            starting_index += 1

        # If the current_subarray_sum equals the target_sum, check if this subarray is longer
        # than the previously found subarray (if any)
        if current_subarray_sum == target_sum:
            if (
                len(indices) == 0  # If no subarray has been found yet
                or indices[1] - indices[0]
                < ending_index - starting_index  # Or if the current subarray is longer
            ):
                # Update the indices to the current subarray's starting and ending indices
                indices = [starting_index, ending_index]

        # Move the ending_index forward to expand the subarray
        ending_index += 1

    # Return the indices of the longest subarray with the target_sum
    return indices


# Test Cases:

print(longest_subarray_with_sum([1, 2, 3, 4, 3, 3, 1, 2, 1], 10))
# Output: [4, 8]

print(longest_subarray_with_sum([1, 2, 3, 4, 0, 0, 0, 0, 0, 3, 3, 1, 2, 1], 7))
# Output: [4, 11]

print(longest_subarray_with_sum([61, 54, 1, 499, 2212, 4059, 1, 2, 3, 1, 3], 19))
# Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `longest_subarray_with_sum` function is **O(n)**, where **n** is the length of the input array.

Here's why:

1. **Outer Loop**: The `ending_index` iterates through the entire array once, from `0` to `len(array) - 1`.
This contributes **O(n)** to the time complexity.

2. **Inner Loop**: The `starting_index` is incremented only when the current subarray sum exceeds the `target_sum`.
Since `starting_index` starts at `0` and can only move forward (it never goes backward), it will traverse the array
at most once in total. This means the inner loop also contributes **O(n)** in total across all iterations of the outer loop.

Combining these two, the overall time complexity is **O(n)**.

---

### Space Complexity Analysis

The space complexity of the function is **O(1)**, which means it uses constant extra space.

Here's why:

1. The function uses a fixed number of variables (`indices`, `current_subarray_sum`, `starting_index`, and `ending_index`),
regardless of the size of the input array.

2. No additional data structures (like hash maps or arrays) are used that grow with the input size.

Thus, the space complexity is **O(1)**.

---

### Summary

- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(1)**

This makes the algorithm efficient for large input sizes.

"""

# =========================================================================================================================== #
