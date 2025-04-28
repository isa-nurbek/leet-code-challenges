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
1 

// knight_a moves to [2, 1], knight_b captures knight_a on [2, 1]
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

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the bidirectional BFS algorithm depends on the number of nodes (positions) explored during the search.

Here's a breakdown:

1. **Branching Factor**: A knight has 8 possible moves from any given position, so the branching factor `b` is 8.

2. **Bidirectional BFS**: In bidirectional BFS, the search proceeds from both the start and the target positions simultaneously.
The search stops when the two BFS frontiers meet.

3. **Number of Levels Explored**: Let `d` be the minimum number of moves required to connect the two knights.
In bidirectional BFS, each BFS explores roughly `d/2` levels before they meet.

4. **Total Nodes Explored**: The total number of nodes explored by both BFS searches is approximately (2 * b^d/2).
This is because each BFS explores (b^d/2) nodes.

Thus, the **time complexity** is:

    O(b^d/2)

where `b = 8` (the branching factor) and `d` is the minimum number of moves required to connect the two knights.

---

### Space Complexity Analysis

The space complexity is determined by the number of nodes stored in the queues and the visited sets during the BFS.

1. **Queue Size**: At any level, the queue stores all nodes at the current level. Since each BFS explores (b^d/2)
nodes, the maximum size of the queue is O(b^d/2).

2. **Visited Sets**: The visited sets store all explored nodes. Since both BFS searches explore (b^d/2) nodes each,
the total space required for the visited sets is O(b^d/2).

Thus, the **space complexity** is:

    O(b^d/2)

---

### Summary

- **Time Complexity**: O(8^d/2), where `d` is the minimum number of moves required to connect the two knights.
- **Space Complexity**: O(8^d/2), where `d` is the minimum number of moves required to connect the two knights.

This is significantly more efficient than a standard BFS, which would have a time and space complexity of O(8d).
Bidirectional BFS reduces the search space by exploring from both ends simultaneously.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code:**

This Python program implements **Bidirectional Breadth-First Search (BFS)** to determine the minimum number of knight moves
required to move from a starting position to a target position on an infinite chessboard.

---

### **Understanding the Problem Statement:**

A **knight** in chess moves in an **L-shape**:
- Two squares in one direction and then one square perpendicular.
- Or one square in one direction and then two squares perpendicular.

The goal is to determine the **minimum number of moves** needed for a knight to move from `knight_a` to `knight_b`.

---

### **Step-by-Step Execution:**

1. **Handle the Base Case:**
   ```
   if knight_a == knight_b:
       return 0
   ```
   - If the starting position is the same as the target position, **0 moves** are required.

2. **Define Possible Knight Moves:**
   ```
   possible_moves = [
       (-2, 1), (-1, 2), (1, 2), (2, 1),
       (2, -1), (1, -2), (-1, -2), (-2, -1)
   ]
   ```
   - These are the **8 possible moves** a knight can make.

3. **Initialize Two Queues for Bidirectional BFS:**
   ```
   queue_start = deque([(knight_a[0], knight_a[1], 0)])  # (x, y, steps)
   queue_end = deque([(knight_b[0], knight_b[1], 0)])
   ```
   - `queue_start`: BFS starting from `knight_a`.
   - `queue_end`: BFS starting from `knight_b`.
   - Each queue stores `(x, y, steps)`, where `steps` is the number of moves taken so far.

4. **Initialize Two Visited Sets:**
   ```
   visited_start = {tuple(knight_a)}
   visited_end = {tuple(knight_b)}
   ```
   - `visited_start`: Tracks positions visited from `knight_a`.
   - `visited_end`: Tracks positions visited from `knight_b`.
   - Helps prevent revisiting the same position.

5. **Bidirectional BFS:**
   ```
   while queue_start and queue_end:
   ```
   - The loop runs until **one of the queues is empty**.
   - The search expands from both directions.

6. **Expand One Level from `queue_start`:**
   ```
   result = expand(queue_start, visited_start, visited_end, possible_moves)
   if result is not None:
       return result
   ```
   - Calls `expand()`, which explores all possible moves for the current level.
   - If a position from `queue_start` **intersects** with `visited_end`, the total move count is returned.

7. **Expand One Level from `queue_end`:**
   ```
   result = expand(queue_end, visited_end, visited_start, possible_moves)
   if result is not None:
       return result
   ```
   - Similarly expands `queue_end`.
   - If an intersection is found, return the move count.

8. **`expand()` Function:**
   ```
   def expand(queue, visited_self, visited_other, possible_moves):
   ```
   - Expands the BFS for one step in a given direction.

   **Processing Each Position in the Queue:**
   ```
   for _ in range(len(queue)):
       x, y, steps = queue.popleft()
   ```
   - Dequeues all positions in the current level.

   **Try All Possible Moves:**
   ```
   for dx, dy in possible_moves:
       new_pos = (x + dx, y + dy)
   ```
   - Generates new possible positions.

   **Check for Intersection:**
   ```
   if new_pos in visited_other:
       return steps + 1
   ```
   - If `new_pos` is in `visited_other`, both searches have met, returning the total step count.

   **Add New Positions to Queue:**
   ```
   if new_pos not in visited_self:
       visited_self.add(new_pos)
       queue.append((new_pos[0], new_pos[1], steps + 1))
   ```
   - If `new_pos` has not been visited, mark it as visited and add it to the queue.

9. **Return -1 if No Path is Found (Not Expected):**
   ```
   return -1
   ```
   - This should not happen for valid inputs.

---

### **Time and Space Complexity Analysis:**

- **Time Complexity: O(n²)** (since each new position expands in 8 directions and both BFS searches run simultaneously).
- **Space Complexity: O(n²)** (because we store visited positions in sets).

---

### **Example Walkthrough:**

#### **Example 1:**
```
knight_connection([0, 0], [4, 2])
```
- The knight moves:
  ```
  [0,0] → [2,1] → [4,2]
  ```
- **Output:** `1` (in just **one move**).

#### **Example 2:**
```
knight_connection([15, -12], [15, -12])
```
- **Same start and end position**, so **0 moves** required.

#### **Example 3:**
```
knight_connection([0, 0], [20, 20])
```
- The knight needs **7 moves** to reach `[20,20]` using optimal moves.

---

### **Why Use Bidirectional BFS?**
- **Faster than Single BFS:** Instead of exploring all possible positions from the start, we meet in the middle.
- **Reduces the Number of Explored Nodes:** Expanding from two directions reduces the search space compared to a single BFS.

---

### **Final Thoughts**
This code efficiently finds the shortest path for a knight using **Bidirectional BFS**, improving performance over a traditional
BFS approach. The implementation ensures that unnecessary moves are avoided, making it suitable for large chessboard problems. 

"""
