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
