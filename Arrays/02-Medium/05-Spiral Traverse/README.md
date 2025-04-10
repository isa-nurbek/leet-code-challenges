# Spiral Traverse

Write a function that takes in an `n x m` two-dimensional array (that can be square-shaped when `n == m`) and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.

## Sample Input

```plaintext
array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]
```

## Sample Output

```plaintext
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

## Optimal Time & Space Complexity

`O(n)` time | `O(n)` space - where `n` is the total number of elements in the array.
