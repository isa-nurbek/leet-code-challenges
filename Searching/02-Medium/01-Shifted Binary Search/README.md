# Shifted Binary Search

Write a function that takes in a sorted array of distinct integers as well as a target integer. The caveat is that the integers in the array have been shifted by some amount; in other words, they've been moved to the left or to the right by one or more positions. For example, `[1, 2, 3, 4]` might have turned into `[3, 4, 1, 2]`.

The function should use a variation of the `Binary Search` algorithm to determine if the target integer is contained in the array and should return its `index` if it is, otherwise `-1`.

## Sample Input

```plaintext
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
```

## Sample Output

```plaintext
8
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

The Binary Search algorithm involves a left pointer and a right pointer and using those pointers to find the middle number in an array. Unlike with a normal sorted array however, you cannot simply find the middle number of the array and compare it to the target here, because the shift could lead you in the wrong direction. Instead, realize that whenever you find the middle number in the array, the following two scenarios are possible (assuming the middle number is not equal to the target number, in which case you're done): either the left-pointer number is smaller than or equal to the middle number, or it is bigger. Figure out a way to eliminate half of the array depending on the scenario.

</details>

<details>
<summary><b>Hint 2</b></summary>

In the scenario where the left-pointer number is smaller than or equal to the middle number, two other scenarios can arise: either the target number is smaller than the middle number and greater than or equal to the left-pointer number, or it's not. In the first scenario, the right half of the array can be eliminated; in the second scenario, the left half can be eliminated. Figure out the scenarios that can arise if the left-pointer number is greater than the middle number and apply whatever logic you come up with recursively until you find the target number or until you run out of numbers in the array.

</details>

<details>
<summary><b>Hint 3</b></summary>

Can you implement this algorithm `iteratively`? Are there any advantages to doing so?

</details>

## Optimal Time & Space Complexity

`O(log(n))` time | `O(1)` space - where `n` is the length of the input array.
