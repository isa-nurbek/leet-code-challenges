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
def merge_overlapping_intervals(intervals):
    # Sort the intervals based on the start value of each interval
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # Initialize a list to store the merged intervals
    merged_intervals = []

    # Start with the first interval in the sorted list
    current_interval = sorted_intervals[0]
    merged_intervals.append(current_interval)

    # Iterate through the sorted intervals starting from the second interval
    for next_interval in sorted_intervals:
        # Extract the end value of the current interval
        _, current_interval_end = current_interval

        # Extract the start and end values of the next interval
        next_interval_start, next_interval_end = next_interval

        # Check if the current interval overlaps with the next interval
        if current_interval_end >= next_interval_start:
            # If they overlap, merge them by updating the end value of the current interval
            current_interval[1] = max(current_interval_end, next_interval_end)
        else:
            # If they don't overlap, move to the next interval and add it to the merged list
            current_interval = next_interval
            merged_intervals.append(current_interval)

    # Return the list of merged intervals
    return merged_intervals


# Test Cases:

print(merge_overlapping_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
# Output: [1, 2], [3, 8], [9, 10]]

print(merge_overlapping_intervals([[1, 3], [2, 8], [9, 10]]))
# Output: [[1, 8], [9, 10]]

print(merge_overlapping_intervals([[100, 105], [1, 104]]))
# Output: [[1, 105]]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **Sorting**: The first step in the function is to sort the intervals based on their start times. Sorting a list
of `n` intervals takes O(n log n) time.

2. **Merging**: After sorting, the function iterates through the sorted list once to merge overlapping intervals.
This iteration takes O(n) time since each interval is processed exactly once.

Combining these two steps, the overall time complexity is dominated by the sorting step:

    O(n log n) + O(n) = O(n log n)

---

### Space Complexity Analysis

1. **Sorting**: The sorting step typically requires O(n) additional space (for the sorted list), depending on the
sorting algorithm used.

2. **Merging**: The `merged_intervals` list stores the final merged intervals. In the worst case, if no intervals overlap,
this list will contain all `n` intervals, requiring O(n) space.

Thus, the overall space complexity is: O(n)

---

### Summary

- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)

"""

# =========================================================================================================================== #
