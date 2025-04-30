# Knight Connection

You're given the position of two knight pieces on an infinite chess board. Write a function that returns the minimum number of turns required before one of the knights is able to capture the other knight, assuming the knights are working together to achieve this goal.

The position of each knight is given as a list of `2 values`, the `x` and `y` coordinates. A knight can make `1 of 8` possible moves on any given turn. Each of these moves involves moving in an `"L"` shape. This means they can either move `2` squares horizontally and `1` square vertically, or they can move `1` square horizontally and `2` squares vertically. For example, if a knight is currently at position [0, 0], then it can move to any of these `8` locations on its next move:

```plaintext
[
  [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]
]
```

A knight is able to capture the other knight when it is able to move onto the square currently occupied by the other knight.

Each turn allows each knight to move up to one time. For example, if both knights moved towards each other once, and then `knight_a` captures `knight_b` on its next move, two turns would have been used (even though `knight_b` never made its second move).

## Sample Input

```plaintext
knight_a = [0, 0]
knight_b = [4, 2]
```

## Sample Output

```plaintext
1

// knight_a moves to [2, 1], knight_b captures knight_a on [2, 1]
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

The number of turns needed for two knights to meet on a common square is the same as the number of moves needed for a single knight to reach the other knight divided by two (and rounded up to account for odd numbers of moves).

</details>

<details>
<summary><b>Hint 2</b></summary>

Rather than thinking of this problem in terms of chess, try thinking about it as a graph problem. What are the nodes and what are the edges?

</details>

<details>
<summary><b>Hint 3</b></summary>

As a graph problem, you can consider each square on the board as a node, and each possible knight move as an edge. Then you can find the distance between those nodes using standard graph algorithms, such as `Breadth-First-Search` (BFS).

</details>

## Optimal Time & Space Complexity

`O(n * m)` time | `O(n * m)` space - where `n` is horizontal distance between the knights and `m` is the vertical distance between the knights.
