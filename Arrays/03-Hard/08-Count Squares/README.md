# Count Squares

Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates) and returns the number of squares that can be formed by these coordinates.

A square must have its four corners amongst the coordinates in order to be counted. A single coordinate can be used as a corner for multiple different squares.

You can also assume that no coordinate will be farther than 100 units from the origin.

## Sample Input

```plaintext
points = [
  [1, 1],
  [0, 0],
  [-4, 2],
  [-2, -1],
  [0, 1],
  [1, 0],
  [-1, 4],
]
```

## Sample Output

```plaintext
2

// [1, 1], [0, 0], [0, 1], and [1, 0] makes a square, as does [1, 1], [-4, 2], [-2, -1], and [-1, 4]
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Given any two points, there are exactly three pairs of points that would make a square.

</details>

<details>
<summary><b>Hint 2</b></summary>

If two points are assumed to be diagonally across from each other in a square, there is only one pair of points that would complete the square.

</details>

<details>
<summary><b>Hint 3</b></summary>

All four points of a square will always be equidistant from the midpoint.

</details>

<details>
<summary><b>Hint 4</b></summary>

The slopes of the two diagonals of a square are always negative reciprocals of each other.

</details>

## Optimal Time & Space Complexity

`O(n^2)` time | `O(n)` space - where `n` is the number of points.
