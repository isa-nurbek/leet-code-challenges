# Description:

"""
                                    One Edit

You're given two strings `stringOne` and `stringTwo`. Write a function that determines if these two
strings can be made equal using only one edit.

There are 3 possible edits:

- **Replace:** One character in one string is swapped for a different character.
- **Add:** One character is added at any index in one string.
- **Remove:** One character is removed at any index in one string.

Note that both strings will contain at least one character. If the strings are the same, your function should return true.


## Sample Input:
```
stringOne = "hello"
stringTwo = "hollo"
```

## Sample Output:
```
True // A single replace at index 1 of either string can make the strings equal
```

## Optimal Time & Space Complexity:
```
`O(n)` time | `O(1)` space - where `n` is the length of the shorter string.
```

"""

# =============================================================================================== #

# Solution


# `O(n + m)` time | `O(n + m)` space - where `n` is the length of stringOne, and
# `m` is the length of stringTwo
def one_edit(string_one, string_two):
    length_one, length_two = len(string_one), len(string_two)

    if abs(length_one - length_two) > 1:
        return False

    for i in range(min(length_one, length_two)):
        if string_one[i] != string_two[i]:
            if length_one > length_two:
                return string_one[i + 1 :] == string_two[i:]
            elif length_two > length_one:
                return string_one[i:] == string_two[i + 1 :]
            else:
                return string_one[i + 1 :] == string_two[i + 1 :]

    return True


# Test Case 1
print(one_edit("hello", "hollo"))  # Output: True

# Test Case 2
print(one_edit("abc", "b"))  # Output: False

# Test Case 3
print(one_edit("abcdefghijk", "abcdefghijk"))  # Output: True
