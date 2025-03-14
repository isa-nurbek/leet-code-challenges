# Move Element To End

You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.

## Sample Input

```plaintext
array = [2, 1, 2, 2, 2, 3, 4, 2]
to_move = 2
```

## Sample Output

```plaintext
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently
```

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the length of the array.
