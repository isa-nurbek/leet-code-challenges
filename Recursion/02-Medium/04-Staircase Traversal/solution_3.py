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


# O(n * k) time | O(n) space
def staircase_traversal(height, max_steps):
    """
    Calculates the number of ways to climb a staircase of given height
    where you can take 1 to max_steps at each move.

    Args:
        height: The total number of steps in the staircase (int)
        max_steps: The maximum number of steps that can be taken at once (int)

    Returns:
        The number of distinct ways to reach the top (int)
    """

    # Initialize a dynamic programming array to store ways to reach each step
    # ways_to_top[i] will store the number of ways to reach step i
    ways_to_top = [0 for _ in range(height + 1)]

    # Base cases:
    # There's 1 way to stay at ground level (do nothing)
    ways_to_top[0] = 1
    # There's only 1 way to reach step 1 (single step of 1)
    ways_to_top[1] = 1

    # Build up the solution from bottom to top
    for current_height in range(2, height + 1):
        step = 1  # Represents the step size we're considering (1 to max_steps)

        # For each possible step size up to max_steps or current_height
        while step <= max_steps and step <= current_height:
            # The ways to reach current_height is the sum of ways to reach
            # (current_height - step) for all valid step sizes
            ways_to_top[current_height] = (
                ways_to_top[current_height] + ways_to_top[current_height - step]
            )
            step += 1

    # The answer is stored in ways_to_top[height]
    return ways_to_top[height]


# Test Cases:

print(staircase_traversal(4, 2))  #  Output: 5
print(staircase_traversal(10, 1))  #  Output: 1
print(staircase_traversal(6, 3))  #  Output: 24

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis


### **Space Complexity**
- The function uses an array `ways_to_top` of size `height + 1` to store intermediate results.
- Thus, the **space complexity is `O(height)`**, as the space grows linearly with the input `height`.

### **Time Complexity**
1. The outer loop runs from `2` to `height`, so it iterates `O(height)` times.
2. The inner `while` loop runs up to `max_steps` times for each iteration of the outer loop.
   - In the worst case, `max_steps` could be as large as `height`, making this loop `O(max_steps)` per iteration.
   - However, if `max_steps` is small compared to `height`, this reduces the time complexity.

Thus, the **time complexity is `O(height * max_steps)`**, since for each step in `height`, we perform up to `max_steps` operations.

### **Optimization Consideration (Sliding Window Approach)**
The current approach uses a dynamic programming (DP) method with nested loops. However, this can be optimized further using a
**sliding window technique** to reduce the time complexity to `O(height)` while keeping space complexity at `O(height)`
(or even `O(max_steps)` with further optimization).

### **Final Complexity Analysis**

| Aspect           | Complexity               |
|------------------|--------------------------|
| **Time**         | `O(height * max_steps)`  |
| **Space**        | `O(height)`              |

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function `staircase_traversal(height, max_steps)` calculates the **number of distinct ways** you can climb a staircase of
a given `height` when you are allowed to take up to `max_steps` at a time (e.g., 1 step, 2 steps, ..., up to `max_steps`).

Let’s break it down **step by step**:

---

### ✅ **1. Problem Statement:**
You are standing at the bottom of a staircase with `height` steps. You can climb **up to `max_steps` steps at a time**.
How many **distinct ways** are there to reach the top?

For example:
- If `height = 4` and `max_steps = 2`, then you can climb in ways like:
  - 1+1+1+1  
  - 1+1+2  
  - 1+2+1  
  - 2+1+1  
  - 2+2  
  => **5 total ways**

---

### ✅ **2. Code Walkthrough:**

```
ways_to_top = [0 for _ in range(height + 1)]
```
- Create a list to store the number of ways to reach each step.
- `ways_to_top[i]` = number of ways to reach step `i`.

```
ways_to_top[0] = 1
ways_to_top[1] = 1
```
- Base cases:
  - 1 way to stay at step 0 (do nothing).
  - 1 way to reach step 1 (1 step).

> These are **initial seeds** for the bottom-up dynamic programming approach.

---

### ✅ **3. Main DP Logic:**

```
for current_height in range(2, height + 1):
```
- Start from step 2 and go up to the target `height`.

```
step = 1
while step <= max_steps and step <= current_height:
    ways_to_top[current_height] += ways_to_top[current_height - step]
    step += 1
```
- For each `current_height`, you check how you could get there from up to `max_steps` previous steps.
- For example:
  - To reach height 4, you could have come from:
    - height 3 (if you took 1 step)
    - height 2 (if you took 2 steps)
  - So the number of ways to reach 4:
    ```python
    ways_to_top[4] = ways_to_top[3] + ways_to_top[2]
    ```

This is classic **bottom-up dynamic programming** where the value of a state depends on previous states.

---

### ✅ **4. Return the Final Answer:**

```
return ways_to_top[height]
```
- Return the number of ways to reach the top step.

---

### ✅ **Test Case Breakdown:**

```
print(staircase_traversal(4, 2))  # Output: 5
```
- 5 ways to climb 4 steps using up to 2 steps at a time.

```
print(staircase_traversal(10, 1))  # Output: 1
```
- Only 1 way to climb 10 steps using only 1 step at a time.

```
print(staircase_traversal(6, 3))  # Output: 24
```
- 24 ways to reach step 6 using 1, 2, or 3 steps at a time.

---

Let's break down the `staircase_traversal(6, 3)` example — where `height = 6` and `max_steps = 3` — and show **why there are
24 ways** to reach the top.

### 🎯 Goal:
Climb 6 steps using any combination of 1, 2, or 3 steps.

This is a variation of the **“staircase problem”** using **dynamic programming** to avoid recomputation, but for understanding,
let’s enumerate all the possible **combinations** manually.

---

### 🧠 Strategy:
We’re finding all sequences of steps that **sum up to 6**, where each step is either `1`, `2`, or `3`.

---

### ✅ All Valid Step Sequences:

We’ll group by the **number of total steps in each path** (this affects the number of permutations):

#### 1. Using six 1’s:  
- `1 + 1 + 1 + 1 + 1 + 1` → 1 way

#### 2. Using three 2’s:
- `2 + 2 + 2` → 1 way

#### 3. Using two 3’s:
- `3 + 3` → 1 way

---

Now let’s explore **mixed combinations**, and count all **unique permutations** for each type.

---

#### A. Combinations of 1’s and 2’s:

Let’s say:
- 2 twos (2 + 2 = 4), rest with 1’s (2)
  - Sequence = [2, 2, 1, 1]  
  - Count of permutations = `4! / (2! * 2!) = 6`

- 1 two (2), rest with 1’s (4)  
  - Sequence = [2, 1, 1, 1, 1]  
  - Permutations = `5! / (1! * 4!) = 5`

---

#### B. Combinations of 1’s and 3’s:

- 1 three (3), rest 1’s (3)  
  - [3, 1, 1, 1]  
  - Permutations = `4! / (1! * 3!) = 4`

- 1 three (3), 1 two (2), 1 one (1)  
  - [3, 2, 1]  
  - Permutations = `3! = 6`

---

#### C. Combinations of 2’s and 3’s:

- 1 three (3), 1 two (2), 1 one (1) — already counted above.

- 2 twos (4) + 1 three (not possible, 4 + 3 = 7 > 6) ❌

---

#### D. Using all three: (3, 2, 1)
- Already counted: [3, 2, 1] → permutations = `3! = 6`

---

#### E. Using two 3’s:
- Already counted: [3, 3] → 1 way

---

### ✅ Total Breakdown:

| Sequence Type         | Count |
|-----------------------|-------|
| [1,1,1,1,1,1]         | 1     |
| [2,2,2]               | 1     |
| [3,3]                 | 1     |
| [2,2,1,1]             | 6     |
| [2,1,1,1,1]           | 5     |
| [3,1,1,1]             | 4     |
| [3,2,1]               | 6     |

---

### ✅ Total Ways = **1 + 1 + 1 + 6 + 5 + 4 + 6 = 24**

---

So, the function `staircase_traversal(6, 3)` returns **24** because there are 24 unique ways to climb 6 steps taking 1–3 steps
at a time.

"""
