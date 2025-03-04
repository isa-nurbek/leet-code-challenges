# Common Characters

Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common to all strings in the list, ignoring multiplicity.

Note that the strings are not guaranteed to only contain alphanumeric characters. The list you return can be in any order.

## Sample Input

```plaintext
strings = ["abc", "bcd", "cbaccd"]
```

## Sample Output

```plaintext
["b", "c"] // The characters could be ordered differently.
```

## Optimal Space & Time Complexity

`O(n * m)` time | `O(m)` space - where `n` is the number of strings, and `m` is the length of the longest string.
