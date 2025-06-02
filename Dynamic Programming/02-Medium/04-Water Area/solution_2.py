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


# O(n) time | O(1) space
def water_area(heights):
    # Handle empty input case
    if not heights:
        return 0

    # Initialize two pointers at the start and end of the array
    left = 0
    right = len(heights) - 1

    # Track the maximum heights encountered so far from both ends
    left_max = heights[left]
    right_max = heights[right]

    # This will accumulate the total water trapped
    water = 0

    # Continue until the two pointers meet
    while left < right:
        # The side with the smaller current height determines the water trapping potential
        if heights[left] < heights[right]:
            # Move the left pointer forward
            left += 1
            # Update the left maximum if current height is greater
            left_max = max(left_max, heights[left])
            # The water trapped at this position is the difference between
            # the left maximum and current height (since right max is even larger)
            water += left_max - heights[left]
        else:
            # Move the right pointer backward
            right -= 1
            # Update the right maximum if current height is greater
            right_max = max(right_max, heights[right])
            # The water trapped at this position is the difference between
            # the right maximum and current height (since left max is even larger)
            water += right_max - heights[right]

    return water


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

## **Time Complexity Analysis**

The algorithm uses a **two-pointer approach**:
- **Initialization**: Setting `left`, `right`, `left_max`, and `right_max` takes O(1) time.
- **Main Loop**: The loop runs while `left < right`, and in each iteration, either `left` is incremented or `right` is decremented.
This means the loop runs at most O(n) times (where `n` is the length of the input array `heights`).

- **Operations Inside the Loop**:
  - Comparing `heights[left]` and `heights[right]` is O(1).
  - Updating `left_max`/`right_max` is O(1) (using `max`).
  - Calculating and adding to `water` is O(1).

Thus, the **time complexity is O(n)**, where `n` is the number of elements in `heights`.

## **Space Complexity Analysis**

The algorithm uses **constant extra space**:
- Variables: `left`, `right`, `left_max`, `right_max`, `water` (all O(1)).
- No additional data structures (like arrays or stacks) are used.

Thus, the **space complexity is O(1)**.

### **Final Answer**
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

This approach efficiently computes the trapped water in linear time without extra space.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s go through the `water_area` function in detail.

---

## **Problem: Trapping Rain Water**

You are given a list of integers called `heights`, where each integer represents the height of a vertical bar.
The goal is to compute how much **water** can be **trapped** between the bars after it rains.

---

## **Approach: Two-Pointer Technique**

The function uses a **two-pointer approach** to efficiently compute the water that can be trapped, in O(n) time and O(1) space.

---

## **Code Explanation**

```
def water_area(heights):
    if not heights:
        return 0
```

* **Base case**: If the list is empty, no water can be trapped.

---

```
    left = 0
    right = len(heights) - 1

    left_max = heights[left]
    right_max = heights[right]

    water = 0
```

* `left` and `right` are two pointers starting from **both ends** of the array.
* `left_max` keeps track of the **maximum height** seen so far from the **left**.
* `right_max` keeps track of the **maximum height** seen so far from the **right**.
* `water` accumulates the total amount of water trapped.

---

```
    while left < right:
        if heights[left] < heights[right]:
            left += 1
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
```

This loop runs until the two pointers meet.

### How it works:

1. At each step, compare `heights[left]` and `heights[right]`.
2. Whichever is **smaller**, we move that pointer inward, because **trapping water is limited by the shorter side**.
3. Update the respective `left_max` or `right_max`:

   * If current height is **less than** the max seen so far → water can be trapped.
   * The amount trapped at that index is `max_so_far - current_height`.

Example walk-through for `[0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]`:

* Between height 8 (index 1) and height 10 (index 7), there are dips (lower bars).
* Water fills up to the **minimum** of the surrounding taller bars.
* The algorithm walks from both sides and accumulates the trapped water step-by-step.

---

```
    return water
```

* Final result: total trapped water.

---

## **Test Case Analysis**

```
print(water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
# Output: 48
```

* Large bars on both sides (8 and 10), lots of dips in between → 48 units of water.

```
print(water_area([]))
# Output: 0
```

* No bars → no water trapped.

```
print(water_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# Output: 19
```

---

## **Time & Space Complexity**

* **Time:** O(n) — Each bar is visited once.
* **Space:** O(1) — Constant space used (no extra arrays).

---

Let's visualize the main test case:

```
heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
```

We'll show:

* Bars as `█`
* Water as `~`
* Empty space as a blank

---

### **Step 1: Find max height**

* The tallest bar is `10`, so we'll draw 10 levels top-down.

---

### **Step 2: Build Visualization**

```
Level 10:            █          
Level  9:            █          
Level  8:   █        █          
Level  7:   █        █          
Level  6:   █        █          
Level  5:   █   █    █          
Level  4:   █   █    █       ~  
Level  3:   █   █    █     ~ █  
Level  2:   █   █    █   ~ ~ █  
Level  1:   █   █ █  █ ~ ~ █ █  
          ----------------------
Index:     0 1 2 3 4 5 6 7 8 9 10 11 12 13
Heights:   0 8 0 0 5 0 0 10 0 0  1  1  0  3
```

### Legend:

* `█` = bar (height)
* `~` = water
* ` ` = empty space

---

### **How water is trapped**

Water collects between:

* `8` (index 1) and `10` (index 7)
* Also small pools between smaller peaks toward the end

For example:

* Between `1` and `3` at the end, water collects at index 12
* Deep pool between `8` (index 1) and `10` (index 7)

"""
