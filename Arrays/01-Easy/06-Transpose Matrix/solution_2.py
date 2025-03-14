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
