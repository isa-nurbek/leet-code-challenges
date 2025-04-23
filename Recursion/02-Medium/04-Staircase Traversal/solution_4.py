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
    # If height is 0 or 1, there's exactly 1 way to traverse (do nothing or take one step)
    if height == 0 or height == 1:
        return 1
    # If max_steps is 1, the only way is to take 1 step each time (only one possible way)
    if max_steps == 1:
        return 1

    # Initialize a dynamic programming array to store number of ways to reach each height
    # ways_to_top[i] will store the number of ways to reach height i
    ways_to_top = [0] * (height + 1)

    # There's 1 way to be at height 0 (base case)
    ways_to_top[0] = 1

    # This will maintain the sum of the previous max_steps elements in the ways_to_top array
    window_sum = 0

    # Calculate the number of ways for each height from 1 to the target height
    for current_height in range(1, height + 1):
        # The start of our sliding window (the element to remove from window_sum)
        start_of_window = current_height - max_steps - 1

        # The end of our sliding window (the element to add to window_sum)
        end_of_window = current_height - 1

        # If the start of window is valid (>= 0), remove that element from our window sum
        # This maintains that our window only considers the last max_steps elements
        if start_of_window >= 0:
            window_sum -= ways_to_top[start_of_window]

        # Add the new element (just before current_height) to our window sum
        window_sum += ways_to_top[end_of_window]

        # The number of ways to reach current_height is the sum of ways to reach
        # the previous max_steps heights (sliding window sum)
        ways_to_top[current_height] = window_sum

    # Return the number of ways to reach the target height
    return ways_to_top[height]


# Test Cases:

print(staircase_traversal(4, 2))  #  Output: 5
print(staircase_traversal(10, 1))  #  Output: 1
print(staircase_traversal(6, 3))  #  Output: 24
