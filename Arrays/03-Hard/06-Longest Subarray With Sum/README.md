# Longest Subarray With Sum

Write a function that takes in a non-empty array of non-negative integers and a non-negative integer representing a target sum. The function should find the longest subarray where the values collectively sum up to equal the target sum. Return an array containing the starting index and ending index of this subarray, both inclusive.

If there is no subarray that sums up to the target sum, the function should return an empty array. You can assume that the given inputs will only ever have one answer.

## Sample Input

```plaintext
array = [1, 2, 3, 4, 3, 3, 1, 2, 1, 2]
target_sum = 10
```

## Sample Output

```plaintext
[4, 8]  // The longest subarray that sums to 10 starts at index 4 and ends at index 8
```

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the length of the input array.
