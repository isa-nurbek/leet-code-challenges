# Problem Description:

"""

                                         # First Duplicate Value

Given an array of integers between `1` and `n`, inclusive, where `n` is the length of the array, write a function that
returns the first integer that appears more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, your function should return
the one whose first duplicate value has the minimum index.

If no integer appears more than once, your function should return `-1`.

Note that you're allowed to mutate the input array.


## Sample Input 1:
```
array = [2, 1, 5, 2, 3, 3, 4]
```

## Sample Output 2:
```
2 // 2 is the first integer that appears more than once.
// 3 also appears more than once, but the second 3 appears after the second 2.
```

## Sample Input 3:
```
array = [2, 1, 5, 3, 3, 2, 4]
```

## Sample Output 3:
```
3 // 3 is the first integer that appears more than once.
// 2 also appears more than once, but the second 2 appears after the second 3.
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n^2) time | O(1) space
def first_duplicate_value(array):
    # Initialize the variable to store the index of the first duplicate found.
    # We start with the length of the array, which is an invalid index, to indicate no duplicate has been found yet.
    minimum_second_index = len(array)

    # Loop through each element in the array.
    for i in range(len(array)):
        value = array[i]  # Get the current element to compare with the rest.

        # Loop through the elements that come after the current element.
        for j in range(i + 1, len(array)):
            value_to_compare = array[j]  # Get the next element to compare.

            # If a duplicate is found, update the minimum_second_index if this duplicate appears earlier.
            if value == value_to_compare:
                minimum_second_index = min(minimum_second_index, j)

    # If no duplicate was found, return -1.
    if minimum_second_index == len(array):
        return -1

    # Return the value of the first duplicate found.
    return array[minimum_second_index]


# Test Cases:

print(first_duplicate_value([2, 1, 5, 2, 3, 3, 4]))
# Output: 2

print(first_duplicate_value([2, 1, 5, 3, 3, 2, 4]))
# Output: 3

print(first_duplicate_value([6, 6, 5, 1, 3, 7, 7, 8]))
# Output: 6

print(first_duplicate_value([1]))
# Output: -1

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The given function `first_duplicate_value` uses a nested loop to find the first duplicate value in the array.
Let's break down the time complexity:

1. **Outer Loop**: The outer loop runs from `i = 0` to `i = len(array) - 1`, which means it iterates `n` times,
where `n` is the length of the array.

2. **Inner Loop**: For each iteration of the outer loop, the inner loop runs from `j = i + 1` to `j = len(array) - 1`. 
The number of iterations of the inner loop decreases as `i` increases:

   - When `i = 0`, the inner loop runs `n - 1` times.
   - When `i = 1`, the inner loop runs `n - 2` times.
   - ...
   - When `i = n - 1`, the inner loop runs `0` times.

   The total number of iterations of the inner loop is approximately:
   
        (n - 1) + (n - 2) + ⋯ + 1 + 0 = n(n - 1) / 2
   
3. **Overall Time Complexity**: The total number of iterations is proportional to `n(n - 1) / 2`, which simplifies to - O(n^2).

   Therefore, the **time complexity** of the function is - O(n^2) .

---

### Space Complexity Analysis

The function uses a constant amount of additional space regardless of the input size:

1. **Variables**: The function uses a few variables like `minimum_second_index`, `value`, and `value_to_compare`, 
but these do not depend on the size of the input array. They use a constant amount of space.

2. **No Additional Data Structures**: The function does not use any additional data structures (e.g., hash maps,
sets, or arrays) that grow with the input size.

   Therefore, the **space complexity** of the function is - O(1).

---

### Summary

- **Time Complexity**: O(n^2) 
- **Space Complexity**: O(1) 

---

### Optimization Suggestion

The current implementation has a quadratic time complexity, which is inefficient for large arrays. We can optimize
this to O(n) time complexity by using a **hash set** to track seen values. 

We will implement optimized solution in (solution_2.py / solution_3.py)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### Explanation of `first_duplicate_value` Function

The function `first_duplicate_value` finds the first duplicate value in a given list (array) by order of appearance.
The first duplicate is defined as the one that appears again at the **earliest** index.

---

### **Step-by-Step Breakdown of the Code**

#### **1. Initialization**
```
minimum_second_index = len(array)
```
- The variable `minimum_second_index` is initialized to the length of the array. This is used to store the 
**smallest second occurrence index** found so far.

#### **2. Outer Loop (Iterating Over Elements)**
```
for i in range(len(array)):
    value = array[i]
```
- The outer loop iterates through each element in the array.
- `value` stores the current element at index `i`.

#### **3. Inner Loop (Checking for Duplicates)**
```
for j in range(i + 1, len(array)):
    value_to_compare = array[j]
```
- The inner loop starts at index `i + 1` and checks all elements that come after `array[i]`.
- `value_to_compare` is the value being checked against `value`.

#### **4. Checking for a Duplicate**
```
if value == value_to_compare:
    minimum_second_index = min(minimum_second_index, j)
```
- If a duplicate of `value` is found at index `j`, we update `minimum_second_index` with the smallest
**second occurrence index** found so far.

#### **5. Checking If No Duplicates Were Found**
```
if minimum_second_index == len(array):
    return -1
```
- If `minimum_second_index` was never updated, it means no duplicates were found, so the function returns `-1`.

#### **6. Returning the First Duplicate Value**
```
return array[minimum_second_index]
```
- If duplicates were found, we return the value at `minimum_second_index`, which represents the first duplicate
value appearing in the list.

---

### **Example Walkthrough**

#### **Example 1**
```
print(first_duplicate_value([2, 1, 5, 2, 3, 3, 4]))
```
- **Step 1:** Start with `minimum_second_index = 7`
- **Step 2:** Outer loop starts with `i = 0`, `value = 2`
  - Inner loop finds `2` again at `j = 3`
  - `minimum_second_index = min(7, 3) = 3`
- **Step 3:** Continue checking but `minimum_second_index` remains 3.
- **Step 4:** Return `array[3] = 2`

- **Output:** `2`

---

#### **Example 2**
```
print(first_duplicate_value([2, 1, 5, 3, 3, 2, 4]))
```
- **Step 1:** Start with `minimum_second_index = 7`
- **Step 2:** `3` is found again at index `4` before `2` appears again at index `5`
- **Step 3:** Return `3`

- **Output:** `3`

---

#### **Example 3**
```
print(first_duplicate_value([6, 6, 5, 1, 3, 7, 7, 8]))
```
- **Step 1:** `6` appears again at index `1`
- **Step 2:** Since `1` is the smallest duplicate index found, return `6`

- **Output:** `6`

---

#### **Example 4**
```
print(first_duplicate_value([1]))
```
- **Step 1:** Only one element, so no duplicates.

- **Output:** `-1`

---

### **Optimization Suggestion**
A more efficient approach using a **set (hashing)** can achieve **O(n) time complexity**.

This method avoids nested loops and improves performance significantly.

"""
