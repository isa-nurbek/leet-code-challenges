# Problem Description:

"""
                                    Longest Balanced Substring

Write a function that takes in a string made up of parentheses ( ( and ) ). The function should return an integer
representing the length of the longest balanced substring with regards to parentheses.

A string is said to be balanced if it has as many opening parentheses as it has closing parentheses and if no parenthesis
is unmatched. Note that an opening parenthesis can't match a closing parenthesis that comes before it, and similarly,
a closing parenthesis can't match an opening parenthesis that comes after it.


## Sample Input:
```
string = "(()))("
```

## Sample Output:
```
4 // The longest balanced substring is "(())".
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input string.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space - where `n` is the length of the input string.
def longest_balanced_substring(string):
    # This will store the length of the longest balanced substring found.
    max_length = 0

    # First pass: Traverse the string from left to right.
    opening_count = 0  # Count of opening brackets '('
    closing_count = 0  # Count of closing brackets ')'

    for char in string:
        if char == "(":
            opening_count += 1  # Increment the count of opening brackets.
        else:
            closing_count += 1  # Increment the count of closing brackets.

        # If the number of opening and closing brackets are equal, we have a balanced substring.
        if opening_count == closing_count:
            # Update max_length if the current balanced substring is longer.
            max_length = max(max_length, closing_count * 2)
        # If closing brackets exceed opening brackets, reset the counts.
        # This is because we cannot have a balanced substring if there are more closing brackets.
        elif closing_count > opening_count:
            opening_count = 0
            closing_count = 0

    # Second pass: Traverse the string from right to left.
    # This is necessary to handle cases where the balanced substring starts with more closing brackets.
    opening_count = 0
    closing_count = 0

    for i in reversed(range(len(string))):
        char = string[i]

        if char == "(":
            opening_count += 1  # Increment the count of opening brackets.
        else:
            closing_count += 1  # Increment the count of closing brackets.

        # If the number of opening and closing brackets are equal, we have a balanced substring.
        if opening_count == closing_count:
            # Update max_length if the current balanced substring is longer.
            max_length = max(max_length, opening_count * 2)
        # If opening brackets exceed closing brackets, reset the counts.
        # This is because we cannot have a balanced substring if there are more opening brackets.
        elif opening_count > closing_count:
            opening_count = 0
            closing_count = 0

    return max_length  # Return the length of the longest balanced substring found.


# Test Cases:

print(longest_balanced_substring("(()))("))
# Output: 4

print(longest_balanced_substring("((()))()()()()()()()()()()"))
# Output: 26

print(longest_balanced_substring("(("))
# Output: 0

# =========================================================================================================================== #
