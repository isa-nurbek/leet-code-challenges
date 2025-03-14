# Problem Description:

"""

                                        # Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing
elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.


## Sample Input:
```
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
```

## Sample Output:
```
True
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space - where `n` is the length of the array
def is_monotonic(array):
    # If the array has 2 or fewer elements, it is always monotonic
    if len(array) <= 2:
        return True

    # Calculate the initial direction of the array (increasing or decreasing)
    direction = array[1] - array[0]

    # Iterate through the array starting from the third element
    for i in range(2, len(array)):
        # If the direction is still undetermined (i.e., direction == 0),
        # update the direction based on the current and previous elements
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue

        # Check if the current element breaks the previously determined direction
        if breaks_direction(direction, array[i - 1], array[i]):
            return False

    # If no elements break the direction, the array is monotonic
    return True


def breaks_direction(direction, previous_int, current_int):
    # Calculate the difference between the current and previous elements
    difference = current_int - previous_int

    # If the initial direction was increasing, check if the current difference is decreasing
    if direction > 0:
        return difference < 0

    # If the initial direction was decreasing, check if the current difference is increasing
    return difference > 0


# Test cases:

print(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
# Output: True

print(is_monotonic([2, 2, 2, 1, 4, 5]))
# Output: False

print(is_monotonic([]))
# Output: True

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

1. **Initialization and Edge Case Check**:
   - The function starts by checking if the length of the array is less than or equal to 2. This is an O(1) operation.
   
2. **Direction Calculation**:
   - The direction is calculated as `array[1] - array[0]`, which is also an O(1) operation.

3. **Loop Through the Array**:
   - The loop runs from the 2nd index to the end of the array, so it iterates (n-2) times, where `n` is the length of the array.
   - Inside the loop, the function checks if the direction is 0 and updates it if necessary. This is an O(1) operation.
   - The `breaks_direction` function is called, which also runs in O(1) time since it performs simple arithmetic and
   comparison operations.

4. **Overall Time Complexity**:
   - The loop dominates the time complexity, and since it runs (n-2) times with O(1) operations inside,
   the overall time complexity is O(n).

---

### Space Complexity:

1. **Variables**:
   - The function uses a few variables (`direction`, `i`, `difference`), but these do not depend on the size of the input array.
   
2. **No Additional Data Structures**:
   - The function does not use any additional data structures that grow with the input size.

3. **Overall Space Complexity**:
   - The space complexity is O(1), meaning it uses constant space regardless of the input size.

### Summary:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

Where `n` is the length of the input array.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the `is_monotonic` Function**

The `is_monotonic` function determines whether a given array is **monotonic**. A sequence is called **monotonic** 
if it is either **entirely non-increasing** or **entirely non-decreasing**.

---

## **Code Breakdown**

### **1. Base Case - Handling Small Arrays**
```
if len(array) <= 2:
    return True
```
- If the array has **0, 1, or 2 elements**, it is trivially monotonic.
- For example, an array like `[]` (empty) or `[3]` (single element) is always monotonic.
- Similarly, `[5, 5]` or `[1, 2]` are monotonic.

---

### **2. Determining Initial Direction**
```
direction = array[1] - array[0]
```
- This determines whether the sequence is **increasing** or **decreasing** based on the first two elements.
- If `direction > 0`, it suggests the sequence is increasing.
- If `direction < 0`, it suggests the sequence is decreasing.
- If `direction == 0`, it means the first two elements are equal, so the function will decide later.

---

### **3. Iterating Through the Array**
```
for i in range(2, len(array)):
```
- The loop starts from the **third element** (`i = 2`), since we already compared the first two.

#### **Handling Neutral Direction (Equal Elements)**
```
if direction == 0:
    direction = array[i] - array[i - 1]
    continue
```
- If the direction was `0` (meaning the first two elements were the same), we update the direction based on the new element.
- Example: If `array = [3, 3, 5]`, the first two elements are equal (`direction = 0`). But when we reach `5`, we realize the
sequence is increasing.

---

### **4. Checking for Direction Breaks**
```
if breaks_direction(direction, array[i - 1], array[i]):
    return False
```
- If the new element contradicts the established direction, the function returns `False` (not monotonic).

---

### **5. Function to Check if Direction Breaks**
```
def breaks_direction(direction, previous_int, current_int):
    difference = current_int - previous_int

    if direction > 0:
        return difference < 0  # Should be increasing but found decreasing

    return difference > 0  # Should be decreasing but found increasing
```
- If the array was **increasing**, but we find a **decreasing** value → return `True` (breaks direction).
- If the array was **decreasing**, but we find an **increasing** value → return `True` (breaks direction).

---

### **6. Returning Final Result**
```
return True
```
- If we go through the entire loop without returning `False`, the array is monotonic.

---

## **Example Walkthroughs**

### **Example 1: `is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])`**

- The array is **decreasing**.
- We check:
  ```
  -5 < -1  ✅ (decreasing)
  -10 < -5 ✅ (decreasing)
  -1100 < -10 ✅ (decreasing)
  -1100 == -1100 ✅ (same value, no change)
  -1101 < -1100 ✅ (decreasing)
  -1102 < -1101 ✅ (decreasing)
  -9001 < -1102 ✅ (decreasing)
  ```
- Since there was no contradiction, **output is `True`**.

---

### **Example 2: `is_monotonic([2, 2, 2, 1, 4, 5])`**

- First elements are equal → `direction = 0`.
- At `1`, the array starts **decreasing**, so `direction = -1`.
- But then at `4`, it **increases**, which **breaks the decreasing trend**.

- The function returns `False`.

---

### **Example 3: `is_monotonic([])`**

- Since the array length is `0`, the condition `len(array) <= 2` applies.
- **Output is `True`** (an empty array is trivially monotonic).

---

Let's go over some **edge cases** in more detail.

---

### **Edge Case 1: Array with All Identical Elements**

#### **Example:**
```
print(is_monotonic([5, 5, 5, 5]))
```
#### **Explanation:**
- `direction = 5 - 5 = 0` (initially undecided)
- Each subsequent difference is also `0`, so no contradiction.
- **Output:** `True` (all elements are equal, so it's both increasing and decreasing at the same time).

---

### **Edge Case 2: Array with Only One Element**

#### **Example:**
```
print(is_monotonic([7]))
```
#### **Explanation:**
- Since `len(array) <= 2`, the function **immediately returns `True`**.
- A single-element array is trivially monotonic.

---

### **Edge Case 3: Already Sorted Increasing Order**

#### **Example:**
```
print(is_monotonic([1, 2, 3, 4, 5]))
```
#### **Explanation:**
- `direction = 2 - 1 = 1` (increasing).
- Each subsequent element **keeps increasing**, so no contradiction.
- **Output:** `True`.

---

### **Edge Case 4: Already Sorted Decreasing Order**

#### **Example:**
```
print(is_monotonic([10, 9, 8, 7, 6]))
```
#### **Explanation:**
- `direction = 9 - 10 = -1` (decreasing).
- Each subsequent element **keeps decreasing**, so no contradiction.
- **Output:** `True`.

---

### **Edge Case 5: Increasing but Then Decreasing**

#### **Example:**
```
print(is_monotonic([1, 2, 3, 2, 1]))
```
#### **Explanation:**
- `direction = 2 - 1 = 1` (initially increasing).
- `3 > 2` ✅ (still increasing).
- `2 < 3` ❌ (breaks the increasing direction).
- **Output:** `False` (not monotonic).

---

### **Edge Case 6: Decreasing but Then Increasing**

#### **Example:**
```
print(is_monotonic([5, 4, 3, 4, 5]))
```
#### **Explanation:**
- `direction = 4 - 5 = -1` (initially decreasing).
- `3 < 4` ✅ (still decreasing).
- `4 > 3` ❌ (breaks the decreasing trend).
- **Output:** `False` (not monotonic).

---

### **Edge Case 7: Mix of Increasing and Constant Elements**

#### **Example:**
```
print(is_monotonic([1, 2, 2, 3, 3, 4]))
```
#### **Explanation:**
- `direction = 2 - 1 = 1` (increasing).
- `2 == 2` ✅ (no change).
- `3 > 2` ✅ (still increasing).
- `3 == 3` ✅ (no change).
- `4 > 3` ✅ (still increasing).
- **Output:** `True` (constant values don’t break monotonicity).

---

### **Edge Case 8: Mix of Decreasing and Constant Elements**

#### **Example:**
```
print(is_monotonic([5, 5, 4, 4, 3, 3, 1]))
```
#### **Explanation:**
- `direction = 5 - 5 = 0` (undecided initially).
- `4 < 5` → Now `direction = -1` (decreasing).
- `4 == 4` ✅ (no change).
- `3 < 4` ✅ (still decreasing).
- `3 == 3` ✅ (no change).
- `1 < 3` ✅ (still decreasing).
- **Output:** `True`.

---

### **Edge Case 9: A Sudden Jump in Values**

#### **Example:**
```
print(is_monotonic([1, 100, 2]))
```
#### **Explanation:**
- `direction = 100 - 1 = 99` (initially increasing).
- `2 < 100` ❌ (breaks increasing trend).
- **Output:** `False`.

---

### **Edge Case 10: A Sudden Drop in Values**

#### **Example:**
```
print(is_monotonic([10, -50, 9]))
```
#### **Explanation:**
- `direction = -50 - 10 = -60` (initially decreasing).
- `9 > -50` ❌ (breaks decreasing trend).
- **Output:** `False`.

---

## **Summary**
- ✅ **Handles empty and small arrays quickly.**  
- ✅ **Accounts for both increasing and decreasing trends**.
- ✅ **Properly identifies when a trend is broken**.
- ✅ **Determines initial direction from first two elements.**  
- ✅ **Updates direction when necessary.**  
- ✅ **Detects when the sequence breaks monotonicity.**  
- ✅ **Efficient with O(N) time complexity.**  

"""
