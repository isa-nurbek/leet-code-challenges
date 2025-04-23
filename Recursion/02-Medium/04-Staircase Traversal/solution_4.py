# Problem Description:

"""

                                          Staircase Traversal

You're given two positive integers representing the height of a staircase and the maximum number of steps that you can
advance up the staircase at a time. Write a function that returns the number of ways in which you can climb the staircase.

For example, if you were given a staircase of `height = 3` and `max_steps = 2` you could climb the staircase in 3 ways. You
could take **1 step, 1 step, then 1 step**, you could also take **1 step, then 2 steps**, and you could take **2 steps,
then 1 step**.

> Note that `max_steps <= height` will always be true.


## Sample Input
```
height = 4
max_steps = 2
```

## Sample Output
```
5
// You can climb the staircase in the following ways:
// 1, 1, 1, 1
// 1, 1, 2
// 1, 2, 1
// 2, 1, 1
// 2, 2
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the height of the staircase.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space
def staircase_traversal(height, max_steps):
    # Base cases:
    # If height is 0 or 1, there's exactly 1 way to traverse (do nothing or take one step)
    if height == 0 or height == 1:
        return 1
    # If max_steps is 1, the only way is to take 1 step each time (only one possible way)
    if max_steps == 1:
        return 1

    # Initialize a dynamic programming array to store number of ways to reach each height
    # ways_to_top[i] will store the number of ways to reach height i
    ways_to_top = [0] * (height + 1)

    # There's 1 way to be at height 0 (base case)
    ways_to_top[0] = 1

    # This will maintain the sum of the previous max_steps elements in the ways_to_top array
    window_sum = 0

    # Calculate the number of ways for each height from 1 to the target height
    for current_height in range(1, height + 1):
        # The start of our sliding window (the element to remove from window_sum)
        start_of_window = current_height - max_steps - 1

        # The end of our sliding window (the element to add to window_sum)
        end_of_window = current_height - 1

        # If the start of window is valid (>= 0), remove that element from our window sum
        # This maintains that our window only considers the last max_steps elements
        if start_of_window >= 0:
            window_sum -= ways_to_top[start_of_window]

        # Add the new element (just before current_height) to our window sum
        window_sum += ways_to_top[end_of_window]

        # The number of ways to reach current_height is the sum of ways to reach
        # the previous max_steps heights (sliding window sum)
        ways_to_top[current_height] = window_sum

    # Return the number of ways to reach the target height
    return ways_to_top[height]


# Test Cases:

print(staircase_traversal(4, 2))  #  Output: 5
print(staircase_traversal(10, 1))  #  Output: 1
print(staircase_traversal(6, 3))  #  Output: 24

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity:**

1. **Initialization:** The array `ways_to_top` is initialized with size `height + 1`, which takes **O(height)** time.
2. **Loop:** The main loop runs from `current_height = 1` to `current_height = height`, so it iterates **O(height)** times.
   - Inside the loop:
     - The operations (`start_of_window` calculation, `window_sum` updates, and array assignment) are all **O(1)** per iteration.
3. **Overall:** The loop dominates the time complexity, so the total time complexity is **O(height)**.


### **Space Complexity:**

1. The `ways_to_top` array takes **O(height)** space.
2. The other variables (`window_sum`, `current_height`, `start_of_window`, `end_of_window`) use **O(1)** space.
3. **Overall:** The space complexity is **O(height)** due to the array.

### **Optimization Insight:**

The algorithm uses a **sliding window** approach to compute the number of ways to reach each step by maintaining a running sum
(`window_sum`) of the previous `max_steps` values. This avoids the need for a nested loop (which would happen in a naive dynamic
programming approach), thus improving time complexity from **O(height × max_steps)** to **O(height)** while keeping space
at **O(height)**.

### **Final Answer:**

- **Time Complexity:** **O(height)**
- **Space Complexity:** **O(height)** (can be optimized to **O(max_steps)** if we only keep a sliding window of the
last `max_steps` values instead of the entire array).  

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### 🧠 **Conceptual Overview**

You are asked to find how many different ways you can reach the **top of a staircase** with `height` steps, given that
**you can climb up to `max_steps` steps at a time**.

For example:
- If `height = 4` and `max_steps = 2`, it means at each step, you can either take 1 or 2 steps.
- You want to count how many distinct combinations of steps will get you from step 0 (ground) to step `height`.

This is a variation of the **staircase problem**, optimized with **dynamic programming and a sliding window** to reduce
time complexity.

---

### 🧮 **High-Level Idea**

Let’s define:
- `ways_to_top[i]`: number of ways to reach step `i`.

You can get to step `i` from:
- step `i-1` with a 1-step move
- step `i-2` with a 2-step move
- ...
- step `i-k` with a `k`-step move (where `k <= max_steps` and `i-k >= 0`)

So:
```
ways_to_top[i] = ways_to_top[i-1] + ways_to_top[i-2] + ... + ways_to_top[i-max_steps]
```

Instead of recalculating the sum every time, we **maintain a sliding window** of this sum to make it efficient.

---

### 🔍 **Code Breakdown**

```
def staircase_traversal(height, max_steps):
    if height == 0 or height == 1:
        return 1
    if max_steps == 1:
        return 1
```
- **Base cases**:
  - If the height is 0 or 1, there's only one way to reach the top (stand still or take one step).
  - If `max_steps == 1`, you can only climb one step at a time — only one way exists (1 + 1 + 1...).

---

```
ways_to_top = [0] * (height + 1)
ways_to_top[0] = 1
```
- Create an array `ways_to_top` to store the number of ways to reach each step.
- `ways_to_top[0] = 1`: there's 1 way to be at the bottom (step 0) — do nothing.

---

```
window_sum = 0
```
- This variable will keep the rolling sum of the last `max_steps` values from the array.

---

```
for current_height in range(1, height + 1):
    start_of_window = current_height - max_steps - 1
    end_of_window = current_height - 1
```
- We iterate over each step from 1 to `height`.
- `start_of_window`: the index that just slid out of the window.
- `end_of_window`: the most recent index that slides into the window.

---

```
if start_of_window >= 0:
    window_sum -= ways_to_top[start_of_window]
```
- If the window has grown beyond `max_steps`, subtract the value that falls out of the window.

---

```
window_sum += ways_to_top[end_of_window]
ways_to_top[current_height] = window_sum
```
- Add the new value to the rolling sum.
- Set the current number of ways based on the rolling sum.

---

```
return ways_to_top[height]
```
- Return the total ways to reach the top of the staircase.

---

### 🧪 **Test Cases Walkthrough**

#### `staircase_traversal(4, 2)`
Means: You can take either 1 or 2 steps, and you want to reach step 4.

All combinations:
- 1+1+1+1
- 1+1+2
- 1+2+1
- 2+1+1
- 2+2  
✅ Total: **5**

---

#### `staircase_traversal(10, 1)`
Only 1 step at a time → there's only one way (1+1+1... repeated 10 times)  
✅ Output: **1**

---

#### `staircase_traversal(6, 3)`
Means: Take 1, 2, or 3 steps at a time.

This will have multiple combinations like:
- 1+1+1+1+1+1
- 1+2+3
- 3+3
- 2+2+2
... and many more  
✅ Output: **24**

---

### ⚡️ Time and Space Complexity

- **Time Complexity**: O(n), where `n = height`
- **Space Complexity**: O(n) for the `ways_to_top` array

"""
