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


# O(n²) time | O(n²) space
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

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity Analysis**

1. **BFS Exploration**:
   - Each position is processed at most once because we maintain a `visited` set.
   - Each position can have **at most 8 neighbors** (since a knight has 8 possible moves).
   - BFS expands outward in layers until it reaches `knight_b`.

2. **Bounding the Number of States**:
   - Since it's an infinite board, BFS continues until the destination is found.
   - On an **n × n** board (or if we assume a bounded region around the starting point), BFS can visit at most **O(n²)**
   positions in the worst case.
   
   - Each position takes **O(1)** time to process and enqueue neighbors.

Thus, the overall **worst-case time complexity** is **O(n²)**, where **n** is the Manhattan distance between `knight_a`
and `knight_b`.

---

### **Space Complexity Analysis**

1. **Queue Storage**:
   - BFS uses a queue to store nodes for exploration.
   - The worst-case number of elements in the queue is proportional to the number of positions reached, **O(n²)** in the worst case.

2. **Visited Set**:
   - Stores each visited position as a string (e.g., `"x,y"`), consuming **O(n²)** space.

Thus, the **worst-case space complexity** is **O(n²)**.

---

### **Final Complexity Summary**

| Complexity            | Worst Case    |
|-----------------------|---------------|
| **Time Complexity**   | **O(n²)**     |
| **Space Complexity**  | **O(n²)**     |

This means that as the distance between `knight_a` and `knight_b` increases, the number of visited positions and memory
usage grow quadratically. However, in practice, the knight's unique movement pattern ensures that BFS often finds the
shortest path much faster than this worst-case bound.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the `knight_connection` Function**

This function calculates the minimum number of moves a knight needs to go from one position (`knight_a`) to another
(`knight_b`) on an infinite chessboard. Let's break it down step by step.

---

### **1. Understanding the Knight's Moves**

A knight moves in an "L" shape on a chessboard, meaning it can move in eight possible directions from any given position:

1. **(−2, +1)**
2. **(−1, +2)**
3. **(+1, +2)**
4. **(+2, +1)**
5. **(+2, −1)**
6. **(+1, −2)**
7. **(−1, −2)**
8. **(−2, −1)**

These moves are stored in the `possible_moves` list:

```
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
```
---

### **2. Initializing the Search**

We use **Breadth-First Search (BFS)** to explore the shortest path. 

#### **Queue Initialization**
The queue is initialized with the starting position (`knight_a`) and a step counter set to `0`:

```
queue = [[knight_a[0], knight_a[1], 0]]
```

Each element in the queue represents `[x, y, steps]`, where:
- `x, y` is the knight's position.
- `steps` keeps track of how many moves have been taken.

#### **Visited Set**

A set called `visited` keeps track of positions already explored:

```
visited = {position_to_string(knight_a)}
```
This prevents revisiting positions and speeds up the search.

---

### **3. BFS Traversal**

We loop through the queue until we find `knight_b`:

```
while True:
    current_position = queue.pop(0)
```
This dequeues the first element (`current_position`), which contains the knight's current position and step count.

#### **Checking If the Target is Reached**

If the knight reaches `knight_b`, return the **ceiling of half the step count**:

```
if current_position[0] == knight_b[0] and current_position[1] == knight_b[1]:
    return math.ceil(current_position[2] / 2)
```
This means the knight has arrived at the destination, and we return the rounded-up half of the total steps.

#### **Exploring Possible Moves**

For each possible move, we calculate the next position:

```
for possible_move in possible_moves:
    position = [
        current_position[0] + possible_move[0],
        current_position[1] + possible_move[1],
    ]
```

We convert the new position into a string format:

```
position_string = position_to_string(position)
```
to check if it has been visited before.

#### **Adding Unvisited Positions to the Queue**

If the position has **not** been visited:

```
if position_string not in visited:
```
- We increase the step count.
- Add the position to the queue.
- Mark it as visited.

```
position.append(current_position[2] + 1)
queue.append(position)
visited.add(position_string)
```

---

### **4. Position Conversion Function**

The function `position_to_string(position)` converts a list `[x, y]` into a string `"x,y"`, allowing it to be stored
in a `set` for quick lookup:

```
def position_to_string(position):
    return ",".join(map(str, position))
```

---

### **5. Understanding the Test Cases**

#### **Case 1: `knight_connection([0, 0], [4, 2])`**

Output: `1`
- The knight can reach `(4,2)` in **two** moves: `(0,0) → (2,1) → (4,2)`.
- Since we return `ceil(2/2) = 1`, the output is `1`.

#### **Case 2: `knight_connection([15, -12], [15, -12])`**

Output: `0`
- The knight is already at the target position.
- No moves are needed, so the output is `0`.

#### **Case 3: `knight_connection([0, 0], [20, 20])`**

Output: `7`
- BFS finds the shortest path in **14 moves**.
- Since we return `ceil(14/2) = 7`, the output is `7`.

---

### **Final Thoughts**

- This algorithm efficiently finds the shortest path using BFS.
- The `ceil(steps / 2)` ensures an optimal step count for knight movement.
- The `visited` set prevents redundant calculations, making it faster.

"""
