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
