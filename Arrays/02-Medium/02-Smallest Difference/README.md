# Smallest Difference

Write a function that takes in two `non-empty` arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of `-5` and `5` is `10`, and the absolute difference of `-5` and `-4` is `1`.

You can assume that there will only be one pair of numbers with the smallest difference.

## Sample Input

```plaintext
array_one = [-1, 5, 10, 20, 28, 3]
array_two = [26, 134, 135, 15, 17]
```

## Sample Output

```plaintext
[28, 26]
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Instead of generating all possible pairs of numbers, try somehow only looking at pairs that you know could actually have the smallest difference. How can you accomplish this?

</details>

<details>
<summary><b>Hint 2</b></summary>

Would it help if the two arrays were sorted? If the arrays were sorted and you were looking at a given pair of numbers, could you efficiently find the next pair of numbers to look at? What are the runtime implications of sorting the arrays?

</details>

<details>
<summary><b>Hint 3</b></summary>

Start by sorting both arrays, as per `Hint #2`. Put a pointer at the beginning of both arrays and evaluate the absolute difference of the pointer-numbers. If the difference is equal to zero, then you've found the closest pair; otherwise, increment the pointer of the smaller of the two numbers to find a potentially better pair. Continue until you get a pair with a difference of zero or until one of the pointers gets out of range of its array.

</details>

## Optimal Time & Space Complexity

`O(n log(n) + m log(m))` time | `O(1)` space - where `n` is the length of the first input array and `m` is the length of the second input array.
