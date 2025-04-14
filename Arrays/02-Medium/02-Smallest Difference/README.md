# Smallest Difference

Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

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
<summary>Hint 1</summary>

Using three for loops to calculate the sums of all possible triplets in the array would generate an algorithm that runs in O(n³) time, where n is the length of the input array. Can you come up with something faster using only two for loops?

</details>

<details>
<summary>Hint 2</summary>

Try sorting the array and traversing it once. At each number, place a left pointer on the number immediately to the right of your current number and a right pointer on the final number in the array. Check if the current number, the left number, and the right number sum up to the target sum. How can you proceed from there, remembering the fact that you sorted the array?

</details>

<details>
<summary>Hint 3</summary>

Since the array is now sorted (see Hint #2), you know that moving the left pointer mentioned in Hint #2 one place to the right will lead to a greater left number and thus a greater sum. Similarly, you know that moving the right pointer one place to the left will lead to a smaller right number and thus a smaller sum. This means that, depending on the size of each triplet's (current number, left number, right number) sum relative to the target sum, you should either move the left pointer, the right pointer, or both to obtain a potentially valid triplet.

</details>

## Optimal Time & Space Complexity

`O(n log(n) + m log(m))` time | `O(1)` space - where `n` is the length of the first input array and `m` is the length of the second input array.
