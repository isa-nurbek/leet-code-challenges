# First Non-Repeating Character

Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string doesn't have any non-repeating characters, your function should return `-1`.

## Sample Input

```plaintext
string = "abcdcaf"
```

## Sample Output

```plaintext
1 // The first non-repeating character is "b" and is found at index 1.
```

## Optimal Time & Space Complexity

`O(n)` time | `O(1)` space - where `n` is the length of the input string The constant space is because the input string only has lowercase English-alphabet letters; thus, our hash table will never have more than `26` character frequencies.
