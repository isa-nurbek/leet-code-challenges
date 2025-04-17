# Longest Palindromic Substring

Write a function that, given a string, returns its longest palindromic substring.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

You can assume that there will only be one longest palindromic substring.

## Sample Input

```plaintext
string = "abaxyzzyxf"
```

## Sample Output

```plaintext
"xyzzyx"
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Try generating all possible substrings of the input string and checking for their palindromic. What is the runtime of the is_palindrome check? What is the total runtime of this approach?

</details>

<details>
<summary><b>Hint 2</b></summary>

Recognize that a palindrome is a string that is symmetrical with respect to its center, which can either be a character (in the case of odd-length palindromes) or an empty string (in the case of even-length palindromes). Thus, you can check the palindromic of a string by simply expanding from its center and making sure that characters on both sides are indeed mirrored.

</details>

<details>
<summary><b>Hint 3</b></summary>

Traverse the input string, and at each index, apply the logic mentioned in Hint #2. What does this accomplish? Is the runtime of this approach better?

</details>

## Optimal Time & Space Complexity

`O(n^2)` time | `O(n)` space - where `n` is the length of the input string.
