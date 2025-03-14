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
    # Initialize an empty list to store the transposed matrix
    transposed_matrix = []

    # Iterate over each column index of the original matrix
    for col in range(len(matrix[0])):
        # Initialize an empty list to represent a new row in the transposed matrix
        new_row = []

        # Iterate over each row index of the original matrix
        for row in range(len(matrix)):
            # Append the element at the current row and column to the new row
            new_row.append(matrix[row][col])

        # Append the newly formed row to the transposed matrix
        transposed_matrix.append(new_row)

    # Return the transposed matrix
    return transposed_matrix


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

print(transpose_matrix(matrix_1))  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

print(transpose_matrix(matrix_2))  # [[0, 1], [0, 1], [0, 1]]

print(transpose_matrix(matrix_3))  # [[-7, 100, -33], [-7, 12, 17]]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity**

The function uses two nested loops:
1. The outer loop iterates over the columns of the original matrix (`for col in range(len(matrix[0]))`).
2. The inner loop iterates over the rows of the original matrix (`for row in range(len(matrix))`).

If the original matrix has dimensions `m x n` (where `m` is the number of rows and `n` is the number of columns),
the total number of iterations is: `m * n`

Thus, the **time complexity** is: O(m * n)

---

### **Space Complexity**

The function creates a new matrix (`transposed_matrix`) to store the transposed result. The size of this new matrix is `n x m`
(since the original matrix is `m x n`). Therefore, the space required is proportional to the size of the input matrix.

The **space complexity** is: O(m * n)

---

### **Summary**
- **Time Complexity**: O(m * n)
- **Space Complexity**: O(m * n)

Where:
- `m`  = number of rows in the original matrix
- `n`  = number of columns in the original matrix

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**

This Python function **`transpose_matrix(matrix)`** takes a 2D list (matrix) as input and returns its **transpose**.
The transpose of a matrix is obtained by swapping its rows and columns.

#### **Step-by-Step Breakdown**
Let's break down how the function works:

#### **1. Function Definition**
```
def transpose_matrix(matrix):
```
- The function takes a single argument **`matrix`**, which is a list of lists representing a 2D array.

#### **2. Initialize an Empty List for the Transposed Matrix**
```
transposed_matrix = []
```
- This list will store the new rows of the transposed matrix.

#### **3. Iterate Over Columns Instead of Rows**
```
for col in range(len(matrix[0])):  
```
- **`len(matrix[0])`** gives the number of columns in the input matrix.
- The loop iterates over each column index **(col)** to construct a new row for the transposed matrix.

#### **4. Create a New Row for the Transposed Matrix**
```
new_row = []
```
- This list stores elements that will make up a row in the transposed matrix.

#### **5. Iterate Over Each Row to Extract Column Elements**
```
for row in range(len(matrix)):  
    new_row.append(matrix[row][col])
```
- **`len(matrix)`** gives the number of rows in the input matrix.
- The **inner loop** iterates over each row (row index).
- **`matrix[row][col]`** extracts the element at the **current row and column**.
- This element is added to **`new_row`**.

#### **6. Append the Constructed Row to the Transposed Matrix**
```
transposed_matrix.append(new_row)
```
- The **newly formed row** (which consists of elements from the same column in the original matrix) is added to **`transposed_matrix`**.

#### **7. Return the Transposed Matrix**
```
return transposed_matrix
```
- The function finally returns the new transposed matrix.

---

## **Example Walkthroughs**

Let's apply this function to different test cases.

### **Test Case 1**

#### **Input:**
```
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```
**Original Matrix (3x3):**
```
1  2  3
4  5  6
7  8  9
```
#### **Execution Steps:**
1. **First iteration (col = 0):**  
   - Extract column 0: `[1, 4, 7]` → **New row 1**
   
2. **Second iteration (col = 1):**  
   - Extract column 1: `[2, 5, 8]` → **New row 2**
   
3. **Third iteration (col = 2):**  
   - Extract column 2: `[3, 6, 9]` → **New row 3**

#### **Transposed Matrix Output (3x3):**
```
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

---

### **Test Case 2**

#### **Input:**
```
matrix_2 = [
    [0, 0, 0],
    [1, 1, 1],
]
```
**Original Matrix (2x3):**
```
0  0  0
1  1  1
```
#### **Execution Steps:**
1. **First iteration (col = 0):**  
   - Extract column 0: `[0, 1]` → **New row 1**
   
2. **Second iteration (col = 1):**  
   - Extract column 1: `[0, 1]` → **New row 2**
   
3. **Third iteration (col = 2):**  
   - Extract column 2: `[0, 1]` → **New row 3**

#### **Transposed Matrix Output (3x2):**
```
[
    [0, 1],
    [0, 1],
    [0, 1]
]
```

---

### **Test Case 3**

#### **Input:**
```
matrix_3 = [
    [-7, -7],
    [100, 12],
    [-33, 17],
]
```
**Original Matrix (3x2):**
```
-7   -7
100  12
-33  17
```
#### **Execution Steps:**
1. **First iteration (col = 0):**  
   - Extract column 0: `[-7, 100, -33]` → **New row 1**
   
2. **Second iteration (col = 1):**  
   - Extract column 1: `[-7, 12, 17]` → **New row 2**

#### **Transposed Matrix Output (2x3):**
```
[
    [-7, 100, -33],
    [-7, 12, 17]
]
```

---

## **Summary**
- The function **iterates over columns** of the original matrix and constructs new rows for the transposed matrix.
- The **nested loops** help extract column elements and rearrange them into new rows.
- The function works for matrices of any size (M * N), transposing them into (N * M).

"""
