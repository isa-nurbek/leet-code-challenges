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


# O(n) time | O(n) space - where `n` is the length of the input string.
def longest_balanced_substring(string):
    # Initialize the maximum length of the balanced substring found so far.
    max_length = 0

    # Use a stack to keep track of indices of characters in the string.
    # Start by pushing -1 onto the stack to handle edge cases where the balanced substring starts from the beginning.
    idx_stack = []
    idx_stack.append(-1)

    # Iterate through each character in the string.
    for i in range(len(string)):
        # If the current character is '(', push its index onto the stack.
        if string[i] == "(":
            idx_stack.append(i)
        else:
            # If the current character is ')', pop the top element from the stack.
            # This represents matching the current ')' with the last unmatched '('.
            idx_stack.pop()

            # If the stack is empty after popping, it means we have an extra ')'.
            # Push the current index onto the stack to mark the new starting point for potential balanced substrings.
            if len(idx_stack) == 0:
                idx_stack.append(i)
            else:
                # If the stack is not empty, calculate the length of the current balanced substring.
                # The start index of the current balanced substring is the index at the top of the stack.
                balanced_substring_start_idx = idx_stack[len(idx_stack) - 1]

                # Calculate the length of the current balanced substring.
                current_length = i - balanced_substring_start_idx

                # Update the maximum length if the current balanced substring is longer.
                max_length = max(max_length, current_length)

    # Return the length of the longest balanced substring found.
    return max_length


# Test Cases:

print(longest_balanced_substring("(()))("))
# Output: 4

print(longest_balanced_substring("((()))()()()()()()()()()()"))
# Output: 26

print(longest_balanced_substring("(("))
# Output: 0

# =========================================================================================================================== #
