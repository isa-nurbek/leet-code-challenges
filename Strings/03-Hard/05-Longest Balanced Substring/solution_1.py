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

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity

1. **Outer Loop (`for i in range(len(string))`)**:
   - This loop runs `n` times, where `n` is the length of the input string.

2. **Inner Loop (`for j in range(i + 2, len(string) + 1, 2)`)**:
   - For each `i`, the inner loop runs approximately `(n - i) / 2` times. In the worst case, this is roughly `n/2` iterations.

3. **`is_balanced` Function**:
   - The `is_balanced` function iterates over the substring `string[i:j]`, which has a length of `j - i`.
   In the worst case, this is `O(n)`.

4. **Overall Time Complexity**:
   - The outer loop runs `n` times.
   - The inner loop runs roughly `n/2` times for each `i`.
   - The `is_balanced` function runs in `O(n)` for each substring.
   
   - Therefore, the total time complexity is:
     
        O(n ⋅ n / 2 ⋅ n)= O(n^3)
     
### Space Complexity

1. **`is_balanced` Function**:
   - The `open_parens_stack` can grow up to `O(n)` in the worst case (if the string is all opening parentheses).

2. **Overall Space Complexity**:
   - The space complexity is dominated by the stack used in the `is_balanced` function, which is `O(n)`.

### Summary

- **Time Complexity**: O(n^3)
- **Space Complexity**: O(n)

### Optimized Approach

The above solution is not efficient for large inputs due to its cubic time complexity. A more efficient approach
would involve using a stack or a two-pointer technique to achieve a linear time complexity O(n).
We will use it in future examples.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### Explanation of the Code

The code provided aims to find the length of the longest balanced substring in a given string of parentheses.
A balanced substring is one where every opening parenthesis `(` has a corresponding closing parenthesis `)`
and they are properly nested.

Let's break down the code step by step:

---

### 1. **`longest_balanced_substring` Function**

This function is responsible for finding the longest balanced substring in the input string.

#### Key Steps:
1. **Initialization**:
   - `max_length` is initialized to `0`. This will store the length of the longest balanced substring found.

2. **Nested Loops**:
   - The outer loop (`for i in range(len(string))`) iterates over each character in the string, treating it as
   the starting index of a potential substring.
   
   - The inner loop (`for j in range(i + 2, len(string) + 1, 2)`) iterates over possible ending indices of the
   substring. The step size of `2` ensures that only even-length substrings are considered (since balanced
   substrings must have an even length).

3. **Check for Balanced Substring**:
   - For each substring `string[i:j]`, the `is_balanced` function is called to check if it is balanced.
   - If the substring is balanced, its length (`j - i`) is calculated and compared with `max_length`.
   If it is longer, `max_length` is updated.

4. **Return Result**:
   - After all possible substrings have been checked, the function returns `max_length`, which is the length
   of the longest balanced substring found.

---

### 2. **`is_balanced` Function**

This function checks whether a given substring is balanced.

#### Key Steps:
1. **Initialization**:
   - `open_parens_stack` is initialized as an empty list. This stack will be used to keep track of opening parentheses `(`.

2. **Iterate Through the Substring**:
   - For each character in the substring:
     - If the character is `(`, it is pushed onto the stack.
     - If the character is `)`:
       - If the stack is not empty, the top element (an opening parenthesis) is popped from the stack (indicating a match).
       - If the stack is empty, the substring is unbalanced, so the function returns `False`.

3. **Final Check**:
   - After processing all characters, the function checks if the stack is empty. If it is, the substring is balanced,
   so the function returns `True`. Otherwise, it returns `False`.

---

### 3. **How It Works**

- The `longest_balanced_substring` function generates all possible even-length substrings of the input string.
- For each substring, the `is_balanced` function checks if it is balanced using a stack-based approach.
- The length of the longest balanced substring is tracked and returned.

---

### 5. **Test Cases**

#### Test Case 1:
```
print(longest_balanced_substring("(()))("))
# Output: 4
```
- The longest balanced substring is `"(())"`, which has a length of `4`.

#### Test Case 2:
```
print(longest_balanced_substring("((()))()()()()()()()()()()"))
# Output: 26
```
- The entire string is balanced, so the longest balanced substring is the string itself, with a length of `26`.

#### Test Case 3:
```
print(longest_balanced_substring("(("))
# Output: 0
```
- There are no balanced substrings, so the output is `0`.

---

### 6. **Optimization**

The current implementation has a high time complexity O(n³). This can be optimized to **O(n)** using a
more efficient approach, such as:
- Using a stack to track indices of unmatched parentheses.
- Using a two-pointer approach to find the longest valid substring.

"""
