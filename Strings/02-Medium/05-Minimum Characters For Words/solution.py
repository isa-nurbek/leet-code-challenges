# Description:

"""
                                       Minimum Characters For Words

Write a function that takes in an array of words and returns the smallest array of characters needed to form
all of the words. The characters don't need to be in any particular order.

For example, the characters `["y", "r", "o", "u"]` are needed to form the words `["your", "you", "or", "yo"]`.

Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.


## Sample Input:
```
words = ["this", "that", "did", "deed", "them!", "a"]
```

## Sample Output:
```
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
// The characters could be ordered differently.
```

## Optimal Time & Space Complexity:
```
`O(n * l)` time | `O(c)` space - where `n` is the number of words, `l` is the length of the longest word,
and `c` is the number of unique characters across all words.
```

"""

# =============================================================================================== #

# Solution


# `O(n * l)` time | `O(c)` space - where `n` is the number of words,
# `l` is the length of the longest word,
# and `c` is the number of unique characters across all words.
def minimum_characters_for_words(words):
    maximum_character_frequencies = {}

    for word in words:
        character_frequencies = count_character_frequencies(word)
        update_maximum_frequencies(character_frequencies, maximum_character_frequencies)

    return make_array_from_character_frequencies(maximum_character_frequencies)


def count_character_frequencies(string):
    character_frequencies = {}

    for character in string:
        if character not in character_frequencies:
            character_frequencies[character] = 0

        character_frequencies[character] += 1

    return character_frequencies


def update_maximum_frequencies(frequencies, maximum_frequencies):
    for character in frequencies:
        frequency = frequencies[character]

        if character in maximum_frequencies:
            maximum_frequencies[character] = max(
                frequency, maximum_frequencies[character]
            )
        else:
            maximum_frequencies[character] = frequency


def make_array_from_character_frequencies(character_frequencies):
    characters = []

    for character in character_frequencies:
        frequency = character_frequencies[character]

        for _ in range(frequency):
            characters.append(character)

    return characters


# Test Case 1
print(minimum_characters_for_words(["this", "that", "did", "deed", "them!", "a"]))
# Output: ['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']

# Test Case 2
print(minimum_characters_for_words(["a", "abc", "ab", "boo"]))
# Output: ['a', 'b', 'c', 'o', 'o']

# Test Case 3
print(minimum_characters_for_words(["!!!2", "234", "222", "432"]))
# Output: ['!', '!', '!', '2', '2', '2', '3', '4']
