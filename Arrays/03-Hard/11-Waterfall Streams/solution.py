# Problem Description:

"""

                                            Waterfall Streams

You're given a two-dimensional array that represents the structure of an indoor waterfall and a positive integer that represents the
column that the waterfall's water source will start at. More specifically, the water source will start directly above the structure
and will flow downwards.

Each row in the array contains `0`s and 1s, where a `0` represents a free space and a `1` represents a block that water can't pass
through. You can imagine that the last row of the array contains buckets that the water will eventually flow into; thus, the last
row of the array will always contain only `0`s. You can also imagine that there are walls on both sides of the structure, meaning
that water will never leave the structure; it will either be trapped against a wall or flow into one of the buckets in the last row.

As water flows downwards, if it hits a block, it splits evenly to the left and right-hand side of that block. In other words, 50%
of the water flows left and `50%` of it flows right. If a water stream is unable to flow to the left or to the right (because of a
block or a wall), the water stream in question becomes trapped and can no longer continue to flow in that direction; it effectively
gets stuck in the structure and can no longer flow downwards, meaning that `50%` of the previous water stream is forever lost.

Lastly, the input array will always contain at least two rows and one column, and the space directly below the water source (in the
first row of the array) will always be empty, allowing the water to start flowing downwards.

Write a function that returns the percentage of water inside each of the bottom buckets after the water has flowed through the
entire structure.

You can refer to the first `4.5` minutes of this question's video explanation for a visual example.


## Sample Input
```
array = [
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0],
]
source = 3
```

## Sample Output
```
[0, 0, 0, 25, 25, 0, 0]

// The water will flow as follows:

[
    [0, 0, 0, ., 0, 0, 0],
    [1, ., ., ., ., ., 0],
    [0, ., 1, 1, 1, ., 0],
    [., ., ., ., ., ., .],
    [1, 1, 1, ., ., 1, 0],
    [0, 0, 0, ., ., 0, 1],
    [0, 0, 0, ., ., 0, 0],
]
```

## Optimal Time & Space Complexity:
```
O(w^2 * h) time | O(w) space - where `w` and `h` are the width and height of the input array.
```
"""

# =========================================================================================================================== #

# Solution:


# O(w^2 * h) time | O(w) space
def waterfall_streams(array, source):
    # Initialize the first row by making a copy of it
    # Mark the source position with -1 (representing 100% water)
    row_above = array[0][:]
    row_above[source] = -1  # Negative value represents water percentage (1 = 100%)

    # Process each subsequent row
    for row in range(1, len(array)):
        # Create a copy of the current row to modify
        current_row = array[row][:]

        # Check each position in the row above
        for idx in range(len(row_above)):
            value_above = row_above[idx]

            # Check if there's water above this position
            has_water_above = value_above < 0
            # Check if current position is a block
            has_block = current_row[idx] == 1

            # If no water above, nothing to do
            if not has_water_above:
                continue

            # If current position isn't a block, water falls straight down
            if not has_block:
                current_row[idx] += value_above
                continue

            # If we reach here, water hits a block and needs to split
            split_water = value_above / 2  # Divide water equally to both sides

            # First, try to move water to the right
            right_idx = idx
            while right_idx + 1 < len(row_above):
                right_idx += 1

                # If we hit a block in the row above while moving right, stop
                if row_above[right_idx] == 1:
                    break

                # If we find an empty space in current row, deposit the split water
                if current_row[right_idx] != 1:
                    current_row[right_idx] += split_water
                    break

            # Then, try to move water to the left
            left_idx = idx
            while left_idx - 1 >= 0:
                left_idx -= 1

                # If we hit a block in the row above while moving left, stop
                if row_above[left_idx] == 1:
                    break

                # If we find an empty space in current row, deposit the split water
                if current_row[left_idx] != 1:
                    current_row[left_idx] += split_water
                    break

        # The current row becomes the row above for the next iteration
        row_above = current_row

    # Convert the negative percentages to positive values
    # Multiply by -100 to convert from decimal (-0.5 → 50)
    final_percentages = list(map(lambda num: num * -100, row_above))

    return final_percentages


# Test Cases:

array = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]
source = 3

print(waterfall_streams(array, source))

# Output: [0, 0, 0, 25.0, 25.0, 0, 0]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity:**

1. **Initial Setup:**
   - Copying the first row: `O(m)`, where `m` is the number of columns.
   
2. **Outer Loop:**
   - Iterates over each row (from the second row to the last row): `O(n)`, where `n` is the number of rows.
   
3. **Inner Loop:**
   - For each row, it iterates over each column: `O(m)`.
   - For each column with water above (`value_above < 0`) and a block (`current_row[idx] == 1`), it splits the water and spreads
   it to the left and right:
     - In the worst case, spreading water to the left or right could take `O(m)` time (e.g., if the water spreads all the way
     to the end of the row).
   
   - Thus, the worst-case time for the inner loop is `O(m^2)` per row (due to nested loops for spreading).

4. **Total Time Complexity:**
   - Since we have `n` rows and for each row, the worst-case time is `O(m^2)`, the total time complexity is: O(n * m^2)
   - This assumes that in the worst case, for every block, the water spreads all the way to the ends of the row.

### **Space Complexity:**

1. **Row Copies:**
   - The function maintains a copy of the previous row (`row_above`) and the current row (`current_row`),
   each of size `m`: `O(m)` space.
   
2. **Final Output:**
   - The `final_percentages` array is of size `m`, but this is part of the output and doesn't count toward auxiliary space.

3. **Total Space Complexity:**
   - The dominant space usage is the two row copies, so the space complexity is: O(m)
   - This is because we only keep track of the previous and current rows at any given time, not the entire matrix.

### **Summary:**
- **Time Complexity:**  O(n * m^2) 
- **Space Complexity:**  O(m) 

"""

"""
The `waterfall_streams` function simulates the flow of water dropped onto a 2D grid from a specific **source column** in the **top row**. The water flows downward unless blocked, and when it hits an obstacle (`1` in the grid), it tries to flow **left and right**. The goal is to calculate **what percentage of water ends up in each column at the bottom row**.

---

### 🧱 **Input Grid:**

Each cell in the grid can be:

* `0` – an open cell where water can flow.
* `1` – a block that stops water.

---

### ✅ **High-Level Steps:**

1. **Initialize the first row** with `-1` at the `source` column, representing 100% water (negative numbers track water flow).
2. **Iterate row by row** simulating the water flowing down.
3. At each cell:

   * If it has water from above and no block below, continue flowing straight down.
   * If there's a block below, try to split the water:

     * Move right until you find an open cell (not blocked above or in the current row), or stop at a block.
     * Move left similarly.
4. After processing all rows, **convert the final water values into percentages** by multiplying by `-100`.

---

### 🔍 **Detailed Line-by-Line Explanation:**

```python
def waterfall_streams(array, source):
    row_above = array[0][:]
    row_above[source] = -1  # Start with -1 (100%) water at the source column
```

* `row_above` stores water values from the row above the current one.
* `-1` means 100% of water is at the source column.

---

```python
    for row in range(1, len(array)):
        current_row = array[row][:]
```

* Iterate through each row starting from the second one.
* Copy the current row to avoid mutating the original grid.

---

```python
        for idx in range(len(row_above)):
            value_above = row_above[idx]

            has_water_above = value_above < 0
            has_block = current_row[idx] == 1
```

* Check each column.
* `value_above` is water amount from the previous row (negative = water present).
* Check if there's a block below the water source.

---

```python
            if not has_water_above:
                continue
```

* Skip if there's no water above.

---

```python
            if not has_block:
                current_row[idx] += value_above
                continue
```

* If there's no block, allow water to fall straight down.

---

### 🔀 **Water Split Logic**

```python
            split_water = value_above / 2
```

* If there is a block below, water splits 50/50 to left and right.

---

```python
            right_idx = idx
            while right_idx + 1 < len(row_above):
                right_idx += 1

                if row_above[right_idx] == 1:
                    break

                if current_row[right_idx] != 1:
                    current_row[right_idx] += split_water
                    break
```

* Try to find a path to the right for water to flow.
* Stop if blocked (`1` in row above), or pour into the first open space.

---

```python
            left_idx = idx
            while left_idx - 1 >= 0:
                left_idx -= 1

                if row_above[left_idx] == 1:
                    break

                if current_row[left_idx] != 1:
                    current_row[left_idx] += split_water
                    break
```

* Same as above, but to the left.

---

```python
        row_above = current_row
```

* After processing current row, make it the new "row above" for the next iteration.

---

### 🧮 **Final Conversion to Percentages:**

```python
    final_percentages = list(map(lambda num: num * -100, row_above))
    return final_percentages
```

* Convert water amounts to positive percentages.
* Cells that never got water remain `0`.

---

### 📊 Test Case Breakdown:

```python
array = [
    [0, 0, 0, 0, 0, 0, 0],  # water starts at column 3
    [1, 0, 0, 0, 0, 0, 0],  # block at column 0
    [0, 0, 1, 1, 1, 0, 0],  # vertical wall in the middle
    [0, 0, 0, 0, 0, 0, 0],  # open
    [1, 1, 1, 0, 0, 1, 0],  # split paths
    [0, 0, 0, 0, 0, 0, 1],  # right side blocked at the end
    [0, 0, 0, 0, 0, 0, 0],
]
source = 3
```

* Water drops at column 3.
* Hits wall at row 2, splits into 2 paths around the wall.
* Eventually, water reaches columns 3 and 4, each with 25%.

**Output:**

```python
[0, 0, 0, 25.0, 25.0, 0, 0]
```

---

Here's an **ASCII visualization** of how the `waterfall_streams` function simulates water flow through the given grid. I’ll show:

* `⬇` – where water flows straight down
* `↙` / `↘` – where water splits and moves left or right
* `█` – a block (`1`)
* `.` – empty space (`0`)
* `%` – where water accumulates in the final row
* `S` – source (start point of water)

---

### 🧩 Grid Layout with Flow:

```plaintext
Row 0:   .   .   .   S   .   .   .
Row 1:   █   .   .   ⬇   .   .   .
Row 2:   .   .   █   █   █   .   .
Row 3:   .   .  ↙.   .   .↘  .   .
Row 4:   █   █   █   ⬇   ⬇   █   .
Row 5:   .   .   .   ⬇   ⬇   .   █
Row 6:   %   .   .  25% 25%  .   .
```

---

### 🔍 Breakdown of the Flow:

* **Row 0:** Water starts at column 3 (`S`)
* **Row 1:** Water flows straight down to column 3 (`⬇`)
* **Row 2:** Hits blocks in columns 2, 3, 4 → water cannot continue straight
* **Row 3:** Water splits: left (to col 2, but blocked) and right (to col 4)
* **Row 4–6:** Water continues straight down where possible
* **Row 6:** 25% water ends in both columns 3 and 4

---

"""
