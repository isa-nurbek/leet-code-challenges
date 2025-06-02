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
