# Problem Description:

"""

                                        # Spiral Traverse

Write a function that takes in an `n x m` two-dimensional array (that can be square-shaped when `n == m`) and returns
a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral
pattern all the way until every element has been visited.


## Sample Input:
```
array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]
```

## Sample Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the total number of elements in the array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def spiral_traverse(array):
    result = []  # This will store the elements in spiral order

    # Initialize boundaries for the spiral
    start_row, end_row = 0, len(array) - 1  # Start and end rows
    start_col, end_col = 0, len(array[0]) - 1  # Start and end columns

    # Loop until all layers of the spiral are traversed
    while start_row <= end_row and start_col <= end_col:
        # Traverse from left to right along the current top row
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])

        # Traverse from top to bottom along the current right column
        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])

        # Traverse from right to left along the current bottom row (if applicable)
        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break  # Avoid duplicate traversal if only one row is left
            result.append(array[end_row][col])

        # Traverse from bottom to top along the current left column (if applicable)
        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break  # Avoid duplicate traversal if only one column is left
            result.append(array[row][start_col])

        # Move the boundaries inward to process the next inner layer of the spiral
        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result  # Return the elements in spiral order


# Test cases:
array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]

array_2 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5],
]

array_3 = [
    [1],
]

print(spiral_traverse(array))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(spiral_traverse(array_2))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(spiral_traverse(array_3))
# Output: [1]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity:

The time complexity of the `spiral_traverse` function is **O(N)**, where **N** is the total number of elements in the 2D array.
This is because the function visits each element of the array exactly once during the traversal.

### Space Complexity:

The space complexity of the `spiral_traverse` function is **O(N)** as well. This is because the `result` list stores all the
elements of the 2D array in spiral order. The space required for the `result` list grows linearly with the number of elements
in the array.

### Explanation:

1. **Time Complexity**:
   - The function processes each element of the 2D array exactly once.
   - The outer `while` loop runs until all layers of the spiral are traversed.
   - The inner loops (for traversing rows and columns) ensure that each element is visited once.
   - Therefore, the time complexity is linear with respect to the total number of elements in the array.

2. **Space Complexity**:
   - The `result` list stores all the elements of the array in spiral order.
   - The size of the `result` list is equal to the total number of elements in the array.
   - No additional space is used that grows with the input size, so the space complexity is **O(N)**.

### Summary:
- **Time Complexity**: **O(N)**
- **Space Complexity**: **O(N)**

Where **N** is the total number of elements in the 2D array.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of `spiral_traverse` Function**

The function `spiral_traverse` takes a 2D list (matrix) as input and returns a list of its elements traversed
in a spiral order (clockwise). 

#### **Step-by-Step Execution**

1. **Initialize Variables**
   ```
   result = []
   start_row, end_row = 0, len(array) - 1
   start_col, end_col = 0, len(array[0]) - 1
   ```
   - `result`: This will store the elements in spiral order.
   - `start_row` and `end_row`: Define the range of rows to traverse.
   - `start_col` and `end_col`: Define the range of columns to traverse.

2. **Traverse the Matrix in a Spiral Manner**
   The traversal continues while `start_row ≤ end_row` and `start_col ≤ end_col`.

   #### **Step 1: Traverse the Top Row (Left to Right)**
   ```
   for col in range(start_col, end_col + 1):
       result.append(array[start_row][col])
   ```
   - Iterate over the columns from `start_col` to `end_col`.
   - Append the elements in the first row.

   #### **Step 2: Traverse the Right Column (Top to Bottom)**
   ```
   for row in range(start_row + 1, end_row + 1):
       result.append(array[row][end_col])
   ```
   - Iterate over the rows from `start_row + 1` to `end_row`.
   - Append the elements in the last column.

   #### **Step 3: Traverse the Bottom Row (Right to Left)**
   ```
   for col in reversed(range(start_col, end_col)):
       if start_row == end_row:
           break
       result.append(array[end_row][col])
   ```
   - Iterate over the columns from `end_col - 1` to `start_col`.
   - Append the elements in the last row.
   - **Edge case**: If `start_row == end_row`, the row was already processed, so we `break`.

   #### **Step 4: Traverse the Left Column (Bottom to Top)**
   ```
   for row in reversed(range(start_row + 1, end_row)):
       if start_col == end_col:
           break
       result.append(array[row][start_col])
   ```
   - Iterate over the rows from `end_row - 1` to `start_row + 1`.
   - Append the elements in the first column.
   - **Edge case**: If `start_col == end_col`, the column was already processed, so we `break`.

3. **Move to the Inner Layer**
   ```
   start_row += 1
   end_row -= 1
   start_col += 1
   end_col -= 1
   ```
   - The boundaries of the matrix are updated to move inward.

4. **Return the Result**
   ```
   return result
   ```
   - The function returns the `result` list containing elements in spiral order.

---

### **Example Walkthrough**

#### **Example 1**
```
array = [
    [1,  2,  3,  4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
]
print(spiral_traverse(array))
```

**Iteration 1:**
- Top row: `[1, 2, 3, 4]`
- Right column: `[5, 6, 7]`
- Bottom row (reverse): `[8, 9, 10]`
- Left column (reverse): `[11, 12]`
- Update boundaries.

**Iteration 2:**
- Top row: `[13, 14]`
- Right column: `[15]`
- Bottom row (reverse): `[16]`
- Left column: (Skipped because only one row remains)

Final Output:  
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

---

#### **Example 2**
```
array_2 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5],
]
print(spiral_traverse(array_2))
```
Steps:
1. Top row: `[1, 2, 3]`
2. Right column: `[4, 5]`
3. Bottom row (reverse): `[6, 7]`
4. Left column (reverse): `[8]`
5. Center: `[9]`

Final Output:  
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

#### **Example 3**
```
array_3 = [
    [1],
]
print(spiral_traverse(array_3))
```
Only one element in the matrix, so the output is:
```
[1]
```

This method efficiently retrieves matrix elements in a **spiral order** using simple boundary updates
and avoids redundant operations. 

"""
