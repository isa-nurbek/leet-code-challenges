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


# O(n * m) time | O(m) space - where `n`` is the number of strings, and `m` is the
# length of the longest string
def common_characters(strings):
    smallest_string = get_smallest_string(strings)
    potential_common_characters = set(smallest_string)

    for string in strings:
        remove_nonexistent_characters(string, potential_common_characters)

    return list(potential_common_characters)


def get_smallest_string(strings):
    smallest_string = strings[0]
    for string in strings:
        if len(string) < len(smallest_string):
            smallest_string = string

    return smallest_string


def remove_nonexistent_characters(string, potential_common_characters):
    unique_string_characters = set(string)

    for character in list(potential_common_characters):
        if character not in unique_string_characters:
            potential_common_characters.remove(character)


print(common_characters(["abc", "bcd", "cbad"]))  # Output: ['b', 'c']
print(common_characters(["a", "b", "c"]))  # Output: []
print(common_characters(["aaaa", "a"]))  # Output: ['a']
print(
    common_characters(["*abc!d", "de!f*", "**!!!****d*****"])
)  # Output: ['d', '!', '*']


# Big O:

"""

### Complexity Analysis



"""

# Code Explanation:

"""


"""
