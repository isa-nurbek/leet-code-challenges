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


# `O(n)` time | `O(1)` space - where `n` is the length of shorter string
def one_edit(string_one, string_two):
    # Get the lengths of both strings
    length_one, length_two = len(string_one), len(string_two)

    # If the difference in lengths is more than 1, more than one edit is needed
    if abs(length_one - length_two) > 1:
        return False

    made_edit = False
    index_one = 0
    index_two = 0

    while index_one < length_one and index_two < length_two:
        if string_one[index_one] != string_two[index_two]:
            if made_edit:
                return False
            made_edit = True

            if length_one > length_two:
                index_one += 1
            elif length_two > length_one:
                index_two += 1
            else:
                index_one += 1
                index_two += 1
        else:
            index_one += 1
            index_two += 1

    return True


# Test Case 1
print(one_edit("hello", "hollo"))  # Output: True

# Test Case 2
print(one_edit("abc", "b"))  # Output: False

# Test Case 3
print(one_edit("abcdefghijk", "abcdefghijk"))  # Output: True
