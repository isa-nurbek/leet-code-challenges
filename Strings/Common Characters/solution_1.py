# Description:

"""

                                    Common Characters

Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common
to all strings in the list, ignoring multiplicity.

Note that the strings are not guaranteed to only contain alphanumeric characters. The list you return can be in any order.


## Sample Input:
```
strings = ["abc", "bcd", "cbaccd"]
```

## Sample Output:
```
["b", "c"] // The characters could be ordered differently.
```

## Optimal Space & Time Complexity:

`O(n * m)` time | `O(m)` space - where `n` is the number of strings, and `m` is the length of the longest string.

"""


# O(n * m) time | O(c) space - where `n`` is the number of strings, `m` is the
# length of the longest string, and `c` is the number of unique characters across
# all strings
def common_characters(strings):
    character_counts = {}

    for string in strings:
        unique_string_characters = set(string)

        for character in unique_string_characters:
            if character not in character_counts:
                character_counts[character] = 0
            character_counts[character] += 1

    final_characters = []
    for character, count in character_counts.items():
        if count == len(strings):
            final_characters.append(character)

    return final_characters


print(common_characters(["abc", "bcd", "cbad"]))  # Output: ['b', 'c']
print(common_characters(["a", "b", "c"]))  # Output: []
print(common_characters(["aaaa", "a"]))  # Output: ['a']
print(
    common_characters(["*abc!d", "de!f*", "**!!!****d*****"])
)  # Output: ['d', '!', '*']


# Big O:

"""



"""


# Code Explanation:

"""


"""
