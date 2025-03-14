# Problem Description:

"""

                                        Transpose Matrix

You're given a 2D array of integers `matrix`. Write a function that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left
to bottom-right); it switches the row and column indices of the original matrix.

You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.


## Sample Input:
```
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

## Sample Output:
```
[
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
]
```

## Optimal Time & Space Complexity:
```
O(w * h) time | O(w * h) space - where `w` is the width of the matrix and `h` is the height.
```

"""

# =========================================================================================================================== #

# Solution:


# O(w * h) time | O(w * h) space - where `w` is the
# width of the matrix and `h` is the height
def transpose_matrix(matrix):
    # The transpose of a matrix is obtained by swapping its rows and columns.
    # This list comprehension iterates over each column index (col) of the original matrix.
    # For each column index, it creates a new row in the transposed matrix by collecting
    # the elements from each row (row) of the original matrix at that column index.
    return [
        [matrix[row][col] for row in range(len(matrix))]
        for col in range(len(matrix[0]))
    ]


# Test Cases
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

matrix_2 = [
    [0, 0, 0],
    [1, 1, 1],
]

matrix_3 = [
    [-7, -7],
    [100, 12],
    [-33, 17],
]

# Expected Output:
print(transpose_matrix(matrix_1))  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

print(transpose_matrix(matrix_2))  # [[0, 1], [0, 1], [0, 1]]

print(transpose_matrix(matrix_3))  # [[-7, 100, -33], [-7, 12, 17]]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:


### **Time Complexity**

The function uses a nested list comprehension:
1. The outer loop iterates over the columns of the original matrix (`col` ranges from `0` to `len(matrix[0])`).
2. The inner loop iterates over the rows of the original matrix (`row` ranges from `0` to `len(matrix)`).

If the original matrix has dimensions (m * n) (where `m` is the number of rows and `n` is the number of columns):
- The outer loop runs `n` times.
- The inner loop runs `m` times for each iteration of the outer loop.

Thus, the total number of iterations is (m * n), and the **time complexity is - O(m * n)**.

---

### **Space Complexity**

The function constructs a new transposed matrix of size (n * m):
- The transposed matrix stores (m * n) elements.

Thus, the **space complexity is - O(m * n)**.

---

### **Summary**
- **Time Complexity:** O(m * n)
- **Space Complexity:** O(m * n)

This is optimal for transposing a matrix, as you need to visit every element at least once and store the result in a new matrix.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The function `transpose_matrix(matrix)` takes a 2D list (matrix) as input and returns its **transpose**. The transpose
of a matrix is obtained by flipping it over its diagonal, meaning the rows become columns and the columns become rows.

---

### **Code Breakdown**

```
def transpose_matrix(matrix):
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]
```

#### **Understanding the Transposition Logic**
1. The function uses **list comprehension** to create the transposed matrix.
2. **Outer List Comprehension (`for col in range(len(matrix[0]))`)**:
   - `matrix[0]` represents the first row.
   - `len(matrix[0])` gives the number of columns in the original matrix.
   
   - This loop iterates over **columns** of the original matrix.
   - Each iteration forms a new row in the transposed matrix.

3. **Inner List Comprehension (`for row in range(len(matrix))`)**:
   - `len(matrix)` gives the number of rows in the original matrix.
   - This loop iterates over the rows of the original matrix.
   - It extracts elements from each row at the **same column index**.

4. **Matrix Transposition Rule**:
   - The element at position `(i, j)` in the original matrix moves to position `(j, i)` in the transposed matrix.

---

### **Example Walkthrough**

#### **Test Case 1: `matrix_1`**
```
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```
Original:
```
1  2  3
4  5  6
7  8  9
```
Transposed:
```
1  4  7
2  5  8
3  6  9
```
#### **Step-by-Step Execution**
- First iteration (`col = 0`): `[matrix[0][0], matrix[1][0], matrix[2][0]]` → `[1, 4, 7]`

- Second iteration (`col = 1`): `[matrix[0][1], matrix[1][1], matrix[2][1]]` → `[2, 5, 8]`

- Third iteration (`col = 2`): `[matrix[0][2], matrix[1][2], matrix[2][2]]` → `[3, 6, 9]`

Output:
```
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

---

#### **Test Case 2: `matrix_2`**
```
matrix_2 = [
    [0, 0, 0],
    [1, 1, 1],
]
```
Original:
```
0  0  0
1  1  1
```
Transposed:
```
0  1
0  1
0  1
```
Output:
```
[[0, 1], [0, 1], [0, 1]]
```

---

#### **Test Case 3: `matrix_3`**
```
matrix_3 = [
    [-7, -7],
    [100, 12],
    [-33, 17],
]
```
Original:
```
-7   -7
100  12
-33  17
```
Transposed:
```
-7   100  -33
-7   12   17
```
Output:
```
[[-7, 100, -33], [-7, 12, 17]]
```

---

### **Alternative Approach using `zip()`**

A more Pythonic way to transpose a matrix:
```
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
```
This uses the `zip()` function to group elements column-wise, making it more concise.

"""
