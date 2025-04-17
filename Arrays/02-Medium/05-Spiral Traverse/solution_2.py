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
    # Initialize an empty list to store the result of the spiral traversal
    result = []
    # Call the helper function to fill the result list in a spiral order
    spiral_fill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)

    return result


def spiral_fill(array, start_row, end_row, start_col, end_col, result):
    # Base case: If the start row/column is greater than the end row/column, we stop the recursion
    if start_row > end_row or start_col > end_col:
        return

    # Traverse from the start column to the end column in the current start row
    for col in range(start_col, end_col + 1):
        result.append(array[start_row][col])

    # Traverse from the start row + 1 to the end row in the current end column
    for row in range(start_row + 1, end_row + 1):
        result.append(array[row][end_col])

    # Traverse from the end column - 1 back to the start column in the current end row
    # Only if the start row is not equal to the end row (to avoid duplicate traversal)
    for col in reversed(range(start_col, end_col)):
        if start_row == end_row:
            break  # Avoid duplicate traversal if the current layer is a single row

        result.append(array[end_row][col])

    # Traverse from the end row - 1 back to the start row + 1 in the current start column
    # Only if the start column is not equal to the end column (to avoid duplicate traversal)
    for row in reversed(range(start_row + 1, end_row)):
        if start_col == end_col:
            break  # Avoid duplicate traversal if the current layer is a single column

        result.append(array[row][start_col])

    # Recursively call the function to traverse the next inner layer of the spiral
    spiral_fill(array, start_row + 1, end_row - 1, start_col + 1, end_col - 1, result)


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

### Time Complexity Analysis

The time complexity of the `spiral_traverse` function is **O(N)**, where **N** is the total number of elements in the 2D array. Here's why:

1. **Traversal of all elements**: The function visits every element in the 2D array exactly once. Each element is appended
to the `result` list in a single pass.

2. **Recursive calls**: The recursive calls (`spiral_fill`) reduce the problem size by moving inward (shrinking the boundaries
of the spiral). However, each recursive call still processes a subset of the elements, and the total number of operations
remains proportional to the total number of elements **N**.

Thus, the time complexity is linear **O(N)** with respect to the total number of elements in the array.

---

### Space Complexity Analysis

The space complexity of the `spiral_traverse` function is **O(N)** in the worst case, where **N** is the total number
of elements in the 2D array. Here's why:

1. **Output space**: The `result` list stores all **N** elements of the 2D array, contributing **O(N)** space.

2. **Recursive call stack**: The recursion depth depends on the number of layers in the spiral. For a 2D array with
dimensions **m x n**, the maximum recursion depth is approximately **min(m, n) / 2**. However, this is still **O(min(m, n))**,
which is less than or equal to **O(N)** in the worst case.

Thus, the dominant factor in space complexity is the `result` list, making the overall space complexity **O(N)**.

---

### Summary

- **Time Complexity**: **O(N)**, where **N** is the total number of elements in the 2D array.
- **Space Complexity**: **O(N)**, due to the `result` list storing all elements.

This implementation is efficient for traversing a 2D array in spiral order.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function `spiral_traverse` takes a 2D array (a matrix) and returns its elements in a spiral order. The traversal starts from
the top-left corner and moves to the right, then down, then left, then up, and continues inward until all elements are visited.

---

## **Detailed Breakdown of the Code**
The function consists of two main parts:

1. `spiral_traverse(array)`:  
   - This is the main function that initializes the `result` list and calls the recursive helper function `spiral_fill`.

2. `spiral_fill(array, start_row, end_row, start_col, end_col, result)`:  
   - This is a recursive function that progressively shrinks the boundaries of the matrix while adding elements in a spiral order.

---

### **Step-by-Step Execution**

#### **Step 1: Initialization**
- The `spiral_traverse` function initializes an empty list `result` to store the elements in spiral order.
- It then calls `spiral_fill` with the full matrix boundaries:
  ```
  spiral_fill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
  ```
  - `start_row = 0`: The first row index
  - `end_row = len(array) - 1`: The last row index
  - `start_col = 0`: The first column index
  - `end_col = len(array[0]) - 1`: The last column index

---

#### **Step 2: Spiral Traversal**
Inside `spiral_fill`, we traverse the matrix in four steps:

1. **Traverse the Top Row (Left to Right)**  
   - We move from `start_col` to `end_col` in the `start_row`:
     ```
     for col in range(start_col, end_col + 1):
         result.append(array[start_row][col])
     ```
   - Example for `array`:
     ```
     [1,  2,  3,  4]   <- Adding these
     [12, 13, 14, 5]
     [11, 16, 15, 6]
     [10, 9,  8,  7]
     ```

2. **Traverse the Right Column (Top to Bottom)**  
   - We move from `start_row + 1` to `end_row` along `end_col`:
     ```
     for row in range(start_row + 1, end_row + 1):
         result.append(array[row][end_col])
     ```
   - Example for `array`:
     ```
     [1,  2,  3,  4]
     [12, 13, 14, (5)]   <- Adding these
     [11, 16, 15, (6)]
     [10, 9,  8,  (7)]
     ```

3. **Traverse the Bottom Row (Right to Left)**
   - We move from `end_col - 1` to `start_col`, but only if `start_row != end_row` (to prevent duplicate elements
   when there’s only one row left).
     ```
     for col in reversed(range(start_col, end_col)):
         if start_row == end_row:
             break
         result.append(array[end_row][col])
     ```
   - Example for `array`:
     ```
     [1,  2,  3,  4]
     [12, 13, 14, 5]
     [11, 16, 15, 6]
     [(10), (9), (8), 7]   <- Adding these
     ```

4. **Traverse the Left Column (Bottom to Top)**
   - We move from `end_row - 1` to `start_row + 1`, but only if `start_col != end_col` (to prevent duplicate elements
   when there’s only one column left).
     ```
     for row in reversed(range(start_row + 1, end_row)):
         if start_col == end_col:
             break
         result.append(array[row][start_col])
     ```
   - Example for `array`:
     ```
     [(1),  2,  3,  4]
     [(12), 13, 14, 5]
     [(11), 16, 15, 6]
     [10, 9,  8,  7]
     ```

---

#### **Step 3: Recursion**
After processing the outermost layer, we **shrink the boundaries** by moving inward and recursively calling `spiral_fill`:
```
spiral_fill(array, start_row + 1, end_row - 1, start_col + 1, end_col - 1, result)
```
- `start_row + 1`: Move the top boundary down
- `end_row - 1`: Move the bottom boundary up
- `start_col + 1`: Move the left boundary right
- `end_col - 1`: Move the right boundary left

This continues until `start_row > end_row` or `start_col > end_col`, at which point the recursion stops.

---

### **Example Execution**
#### **Example 1: 4×4 Matrix**
Input:
```
array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]
```
Step-by-step traversal:
```
[1, 2, 3, 4]  →  [5, 6, 7]  →  [8, 9, 10]  →  [11, 12]  →  [13, 14]  →  [15, 16]
```
Final Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

---

#### **Example 2: 3×3 Matrix**
Input:
```
array_2 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5],
]
```
Step-by-step traversal:
```
[1, 2, 3]  →  [4, 5]  →  [6, 7]  →  [8]  →  [9]
```
Final Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

#### **Example 3: Single Element Matrix**
Input:
```
array_3 = [[1]]
```
- The only element `[1]` is added, and recursion stops immediately.
Output:
```
[1]
```

---

## **Summary**
- The function extracts elements in a **spiral order** from a matrix.
- It uses **recursion** to progressively shrink the boundaries of the matrix.
- It ensures **no duplicate elements** are added by using boundary checks.
- The algorithm is **efficient** with O(N*M) complexity.

"""
