# Palindrome Check

Write a function that takes in a `non-empty` string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

## Sample Input

```plaintext
string = "abcdcba"
```

## Sample Output

```plaintext
True

// It's written the same forward and backward.
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Start by building the input string in reverse order and comparing this newly built string to the input string. Can you do this without using string concatenations?

</details>

<details>
<summary><b>Hint 2</b></summary>

Can you optimize your algorithm by using recursion? What are the implications of recursion on an algorithm's space-time complexity analysis?

</details>

<details>
<summary><b>Hint 3</b></summary>

Go back to an iterative solution and try using pointers to solve this problem: start with a pointer at the first index of the string and a pointer at the final index of the string. What can you do from there?

</details>

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the length of the input string.
