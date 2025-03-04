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


# O(w * n * log(n) + n * w * log(w)) time | O(wn) space - where `w` is the number of words
# and `n` is the length of the longest word
def group_anagrams(words):
    if len(words) == 0:
        return []

    sorted_words = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sorted_words[x])

    result = []
    current_anagram_group = []
    current_anagram = sorted_words[indices[0]]

    for index in indices:
        word = words[index]
        sorted_word = sorted_words[index]

        if sorted_word == current_anagram:
            current_anagram_group.append(word)
            continue

        result.append(current_anagram_group)
        current_anagram_group = [word]
        current_anagram = sorted_word

    result.append(current_anagram_group)

    return result


words_1 = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
words_2 = ["abc", "dabd", "bca", "cab", "ddba"]
words_3 = []

# Test Cases
print(group_anagrams(words_1))
# [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

print(group_anagrams(words_2))  # ['abc', 'bca', 'cab'], ['dabd', 'ddba']]
print(group_anagrams(words_3))  # []

# =============================================================================================== #

# Big O:
