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


# O(n log(n)) time | O(n) space
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

# Detailed Code Explanation:

"""
Your function `merge_overlapping_intervals(intervals)` is designed to merge overlapping intervals in a given list of intervals.
Below is a step-by-step breakdown of how the function works.

---

## **Understanding the Problem**
Given a list of intervals represented as pairs `[start, end]`, the goal is to merge all overlapping intervals and return
a new list with the merged intervals.

**Example:**  
Input:  
```
[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
```
Sorted Input:  
```
[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
```
Merged Output:  
```
[[1, 2], [3, 8], [9, 10]]
```

---

## **Step-by-Step Explanation of the Code**
```
def merge_overlapping_intervals(intervals):
```
This function takes a list of intervals where each interval is a list `[start, end]`.

### **Step 1: Sorting the Intervals**
```
sorted_intervals = sorted(intervals, key=lambda x: x[0])
```
- The intervals are sorted in **ascending order** based on their **start values**.
- Sorting ensures that if two intervals overlap, they will be adjacent in the list.
- **Example:**
  - Given input: `[[3, 5], [1, 2], [4, 7], [6, 8], [9, 10]]`
  - After sorting: `[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]`

### **Step 2: Initialize Merged List**
```
merged_intervals = []
current_interval = sorted_intervals[0]
merged_intervals.append(current_interval)
```
- The first interval is taken as the `current_interval`.
- A new list `merged_intervals` is created to store the merged intervals.
- The first interval is added to this list.

### **Step 3: Iterating Through Intervals and Merging**
```
for next_interval in sorted_intervals:
    _, current_interval_end = current_interval
    next_interval_start, next_interval_end = next_interval
```
- The function loops through each `next_interval` in `sorted_intervals`.
- `current_interval_end` represents the end of the last merged interval.
- `next_interval_start` and `next_interval_end` represent the start and end of the next interval.

#### **Case 1: Overlapping Intervals**
```
if current_interval_end >= next_interval_start:
    current_interval[1] = max(current_interval_end, next_interval_end)
```
- If the `current_interval` **overlaps** with `next_interval`, they are merged.
- The merge is done by updating the end of `current_interval` to be the maximum end value.

#### **Case 2: Non-Overlapping Intervals**
```
else:
    current_interval = next_interval
    merged_intervals.append(current_interval)
```
- If there is **no overlap**, `next_interval` starts a **new non-overlapping group**, so it is added to `merged_intervals`.

---

## **Example Walkthrough**
### **Example 1:**
```
merge_overlapping_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]])
```
#### **Step 1: Sorting**
```
[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
```
#### **Step 2: Merging**
1. Start with `[1, 2]`, add it to `merged_intervals`
2. Compare `[3, 5]` and `[4, 7]` → they overlap → merge into `[3, 7]`
3. Compare `[3, 7]` and `[6, 8]` → they overlap → merge into `[3, 8]`
4. `[9, 10]` does not overlap, so it is added as-is.

#### **Final Output**
```
[[1, 2], [3, 8], [9, 10]]
```

---

### **Example 2:**
```
merge_overlapping_intervals([[1, 3], [2, 8], [9, 10]])
```
#### **Step 1: Sorting**
```
[[1, 3], [2, 8], [9, 10]]
```
#### **Step 2: Merging**
1. `[1, 3]` and `[2, 8]` overlap → merge into `[1, 8]`
2. `[1, 8]` and `[9, 10]` do not overlap → keep `[9, 10]`

#### **Final Output**
```
[[1, 8], [9, 10]]
```

---

### **Example 3:**
```
merge_overlapping_intervals([[100, 105], [1, 104]])
```
#### **Step 1: Sorting**
```
[[1, 104], [100, 105]]
```
#### **Step 2: Merging**
1. `[1, 104]` and `[100, 105]` overlap → merge into `[1, 105]`

#### **Final Output**
```
[[1, 105]]
```

---

## **Issues with the Code**

### **Mutating the Current Interval**
- The line `current_interval[1] = max(current_interval_end, next_interval_end)` **modifies** the original `current_interval`,
which may lead to unintended behavior.
- A **better approach** would be to use a **new list** instead of modifying the existing interval.
  
---

## **Conclusion**

Our function effectively merges overlapping intervals but modifies the original list, which can cause unintended
side effects. Using a copy of the interval (as in the corrected version) makes it safer. The algorithm is efficient,
operating in `O(n log n)` time, which is optimal for this problem.

Next `solution_2` would be implemented an alternative approach using a stack? 🚀

"""
