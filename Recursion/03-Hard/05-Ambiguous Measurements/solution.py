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
