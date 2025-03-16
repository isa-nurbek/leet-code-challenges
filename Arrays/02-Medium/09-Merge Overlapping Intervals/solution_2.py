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

# Detailed Code Explanation:

"""
### **Explanation of `merge_overlapping_intervals_stack` function**

The function `merge_overlapping_intervals_stack(intervals)` takes a list of intervals (represented as pairs of numbers)
and merges overlapping intervals. It uses a **stack-based approach** to efficiently merge intervals.

---

### **Step-by-Step Explanation**

#### **1. Handling Edge Case**
```
if not intervals:
    return []
```
- If the input list is empty, return an empty list immediately.

#### **2. Sorting the Intervals**
```
sorted_intervals = sorted(intervals, key=lambda x: x[0])
```
- The intervals are **sorted by their start times** (`x[0]` ensures sorting by the first element of each interval).
- This sorting step ensures that intervals are processed in increasing order.

##### **Example Sorting**
If the input is:
```
[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
```
After sorting:
```
[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
```
(Since they were already sorted, no change in order.)

#### **3. Initialize Stack with the First Interval**
```
stack = [sorted_intervals[0]]
```
- The stack is initialized with the first interval since there is nothing to compare yet.

#### **4. Iterating Through the Sorted Intervals**
```
for i in range(1, len(sorted_intervals)):
    top = stack[-1]  # Get the last interval in the stack
    current = sorted_intervals[i]  # Current interval
```
- The loop starts from the second interval (`i = 1`) and iterates over all intervals.

- `top` is the last interval in the `stack`, and `current` is the interval being processed.

#### **5. Merging Intervals**
```
if top[1] >= current[0]:
    stack[-1] = [top[0], max(top[1], current[1])]
```
- If the **end time** of `top` (`top[1]`) **overlaps or touches** the **start time** of `current` (`current[0]`), merge them:
  - Update the last interval in `stack` with:
    - **Start time** remains the same (`top[0]`).
    - **End time** is updated to the maximum of `top[1]` and `current[1]` to extend the range.

##### **Example of Merging**

Processing `[[3, 5], [4, 7]]`:
- `top = [3, 5]`
- `current = [4, 7]`
- Since `5 >= 4`, we merge them into `[3, 7]`.

```
stack[-1] = [3, max(5, 7)]  # Updates stack to [[1, 2], [3, 7]]
```

#### **6. Pushing Non-Overlapping Intervals**
```
else:
    stack.append(current)
```
- If no overlap, the current interval is added to the stack separately.

##### **Example of Non-Merging**

Processing `[9, 10]`:
- `top = [3, 8]`
- `current = [9, 10]`
- Since `8 < 9`, no merge happens, and `[9, 10]` is pushed onto the stack.

---

### **Final Output**
```
return stack
```
- The stack now contains the merged intervals.

---

### **Example Walkthrough**

#### **Test Case 1**
```
merge_overlapping_intervals_stack([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]])
```
1. Sort intervals: `[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]`
2. Stack initialized: `[[1, 2]]`
3. Processing `[3, 5]`: Stack → `[[1, 2], [3, 5]]`
4. Processing `[4, 7]`: Merge `[3, 5]` and `[4, 7]` → `[[1, 2], [3, 7]]`
5. Processing `[6, 8]`: Merge `[3, 7]` and `[6, 8]` → `[[1, 2], [3, 8]]`
6. Processing `[9, 10]`: No merge, Stack → `[[1, 2], [3, 8], [9, 10]]`

7. **Final Output**: `[[1, 2], [3, 8], [9, 10]]`

---

#### **Test Case 2**
```
merge_overlapping_intervals_stack([[1, 3], [2, 8], [9, 10]])
```
1. Sort intervals: `[[1, 3], [2, 8], [9, 10]]`
2. Stack initialized: `[[1, 3]]`
3. Processing `[2, 8]`: Merge `[1, 3]` and `[2, 8]` → `[[1, 8]]`
4. Processing `[9, 10]`: No merge, Stack → `[[1, 8], [9, 10]]`

5. **Final Output**: `[[1, 8], [9, 10]]`

---

#### **Test Case 3**
```
merge_overlapping_intervals_stack([[100, 105], [1, 104]])
```
1. Sort intervals: `[[1, 104], [100, 105]]`
2. Stack initialized: `[[1, 104]]`
3. Processing `[100, 105]`: Merge `[1, 104]` and `[100, 105]` → `[[1, 105]]`

4. **Final Output**: `[[1, 105]]`

---

### **Summary**
- **Sort intervals** based on the start time.
- **Use a stack** to store merged intervals.
- **Iterate and merge overlapping intervals** using `max` for the end time.
- **Push non-overlapping intervals** to the stack separately.
- **Returns the merged intervals** as the final result.

"""
