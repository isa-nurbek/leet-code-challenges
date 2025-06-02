# Problem Description:

"""
                                            Water Area

You're given an array of `non-negative` integers where each `non-zero` integer represents the height of a pillar of width `1`.
Imagine water being poured over all of the pillars; write a function that returns the surface area of the water trapped between
the pillars viewed from the front.

> Note that spilled water should be ignored.


## Sample Input:
```
heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
```

## Sample Output:
```
48

Below is a visual representation of the sample input.
The dots and vertical lines represent trapped water and pillars, respectively.
Note that there are 48 dots.
       |
       |
 |.....|
 |.....|
 |.....|
 |..|..|
 |..|..|
 |..|..|.....|
 |..|..|.....|
_|..|..|..||.|
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def water_area(heights):
    # Initialize an array to store water heights or max values
    maxes = [0 for x in heights]

    # First pass: left to right
    # Track the maximum height seen so far from the left
    left_max = 0
    for i in range(len(heights)):
        height = heights[i]
        # Store the current left max before updating it
        maxes[i] = left_max
        # Update left_max to be the maximum between current left_max and current height
        left_max = max(left_max, height)

    # Second pass: right to left
    # Track the maximum height seen so far from the right
    right_max = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        # The minimum between right_max and left_max (stored in maxes[i]) determines
        # the water level at this position
        min_height = min(right_max, maxes[i])

        # If current height is below the water level, store the water amount
        if height < min_height:
            maxes[i] = min_height - height
        else:
            # Otherwise, no water can be trapped here
            maxes[i] = 0

        # Update right_max to be the maximum between current right_max and current height
        right_max = max(right_max, height)

    # The maxes array now contains water amounts at each index
    # Return the total water trapped by summing all values
    return sum(maxes)


# Test Cases:

print(water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
# Output: 48

print(water_area([]))
# Output: 0

print(water_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# Output: 19

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `water_area` function step by step.

## **Time Complexity:**

The function consists of two main loops:
1. **First Loop (Left to Right):**  
   - Iterates through the `heights` array once to compute the left maximum for each position.
   - This loop runs in **O(n)** time, where `n` is the number of elements in `heights`.

2. **Second Loop (Right to Left):**  
   - Iterates through the `heights` array again to compute the right maximum and determine the water trapped at each position.
   - This loop also runs in **O(n)** time.

Since the loops run sequentially (not nested), the **total time complexity is O(n) + O(n) = O(n)**.

---

## **Space Complexity:**

- The function uses an auxiliary array `maxes` of the same size as `heights` to store intermediate results.
- Thus, the **space complexity is O(n)** (due to the `maxes` array).
- The rest of the variables (`left_max`, `right_max`, etc.) use constant space O(1), but they don't dominate the space complexity.

---

### **Summary:**
- **Time Complexity:** **O(n)**  
- **Space Complexity:** **O(n)**  

This is an efficient solution for the "Trapping Rain Water" problem, as it computes the result in linear time with linear extra
space. There are optimizations possible to reduce space to **O(1)**, but this implementation is clear and straightforward.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The `water_area` function calculates how much **water can be trapped** between bars after raining, based on an elevation map
represented by a list of integers (`heights`). This is a classic problem often referred to as "Trapping Rain Water".

---

### 💡 Problem Summary:

You are given a list where each element represents the height of a bar. You need to compute how much water would be trapped
between the bars after a rain.

For example:

```
[0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
```

Imagine these values as bar heights on a graph. Water can be trapped between the taller bars when there's a valley (lower height)
between them.

---

### 🔍 Step-by-Step Breakdown

```
def water_area(heights):
```

This is the main function which takes a list of integers `heights` representing the bar heights.

---

#### Step 1: Prepare an array to store max heights to the **left** of each bar

```
    maxes = [0 for x in heights]
```

Creates an array `maxes` of the same size as `heights` and initializes it with 0s. Later this will store intermediate values.

```
    left_max = 0

    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = left_max
        left_max = max(left_max, height)
```

* `left_max` keeps track of the highest bar seen so far from the **left**.
* For each position `i`, store the current `left_max` in `maxes[i]` before updating it with the current height.
* After this loop, `maxes[i]` holds the highest bar **to the left** of `i` (not including itself).

**Example** (partial):
If `heights = [0, 8, 0, 0, 5]`, `maxes` becomes:
`[0, 0, 8, 8, 8]` (left max for each position)

---

#### Step 2: Update `maxes` with the amount of water that can be trapped

```
    right_max = 0

    for i in reversed(range(len(heights))):
        height = heights[i]
        min_height = min(right_max, maxes[i])
```

* Loop through the array from **right to left**.
* `right_max` keeps track of the highest bar seen so far from the right.
* `min_height` is the minimum of the tallest bar to the **left and right** of the current bar.

```
    if height < min_height:
        maxes[i] = min_height - height
    else:
        maxes[i] = 0

    right_max = max(right_max, height)
```

* If the current bar `height` is smaller than `min_height`, water can be trapped here.
  Water trapped = `min_height - height`
* Else, set to 0 (no water trapped).
* Update `right_max`.

---

#### Step 3: Return the total water trapped

```
    return sum(maxes)
```

After this loop, `maxes` contains the amount of water trapped at each position. We return the total by summing it.

---

### ✅ Example Run:

Input:

```
water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])
```

* Visually: Water is trapped between high bars (8 and 10), with valleys in between.
* Output: `48` units of water.

---

### ⚙️ Time and Space Complexity:

* **Time Complexity:** `O(n)` – We go through the array twice.
* **Space Complexity:** `O(n)` – We use an extra array `maxes` of size `n`.

---

### 🧪 Other Test Cases

```
water_area([]) → 0
```

Empty input; nothing to trap.

```
water_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) → 19
```

Typical non-trivial case with uneven terrain.

---

Great! Here's an **ASCII visualization** of the elevation map for the input:

```python
heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
```

We'll represent:

* `█` = bar (height)
* `~` = water
* ` ` = empty space

---

### 🔎 ASCII Visualization (heights + trapped water)

```
Level 10:        █         
Level  9:        █         
Level  8:  █     █         
Level  7:  █     █         
Level  6:  █     █         
Level  5:  █ █   █         
Level  4:  █ █   █    ~    
Level  3:  █ █   █    ~   █
Level  2:  █ █   █  ~ ~   █
Level  1:  █ █ █ █  ~ ~ █ █
Level  0:  █ █ █ █  █ █ █ █
           0 1 2 3 4 5 6 7 8 9 10 11 12 13  <- indices
```

---

### 🔢 Breakdown:

* At **index 1** and **7**, we have high bars (8 and 10).
* Water collects in the valley from indices 2 to 6 and from 8 to 12.
* For example:

  * At index 2, height is 0, but it's surrounded by 8 (left) and 10 (right), so water can reach level 8.
  * Water fills up to the **minimum** of left and right max height (i.e., `min(left_max, right_max)`).

"""
