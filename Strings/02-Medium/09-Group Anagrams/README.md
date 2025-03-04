# Group Anagrams

Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, `"cinema"` and `"iceman"` are anagrams; similarly, `"foo"` and `"ofo"` are anagrams.

Your function should return a list of anagram groups in no particular order.

## Sample Input

```plaintext
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
```

## Sample Output

```plaintext
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
```

## Optimal Time & Space Complexity

`O(w * n * log(n))` time | `O(wn)` space - where `w` is the number of words and `n` is the length of the longest word.
