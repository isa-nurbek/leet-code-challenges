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
    characters = [char for char in string]
    reverse_list_range(characters, 0, len(characters) - 1)

    start_of_word = 0
    while start_of_word < len(characters):
        end_of_word = start_of_word

        while end_of_word < len(characters) and characters[end_of_word] != " ":
            end_of_word += 1

        reverse_list_range(characters, start_of_word, end_of_word - 1)
        start_of_word = end_of_word + 1

    return "".join(characters)


def reverse_list_range(my_list, start, end):
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
