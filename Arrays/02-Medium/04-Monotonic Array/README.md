# Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

> Note that empty arrays and arrays of one element are monotonic.

## Sample Input

```plaintext
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
```

## Sample Output

```plaintext
True
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

You can solve this question by iterating through the input array from left to right once.

</details>

<details>
<summary><b>Hint 2</b></summary>

Try iterating through the input array from left to right, in search of two adjacent integers that can indicate whether the array is trending upward or downward. Once you've found the tentative trend of the array, at each element thereafter, compare the element to the previous one; if this comparison breaks the previously identified trend, the array isn't monotonic.

</details>

<details>
<summary><b>Hint 3</b></summary>

Alternatively, you can start by assuming that the array is both entirely non-decreasing and entirely non-increasing. As you iterate through each element, perform a check to see if you can invalidate one or both of your assumptions.

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the length of the array.
