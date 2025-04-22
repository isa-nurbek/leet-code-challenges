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
    if height == 0 or height == 1:
        return 1

    sliding_window = [0] * (max_steps + 1)
    sliding_window[0] = 1  # Base case: 1 way to stay at ground
    sliding_window[1] = 1  # Base case: 1 way to reach step 1

    for current_height in range(2, height + 1):
        # Compute the sum of the last 'max_steps' elements
        if current_height <= max_steps:
            total = sum(sliding_window[:current_height])
        else:
            total = sum(sliding_window[-max_steps:])

        # Update the sliding window (shift left and append new value)
        sliding_window.pop(0)
        sliding_window.append(total)

    return sliding_window[-1]


# Test Cases:

print(staircase_traversal(4, 2))  #  Output: 5
print(staircase_traversal(10, 1))  #  Output: 1
print(staircase_traversal(6, 3))  #  Output: 24
