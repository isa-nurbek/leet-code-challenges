# Problem Description:

"""

                                            # Knight Connection

You're given the position of two knight pieces on an infinite chess board. Write a function that returns the minimum number
of turns required before one of the knights is able to capture the other knight, assuming the knights are working together
to achieve this goal.

The position of each knight is given as a list of 2 values, the x and y coordinates. A knight can make 1 of 8 possible moves
on any given turn. Each of these moves involves moving in an "L" shape. This means they can either move 2 squares horizontally
and 1 square vertically, or they can move 1 square horizontally and 2 squares vertically. For example, if a knight is currently
at position [0, 0], then it can move to any of these 8 locations on its next move:

```
[
  [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]
]
```

A knight is able to capture the other knight when it is able to move onto the square currently occupied by the other knight.

Each turn allows each knight to move up to one time. For example, if both knights moved towards each other once, and then
knight_a captures knight_b on its next move, two turns would have been used (even though knight_b never made its second move).


## Sample Input:
```
knight_a = [0, 0]
knight_b = [4, 2]
```

## Sample Output:
```
1 // knight_a moves to [2, 1], knight_b captures knight_a on [2, 1]
```

## Optimal Time & Space Complexity:
```
O(n * m) time | O(n * m) space - where `n` is horizontal distance between the knights
and `m` is the vertical distance between the knights.
```

"""

# =========================================================================================================================== #

# Solution:
from collections import deque


# O(n²) time | O(n²) space
def knight_connection(knight_a, knight_b):
    # If both knights are already at the same position, no moves are needed
    if knight_a == knight_b:
        return 0

    # All possible moves a knight can make in a single step
    possible_moves = [
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
    ]

    # Initialize two queues for bidirectional BFS:
    # - queue_start: BFS from the starting position (knight_a)
    # - queue_end: BFS from the target position (knight_b)
    queue_start = deque([(knight_a[0], knight_a[1], 0)])  # (x, y, steps)
    queue_end = deque([(knight_b[0], knight_b[1], 0)])

    # Initialize two visited sets to keep track of explored positions:
    # - visited_start: positions explored from the starting position
    # - visited_end: positions explored from the target position
    visited_start = {tuple(knight_a)}
    visited_end = {tuple(knight_b)}

    # Perform bidirectional BFS until one of the queues is empty
    while queue_start and queue_end:
        # Expand one level from the starting position
        result = expand(queue_start, visited_start, visited_end, possible_moves)
        if result is not None:
            return result  # If a connection is found, return the number of steps

        # Expand one level from the target position
        result = expand(queue_end, visited_end, visited_start, possible_moves)
        if result is not None:
            return result  # If a connection is found, return the number of steps

    # If no connection is found (should not happen for valid inputs)
    return -1


def expand(queue, visited_self, visited_other, possible_moves):
    """Expands one level in the BFS search."""
    # Process all nodes at the current level
    for _ in range(len(queue)):
        x, y, steps = queue.popleft()  # Get the current position and step count

        # Explore all possible moves from the current position
        for dx, dy in possible_moves:
            new_pos = (x + dx, y + dy)  # Calculate the new position

            # If the new position is in the other BFS's visited set, a connection is found
            if new_pos in visited_other:
                return steps + 1  # Return the total steps taken

            # If the new position hasn't been visited in the current BFS, add it to the queue
            if new_pos not in visited_self:
                visited_self.add(new_pos)  # Mark the new position as visited
                queue.append(
                    (new_pos[0], new_pos[1], steps + 1)
                )  # Add to queue with incremented step count

    # If no connection is found at this level, return None
    return None


# Test Cases:
print(knight_connection([0, 0], [4, 2]))  # Output: 1

print(knight_connection([15, -12], [15, -12]))  # Output: 0

print(knight_connection([0, 0], [20, 20]))  # Output: 7


# =========================================================================================================================== #
