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


# O(n) time | O(1) space - where `n` is the length of the input string
def longest_balanced_substring(string):
    # The function returns the maximum length of a balanced substring by checking
    # both directions (left-to-right and right-to-left) and returning the larger value.
    return max(
        get_longest_balanced_in_direction(string, True),  # Check left-to-right
        get_longest_balanced_in_direction(string, False),  # Check right-to-left
    )


def get_longest_balanced_in_direction(string, left_to_right):
    # Determine the opening parenthesis based on the direction of traversal.
    # If left_to_right is True, we look for '(' as the opening parenthesis.
    # If left_to_right is False, we look for ')' as the opening parenthesis.
    opening_parens = "(" if left_to_right else ")"

    # Set the starting index and step based on the direction of traversal.
    # If left_to_right is True, start at the beginning (index 0) and move forward.
    # If left_to_right is False, start at the end (index len(string) - 1) and move backward.
    start_idx = 0 if left_to_right else len(string) - 1
    step = 1 if left_to_right else -1

    # Initialize the maximum length of a balanced substring found so far.
    max_length = 0

    # Initialize counters for the number of opening and closing parentheses.
    opening_count = 0
    closing_count = 0

    # Start traversing the string from the specified starting index.
    idx = start_idx
    while idx >= 0 and idx < len(string):
        char = string[idx]

        # If the current character is the opening parenthesis, increment the opening count.
        if char == opening_parens:
            opening_count += 1
        # Otherwise, increment the closing count.
        else:
            closing_count += 1

        # If the number of opening and closing parentheses is equal, we have a balanced substring.
        # Update the maximum length if this balanced substring is longer than the previous maximum.
        if opening_count == closing_count:
            max_length = max(max_length, closing_count * 2)
        # If the closing count exceeds the opening count, reset the counters.
        # This is because the substring up to this point cannot be balanced.
        elif closing_count > opening_count:
            opening_count = 0
            closing_count = 0

        # Move to the next character in the specified direction.
        idx += step

    # Return the maximum length of a balanced substring found in this direction.
    return max_length


# Test Cases:

print(longest_balanced_substring("(()))("))
# Output: 4

print(longest_balanced_substring("((()))()()()()()()()()()()"))
# Output: 26

print(longest_balanced_substring("(("))
# Output: 0

# =========================================================================================================================== #
