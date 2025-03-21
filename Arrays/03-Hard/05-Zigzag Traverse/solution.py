# Problem Description:

"""

                                                # Zigzag Traverse

Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a one-dimensional
array of all the array's elements in zigzag order.

Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element, and proceeds in a zigzag pattern
all the way to the bottom right corner.


## Sample Input:
```
array = [
  [1,  3,  4, 10],
  [2,  5,  9, 11],
  [6,  8, 12, 15],
  [7, 13, 14, 16],
]
```

## Sample Output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the total number of elements in the two-dimensional array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def zigzag_traverse(array):
    # Determine the height and width of the 2D array
    height = len(array) - 1  # Last row index
    width = len(array[0]) - 1  # Last column index

    # Initialize an empty list to store the result of the traversal
    result = []

    # Start from the top-left corner of the array (first element)
    row, col = 0, 0

    # A flag to indicate the direction of traversal:
    # `going_down = True` means we're moving diagonally down,
    # `going_down = False` means we're moving diagonally up.
    going_down = True

    # Loop until we go out of bounds (i.e., traverse the entire array)
    while not is_out_of_bounds(row, col, height, width):
        # Append the current element to the result list
        result.append(array[row][col])

        # If we're moving diagonally down
        if going_down:
            # Check if we've hit the left wall or the bottom row
            if col == 0 or row == height:
                # Change direction to move diagonally up
                going_down = False

                # If we're at the bottom row, move right
                if row == height:
                    col += 1
                # Otherwise, move down
                else:
                    row += 1
            else:
                # Move diagonally down-left
                row += 1
                col -= 1
        # If we're moving diagonally up
        else:
            # Check if we've hit the top row or the right wall
            if row == 0 or col == width:
                # Change direction to move diagonally down
                going_down = True

                # If we're at the right wall, move down
                if col == width:
                    row += 1
                # Otherwise, move right
                else:
                    col += 1
            else:
                # Move diagonally up-right
                row -= 1
                col += 1

    # Return the result of the zigzag traversal
    return result


# Helper function to check if the current position is out of bounds
def is_out_of_bounds(row, col, height, width):
    # Ensures `(row, col)` stays within the matrix.
    return row < 0 or row > height or col < 0 or col > width


# Test Cases:

array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16],
]

array_2 = [[1, 2, 3, 4, 5]]

array_3 = [[1]]


print(zigzag_traverse(array))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(zigzag_traverse(array_2))
# Output: [1, 2, 3, 4, 5]

print(zigzag_traverse(array_3))
# Output: [1]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `zigzag_traverse` function is determined by the number of elements in the 2D array.

Let's break it down:

- The 2D array has `n` rows and `m` columns, so the total number of elements is `n * m`.
- The `while` loop runs until all elements are traversed, which means it will iterate exactly `n * m` times.
- Inside the loop, each operation (appending to the result list, checking conditions, updating indices) takes constant time `O(1)`.

Thus, the **time complexity** of the algorithm is:

    O(n * m)

where `n` is the number of rows and `m` is the number of columns in the 2D array.

---

### Space Complexity Analysis

The space complexity is determined by the additional space used by the algorithm, excluding the input space:

1. **Result List**:
   - The `result` list stores all `n * m` elements of the 2D array.
   - This contributes `O(n * m)` space.

2. **Variables**:
   - The variables `row`, `col`, `height`, `width`, and `going_down` use constant space `O(1)`.

Thus, the **space complexity** of the algorithm is:

    O(n * m)

due to the space required for the `result` list.

---

### Summary

- **Time Complexity**: O(n * m)
- **Space Complexity**: O(n * m)

This is optimal for this problem since you need to visit every element in the 2D array at least once, and you need
to store all the elements in the result list.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of Zigzag Traversal Code**

This function traverses a 2D array in a **zigzag** fashion. That means it alternates between moving **down-left** and
**up-right** to visit all elements.

---

### **Understanding the Code Step-by-Step**

#### **1. Initialize Variables**
```
height = len(array) - 1
width = len(array[0]) - 1
```
- `height` is the last row index (`number of rows - 1`).
- `width` is the last column index (`number of columns - 1`).

```
result = []
row, col = 0, 0
going_down = True
```
- `result` stores the traversal order.
- `(row, col)` starts at `(0,0)`, the **top-left** corner.
- `going_down = True` means the first move is **down-left**.

---

#### **2. Main Loop: Traverse Until Out of Bounds**
```
while not is_out_of_bounds(row, col, height, width):
```
- The loop runs until `(row, col)` goes outside the matrix.

```
result.append(array[row][col])
```
- The current element is added to `result`.

---

#### **3. Moving in Zigzag Pattern**

- **Going Down (`going_down == True`)**
  - Move **down-left** `(row + 1, col - 1)`.
  - If at the **bottom** or **left boundary**, switch direction to **up-right**.
    ```
    if col == 0 or row == height:
        going_down = False

        if row == height:
            col += 1  # Move right if at the last row
        else:
            row += 1  # Move down if at the first column
    ```
  - Otherwise, continue **down-left**:
    ```
    else:
        row += 1
        col -= 1
    ```

- **Going Up (`going_down == False`)**

  - Move **up-right** `(row - 1, col + 1)`.
  - If at the **top** or **right boundary**, switch direction to **down-left**.
    ```
    if row == 0 or col == width:
        going_down = True

        if col == width:
            row += 1  # Move down if at the last column
        else:
            col += 1  # Move right if at the first row
    ```
  - Otherwise, continue **up-right**:
    ```
    else:
        row -= 1
        col += 1
    ```

---

#### **4. Out of Bounds Check**
```
def is_out_of_bounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width
```
- Ensures `(row, col)` stays within the matrix.

---

### **How It Works on Example Inputs**

#### **Example 1**
```
array = [
    [1,  3,  4, 10],
    [2,  5,  9, 11],
    [6,  8, 12, 15],
    [7, 13, 14, 16],
]
```
**Zigzag Traversal Steps:**
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15 → 16

**Output:**  
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

---

#### **Example 2**
```
array_2 = [[1, 2, 3, 4, 5]]
```
- The array is a **single row**, so traversal moves right.

**Output:**  
```
[1, 2, 3, 4, 5]
```

---

#### **Example 3**
```
array_3 = [[1]]
```
- The array has **one element**.
**Output:**  
```
[1]
```

---

### **Summary**
- Moves **down-left** until hitting a boundary.
- Then moves **up-right** until hitting a boundary.
- Continues alternating until all elements are visited.
- Works efficiently in **O(N) time** where `N` is the number of elements.

"""
