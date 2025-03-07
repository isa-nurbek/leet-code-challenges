# Description:

"""
                                    Smallest Substring Containing

You're given two non-empty strings: a big string and a small string. Write a function that returns the smallest
substring in the big string that contains all of the small string's characters.

Note that:

- The substring can contain other characters not found in the small string.

- The characters in the substring don't have to be in the same order as they appear in the small string.

- If the small string has duplicate characters, the substring has to contain those duplicate characters
(it can also contain more, but not fewer).

You can assume that there will only be one relevant smallest substring.


## Sample Input:
```
bigString = "abcd$ef$axb$c$"
smallString = "$$abf"
```

## Sample Output:
```
"f$axb$"
```

## Optimal Time & Space Complexity:
```
`O(b + s)` time | `O(b + s)` space - where `b` is the length of the big input string
and `s` is the length of the small input string.
```

"""

# =============================================================================================== #

# Solution:


# `O(b + s)` time | `O(b + s)` space - where `b` is the length of the big
# input string and `s` is the length of the small input string
def smallest_substring_containing(big_string, small_string):
    target_char_counts = get_char_counts(small_string)
    substring_bounds = get_substring_bounds(big_string, target_char_counts)

    return get_string_from_bounds(big_string, substring_bounds)


def get_char_counts(string):
    char_counts = {}

    for char in string:
        increase_char_count(char, char_counts)

    return char_counts


def get_substring_bounds(string, target_char_counts):
    substring_bounds = [0, float("inf")]
    substring_char_counts = {}

    num_unique_chars = len(target_char_counts.keys())
    num_unique_chars_done = 0

    left_idx = 0
    right_idx = 0

    while right_idx < len(string):
        right_char = string[right_idx]

        if right_char not in target_char_counts:
            right_idx += 1
            continue

        increase_char_count(right_char, substring_char_counts)
        if substring_char_counts[right_char] == target_char_counts[right_char]:
            num_unique_chars_done += 1

        while num_unique_chars_done == num_unique_chars and left_idx <= right_idx:
            substring_bounds = get_closer_bounds(
                left_idx, right_idx, substring_bounds[0], substring_bounds[1]
            )

            left_char = string[left_idx]
            if left_char not in target_char_counts:
                left_idx += 1
                continue

            if substring_char_counts[left_char] == target_char_counts[left_char]:
                num_unique_chars_done -= 1

            decrease_char_count(left_char, substring_char_counts)
            left_idx += 1

        right_idx += 1

    return substring_bounds


def get_closer_bounds(idx_1, idx_2, idx_3, idx_4):
    return [idx_1, idx_2] if idx_2 - idx_1 < idx_4 - idx_3 else [idx_3, idx_4]


def get_string_from_bounds(string, bounds):
    start, end = bounds

    if end == float("inf"):
        return ""

    return string[start : end + 1]


def increase_char_count(char, char_counts):
    if char not in char_counts:
        char_counts[char] = 0
    char_counts[char] += 1


def decrease_char_count(char, char_counts):
    char_counts[char] -= 1


# Test Cases:
big_string = "abcd$ef$axb$c$"
small_string = "$$abf"

big_string_2 = "abcdef"
small_string_2 = "fa"

big_string_3 = "a$fuu+afff+affaffa+a$Affab+a+a+$a$"
small_string_3 = "a+$aaAaaaa$++"

print(smallest_substring_containing(big_string, small_string))
# Output: "f$axb$"

print(smallest_substring_containing(big_string_2, small_string_2))
# Output: "abcdef"

print(smallest_substring_containing(big_string_3, small_string_3))
# Output: "affa+a$Affab+a+a+$a"

# =============================================================================================== #
