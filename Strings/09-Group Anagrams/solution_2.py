# Description:

"""
                            Group Anagrams

Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example,
"cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.


## Sample Input:
```
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
```

## Sample Output:
```
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
```

## Optimal Time & Space Complexity:
```
`O(w * n * log(n))` time | `O(wn)` space - where `w` is the number of words
and `n` is the length of the longest word.
```

"""

# =============================================================================================== #

# Solution


# O(w * n * log(n) time | O(w * n) space - where `w` is the number of words
# and `n` is the length of the longest word
def group_anagrams(words):
    anagrams = {}

    for word in words:
        sorted_word = "".join(sorted(word))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())


# Test Cases
words_1 = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
words_2 = ["abc", "dabd", "bca", "cab", "ddba"]
words_3 = []

# Test Case 1
print(group_anagrams(words_1))
# Expected Output: [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

# Test Case 2
print(group_anagrams(words_2))
# Expected Output: [['abc', 'bca', 'cab'], ['dabd', 'ddba']]

# Test Case 3 (Empty Input)
print(group_anagrams(words_3))
# Expected Output: []
