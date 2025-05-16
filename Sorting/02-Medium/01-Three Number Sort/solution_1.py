# Problem Description:

"""
                                               Three Number Sort

You're given an array of integers and another array of three distinct integers. The first array is guaranteed to only contain
integers that are in the second array, and the second array represents a desired order for the integers in the first array. For
example, a second array of `[x, y, z]` represents a desired order of `[x, x, ..., x, y, y, ..., y, z, z, ..., z]` in the first array.

Write a function that sorts the first array according to the desired order in the second array.

The function should perform this in place (i.e., it should mutate the input array), and it shouldn't use any auxiliary space
(i.e., it should run with constant space: `O(1)` space).

> Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily contain all
three integers found in the second array—it might only contain one or two.


## Sample Input:
```
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
```

## Sample Output:
```
[0, 0, 0, 1, 1, 1, -1, -1]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def three_number_sort(array, order):
    # Initialize a list to keep count of how many times each number in 'order' appears
    value_counts = [0, 0, 0]

    # Count occurrences of each value in the array based on their order in 'order'
    for element in array:
        # Find the index of the current element in the 'order' list
        order_idx = order.index(element)
        # Increment the count for that index
        value_counts[order_idx] += 1

    # Reconstruct the array in the desired order
    for i in range(3):
        # Get the value that should appear in this position of the sorted array
        value = order[i]
        # Get how many times this value appears in the original array
        count = value_counts[i]

        # Calculate where this block of values should start in the array
        # It's the sum of counts of all previous values in the order
        num_elements_before = sum(value_counts[:i])

        # Fill the appropriate positions in the array with the current value
        for n in range(count):
            # Calculate the current index to fill
            current_idx = num_elements_before + n
            # Assign the value to its correct position
            array[current_idx] = value

    return array


# Test Cases:

print(three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
# Output: [0, 0, 0, 1, 1, 1, -1, -1]

print(three_number_sort([7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9], [8, 7, 9]))
# Output: [8, 8, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9]

print(three_number_sort([], [0, 7, 9]))
# Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity:**

1. **Counting Occurrences:**
   - The first loop iterates through each element in the `array` (length `N`).
   - For each element, it calls `order.index(element)`, which in the worst case takes `O(3)` = `O(1)` time (since `order` has
   only 3 elements).
   - Thus, this part takes `O(N * 3)` = `O(N)` time.

2. **Reconstructing the Sorted Array:**
   - The outer loop runs 3 times (for each unique value in `order`).
   - The inner loop runs `count` times (where `count` is the number of occurrences of the current value in `order`).
   - The total number of assignments in the inner loop is `N` (since we're reconstructing the entire array).
   - The `sum(value_counts[:i])` is `O(3)` = `O(1)` since `i` is at most 2.
   - Thus, this part also takes `O(N)` time.

**Total Time Complexity:** `O(N) + O(N)` = `O(N)`.

### **Space Complexity:**

- The only additional space used is `value_counts`, which is of fixed size `3` (since `order` has only 3 unique values).
- No other significant extra space is used (the input array is modified in-place).

**Total Space Complexity:** `O(1)` (constant extra space).

### **Summary:**
- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

This is an efficient in-place sorting algorithm for this constrained problem (where the array only contains 3 distinct values
in a known order). It works similarly to the "Dutch National Flag" problem solution.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through what this Python function does and how it works step by step.

---

### 🔍 Function Goal:

The function `three_number_sort(array, order)` takes:

* `array`: a list of integers (only containing three distinct values)
* `order`: a list of exactly 3 distinct integers representing the desired order

The function returns the sorted version of `array` according to the order defined in `order`.

---

### 📦 Example:

Input:

```
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
```

Expected Output:

```
[0, 0, 0, 1, 1, 1, -1, -1]
```

This means: Put all `0`s first, then all `1`s, then all `-1`s.

---

### 🔧 Step-by-step Breakdown:

#### Step 1: Initialize value counts

```
value_counts = [0, 0, 0]
```

This list will count how many times each number from `order` appears in `array`. The index of each count matches the index of
the corresponding number in `order`.

#### Step 2: Count elements from array

```
for element in array:
    order_idx = order.index(element)
    value_counts[order_idx] += 1
```

* For every element in `array`, it looks up its index in the `order` list.
* Then it increments the count at that index in `value_counts`.

Example:
For array `[1, 0, 0, -1, -1, 0, 1, 1]` and order `[0, 1, -1]`, the result will be:

```
value_counts = [3, 3, 2]  # 3 zeros, 3 ones, 2 minus ones
```

#### Step 3: Overwrite the array based on counts

```
for i in range(3):
    value = order[i]
    count = value_counts[i]

    num_elements_before = sum(value_counts[:i])
    for n in range(count):
        current_idx = num_elements_before + n
        array[current_idx] = value
```

This step reconstructs the original array using the counts:

* Loop through each value in `order`
* Use the count to figure out how many times it should appear
* Compute the starting index for that value in the sorted array using `sum(value_counts[:i])`
* Write that value into the correct number of positions

---

### ✅ Why this works:

* It counts how many of each of the 3 values exist.
* It knows the order in which they should appear.
* It reconstructs the array in-place according to the counts and order.

---

### ⏱️ Time and Space Complexity:

* Time: O(n), where n is the length of the array

  * One pass to count
  * One pass to overwrite
* Space: O(1)

  * Only uses a fixed-size list `value_counts` of size 3

---

### 🧪 Test Case Review:

1. ✅ `three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1])` → `[0, 0, 0, 1, 1, 1, -1, -1]`
2. ✅ `three_number_sort([7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9], [8, 7, 9])` → `[8, 8, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9]`
3. ✅ `three_number_sort([], [0, 7, 9])` → `[]`

---

Here's an ASCII visualization of how the function three_number_sort works step by step.

Let's use this example:

```
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
```

---

### 📦 Step 1: Count elements in array

We count how many times each value in order appears in the array.

```
order         = [0,   1,   -1]
value_counts  = [0,   0,    0]   ← initial

Processing array:
array = [1, 0, 0, -1, -1, 0, 1, 1]

         ^        1 is at index 1 in order → value_counts[1] += 1 → [0, 1, 0]
            ^     0 is at index 0 in order → value_counts[0] += 1 → [1, 1, 0]
               ^  0 → value_counts[0] += 1 → [2, 1, 0]
                  ^ -1 → value_counts[2] += 1 → [2, 1, 1]
                      ^ -1 → value_counts[2] += 1 → [2, 1, 2]
                          ^ 0 → value_counts[0] += 1 → [3, 1, 2]
                             ^ 1 → value_counts[1] += 1 → [3, 2, 2]
                                ^ 1 → value_counts[1] += 1 → [3, 3, 2]

Final value_counts = [3, 3, 2]
```

---

### 🧱 Step 2: Reconstruct array

We overwrite the array according to the order and value_counts.

```
order =        [0, 1, -1]
value_counts = [3, 3, 2]

We now write:
- Three 0's starting at index 0
- Three 1's starting at index 3
- Two -1's starting at index 6
```

ASCII view of how we fill array:

```
Initial (empty slots for clarity):
[_, _, _, _, _, _, _, _]

Write 0s:
[0, 0, 0, _, _, _, _, _]

Write 1s:
[0, 0, 0, 1, 1, 1, _, _]

Write -1s:
[0, 0, 0, 1, 1, 1, -1, -1]
```

---

### ✅ Final Output:

```
[0, 0, 0, 1, 1, 1, -1, -1]
```

"""
