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


# O(n^2) time | O(1) space
def longest_subarray_with_sum(array, target_sum):
    # Initialize an empty list to store the indices of the longest subarray
    indices = []

    # Iterate over the array to consider each element as the starting index of a subarray
    for starting_index in range(len(array)):
        # Initialize a variable to keep track of the sum of the current subarray
        current_subarray_sum = 0

        # Iterate over the array starting from the current starting_index to the end
        for ending_index in range(starting_index, len(array)):
            # Add the current element to the sum of the current subarray
            current_subarray_sum += array[ending_index]

            # Check if the sum of the current subarray equals the target sum
            if current_subarray_sum == target_sum:
                # If the current subarray is longer than the previously found subarray,
                # or if no subarray has been found yet, update the indices
                if (
                    len(indices) == 0  # No subarray found yet
                    or indices[1] - indices[0]
                    < ending_index - starting_index  # Current subarray is longer
                ):
                    # Update the indices to the current subarray's start and end
                    indices = [starting_index, ending_index]

    # Return the indices of the longest subarray with the target sum
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

1. **Outer Loop**: The outer loop runs from `starting_index = 0` to `starting_index = len(array) - 1`. This means
it iterates `n` times, where `n` is the length of the array.

2. **Inner Loop**: For each `starting_index`, the inner loop runs from `ending_index = starting_index` to
`ending_index = len(array) - 1`. In the worst case, this inner loop also iterates `n` times.

3. **Total Iterations**: Since the inner loop runs `n` times for each iteration of the outer loop, the total number
of iterations is n * n = n^2.

4. **Operations Inside the Loops**: Inside the inner loop, the function performs a constant number of operations
(addition, comparison, and assignment). These operations do not depend on the size of the array and are O(1).

Thus, the **time complexity** of the function is: O(n^2)

---

### Space Complexity Analysis

The space complexity of the function is determined by the additional space used by the algorithm, excluding the input array.

1. **Variables**: The function uses a few variables (`indices`, `starting_index`, `ending_index`, `current_subarray_sum`),
all of which occupy constant space O(1).

2. **Output**: The `indices` list stores at most two integers (the starting and ending indices of the subarray), which
also occupies constant space O(1).

Thus, the **space complexity** of the function is: O(1)

---

### Summary

- **Time Complexity**: O(n^2) 
- **Space Complexity**: O(1) 

"""

# =========================================================================================================================== #
