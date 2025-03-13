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


# O(n log n) time | O(n) space
def sorted_squared_array(array):
    # Initialize a new array called 'sorted_squares' with the same length as the input array.
    # This array will store the squared values of the input array.
    sorted_squares = [0 for _ in array]

    # Iterate over each element in the input array using a for loop.
    for idx in range(len(array)):
        # Get the current element from the input array.
        value = array[idx]

        # Square the current element and store it in the corresponding position
        # in the 'sorted_squares' array.
        sorted_squares[idx] = value * value

    # Sort the 'sorted_squares' array in ascending order.
    # This ensures that the squared values are returned in sorted order.
    sorted_squares.sort()

    # Return the sorted array of squared values.
    return sorted_squares


# Test Cases
print(sorted_squared_array([1, 2, 3, 5, 6, 8, 9]))  # Output: [1, 4, 9, 25, 36, 64, 81]
print(sorted_squared_array([-5, -4, -3, -2, -1]))  # Output: [1, 4, 9, 16, 25]
print(sorted_squared_array([-10, -5, 0, 5, 10]))  # Output: [0, 25, 25, 100, 100]
print(sorted_squared_array([0]))  # Output: [0]

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:

1. **Squaring each element**: The loop that iterates over the array and squares each element runs in `O(n)` time,
where `n` is the length of the array.

2. **Sorting the squared array**: The `sort()` function in Python uses the Timsort algorithm, which has a
time complexity of `O(n log n)`.

Thus, the overall time complexity is:

    O(n) + O(n log n) = `O(n log n)`


### Space Complexity:

1. **Creating the `sorted_squares` array**: This requires `O(n)` space to store the squared values.
2. **Sorting**: The `sort()` function in Python sorts the array in-place, so it does not require additional space.

Thus, the overall space complexity is: `O(n)`

### Summary:
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`

"""

# Detailed Code Explanation:

"""

The provided Python function `sorted_squared_array` computes the squares of elements in the input array
and returns them sorted in non-decreasing order. Let's break it down step-by-step to understand how
it works and its time/space complexity.

---

### **Code Analysis**

1. **Initialization of `sorted_squares`**
   ```
   sorted_squares = [0 for _ in array]
   ```
   - This creates a new list, `sorted_squares`, of the same length as the input array. Initially, all elements
   in this list are set to `0`.
   - Example: If `array = [1, 2, 3]`, then `sorted_squares = [0, 0, 0]`.

---

2. **Compute the Squares**
   ```
   for idx in range(len(array)):
       value = array[idx]
       sorted_squares[idx] = value * value
   ```
   - This loop iterates over each element in the input array.
   - For each element, it computes the square of the value and stores it in the corresponding index of the `sorted_squares` list.

   Example:
   - Input: `array = [1, 2, 3]`
   - Iteration 1: `value = 1`, `sorted_squares[0] = 1 * 1 = 1`
   - Iteration 2: `value = 2`, `sorted_squares[1] = 2 * 2 = 4`
   - Iteration 3: `value = 3`, `sorted_squares[2] = 3 * 3 = 9`
   - Result: `sorted_squares = [1, 4, 9]`

---

3. **Sorting the Squared Values**
   ```
   sorted_squares.sort()
   ```
   - The `sort()` method is applied to sort the squared values in non-decreasing order.
   - If the input array contains both positive and negative numbers, their squares may not be in order.
   For instance:
     - Input: `array = [-3, -2, 1, 4]`
     - Squared: `sorted_squares = [9, 4, 1, 16]`
     - After sorting: `sorted_squares = [1, 4, 9, 16]`

---

4. **Return the Sorted Squares**
   ```
   return sorted_squares
   ```
   - Finally, the sorted list of squared values is returned.

---

### **Example Walkthrough**

### **Example 1**
For input:
```
array = [1, 2, 3, 5, 6, 8, 9]
```

#### Step-by-Step Execution:
1. **Initialization**:
   ```
   sorted_squares = [0, 0, 0, 0, 0, 0, 0]
   ```

2. **Squaring**:
   - Iteration 1: `value = 1`, `sorted_squares[0] = 1 * 1 = 1`
   - Iteration 2: `value = 2`, `sorted_squares[1] = 2 * 2 = 4`
   - Iteration 3: `value = 3`, `sorted_squares[2] = 3 * 3 = 9`
   - Iteration 4: `value = 5`, `sorted_squares[3] = 5 * 5 = 25`
   - Iteration 5: `value = 6`, `sorted_squares[4] = 6 * 6 = 36`
   - Iteration 6: `value = 8`, `sorted_squares[5] = 8 * 8 = 64`
   - Iteration 7: `value = 9`, `sorted_squares[6] = 9 * 9 = 81`
   ```
   sorted_squares = [1, 4, 9, 25, 36, 64, 81]
   ```

3. **Sorting**:
   - The array is already sorted, so no changes are made:
   ```
   sorted_squares = [1, 4, 9, 25, 36, 64, 81]
   ```

4. **Return**:
   ```
   return [1, 4, 9, 25, 36, 64, 81]
   ```

Let's analyze each of the examples step by step based on how the `sorted_squared_array` function processes them.

---

### **Example 2**

#### Input Array:
```
array = [-5, -4, -3, -2, -1]
```

#### Steps:
1. **Initialization**:
   ```
   sorted_squares = [0, 0, 0, 0, 0]
   ```

2. **Squaring**:
   Each element of `array` is squared:
   - Iteration 1: `value = -5`, `sorted_squares[0] = (-5)^2 = 25`
   - Iteration 2: `value = -4`, `sorted_squares[1] = (-4)^2 = 16`
   - Iteration 3: `value = -3`, `sorted_squares[2] = (-3)^2 = 9`
   - Iteration 4: `value = -2`, `sorted_squares[3] = (-2)^2 = 4`
   - Iteration 5: `value = -1`, `sorted_squares[4] = (-1)^2 = 1`
   ```
   sorted_squares = [25, 16, 9, 4, 1]
   ```

3. **Sorting**:
   After sorting the squared values:
   ```
   sorted_squares = [1, 4, 9, 16, 25]
   ```

4. **Output**:
   ```
   return [1, 4, 9, 16, 25]
   ```

---

### **Example 3**

#### Input Array:
```
array = [-10, -5, 0, 5, 10]
```

#### Steps:
1. **Initialization**:
   ```
   sorted_squares = [0, 0, 0, 0, 0]
   ```

2. **Squaring**:
   Each element of `array` is squared:
   - Iteration 1: `value = -10`, `sorted_squares[0] = (-10)^2 = 100`
   - Iteration 2: `value = -5`, `sorted_squares[1] = (-5)^2 = 25`
   - Iteration 3: `value = 0`, `sorted_squares[2] = (0)^2 = 0`
   - Iteration 4: `value = 5`, `sorted_squares[3] = (5)^2 = 25`
   - Iteration 5: `value = 10`, `sorted_squares[4] = (10)^2 = 100`
   ```
   sorted_squares = [100, 25, 0, 25, 100]
   ```

3. **Sorting**:
   After sorting the squared values:
   ```
   sorted_squares = [0, 25, 25, 100, 100]
   ```

4. **Output**:
   ```
   return [0, 25, 25, 100, 100]
   ```

---

### **Example 4**

#### Input Array:
```
array = [0]
```

#### Steps:
1. **Initialization**:
   ```
   sorted_squares = [0]
   ```

2. **Squaring**:
   Each element of `array` is squared:
   - Iteration 1: `value = 0`, `sorted_squares[0] = (0)^2 = 0`
   ```
   sorted_squares = [0]
   ```

3. **Sorting**:
   No sorting is needed as the array has only one element:
   ```
   sorted_squares = [0]
   ```

4. **Output**:
   ```
   return [0]
   ```

---

### **Key Observations**
1. **Negative Numbers**:
   - Negative numbers squared yield positive results, but the order of the squared values depends on their absolute values.
   - The sorting step ensures that the results are in non-decreasing order.
   
2. **Zeros**:
   - A `0` squared remains `0`, and it does not affect the sorting.

3. **Symmetry**:
   - For inputs containing symmetric values around `0` (like `-10` and `10`), their squared values are the same,
   and sorting ensures duplicates appear in the correct order.

---

### **Potential Optimization**
The current algorithm uses `O(n log n)` time due to sorting. However, if the input array is already
sorted in non-decreasing order (as in this case), we can optimize this to **`O(n)`** time and
**`O(n)`** space by using a two-pointer approach.

"""
