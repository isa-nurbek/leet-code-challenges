# Problem Description:

"""

                                                # Subarray Sort

Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices
of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted
(in ascending order).

If the input array is already sorted, the function should return `[-1, -1]`.


## Sample Input:
```
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
```

## Sample Output:
```
[3, 9]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def subarray_sort(array):
    # Initialize variables to track the minimum and maximum values that are out of order
    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")

    # Iterate through the array to find the smallest and largest elements that are out of order
    for i in range(len(array)):
        num = array[i]

        # Check if the current element is out of order
        if is_out_of_order(i, num, array):
            # Update the minimum and maximum out-of-order elements
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)

    # If no elements are out of order, return [-1, -1]
    if min_out_of_order == float("inf"):
        return [-1, -1]

    # Find the left index of the subarray that needs to be sorted
    subarray_left_idx = 0

    while min_out_of_order >= array[subarray_left_idx]:
        subarray_left_idx += 1

    # Find the right index of the subarray that needs to be sorted
    subarray_right_idx = len(array) - 1

    while max_out_of_order <= array[subarray_right_idx]:
        subarray_right_idx -= 1

    # Return the indices of the subarray that needs to be sorted
    return [subarray_left_idx, subarray_right_idx]


def is_out_of_order(i, num, array):
    # Check if the current element is out of order based on its position in the array

    # If it's the first element, it's out of order if it's greater than the next element
    if i == 0:
        return num > array[i + 1]

    # If it's the last element, it's out of order if it's smaller than the previous element
    if i == len(array) - 1:
        return num < array[i - 1]

    # For elements in the middle, it's out of order if it's greater than the next element
    # or smaller than the previous element
    return num > array[i + 1] or num < array[i - 1]


# Test Cases:

print(subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
# Output: [3, 9]

print(subarray_sort([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]))
# Output: [1, 11]

print(subarray_sort([1, 2]))
# Output: [-1, -1]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `subarray_sort` function can be broken down as follows:

1. **First Loop (Finding `min_out_of_order` and `max_out_of_order`):**
   - The loop iterates over the entire array once, which takes O(n) time, where `n` is the length of the array.
   - Inside the loop, the `is_out_of_order` function is called, which performs constant-time operations (comparisons).
   Thus, the `is_out_of_order` function runs in O(1) time.
   
   - Therefore, the first loop runs in O(n) * O(1) = O(n)\) time.

2. **Finding `subarray_left_idx`:**
   - This loop iterates from the start of the array until it finds the correct position for `min_out_of_order`.
   In the worst case, this could take O(n) time.

3. **Finding `subarray_right_idx`:**
   - This loop iterates from the end of the array until it finds the correct position for `max_out_of_order`.
   In the worst case, this could also take O(n) time.

4. **Overall Time Complexity:**
   - The total time complexity is the sum of the time complexities of the three steps: O(n) + O(n) + O(n) = O(n).

---

### Space Complexity Analysis

The space complexity of the `subarray_sort` function is determined by the additional space used by the algorithm:

1. **Variables:**
   - The algorithm uses a few variables (`min_out_of_order`, `max_out_of_order`, `subarray_left_idx`, `subarray_right_idx`),
   which take constant space O(1).

2. **No Additional Data Structures:**
   - The algorithm does not use any additional data structures that grow with the input size.

3. **Overall Space Complexity:**
   - The space complexity is O(1), as the algorithm uses only a constant amount of extra space regardless of the input size.

### Summary

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

This makes the algorithm efficient for large inputs, as it processes the array in linear time and uses minimal extra space.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of `subarray_sort` Algorithm**

The function `subarray_sort` takes an array as input and finds the smallest subarray that, if sorted, would make the
entire array sorted.

---

## **Step-by-Step Breakdown of the Code**

Let's go through the function line by line.

### **Step 1: Initialize Variables**
```
min_out_of_order = float("inf")
max_out_of_order = float("-inf")
```
- These variables track the **minimum** and **maximum** numbers that are out of order.
- `float("inf")` represents positive infinity, and `float("-inf")` represents negative infinity.

---

### **Step 2: Identify Out-of-Order Elements**
```
for i in range(len(array)):
    num = array[i]

    if is_out_of_order(i, num, array):
        min_out_of_order = min(min_out_of_order, num)
        max_out_of_order = max(max_out_of_order, num)
```
- The function iterates over the array and checks if each number is **out of order**.
- The helper function `is_out_of_order(i, num, array)` determines whether a number is in the wrong position.

- If a number is out of order:
  - It updates `min_out_of_order` to the smallest out-of-order number.
  - It updates `max_out_of_order` to the largest out-of-order number.

#### **Helper Function: `is_out_of_order`**
```
def is_out_of_order(i, num, array):
    if i == 0:
        return num > array[i + 1]

    if i == len(array) - 1:
        return num < array[i - 1]

    return num > array[i + 1] or num < array[i - 1]
```
- If `num` is at **index 0**, it checks if it is **greater than** the next element (should be in ascending order).
- If `num` is at the **last index**, it checks if it is **less than** the previous element.
- Otherwise, it checks if `num` is either **greater than the next number** or **less than the previous number**.

##### **Example of `is_out_of_order`**

For `array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]`
- `7` at index `6` is **out of order** because `7 < 11`.
- `6` at index `8` is **out of order** because `6 < 12`.
- `7` at index `9` is **out of order** because `7 < 12`.

At the end of this loop:
- `min_out_of_order = 6`
- `max_out_of_order = 11`

---

### **Step 3: Check If Already Sorted**
```
if min_out_of_order == float("inf"):
    return [-1, -1]
```
- If `min_out_of_order` was never updated (remains `inf`), the array is already sorted.
- It returns `[-1, -1]`.

##### **Example:**
For `[1, 2]`, no element is out of order, so the function returns `[-1, -1]`.

---

### **Step 4: Find the Leftmost Position to Fix**
```
subarray_left_idx = 0
while min_out_of_order >= array[subarray_left_idx]:
    subarray_left_idx += 1
```
- It finds where `min_out_of_order` **should be placed** by checking the left side.
- It increments `subarray_left_idx` **until it finds a number greater than `min_out_of_order`**.

##### **Example:**

For `[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]`
- `min_out_of_order = 6`
- It starts at index `0` and stops at index **`3`** (`7 > 6`).

Thus, `subarray_left_idx = 3`.

---

### **Step 5: Find the Rightmost Position to Fix**
```
subarray_right_idx = len(array) - 1
while max_out_of_order <= array[subarray_right_idx]:
    subarray_right_idx -= 1
```
- It finds where `max_out_of_order` **should be placed** by checking the right side.
- It decrements `subarray_right_idx` **until it finds a number smaller than `max_out_of_order`**.

##### **Example:**

For `[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]`
- `max_out_of_order = 11`
- It starts at the last index and stops at index **9** (`7 < 11`).

Thus, `subarray_right_idx = 9`.

---

### **Step 6: Return the Range**
```
return [subarray_left_idx, subarray_right_idx]
```
- Returns the indices **where sorting should start and end**.

---

## **Example Test Cases**

### **Test Case 1**
```
subarray_sort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
```
- Output: **`[3, 9]`**
- Sorting the subarray `[7, 10, 11, 7, 12, 6, 7]` results in a fully sorted array.

---

### **Test Case 2**
```
subarray_sort([-41, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57])
```
- Output: **`[1, 11]`**
- Sorting the subarray `[8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11]` results in a sorted array.

---

### **Test Case 3**
```
subarray_sort([1, 2])
```
- Output: **`[-1, -1]`**
- The array is already sorted.

---

## **Summary**
- **Finds the minimum and maximum out-of-order elements.**
- **Determines where they should be placed.**
- **Returns the smallest subarray that, if sorted, makes the entire array sorted.**
- **Runs in O(n) time.**

"""
