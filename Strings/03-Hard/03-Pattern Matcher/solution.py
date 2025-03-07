# Description:

"""
                                        Pattern Matcher

You're given two non-empty strings. The first one is a pattern consisting of only `"x"`s and / or `"y"`s; the other
one is a normal string of alphanumeric characters. Write a function that checks whether the normal string matches the pattern.

A string `S0` is said to match a pattern if replacing all `"x"`s in the pattern with some non-empty substring `S1` of `S0`
and replacing all `"y"`s in the pattern with some non-empty substring `S2` of `S0` yields the same string `S0`.

If the input string doesn't match the input pattern, the function should return an empty array; otherwise, it should return
an array holding the strings `S1` and `S2` that represent `"x"` and `"y"` in the normal string, in that order. If the pattern
doesn't contain any `"x"`s or `"y"`s, the respective letter should be represented by an empty string in the final array that
you return.

You can assume that there will never be more than one pair of strings `S1` and `S2` that appropriately represent `"x"` and
`"y"` in the normal string.


## Sample Input:
```
pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"
```

## Sample Output:
```
["go", "powerranger"]
```

## Optimal Time & Space Complexity:
```
`O(n^2 + m)` time | `O(n + m)` space - where `n` is the length of the main string and
`m` is the length of the pattern.
```

"""

# =============================================================================================== #

# Solution:


# `O(n^2 + m)` time | `O(n + m)` space
def pattern_matcher(pattern, string):
    if len(pattern) > len(string):
        return []

    new_pattern = get_new_pattern(pattern)
    did_switch = new_pattern[0] != pattern[0]

    counts = {"x": 0, "y": 0}
    first_y_pos = get_counts_and_first_y_pos(new_pattern, counts)

    if counts["y"] != 0:
        for len_of_x in range(1, len(string)):
            len_of_y = (len(string) - len_of_x * counts["x"]) / counts["y"]

            if len_of_y <= 0 or len_of_y % 1 != 0:
                continue

            len_of_y = int(len_of_y)
            y_idx = first_y_pos * len_of_x

            x = string[:len_of_x]
            y = string[y_idx : y_idx + len_of_y]

            potential_match = map(lambda char: x if char == "x" else y, new_pattern)

            if string == "".join(potential_match):
                return [x, y] if not did_switch else [y, x]
    else:
        len_of_x = len(string) / counts["x"]

        if len_of_x % 1 == 0:
            len_of_x = int(len_of_x)

            x = string[:len_of_x]
            potential_match = map(lambda char: x, new_pattern)

            if string == "".join(potential_match):
                return [x, ""] if not did_switch else ["", x]

    return []


def get_new_pattern(pattern):
    pattern_letters = list(pattern)

    if pattern[0] == "x":
        return pattern_letters
    else:
        return list(map(lambda char: "x" if char == "y" else "y", pattern_letters))


def get_counts_and_first_y_pos(pattern, counts):
    first_y_pos = None

    for i, char in enumerate(pattern):
        counts[char] += 1

        if char == "y" and first_y_pos is None:
            first_y_pos = i

    return first_y_pos


# Test Cases:
pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"

pattern_2 = "xyx"
string_2 = "thisshouldobviouslybewrong"

pattern_3 = "xxxx"
string_3 = "testtesttesttest"

print(pattern_matcher(pattern, string))
# Output: ['go', 'powerranger']

print(pattern_matcher(pattern_2, string_2))
# Output: []

print(pattern_matcher(pattern_3, string_3))
# Output: ['test', '']
