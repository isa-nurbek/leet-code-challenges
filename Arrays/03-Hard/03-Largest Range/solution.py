# Problem Description:

"""

                                                # Largest Range

Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of integers
contained in that array.

The first number in the output array should be the first number in the range, while the second number should be the last number
in the range.

A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For instance,
the output array `[2, 6]` represents the range `{2, 3, 4, 5, 6}`, which is a range of length 5. Note that numbers don't need
to be sorted or adjacent in the input array in order to form a range.

You can assume that there will only be one largest range.


## Sample Input:
```
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
```

## Sample Output:
```
[0, 7]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def largest_range(array):
    # Initialize the best_range to store the result (the largest range)
    best_range = []

    # Initialize longest_length to keep track of the length of the largest range found
    longest_length = 0

    # Create a dictionary to store all the numbers in the array as keys.
    # The value `True` indicates that the number has not been processed yet.
    nums = {}
    for num in array:
        nums[num] = True

    # Iterate through each number in the array
    for num in array:
        # If the number has already been processed, skip it
        if not nums[num]:
            continue

        # Mark the current number as processed
        nums[num] = False

        # Initialize the current_length to 1 (since we have at least one number in the range)
        current_length = 1

        # Initialize pointers to explore the range to the left and right of the current number
        left = num - 1
        right = num + 1

        # Explore the range to the left of the current number
        while left in nums:
            # Mark the left number as processed
            nums[left] = False
            # Increase the current_length since we found a consecutive number
            current_length += 1
            # Move the left pointer further to the left
            left -= 1

        # Explore the range to the right of the current number
        while right in nums:
            # Mark the right number as processed
            nums[right] = False
            # Increase the current_length since we found a consecutive number
            current_length += 1
            # Move the right pointer further to the right
            right += 1

        # After exploring both left and right, check if the current range is the longest found so far
        if current_length > longest_length:
            # Update the longest_length with the current_length
            longest_length = current_length
            # Update the best_range with the new range [left + 1, right - 1]
            # left + 1 because we decremented left one extra time in the while loop
            # right - 1 because we incremented right one extra time in the while loop
            best_range = [left + 1, right - 1]

    # Return the best_range, which represents the largest range of consecutive numbers
    return best_range


# Test Cases:

print(largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
# Output: [0, 7]

print(largest_range([-1, 0, 1]))
# Output: [-1, 1]

print(largest_range([0, 9, 19, -1, 18, 17, 2, -10, 3, 12, 5, -16, 4, 11, 8, 7, 6, 15]))
# Output: [2, 9]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **Initialization of the `nums` dictionary:**
   - We iterate through the input array once to populate the `nums` dictionary. This operation takes O(n) time,
   where `n` is the number of elements in the array.

2. **Main loop to find the largest range:**
   - We iterate through the array again. For each element, we check if it is still marked as `True` in the `nums` dictionary.
   - If it is, we start expanding to the left and right to find the range of consecutive numbers.
   - Each number is visited at most twice: once when it is the starting point of a range, and once when it is part of another range.
   
   This ensures that the inner `while` loops do not cause the time complexity to exceed O(n).

3. **Overall Time Complexity:**
   - The overall time complexity is O(n), where `n` is the number of elements in the array.

---

### Space Complexity Analysis

1. **`nums` dictionary:**
   - We store each element of the array in the `nums` dictionary. This requires O(n) space.

2. **Other variables:**
   - The variables `best_range`, `longest_length`, `current_length`, `left`, and `right` use constant space, O(1).

3. **Overall Space Complexity:**
   - The overall space complexity is O(n), where `n` is the number of elements in the array.

### Summary

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

This algorithm efficiently finds the largest range of consecutive numbers in the array with linear time and space complexity.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of `largest_range` Algorithm**

The `largest_range` function finds the longest consecutive sequence (range) of numbers in an unsorted array.
The function returns a list containing the start and end of that range.

---

## **Step-by-Step Breakdown of the Code**

Let's analyze the function line by line.

### **Step 1: Initialize Variables**
```
best_range = []
longest_length = 0
```
- `best_range`: Stores the **start and end** of the longest range found.
- `longest_length`: Tracks the **length of the longest range**.

---

### **Step 2: Store Numbers in a Hash Table**
```
nums = {}
for num in array:
    nums[num] = True
```
- Creates a **hash table (dictionary)** `nums` where:
  - Keys are numbers in the array.
  - Values are `True`, indicating that the number has not been visited.

##### **Example:**

For `array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]`,  
The dictionary `nums` looks like:
```
{1: True, 11: True, 3: True, 0: True, 15: True, 5: True, 2: True,
 4: True, 10: True, 7: True, 12: True, 6: True}
```

---

### **Step 3: Find the Longest Consecutive Range**
```
for num in array:
    if not nums[num]:
        continue
```
- **Iterates through each number in the array.**
- **If the number was already visited (`False`), it skips processing** (avoids duplicate calculations).

---

### **Step 4: Expand Left and Right to Find the Range**
```
nums[num] = False
current_length = 1

left = num - 1
right = num + 1
```
- **Marks `num` as visited** (`nums[num] = False`).
- **Initializes `current_length = 1`** because a single number forms a range of length `1`.
- **Sets `left` to `num - 1`** (to check the left side of the range).
- **Sets `right` to `num + 1`** (to check the right side of the range).

---

### **Step 5: Expand Left**
```
while left in nums:
    nums[left] = False
    current_length += 1
    left -= 1
```
- **If `left` exists in `nums`**, mark it as visited.
- **Increase `current_length`** because we found another number in the range.
- **Keep decreasing `left`** to expand the range as far as possible.

---

### **Step 6: Update Best Range**
```
if current_length > longest_length:
    longest_length = current_length
    best_range = [left + 1, right - 1]
```
- If we found a **longer range**, update:
  - `longest_length`
  - `best_range` (adjusting `left + 1` because `left` was decreased one extra step)

---

### **Step 7: Return the Result**
```
return best_range
```
- Returns the longest consecutive range found.

---

## **Example Test Cases**

### **Test Case 1**
```
largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6])
```
#### **Step-by-Step Execution**

1. **Dictionary `nums` Created:**
   ```
   {1: True, 11: True, 3: True, 0: True, 15: True, 5: True, 2: True,
    4: True, 10: True, 7: True, 12: True, 6: True}
   ```
2. **Processing each number:**
   - Starting from `1`, expands to `[0, 1, 2, 3, 4, 5, 6, 7]` → Length = `8`
   - **Best range updated:** `[0, 7]`
   - Other numbers processed but do not exceed length `8`.

**Final Output:**
```
[0, 7]
```

---

### **Test Case 2**
```
largest_range([-1, 0, 1])
```
1. **Dictionary `nums`:**
   ```
   {-1: True, 0: True, 1: True}
   ```
2. **Processing -1:**
   - Expands to `[-1, 0, 1]` → Length = `3`
   - **Best range updated:** `[-1, 1]`

**Final Output:**
```
[-1, 1]
```

---

### **Test Case 3**
```
largest_range([0, 9, 19, -1, 18, 17, 2, -10, 3, 12, 5, -16, 4, 11, 8, 7, 6, 15])
```
1. **Dictionary `nums`:**
   ```
   {0: True, 9: True, 19: True, -1: True, 18: True, 17: True, 2: True,
    -10: True, 3: True, 12: True, 5: True, -16: True, 4: True,
    11: True, 8: True, 7: True, 6: True, 15: True}
   ```
2. **Processing 2:**
   - Expands to `[2, 3, 4, 5, 6, 7, 8, 9]` → Length = `8`
   - **Best range updated:** `[2, 9]`

**Final Output:**
```
[2, 9]
```

---

## **Summary**
- Uses a **hash table** to store numbers for **quick lookups**.
- Iterates through numbers and **expands left and right** to find the **longest consecutive sequence**.
- Runs in **O(n) time**, making it highly efficient.
- Works well even for large inputs.

"""
