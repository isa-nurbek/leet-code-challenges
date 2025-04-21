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


# O(kⁿ) time | O(n) space
def staircase_traversal(height, max_steps):
    """Main function to calculate number of ways to climb a staircase.

    Args:
        height: Total number of steps in the staircase
        max_steps: Maximum number of steps you can take at a time

    Returns:
        Number of distinct ways to climb the staircase
    """
    return number_of_ways_to_top(height, max_steps)


def number_of_ways_to_top(height, max_steps):
    """Recursive helper function to calculate ways to reach the top.

    The approach uses recursion with the idea that:
    The number of ways to reach step n is the sum of ways to reach
    steps n-1, n-2, ..., n-max_steps (since you can jump up to max_steps at a time)

    Args:
        height: Remaining height/steps to climb
        max_steps: Maximum steps that can be taken at once

    Returns:
        Number of ways to climb the remaining height
    """
    # Base case: if height is 0 or 1, there's only 1 way (do nothing or take one step)
    if height <= 1:
        return 1

    number_of_ways = 0
    # Consider all possible step sizes we can take at this point (from 1 to max_steps)
    for step in range(1, min(max_steps, height) + 1):
        # Add the number of ways from the resulting sub-problem
        number_of_ways += number_of_ways_to_top(height - step, max_steps)

    return number_of_ways


# Test Cases:

print(staircase_traversal(4, 2))  #  Output: 5
print(staircase_traversal(10, 1))  #  Output: 1
print(staircase_traversal(6, 3))  #  Output: 24

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity Analysis

The given code is a recursive solution for the staircase traversal problem, where we want to find the number of ways to reach
the top of a staircase of `height` steps, taking at most `max_steps` at a time.

1. **Recursive Tree Structure**: 
   - At each step, the function makes up to `max_steps` recursive calls, each with a reduced height (`height - step`).
   - The depth of the recursion tree can go up to `height` (in the worst case where `max_steps >= height`), as we reduce the
   height by at least 1 in each recursive call.

2. **Branching Factor**:
   - The branching factor is `max_steps` because in each call, we loop from 1 to `min(max_steps, height)`, which can be up to
   `max_steps` branches.

3. **Worst-Case Time Complexity**:
   - The worst-case time complexity is exponential, specifically `O(max_steps^height)`. This is because the recursion tree can
   have up to `max_steps` branches at each level, and the tree can be up to `height` levels deep.
   - For example, if `max_steps = height`, the time complexity is `O(height^height)`, which is very inefficient.

### Space Complexity Analysis

1. **Recursion Stack**:
   - The maximum depth of the recursion stack is `height` (since we reduce the height by at least 1 in each call).
   - Thus, the space complexity due to the recursion stack is `O(height)`.

2. **Additional Space**:
   - No additional space is used apart from the recursion stack (no memoization or other data structures), so the total
   space complexity is `O(height)`.

### Example to Illustrate

For `height = 4` and `max_steps = 2`:
- The recursion tree will have calls like:
  - `number_of_ways_to_top(4, 2)`
    - `number_of_ways_to_top(3, 2)` (step=1)
      - `number_of_ways_to_top(2, 2)`
        - `number_of_ways_to_top(1, 2)`
        - `number_of_ways_to_top(0, 2)`
      - `number_of_ways_to_top(1, 2)`
    - `number_of_ways_to_top(2, 2)` (step=2)
      - `number_of_ways_to_top(1, 2)`
      - `number_of_ways_to_top(0, 2)`
- The tree has a depth of 4 (`height`) and a branching factor of 2 (`max_steps`), leading to roughly `2^4 = 16` operations
(though some branches terminate early).

### Optimizing the Solution

The current recursive solution is inefficient due to repeated calculations (overlapping subproblems). This can be optimized
using **memoization** (top-down dynamic programming) or **bottom-up dynamic programming**, reducing the time complexity
to `O(height * max_steps)` and space complexity to `O(height)`.

### Final Answer

- **Time Complexity**: `O(max_steps^height)` (exponential time).
- **Space Complexity**: `O(height)` (due to recursion stack).

This is highly inefficient for large `height` or `max_steps`, and dynamic programming approaches are strongly recommended
for practical use.

"""
