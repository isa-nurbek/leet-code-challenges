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
