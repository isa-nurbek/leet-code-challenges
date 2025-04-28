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
1, 1, 1, 1
1, 1, 2
1, 2, 1
2, 1, 1
2, 2
```

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the height of the staircase.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n * k) time | O(n) space
def staircase_traversal(height, max_steps):
    """Main function to calculate number of ways to climb a staircase.

    Args:
        height: Total number of steps in the staircase
        max_steps: Maximum number of steps you can climb at once

    Returns:
        Number of distinct ways to reach the top
    """
    # Initialize memoization dictionary with base cases:
    # - 0 steps: 1 way (doing nothing)
    # - 1 step: 1 way (single step)
    return number_of_ways_to_top(height, max_steps, {0: 1, 1: 1})


def number_of_ways_to_top(height, max_steps, memoize):
    """Recursive helper function with memoization to calculate ways to climb.

    Args:
        height: Remaining steps to climb
        max_steps: Maximum steps allowed per move
        memoize: Dictionary to store already computed results

    Returns:
        Number of ways to climb remaining 'height' steps
    """
    # If we've already computed this height before, return stored value
    if height in memoize:
        return memoize[height]

    number_of_ways = 0

    # Consider all possible step sizes we could take next (from 1 to max_steps)
    # We use min(max_steps, height) to avoid steps larger than remaining height
    for step in range(1, min(max_steps, height) + 1):
        # Recursively calculate ways from the new height after taking this step
        number_of_ways += number_of_ways_to_top(height - step, max_steps, memoize)

    # Store the computed value for this height to avoid recomputation later
    memoize[height] = number_of_ways

    return number_of_ways


# Test Cases:

print(staircase_traversal(4, 2))  #  Output: 5
print(staircase_traversal(10, 1))  #  Output: 1
print(staircase_traversal(6, 3))  #  Output: 24

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

Let's analyze the time and space complexity of the given `staircase_traversal` function, which uses memoization to compute
the number of ways to climb a staircase of height `height` with a maximum step size of `max_steps`.

### **Time Complexity:**

1. **Recursive Calls with Memoization:**
   - The function `number_of_ways_to_top` is called recursively for each step from 1 to `min(max_steps, height)`.
   - However, with memoization, each subproblem (i.e., each unique `height`) is computed only once.
   - For each `height`, the function performs `O(max_steps)` work (since the loop runs up to `max_steps` times).

2. **Total Subproblems:**
   - There are `O(height)` unique subproblems (since `height` can range from 0 to the input `height`).

3. **Overall Time Complexity:**
   - Since each of the `O(height)` subproblems is solved in `O(max_steps)` time, the total time complexity is:

        O(height * max_steps)


### **Space Complexity:**

1. **Memoization Dictionary:**
   - The memoization dictionary stores results for all `height` values from 0 up to the input `height`, so it uses `O(height)` space.

2. **Recursion Call Stack:**
   - In the worst case, the recursion can go as deep as `height` (e.g., when `max_steps = 1`, the recursion depth is `height`).
   - Thus, the call stack also uses `O(height)` space.

3. **Overall Space Complexity:**
   - The total space complexity is the sum of the memoization dictionary and the call stack:

        O(height) + O(height) = O(height)


### **Summary:**
- **Time Complexity:** O(height * max_steps)
- **Space Complexity:** O(height)

### **Note:**
- If `max_steps` is very large (e.g., `max_steps >= height`), the time complexity simplifies to O(height^2), since
the loop runs up to `height` times for each subproblem.
- The space complexity is dominated by the memoization storage and the recursion depth, both of which are linear in `height`.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break this down step by step to understand how the **`staircase_traversal`** function works and what it's doing under the hood.

---

### 🔧 **Problem Statement**

You are given:
- `height`: the total number of stairs.
- `max_steps`: the maximum number of stairs you can climb at once.

You need to **count the number of distinct ways** to reach the top (i.e., the `height`-th step), starting from the ground 
(step 0), if you can climb up to `max_steps` at a time.

---

### 🧠 **Intuition**

This is a classic **Dynamic Programming** (DP) problem. It's similar to the **"ways to climb stairs"** problem. At any stair `n`,
the number of ways to reach it is the sum of the number of ways to reach all stairs from `n - 1` down to `n - max_steps`.

---

### 🧩 **Code Breakdown**

#### 🔹 Main Function: `staircase_traversal(height, max_steps)`

```
def staircase_traversal(height, max_steps):
    return number_of_ways_to_top(height, max_steps, {0: 1, 1: 1})
```

- This function is just a wrapper.
- It calls the recursive helper `number_of_ways_to_top()`.
- It initializes a **memoization dictionary** (`memoize`) with base cases:
  - `{0: 1}` → There is 1 way to stay at the ground (by doing nothing).
  - `{1: 1}` → There is 1 way to reach the first step (1 step at a time).

#### 🔹 Helper Function: `number_of_ways_to_top(height, max_steps, memoize)`

```
def number_of_ways_to_top(height, max_steps, memoize):
    if height in memoize:
        return memoize[height]
```

- If the result for a specific `height` is already computed and stored in `memoize`, we return it directly (avoids re-computation).

```
number_of_ways = 0
for step in range(1, min(max_steps, height) + 1):
    number_of_ways += number_of_ways_to_top(height - step, max_steps, memoize)
```

- We try **all possible steps** from 1 to `max_steps`.
- For each step size, we recursively calculate the number of ways to reach `(height - step)`.
- We sum these up to get the total number of ways to reach the current `height`.

```
memoize[height] = number_of_ways
return number_of_ways
```

- We **store** the result in `memoize` for future lookups.
- Then we return the total number of ways to reach the given `height`.

---

### ✅ **Example: `staircase_traversal(4, 2)`**

You're at the bottom and need to reach step 4, taking up to 2 steps at a time.

Let’s manually enumerate:
- 1-1-1-1  
- 1-1-2  
- 1-2-1  
- 2-1-1  
- 2-2  

There are **5 ways**, which matches the output.

---

### 🔬 Test Case Outputs Recap

```
print(staircase_traversal(4, 2))   # Output: 5
print(staircase_traversal(10, 1))  # Output: 1
print(staircase_traversal(6, 3))   # Output: 24
```

- `10, 1` → Only one way: take 1 step 10 times.
- `6, 3` → Multiple combinations using steps of 1, 2, and 3. Total = 24.

"""
