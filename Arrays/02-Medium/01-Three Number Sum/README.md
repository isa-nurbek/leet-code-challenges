# Three Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

## Sample Input

```plaintext
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
```

## Sample Output

```plaintext
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
```

## Optimal Time & Space Complexity

`O(n^2)` time | `O(n)` space - where `n`  is the length of the input array.
