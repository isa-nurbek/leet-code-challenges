# Description:

"""
                                Longest Substring Without Duplication

Write a function that takes in a string and returns its longest substring without duplicate characters.

You can assume that there will only be one longest substring without duplication.


## Sample Input:
```
string = "kilimandjaro"
```

## Sample Output:
```
"limandj"
```

## Optimal Time & Space Complexity:
```
`O(n)` time | `O(min(n, a))` space - where `n` is the length of the input string and `a` is the length of the character alphabet represented in the input string.
```

"""

# =============================================================================================== #

# Solution


# `O(n)` time | `O(1)` space - where `n` is the length of shorter string
def longest_substring_without_duplication(string):
    last_seen = {}
    longest = [0, 1]
    start_idx = 0

    for i, char in enumerate(string):
        if char in last_seen:
            start_idx = max(start_idx, last_seen[char] + 1)

        if longest[1] - longest[0] < i + 1 - start_idx:
            longest = [start_idx, i + 1]
        last_seen[char] = i

    return string[longest[0] : longest[1]]


# Test Case 1
print(longest_substring_without_duplication("kilimandjaro"))  # Output: limandj

# Test Case 2
print(longest_substring_without_duplication("abacacacaaabacaaaeaaafa"))  # Output: bac

# Test Case 3
print(longest_substring_without_duplication("a"))  # Output: a
