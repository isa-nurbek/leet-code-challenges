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
    if not intervals:
        return []

    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    stack = [sorted_intervals[0]]

    for i in range(1, len(sorted_intervals)):
        top = stack[-1]
        current = sorted_intervals[i]

        if top[1] >= current[0]:
            stack[-1] = [top[0], max(top[1], current[1])]
        else:
            stack.append(current)

    return stack


# Test Cases:

print(merge_overlapping_intervals_stack([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
# Output: [1, 2], [3, 8], [9, 10]]

print(merge_overlapping_intervals_stack([[1, 3], [2, 8], [9, 10]]))
# Output: [[1, 8], [9, 10]]

print(merge_overlapping_intervals_stack([[100, 105], [1, 104]]))
# Output: [[1, 105]]

# =========================================================================================================================== #
