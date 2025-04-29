# Problem Description:

"""

                                            Ambiguous Measurements

This problem deals with measuring cups that are missing important measuring labels. Specifically, a measuring cup only has two
measuring lines, a Low (L) line and a High (H) line. This means that these cups can't precisely measure and can only guarantee that
the substance poured into them will be between the L and H line. For example, you might have a measuring cup that has a Low line at
`400ml` and a high line at `435ml`. This means that when you use this measuring cup, you can only be sure that what you're measuring
is between `400ml` and `435ml`.

You're given a list of measuring cups containing their low and high lines as well as one `low` integer and one `high` integer
representing a range for a target measurement. Write a function that returns a boolean representing whether you can use the cups
to accurately measure a volume in the specified `[low, high]` range (the range is inclusive).

> Note that:

- Each measuring cup will be represented by a pair of positive integers `[L, H]`, where `0 <= L <= H`.
- You'll always be given at least one measuring cup, and the `low` and `high` input parameters will always satisfy the following
constraint: `0 <= low <= high`.
- Once you've measured some liquid, it will immediately be transferred to a larger bowl that will eventually (possibly) contain the
target measurement.
- You can't pour the contents of one measuring cup into another cup.


## Sample Input
```
measuring_cups = [
  [200, 210],
  [450, 465],
  [800, 850],
]

low = 2100
high = 2300
```

## Sample Output
```
True


// We use cup [450, 465] to measure four volumes:
// First measurement: Low = 450, High = 465
// Second measurement: Low = 450 + 450 = 900, High = 465 + 465 = 930
// Third measurement: Low = 900 + 450 = 1350, High = 930 + 465 = 1395
// Fourth measurement: Low = 1350 + 450 = 1800, High = 1395 + 465 = 1860

// Then we use cup [200, 210] to measure two volumes:
// Fifth measurement: Low = 1800 + 200 = 2000, High = 1860 + 210 = 2070
// Sixth measurement: Low = 2000 + 200 = 2200, High = 2070 + 210 = 2280

// We've measured a volume in the range [2200, 2280].
// This is within our target range, so we return `True`.

// Note: there are other ways to measure a volume in the target range.

```

## Optimal Time & Space Complexity:
```
O(low * high * n) time | O(low * high) space - where `n` is the number of measuring cups.
```
"""

# =========================================================================================================================== #

# Solution:


# O(low * high * n) time | O(low * high) space
def ambiguous_measurements(measuring_cups, low, high):
    # Initialize memoization dictionary to store already computed results
    memoization = {}

    # Start the recursive measurement checking process
    return can_measure_in_range(measuring_cups, low, high, memoization)


def can_measure_in_range(measuring_cups, low, high, memoization):
    # Create a unique key for the current low and high values for memoization
    memoize_key = create_hashable_key(low, high)

    # If we've already computed this range before, return the stored result
    if memoize_key in memoization:
        return memoization[memoize_key]

    # Base case: if both low and high are <= 0, we can't measure anything
    if low <= 0 and high <= 0:
        return False

    can_measure = False  # Initialize result for current range

    # Check each measuring cup to see if it can help measure the desired range
    for cup in measuring_cups:
        cup_low, cup_high = cup  # Unpack the cup's measurement range

        # Case 1: If the cup's range fits entirely within our target range
        if low <= cup_low and cup_high <= high:
            can_measure = True
            break

        # Case 2: Subtract the cup's range from our target range and recurse
        # This represents using this cup once and seeing if we can measure the remainder
        new_low = max(0, low - cup_low)  # Don't go below 0
        new_high = max(0, high - cup_high)  # Don't go below 0

        # Recursively check if we can measure the new reduced range
        can_measure = can_measure_in_range(
            measuring_cups, new_low, new_high, memoization
        )
        if can_measure:
            break

    # Store the result for this range before returning
    memoization[memoize_key] = can_measure
    return can_measure


def create_hashable_key(low, high):
    # Helper function to create a string key from low and high values
    return str(low) + ":" + str(high)


# Test Cases:

measuring_cups = [
    [200, 210],
    [450, 465],
    [800, 850],
]

low = 2100
high = 2300

measuring_cups_2 = [
    [1, 3],
    [2, 4],
    [5, 7],
    [10, 20],
]

low_2 = 10
high_2 = 12

print(ambiguous_measurements(measuring_cups, low, high))  # True
# Explanation: 4*[450,465] + 2*[200,210] = [2200,2280] which is within [2100,2300]

print(ambiguous_measurements(measuring_cups_2, low_2, high_2))  # False
# Explanation: No combination of cups sums up to a range within [10,12]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity:**

The algorithm uses a recursive approach with memoization to avoid redundant calculations. Here's how we can break it down:

1. **Recursive Calls:**
   - At each step, the function tries all possible measuring cups (let's say there are `n` cups).
   - For each cup, it reduces the problem to a new subproblem with updated `low` and `high` values (`new_low = max(0, low - cup_low)
   ` and `new_high = max(0, high - cup_high)`).
   - The recursion continues until `low` and `high` become ≤ 0 or a valid measurement is found.

2. **Memoization:**
   - The memoization ensures that each unique `(low, high)` pair is computed only once.
   - The number of unique `(low, high)` pairs is bounded by `O(low * high)` because `low` and `high` decrease in each recursive
   call (but not below 0).

3. **Total Work:**
   - For each `(low, high)` pair, the algorithm iterates over all `n` measuring cups.
   - Therefore, the total time complexity is:

        O(n ⋅ low ⋅ high)

   - This is because there are `O(low * high)` possible subproblems, and each subproblem takes `O(n)` time.

### **Space Complexity:**

The space complexity is determined by:
1. **Memoization Storage:**
   - The memoization dictionary stores results for `O(low * high)` unique `(low, high)` pairs.
   - Each entry takes constant space (since we store a boolean).
   - Thus, the space required for memoization is:

        O(low ⋅ high)

2. **Recursion Stack:**
   - The maximum recursion depth is bounded by the number of times we can subtract `cup_low` and `cup_high` from `low` and `high`
   before they become ≤ 0.
   - In the worst case, this is `O(low + high)` (if we subtract the smallest possible values each time).
   - However, since memoization avoids redundant calls, the recursion stack does not grow beyond `O(low + high)`.

Thus, the total space complexity is:

    O(low ⋅ high + low + high) = O(low ⋅ high)

(because `low * high` dominates `low + high` for large values).

### **Summary:**
- **Time Complexity:**  O(n ⋅ low ⋅ high)
- **Space Complexity:**  O(low ⋅ high)

### **Optimization Consideration:**
- If `low` and `high` are very large, this approach may not be efficient due to the `O(low * high)` factor.
- Alternative approaches (e.g., dynamic programming with GCD-based pruning or BFS over possible measurements) could be more
efficient in some cases.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s walk through your code carefully and break it down step-by-step:

## **1. Problem Statement**
You are given:
- A list of **measuring cups** where each cup has a **low** and **high** measurement (because measuring is imprecise).
- A **target range** `[low, high]`.

You want to determine **if you can use any combination of the cups** (each cup can be used any number of times) to measure an
amount **that falls within** the target range.

---

## **2. Code Overview**

There are 3 main parts:

### 2.1. `ambiguous_measurements(measuring_cups, low, high)`
- Main function you call.
- It initializes a **memoization dictionary** to avoid recalculating subproblems.
- It calls the helper `can_measure_in_range(...)`.

---

### 2.2. `can_measure_in_range(measuring_cups, low, high, memoization)`
This is a **recursive function** that tries to solve the problem.

Here’s what it does:
1. **Memoization Check**:
   - It creates a `memoize_key` by combining `low` and `high` into a string (like `'2100:2300'`).
   - If this key has been computed before, return its stored value.

2. **Base Case**:
   - If both `low` and `high` are **≤ 0**, return `False`.
   - (This means you've subtracted too much — you can’t have negative liquid amounts.)

3. **Main Recursive Work**:
   - For each measuring cup:
     - Get its `cup_low` and `cup_high` values.
   
     - **Direct Match Check**:
       - If the cup's range `[cup_low, cup_high]` fits **inside** the current `[low, high]`, immediately return `True`.
       - Example: if you need between 10–12 units and the cup measures 11 units, you're good.

     - **Recursive Attempt**:
       - Otherwise, "pretend" you used this cup and **decrease** the target range:
         - `new_low = max(0, low - cup_low)`
         - `new_high = max(0, high - cup_high)`
       - Recurse on the new smaller range.
       - (You're trying to see: if I use this cup now, can I measure the remaining quantity?)

     - If **any** cup eventually leads to success (`can_measure == True`), break and return True.

4. **Memoization Save**:
   - After trying all cups, save the result (True or False) in `memoization` to avoid recomputing this `(low, high)` range
   in the future.

5. **Return the Result**.

---

### 2.3. `create_hashable_key(low, high)`
- Just a helper that makes a string out of `(low, high)`, because Python dictionaries need **hashable keys** and lists/tuples
might cause problems if low/high change dynamically.

---

## **3. Example Walkthrough**

### Example 1:
```
measuring_cups = [
    [200, 210],
    [450, 465],
    [800, 850],
]
low = 2100
high = 2300
```

- Start with `[2100, 2300]`.
- Try using one cup:
  - Use `[800, 850]`:
    - New range becomes `[2100-850, 2300-800]` → `[1250, 1500]`.
  - Again, try using `[800, 850]`:
    - New range: `[1250-850, 1500-800]` → `[400, 700]`.
  - Keep trying:
    - Maybe now try `[450, 465]`:
      - New range: `[400-465, 700-450]` → `[0, 250]`.
    - Now you try `[200, 210]`:
      - New range: `[0-210, 250-200]` → `[0, 50]`.
- Eventually, it checks whether you can get exactly into the target window. 
- It finds a valid combination: **True**.

---

### Example 2:
```
measuring_cups = [
    [1, 3],
    [2, 4],
    [5, 7],
    [10, 20],
]
low = 10
high = 12
```

- Need to measure between 10–12 units.
- Try:
  - `[1,3]` → New range `[7,11]`
  - `[2,4]` → New range `[6,10]`
  - `[5,7]` → New range `[3,7]`
- None of these combinations fit perfectly inside `[10,12]` when you recurse.
- Eventually, recursion exhausts all options.
- **Returns False**.

---

## **4. Summary**

- **Technique**: Recursion + Memoization (Dynamic Programming).
- **Key Idea**: For every `(low, high)`, try each cup and check whether using it helps reach the goal.
- **Efficiency**: Memoization ensures you don't recompute the same `(low, high)` multiple times → much faster.

---

## **5. Important Points**
- **Memoization** is crucial; otherwise, recursion would become exponentially slow.
- **Base cases** are carefully thought out (checking when `low` and `high` are ≤ 0).
- **Greedy matching** (checking if a single cup fits) helps short-circuit the recursion early.
- **max(0, ...)** ensures no negative liquid amounts — you cannot "owe" liquid.

---

Let's **visualize** the recursive tree for the **first example**:

---
### **Example 1:**
```
measuring_cups = [
    [200, 210],
    [450, 465],
    [800, 850],
]
low = 2100
high = 2300
```

We need to measure between **2100 and 2300** units.

---

### **Starting point:**

```
Goal: [2100, 2300]
```
Now, try each cup:

---

### **Level 1:**
(At each level, we pick one cup and shrink the [low, high] accordingly.)

- Try using `[200,210]`:
  ```
  New range: [2100-210, 2300-200] → [1890, 2100]
  ```
- Try using `[450,465]`:
  ```
  New range: [2100-465, 2300-450] → [1635, 1850]
  ```
- Try using `[800,850]`:
  ```
  New range: [2100-850, 2300-800] → [1250, 1500]
  ```
  
---

### **Branching from [1250,1500]**:
(we took `[800,850]` in the first move)

Now, again try all cups:

- Use `[200,210]`:
  ```
  [1250-210, 1500-200] → [1040, 1300]
  ```
- Use `[450,465]`:
  ```
  [1250-465, 1500-450] → [785, 1050]
  ```
- Use `[800,850]`:
  ```
  [1250-850, 1500-800] → [400, 700]
  ```

---

### **Branching from [400,700]**:
(we took `[800,850]` again)

Try all cups:

- Use `[200,210]`:
  ```
  [400-210, 700-200] → [190, 500]
  ```
- Use `[450,465]`:
  ```
  [400-465, 700-450] → [0, 250]   <-- Important! Notice 0.
  ```
- Use `[800,850]`:
  ```
  [400-850, 700-800] → [0, 0]     (but negative values not allowed)
  ```

---

### **Branching from [0,250]**:
(now from `[400,700]` after picking `[450,465]`)

Try cups again:

- Use `[200,210]`:
  ```
  [0-210, 250-200] → [0, 50]
  ```
- Use `[450,465]`:
  ```
  [0-465, 250-450] → [0, 0]
  ```
- Use `[800,850]`:
  ```
  [0-850, 250-800] → [0, 0]
  ```

---

### **Branching from [0,50]**:
Try cups again:

- Use `[200,210]`: cannot fit — cup range is 200–210, too big.
- Use `[450,465]`: cannot fit — cup range too big.
- Use `[800,850]`: cannot fit.

No success here.

---

### **What happened?**

At `[0,250]`, no immediate match.
At `[400,700]`, we tried `[450,465]`, but **still not complete**.

---

However, **notice another path** we missed earlier:

When starting from `[1250,1500]`, **if you pick [450,465]** immediately:

```
[1250-465, 1500-450] → [785,1050]
```

From `[785,1050]`:

- Pick `[800,850]` again:
  ```
  [785-850, 1050-800] → [0,250]
  ```

And so on.

---

### **Conclusion:**
The recursion keeps trying:
- Use [800–850] as many times as needed.
- Then [450–465] to adjust.
- Then [200–210] to finalize.

**Eventually,** it can match the range `[2100,2300]` exactly by clever combinations of the cups.

Thus, **Answer: True** ✅

---

# 🎯 **Tree Summary**
```
[2100,2300]
├── [1890,2100] (by 200–210) --> keep recursing
├── [1635,1850] (by 450–465) --> keep recursing
└── [1250,1500] (by 800–850)
     ├── [1040,1300] (by 200–210)
     ├── [785,1050] (by 450–465)
     │    ├── [0,250] (by 800–850)
     │         ├── [0,50] (by 200–210)
     └── [400,700] (by 800–850)
          ├── [0,250] (by 450–465)
```

---

## 🔥 **Key Insight**
- **Recursive tree**: each node represents trying a new cup and shrinking the target.
- **Memoization** prevents revisiting the same `[low, high]` pairs repeatedly.
- **Goal** is to reach a "safe zone" where the cup exactly fits inside `[low, high]`.

"""
