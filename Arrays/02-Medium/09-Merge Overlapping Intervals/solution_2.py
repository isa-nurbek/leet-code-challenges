# Problem Description:

"""

                                         # Merge Overlapping Intervals

Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, and returns
the new intervals in no particular order.

Each interval `interval` is an array of two integers, with `interval[0]` as the start of the interval and `interval[1]` as
the end of the interval.

Note that back-to-back intervals aren't considered to be overlapping. For example, `[1, 5]` and `[6, 7]` aren't overlapping;
however, `[1, 6]` and `[6, 7]` are indeed overlapping.

Also note that the start of any particular interval will always be less than or equal to the end of that interval.


## Sample Input:
```
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
```

## Sample Output:
```
[[1, 2], [3, 8], [9, 10]]
// Merge the intervals [3, 5], [4, 7], and [6, 8].
// The intervals could be ordered differently.
```

## Optimal Time & Space Complexity:
```
O(n log(n)) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n log(n)) time | O(n) space - where `n` is the length of the input array.
def merge_overlapping_intervals_stack(intervals):
    # If the input list is empty, return an empty list
    if not intervals:
        return []

    # Sort the intervals based on the start value of each interval
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # Initialize a stack with the first interval
    stack = [sorted_intervals[0]]

    # Iterate through the sorted intervals starting from the second interval
    for i in range(1, len(sorted_intervals)):
        # Get the top interval from the stack
        top = stack[-1]
        # Get the current interval
        current = sorted_intervals[i]

        # Check if the current interval overlaps with the top interval in the stack
        if top[1] >= current[0]:
            # If they overlap, merge them by updating the end value of the top interval
            stack[-1] = [top[0], max(top[1], current[1])]
        else:
            # If they don't overlap, push the current interval onto the stack
            stack.append(current)

    # Return the merged intervals stored in the stack
    return stack


# Test Cases:

print(merge_overlapping_intervals_stack([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
# Output: [1, 2], [3, 8], [9, 10]]

print(merge_overlapping_intervals_stack([[1, 3], [2, 8], [9, 10]]))
# Output: [[1, 8], [9, 10]]

print(merge_overlapping_intervals_stack([[100, 105], [1, 104]]))
# Output: [[1, 105]]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **Sorting**: 
   - The first step is sorting the intervals based on their start times. Sorting a list of `n` intervals takes O(n log n) time.

2. **Iterating through the intervals**:
   - After sorting, the algorithm iterates through the list of intervals once. This iteration takes O(n) time.

3. **Merging intervals**:
   - During the iteration, each interval is either merged with the previous one or added to the stack. Merging or appending
   to the stack takes O(1) time per interval.

Thus, the overall time complexity is dominated by the sorting step, which is - O(n log n).

---

### Space Complexity Analysis

1. **Stack**:
   - The stack is used to store the merged intervals. In the worst case, if no intervals overlap, the stack will contain
   all `n` intervals. Therefore, the space complexity is O(n).

2. **Sorting**:
   - Sorting typically requires O(n) additional space (for the sorting algorithm's internal data structures).

Thus, the overall space complexity is - O(n).

---

### Summary

- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)

This approach ensures that all overlapping intervals are merged efficiently, and the final list of intervals is non-overlapping.

"""

# =========================================================================================================================== #
