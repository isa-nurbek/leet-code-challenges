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
    # - If height is 0, there's 1 way (doing nothing)
    # - If height is 1, there's 1 way (single step)
    if height == 0 or height == 1:
        return 1

    # Initialize a dynamic programming array to store number of ways to reach each step
    # ways_to_top[i] will store the number of ways to reach step i
    ways_to_top = [0] * (height + 1)

    # Base case values:
    ways_to_top[0] = 1  # One way to stay at ground level (do nothing)
    ways_to_top[1] = 1  # One way to reach first step (single step of 1)

    # Build up the solution from bottom to top
    for current_height in range(2, height + 1):
        # The starting point of our sliding window is either:
        # - 0 (if we're within max_steps from the beginning)
        # - or (current_height - max_steps) to look back max_steps steps
        window_start = max(0, current_height - max_steps)

        # The number of ways to reach current_height is the sum of ways to reach
        # all previous steps that can jump directly to current_height
        # (within max_steps range)
        ways_to_top[current_height] = sum(ways_to_top[window_start:current_height])

    # Return the number of ways to reach the top (final height)
    return ways_to_top[height]


# Test Cases:

print(staircase_traversal(4, 2))  #  Output: 5
print(staircase_traversal(10, 1))  #  Output: 1
print(staircase_traversal(6, 3))  #  Output: 24
