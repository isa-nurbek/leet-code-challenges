# Smallest Substring Containing

You're given two non-empty strings: a big string and a small string. Write a function that returns the smallest substring in the big string that contains all of the small string's characters.

Note that:

- The substring can contain other characters not found in the small string.
  
- The characters in the substring don't have to be in the same order as they appear in the small string.
  
- If the small string has duplicate characters, the substring has to contain those duplicate characters (it can also contain more, but not fewer).
  
You can assume that there will only be one relevant smallest substring.

## Sample Input

```plaintext
bigString = "abcd$ef$axb$c$"
smallString = "$$abf"
```

## Sample Output

```plaintext
"f$axb$"
```

## Optimal Time & Space Complexity

`O(b + s)` time | `O(b + s)` space - where `b` is the length of the big input string and `s` is the length of the small input string.
