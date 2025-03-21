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

# Detailed Code Explanation:

"""
### **Understanding the Function:**

The function `longest_subarray_with_sum(array, target_sum)` finds the longest contiguous subarray within `array` that
sums up to `target_sum`. If multiple such subarrays exist, it returns the indices `[start, end]` of the longest one.
If no subarray sums up to `target_sum`, it returns an empty list `[]`.

---

### **Code Breakdown**

#### **1. Initialization**
```
indices = []
current_subarray_sum = 0
starting_index = 0
ending_index = 0
```
- `indices`: Stores the starting and ending indices of the longest valid subarray found.
- `current_subarray_sum`: Maintains the sum of elements in the current subarray.
- `starting_index`: The left boundary of the current subarray.
- `ending_index`: The right boundary of the current subarray, which we increment as we traverse.

---

#### **2. Expanding the Sliding Window**
```
while ending_index < len(array):
    current_subarray_sum += array[ending_index]
```
- This loop iterates over `array`, expanding `ending_index` to include more elements in `current_subarray_sum`.

---

#### **3. Shrinking the Window If Needed**
```
while starting_index < ending_index and current_subarray_sum > target_sum:
    current_subarray_sum -= array[starting_index]
    starting_index += 1
```
- If `current_subarray_sum` exceeds `target_sum`, we remove elements from the left (`starting_index`) to reduce the sum.

---

#### **4. Updating the Longest Subarray**
```
if current_subarray_sum == target_sum:
    if (
        len(indices) == 0
        or indices[1] - indices[0] < ending_index - starting_index
    ):
        indices = [starting_index, ending_index]
```
- If `current_subarray_sum` matches `target_sum`, we check if this subarray is longer than the previous one stored in `indices`.
- If it's the longest found so far, we update `indices` with the current `[starting_index, ending_index]`.

---

#### **5. Continue Searching**
```
ending_index += 1
```
- We move `ending_index` forward to search for other possible valid subarrays.

---

#### **6. Returning the Result**
```
return indices
```
- The function returns the indices of the longest subarray found.

---

### **Example Walkthroughs**

#### **Example 1: `[1, 2, 3, 4, 3, 3, 1, 2, 1]`, `target_sum = 10`**

**Steps:**
- Expanding: `[1, 2, 3, 4]` (sum = 10) → `[0, 3]` stored.
- Continue expanding: `[3, 3, 1, 2, 1]` (sum = 10) → `[4, 8]` (longer than `[0,3]`).

- Final Output: `[4, 8]`.

#### **Example 2: `[1, 2, 3, 4, 0, 0, 0, 0, 0, 3, 3, 1, 2, 1]`, `target_sum = 7`**

**Steps:**
- Expanding: `[3, 4]` (sum = 7) → `[2, 3]` stored.
- Expanding: `[0, 0, 0, 0, 0, 3, 3, 1, 2, 1]` (sum = 7) → `[4, 11]` (longer).

- Final Output: `[4, 11]`.

#### **Example 3: `[61, 54, 1, 499, 2212, 4059, 1, 2, 3, 1, 3]`, `target_sum = 19`**

**Steps:**
- No subarray sums up to 19.

- Returns `[]`.

"""
