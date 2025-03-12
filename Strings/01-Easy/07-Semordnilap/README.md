# Semordnilap

Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.

A semordnilap pair is defined as a set of different strings where the reverse of one word is the same as the forward version of the other. For example the words `"diaper"` and `"repaid"` are a semordnilap pair, as are the words `"palindromes"` and `"semordnilap"`.

The order of the returned pairs and the order of the strings within each pair does not matter.

## Sample Input

```plaintext
words = ["diaper", "abc", "test", "cba", "repaid"]
```

## Sample Output

```plaintext
[["diaper", "repaid"], ["abc", "cba"]]
```

## Optimal Time & Space Complexity

`O(n * m)` time | `O(n)` space - where `n` is the number of words and `m` is the length of the longest word.
