# Problem Description:

"""

                                    Sorted Squared Array

Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns
a new array of the same length with the squares of the original integers also sorted in ascending order.


## Sample Input:
```
array = [1, 2, 3, 5, 6, 8, 9]
```

## Sample Output:
```
[1, 4, 9, 25, 36, 64, 81]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input array.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def sorted_squared_array(array):
    # Initialize a list to store the sorted squares, filled with zeros initially
    sorted_squares = [0 for _ in array]

    # Pointers for the smallest and largest values in the input array
    smaller_value_idx = 0
    larger_value_idx = len(array) - 1

    # Iterate over the array in reverse order to fill the sorted_squares array
    for idx in reversed(range(len(array))):
        # Get the smallest and largest values using the pointers
        smaller_value = array[smaller_value_idx]
        larger_value = array[larger_value_idx]

        # Compare the absolute values of the smallest and largest elements
        if abs(smaller_value) > abs(larger_value):
            # If the smallest value's absolute value is larger, square it and place it at the current index
            sorted_squares[idx] = smaller_value * smaller_value
            # Move the smaller value pointer to the right
            smaller_value_idx += 1
        else:
            # If the largest value's absolute value is larger or equal, square it and place it at the current index
            sorted_squares[idx] = larger_value * larger_value
            # Move the larger value pointer to the left
            larger_value_idx -= 1

    # Return the sorted array of squares
    return sorted_squares


# Test Cases
print(sorted_squared_array([-5, -4, -3, -2, -1]))  # Output: [1, 4, 9, 16, 25]
print(sorted_squared_array([1, 2, 3, 5, 6, 8, 9]))  # Output: [1, 4, 9, 25, 36, 64, 81]
print(sorted_squared_array([-10, -5, 0, 5, 10]))  # Output: [0, 25, 25, 100, 100]
print(sorted_squared_array([0]))  # Output: [0]

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis:

### **Time Complexity: O(n)**
- The function iterates through the input array **once** using two pointers (`smaller_value_idx` and `larger_value_idx`).
- The loop runs for `n` iterations, where `n` is the length of the input array.
- Each iteration performs a constant amount of work (comparisons, squaring, and updating indices).
- Thus, the time complexity is **O(n)**.

---

### **Space Complexity: O(n)**
- The function creates a new array `sorted_squares` of the same size as the input array to store the squared values.
- No additional data structures are used that grow with the input size.
- Thus, the space complexity is **O(n)**.

---

### **Summary**
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)  

This is an optimal solution for the problem.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""

### Explanation of the Code: `sorted_squared_array`

This Python function efficiently computes the **squares** of all numbers in a sorted array and returns the squares
in **sorted order**. The algorithm uses a two-pointer approach, making it run in O(n) time and use O(n) space.

---

### Step-by-Step Breakdown:

#### **1. Input Assumption:**
- The input array is sorted in **non-decreasing order** (increasing order).
- The array can contain negative numbers, positive numbers, and zero.

---

#### **2. Key Idea:**
- When you square numbers, negative and positive values have the same result (e.g., -3^2 = 3^2 = 9 ).
- The largest squared value will always come from the largest absolute value in the array.
- By comparing the absolute values of the numbers at the **start** and **end** of the array, we can place
the largest squared values into the result array **from right to left**.

---

#### **3. Code Explanation:**

##### **a. Initialize Variables:**

```
sorted_squares = [0 for _ in array]
```
- Create an array `sorted_squares` to store the squared values in sorted order. The size matches the input array
and is initialized with zeros.

```
smaller_value_idx = 0
larger_value_idx = len(array) - 1
```
- Two pointers are defined:
  - `smaller_value_idx` starts at the **beginning** of the array.
  - `larger_value_idx` starts at the **end** of the array.

---

##### **b. Iterate in Reverse:**

```
for idx in reversed(range(len(array))):
```
- We iterate from the **last index** (rightmost position) to the first index. 
- This ensures the largest squared values are placed in the correct position in `sorted_squares` as we compute them.

---

##### **c. Compare Absolute Values:**

```
smaller_value = array[smaller_value_idx]
larger_value = array[larger_value_idx]
```
- Fetch the current values at the two pointers.

```
if abs(smaller_value) > abs(larger_value):
```
- Compare the absolute values of `smaller_value` and `larger_value`:
  - If the absolute value of `smaller_value` is larger:
    - Square `smaller_value` and place it at index `idx` in `sorted_squares`.
    - Move `smaller_value_idx` to the right (increment by 1).
  - Otherwise:
    - Square `larger_value` and place it at index `idx` in `sorted_squares`.
    - Move `larger_value_idx` to the left (decrement by 1).

---

##### **d. Return Result:**

```
return sorted_squares
```
- Return the `sorted_squares` array.

---

### Example Walkthrough:

#### **Input:** `[-5, -4, -3, -2, -1]`

1. **Initial State:**
   - `smaller_value_idx = 0` (points to -5)
   - `larger_value_idx = 4` (points to -1)
   - `sorted_squares = [0, 0, 0, 0, 0]`

2. **Iteration 1:** (`idx = 4`)
   - Compare: |-5| > |-1| → 5 > 1.
   - Square `-5` → 25, place at index 4.
   - Move `smaller_value_idx` → 1.
   - `sorted_squares = [0, 0, 0, 0, 25]`

3. **Iteration 2:** (`idx = 3`)
   - Compare: |-4| > |-1| → 4 > 1.
   - Square `-4` → 16, place at index 3.
   - Move `smaller_value_idx` → 2.
   - `sorted_squares = [0, 0, 0, 16, 25]`

4. **Continue Similarly...**

5. **Final State:**
   - `sorted_squares = [1, 4, 9, 16, 25]`

#### **Input:** `[1, 2, 3, 5, 6, 8, 9]`

1. **Initial State:**
   - Positive numbers only.
   - Squares directly sorted by the algorithm.
   - Result: `[1, 4, 9, 25, 36, 64, 81]`.

#### **Input:** `[-10, -5, 0, 5, 10]`

1. **Initial State:**
   - Mix of positive, negative, and zero.
   - Largest absolute values are `10` and `-10`, contributing 100 each.
   - Result: `[0, 25, 25, 100, 100]`.

"""
