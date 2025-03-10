# Description:

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
`O(n)` time | `O(1)` space - where `n` is the length of the input string.
```

"""

# =============================================================================================== #

# Solution:

# O(n^3) time | O(n) space - where `n` is the length of the input string.
def longest_balanced_substring(string):
    # Initialize the maximum length of a balanced substring to 0
    max_length = 0
    
    # Iterate over all possible starting positions of a substring
    for i in range(len(string)):
        # Iterate over all possible ending positions of a substring, starting from i + 2
        # and incrementing by 2 each time (since balanced substrings must have even length)
        for j in range(i + 2, len(string) + 1, 2):
            # Check if the substring from i to j is balanced
            if is_balanced(string[i:j]):
                # If it is balanced, calculate its length
                current_length = j - i
                
                # Update the maximum length if the current substring is longer
                max_length = max(max_length, current_length)
                
    # Return the length of the longest balanced substring found
    return max_length

            
def is_balanced(string):
    # Initialize a stack to keep track of open parentheses
    open_parens_stack = []
    
    # Iterate over each character in the string
    for char in string:
        # If the character is an open parenthesis, push it onto the stack
        if char == "(":
            open_parens_stack.append("(")
        # If the character is a close parenthesis, pop from the stack
        # (assuming it matches an open parenthesis)
        elif len(open_parens_stack) > 0:
            open_parens_stack.pop()
        else:
            # If there's no matching open parenthesis, the string is not balanced
            return False
        
    # The string is balanced if the stack is empty (all open parentheses have been matched)
    return len(open_parens_stack) == 0

# Test Cases:

print(longest_balanced_substring("(()))("))
# Output: 4

print(longest_balanced_substring("((()))()()()()()()()()()()"))
# Output: 26

print(longest_balanced_substring("(("))
# Output: 0



# =============================================================================================== #