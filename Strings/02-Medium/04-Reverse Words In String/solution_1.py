# Description:

"""
                                       Reverse Words In String

Write a function that takes in a string of words separated by one or more whitespaces and returns a string that
has these words in reverse order. For example, given the string `"tim is great"`, your function should return `"great is tim"`.

For this problem, a word can contain special characters, punctuation, and numbers. The words in the string will be
separated by one or more whitespaces, and the reversed string must contain the same whitespaces as the original string.
For example, given the string `"whitespaces    4"` you would be expected to return `"4    whitespaces"`.

Note that you're not allowed to to use any built-in `split` or `reverse` methods/functions. However, you are allowed
to use a built-in `join` method/function.

Also note that the input string isn't guaranteed to always contain words.


## Sample Input:
```
string = "AlgoExpert is the best!"
```

## Sample Output:
```
"best! the is AlgoExpert"
```

## Optimal Time & Space Complexity:
```
`O(n)` time | `O(n)` space - where `n` is the length of the string.
```

"""

# =============================================================================================== #

# Solution


# `O(n)` time | `O(n)` space - where `n` is the length of the string.
def reverse_words_in_string(string):
    words = []
    start_of_word = 0

    for idx in range(len(string)):
        character = string[idx]

        if character == " ":
            words.append(string[start_of_word:idx])
            start_of_word = idx
        elif string[start_of_word] == " ":
            words.append(" ")
            start_of_word = idx

    words.append(string[start_of_word:])

    reverse_list(words)
    return "".join(words)


def reverse_list(my_list):
    start, end = 0, len(my_list) - 1

    while start < end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1


# Test Case 1
print(reverse_words_in_string("AlgoExpert is the best!"))
# Output: "best! the is AlgoExpert"

# Test Case 2
print(reverse_words_in_string("Reverse These Words"))
# Output: "Words These Reverse"

# Test Case 2
print(reverse_words_in_string("his      string     has a     lot of   whitespace"))
# Output: "whitespace   of lot     a has     string      his"

# =============================================================================================== #

# Big O:

"""

"""
