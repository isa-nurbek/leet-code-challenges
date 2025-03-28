# Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order.

If no four numbers sum up to the target sum, the function should return an empty array.

## Sample Input

```plaintext
array = [7, 6, 4, -1, 1, 2]
targetSum = 16
```

## Sample Output

```plaintext
[[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently
```

## Optimal Time & Space Complexity

**Average:** `O(n^2)` time | `O(n^2)` space - where `n` is the length of the input array.

**Worst:** `O(n^3)` time | `O(n^2)` space - where `n` is the length of the input array.
