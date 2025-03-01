# Description:

"""

                                        Transpose Matrix

You're given a 2D array of integers `matrix`. Write a function that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left
to bottom-right); it switches the row and column indices of the original matrix.

You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.

## Sample Input #1

```
matrix = [
  [1, 2],
]
```

## Sample Output #1

```
[
  [1],
  [2]
]
```

## Sample Input #2

```
matrix = [
  [1, 2],
  [3, 4],
  [5, 6]
]
```

## Sample Output #2

```
[
  [1, 3, 5],
  [2, 4, 6]
]
```

## Sample Input #3

```
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

## Sample Output #3

```
[
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9]
]
```

## Optimal Space & Time Complexity

```
`O(w*h)` time | `O(w*h)` space - where `w` is the width of the matrix and `h` is the height
```

"""

# Solution:


# `O(w*h)` time | `O(w*h)` space - where `w` is the
# width of the matrix and `h` is the height
def transpose_matrix(matrix):
    transposed_matrix = []

    for col in range(len(matrix[0])):
        new_row = []

        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed_matrix.append(new_row)

    return transposed_matrix


matrix_1 = [
    [1, 2],
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

print(transpose_matrix(matrix_1))  # [[1], [2]]
print(transpose_matrix(matrix_2))  # [[0, 1], [0, 1], [0, 1]]
print(transpose_matrix(matrix_3))  # [[-7, 100, -33], [-7, 12, 17]]


# Big O:

"""

## Time and Space Complexity:

### Time Complexity:
- The function uses two nested loops:
  - The outer loop iterates over each column of the original matrix, which runs `len(matrix[0])` times.
  - The inner loop iterates over each row of the original matrix, which runs `len(matrix)` times.
- For each combination of row and column, the function appends an element to a new row.
- Therefore, the total number of operations is proportional to the number of elements in the matrix, which
is `len(matrix) * len(matrix[0])`.

Thus, the **time complexity** is:

    O(rows * columns)

where `rows` is the number of rows in the original matrix, and `columns` is the number of columns.

---

### Space Complexity:
- The function creates a new matrix (`transposed_matrix`) to store the result.
- The size of the transposed matrix is `len(matrix[0])` rows and `len(matrix)` columns.
- Therefore, the space required is proportional to the number of elements in the original matrix.

Thus, the **space complexity** is:

    O(rows * columns)

---

### Example Analysis:
1. For `matrix_1`:
   - Input size: 1 row × 2 columns.
   - Time complexity: O(1 * 2) = O(2).
   - Space complexity: O(2 * 1) = O(2).

2. For `matrix_2`:
   - Input size: 2 rows × 3 columns.
   - Time complexity: O(2 * 3) = O(6).
   - Space complexity: O(3 * 2) = O(6).

3. For `matrix_3`:
   - Input size: 3 rows × 2 columns.
   - Time complexity: O(3 * 2) = O(6).
   - Space complexity: O(2 * 3) = O(6).

---

### Summary:
- **Time Complexity**: O(rows * columns}).
- **Space Complexity**: O(rows * columns}).

This is optimal for transposing a matrix, as you need to process and store every element.

"""

# Code Explanation:

"""
### Code Explanation: `transpose_matrix(matrix)`

The `transpose_matrix` function takes a 2D list (matrix) as input and returns its transpose. The transpose of a matrix
is obtained by flipping the matrix over its diagonal, which means that the row and column indices of the matrix are swapped.

Here’s a step-by-step breakdown of how the function works:

---

#### 1. **Input Matrix**
The input is a 2D list (matrix) where:
- Each inner list represents a row of the matrix.
- The outer list contains all the rows.

For example:
```
matrix_1 = [
    [1, 2],
]
```
Here, `matrix_1` has 1 row and 2 columns.

---

#### 2. **Initialize the Transposed Matrix**
The function starts by initializing an empty list called `transposed_matrix`. This will eventually store the transposed matrix.

```
transposed_matrix = []
```

---

#### 3. **Iterate Over Columns**
The outer loop iterates over the columns of the input matrix. The number of columns is determined by `len(matrix[0])`,
which gives the length of the first row (assuming all rows have the same number of columns).

```
for col in range(len(matrix[0])):
```

For example:
- In `matrix_1`, there are 2 columns, so the loop runs twice (`col = 0` and `col = 1`).

---

#### 4. **Create a New Row for the Transposed Matrix**
For each column, a new row (`new_row`) is initialized. This row will eventually become a column in the transposed matrix.

```
new_row = []
```

---

#### 5. **Iterate Over Rows**
The inner loop iterates over the rows of the input matrix. The number of rows is determined by `len(matrix)`.

```
for row in range(len(matrix)):
```

For example:
- In `matrix_1`, there is 1 row, so the loop runs once (`row = 0`).

---

#### 6. **Append Elements to the New Row**
For each row, the element at the current column (`col`) is appended to `new_row`.

```
new_row.append(matrix[row][col])
```

For example:
- In `matrix_1`, when `col = 0` and `row = 0`, the element `matrix[0][0]` (which is `1`) is appended to `new_row`.
- When `col = 1` and `row = 0`, the element `matrix[0][1]` (which is `2`) is appended to `new_row`.

---

#### 7. **Add the New Row to the Transposed Matrix**
After collecting all elements for the current column, `new_row` is appended to `transposed_matrix`.

```
transposed_matrix.append(new_row)
```

For example:
- After processing `col = 0`, `new_row = [1]` is added to `transposed_matrix`.
- After processing `col = 1`, `new_row = [2]` is added to `transposed_matrix`.

---

#### 8. **Return the Transposed Matrix**
Finally, the function returns the `transposed_matrix`.

```
return transposed_matrix
```

---

### Example Walkthroughs

#### Example 1: `matrix_1`
Input:
```
matrix_1 = [
    [1, 2],
]
```
Steps:
1. Iterate over columns (`col = 0` and `col = 1`).
2. For `col = 0`, collect elements from each row: `[1]`.
3. For `col = 1`, collect elements from each row: `[2]`.
4. Combine the results: `[[1], [2]]`.

Output:
```
[[1], [2]]
```

---

#### Example 2: `matrix_2`
Input:
```
matrix_2 = [
    [0, 0, 0],
    [1, 1, 1],
]
```
Steps:
1. Iterate over columns (`col = 0`, `col = 1`, `col = 2`).
2. For `col = 0`, collect elements from each row: `[0, 1]`.
3. For `col = 1`, collect elements from each row: `[0, 1]`.
4. For `col = 2`, collect elements from each row: `[0, 1]`.
5. Combine the results: `[[0, 1], [0, 1], [0, 1]]`.

Output:
```
[[0, 1], [0, 1], [0, 1]]
```

---

#### Example 3: `matrix_3`
Input:
```
matrix_3 = [
    [-7, -7],
    [100, 12],
    [-33, 17],
]
```
Steps:
1. Iterate over columns (`col = 0` and `col = 1`).
2. For `col = 0`, collect elements from each row: `[-7, 100, -33]`.
3. For `col = 1`, collect elements from each row: `[-7, 12, 17]`.
4. Combine the results: `[[-7, 100, -33], [-7, 12, 17]]`.

Output:
```
[[-7, 100, -33], [-7, 12, 17]]
```

---

### Summary
The function works by:
1. Iterating over the columns of the input matrix.
2. For each column, collecting elements from all rows to form a new row in the transposed matrix.
3. Appending the new row to the transposed matrix.
4. Returning the final transposed matrix.

This approach ensures that the rows and columns of the input matrix are swapped correctly.

"""
