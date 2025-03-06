# One Edit

You're given two strings `stringOne` and `stringTwo`. Write a function that determines if these two strings can be made equal using only one edit.

There are 3 possible edits:

    - **Replace:** One character in one string is swapped for a different character.
    - **Add:** One character is added at any index in one string.
    - **Remove:** One character is removed at any index in one string.
    - 
Note that both strings will contain at least one character. If the strings are the same, your function should return true.

## Sample Input

```plaintext
stringOne = "hello"
stringTwo = "hollo"
```

## Sample Output

```plaintext
True // A single replace at index 1 of either string can make the strings equal
```

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the length of the shorter string.
