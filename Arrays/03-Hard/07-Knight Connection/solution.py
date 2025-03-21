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
O(n * m) time | O(n * m) space - where `n` is horizontal distance between the knights and `m` is the vertical distance between the knights.
```

"""

# =========================================================================================================================== #

# Solution:
import math


# O(n * m) time | O(n * m) space
def knight_connection(knight_a, knight_b):
    # Define all possible moves a knight can make on a chessboard.
    # A knight moves in an "L" shape: 2 squares in one direction and 1 square in the other.
    possible_moves = [
        [-2, 1],
        [-1, 2],
        [1, 2],
        [2, 1],
        [2, -1],
        [1, -2],
        [-1, -2],
        [-2, -1],
    ]

    # Initialize a queue with the starting position of knight_a and the number of moves taken so far (0).
    queue = [[knight_a[0], knight_a[1], 0]]

    # Create a set to keep track of visited positions to avoid revisiting them.
    visited = {position_to_string(knight_a)}

    # Start the Breadth-First Search (BFS) loop.
    while True:
        # Get the first position in the queue.
        current_position = queue.pop(0)

        # Check if the current position matches the target position (knight_b).
        if current_position[0] == knight_b[0] and current_position[1] == knight_b[1]:
            # If the target is reached, return the number of moves divided by 2 (rounded up).
            # This is because the problem likely involves two knights moving towards each other.
            return math.ceil(current_position[2] / 2)

        # Explore all possible moves from the current position.
        for possible_move in possible_moves:
            # Calculate the new position after making the move.
            position = [
                current_position[0] + possible_move[0],
                current_position[1] + possible_move[1],
            ]

            # Convert the position to a string to check if it has been visited.
            position_string = position_to_string(position)

            # If the position hasn't been visited, add it to the queue and mark it as visited.
            if position_string not in visited:
                # Append the new position to the queue, incrementing the move count by 1.
                position.append(current_position[2] + 1)

                queue.append(position)
                visited.add(position_string)


# Helper function to convert a position (list of coordinates) to a string.
# This is used to store positions in the `visited` set.
def position_to_string(position):
    return ",".join(map(str, position))


# Test Cases:

print(knight_connection([0, 0], [4, 2]))
# Output: 1

print(knight_connection([15, -12], [15, -12]))
# Output: 0

print(knight_connection([0, 0], [20, 20]))
# Output: 7

# =========================================================================================================================== #
