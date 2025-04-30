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


# O(k * high^2) time | O(high^2) space
from collections import deque


def ambiguous_measurements(measuring_cups, low, high):
    """
    Determines if we can measure a quantity between `low` and `high` using the given measuring cups.

    Each measuring cup provides a range [cup_low, cup_high]. The goal is to see if by combining
    these cups (summing their ranges), we can achieve a range that falls within [low, high].

    Args:
        measuring_cups: List of tuples, where each tuple represents a cup's measurement range (low, high).
        low: The target lower bound.
        high: The target upper bound.

    Returns:
        bool: True if a valid combination exists, False otherwise.
    """

    # We use a queue to perform a BFS (Breadth-First Search) over possible sums of ranges.
    # Each element in the queue is a tuple (current_sum_low, current_sum_high).
    queue = deque()
    queue.append((0, 0))  # Start with zero measurements

    # A set to keep track of visited states to avoid redundant processing.
    visited = set()
    visited.add((0, 0))  # Mark the initial state as visited

    while queue:
        current_low_sum, current_high_sum = queue.popleft()

        # Check if the current summed range falls within the target [low, high]
        if current_low_sum >= low and current_high_sum <= high:
            return True  # Found a valid combination

        # Explore all possible next steps by adding each measuring cup's range
        for cup in measuring_cups:
            cup_low, cup_high = cup

            # Calculate new summed range after using the current cup
            new_low_sum = current_low_sum + cup_low
            new_high_sum = current_high_sum + cup_high

            # If the new high exceeds the target high, skip this path (pruning)
            if new_high_sum > high:
                continue

            # Check if this new state has been visited before
            if (new_low_sum, new_high_sum) not in visited:
                visited.add((new_low_sum, new_high_sum))  # Mark as visited
                queue.append(
                    (new_low_sum, new_high_sum)
                )  # Add to queue for further exploration

    # If queue is exhausted and no valid combination found, return False
    return False


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

### Time Complexity:

1. **Breadth-First Search (BFS)**: The algorithm uses BFS to explore all possible sums of measuring cup measurements. Each state
in the BFS is represented by `(current_low_sum, current_high_sum)`.
2. **State Exploration**: In the worst case, the algorithm explores all possible combinations of `current_low_sum` and
`current_high_sum` up to `high`. The number of unique states is bounded by `O(high^2)` because both `current_low_sum` and
`current_high_sum` can range from `0` to `high`.
3. **Processing Each State**: For each state, the algorithm iterates over all `measuring_cups` (let's say there are `k` cups).
Thus, the total time complexity is `O(k * high^2)`.

### Space Complexity:

1. **Queue**: The queue stores the states to be processed. In the worst case, it can hold all unique states, which is `O(high^2)`.
2. **Visited Set**: The visited set also stores all unique states, which is `O(high^2)`.
3. **Overall Space Complexity**: The dominant factor is the queue and the visited set, so the space complexity is `O(high^2)`.

### Summary:
- **Time Complexity**: `O(k * high^2)`, where `k` is the number of measuring cups.
- **Space Complexity**: `O(high^2)`.

### Notes:
- The algorithm is efficient when `high` is not too large, but it can become slow for very large values of `high` due to the
quadratic dependence on `high`.
- The `visited` set ensures that no state is processed more than once, which is crucial for avoiding redundant work and keeping
the complexity manageable.

"""
