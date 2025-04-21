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
