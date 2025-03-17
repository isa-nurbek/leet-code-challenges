# Missing Numbers

You're given an unordered list of unique integers `nums` in the range `[1, n]`, where `n` represents the length of `nums + 2`. This means that two numbers in this range are missing from the list.

Write a function that takes in this list and returns a new list with the two missing numbers, sorted numerically.

## Sample Input

```plaintext
nums = [1, 4, 3]
```

## Sample Output

```plaintext
[2, 5]  // n is 5, meaning the completed list should be [1, 2, 3, 4, 5]
```

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the length of the input array.
