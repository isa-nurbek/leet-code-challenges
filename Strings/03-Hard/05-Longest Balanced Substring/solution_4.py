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

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity

The time complexity of the `longest_balanced_substring` function is determined by the two calls to
`get_longest_balanced_in_direction`, which scans the string in both directions (left-to-right and right-to-left).

1. **Scanning the string in one direction**: The `get_longest_balanced_in_direction` function iterates through the string once,
either from left to right or from right to left. This operation takes O(n) time, where `n` is the length of the string.

2. **Scanning the string in both directions**: Since the `longest_balanced_substring` function calls
`get_longest_balanced_in_direction` twice (once for each direction), the total time complexity is O(n) + O(n) = O(n).

Thus, the **time complexity** of the algorithm is **O(n)**.

---

### Space Complexity

The space complexity is determined by the additional memory used by the algorithm, excluding the input string.

1. **Variables**: The algorithm uses a constant number of variables (`start_idx`, `step`, `max_length`, `opening_count`,
`closing_count`, `idx`, etc.), which do not depend on the size of the input string.

2. **No additional data structures**: The algorithm does not use any additional data structures like stacks, arrays,
or hash maps that grow with the input size.

Thus, the **space complexity** of the algorithm is **O(1)**.

---

### Summary

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

This is an efficient solution for finding the longest balanced substring in a string of parentheses.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This Python function finds the length of the longest balanced (valid) substring of parentheses in a given string.
It does this by scanning the string in two directions: left-to-right and right-to-left.

---

## **Understanding the Code**

### **1. Main Function: `longest_balanced_substring(string)`**
This function calls another helper function, `get_longest_balanced_in_direction()`, twice:
- **Once scanning left-to-right**
- **Once scanning right-to-left**

It then returns the maximum result from both directions.

### **2. Helper Function: `get_longest_balanced_in_direction(string, left_to_right)`**
This function finds the longest balanced substring in a single direction.

#### **Parameters:**
- `string`: The input string consisting of `(` and `)`.
- `left_to_right`: A boolean flag indicating the scanning direction:
  - `True` → Left-to-right (`(` is treated as the opening bracket).
  - `False` → Right-to-left (`)` is treated as the opening bracket).

#### **Variables:**
- `opening_parens`: Decides which character is treated as the opening parenthesis based on the scanning direction.
- `start_idx`: Sets the starting index (`0` for left-to-right, `len(string) - 1` for right-to-left).
- `step`: Determines iteration direction (`1` for left-to-right, `-1` for right-to-left).
- `max_length`: Keeps track of the longest balanced substring found.
- `opening_count`: Counts the opening parentheses.
- `closing_count`: Counts the closing parentheses.

---

### **Step-by-Step Execution:**
#### **Iterating through the string**
1. Loop through the string from `start_idx` with the given `step`.
2. If the character is an opening parenthesis (based on the `opening_parens` variable), increase `opening_count`.
3. If the character is a closing parenthesis, increase `closing_count`.

#### **Checking for a Balanced Substring**
4. If `opening_count == closing_count`, update `max_length` with the current balanced substring length (`closing_count * 2`).
5. If `closing_count > opening_count`, reset both counts to `0` (invalid sequence, must start fresh).

#### **Returning the Max Length**
After the loop, the function returns `max_length`.

---

## **Why Two Passes (Left-to-Right and Right-to-Left)?**
- A single pass from left-to-right does **not** handle cases where there are extra opening brackets.
- Scanning again from right-to-left ensures we count balanced substrings even if the imbalance is due to excessive opening brackets.

---

## **Example Walkthrough**

### **Example 1: `"(()))("`**

#### **First Pass (Left to Right)**
1. `"("` → `opening_count = 1, closing_count = 0`
2. `"("` → `opening_count = 2, closing_count = 0`
3. `")"` → `opening_count = 2, closing_count = 1`
4. `")"` → `opening_count = 2, closing_count = 2` (**Balanced** → `max_length = 4`)
5. `")"` → `closing_count = 3` (reset)
6. `"("` → `opening_count = 1, closing_count = 0`

**Max Length So Far** = 4

#### **Second Pass (Right to Left)**
- This won't improve the `max_length`, so final result is **4**.

**Final Output:** `4`

---

### **Example 2: `"((()))()()()()()()()()()()"`**

- Left-to-right scan finds a **fully balanced** sequence of **26 characters**.
- Right-to-left scan doesn't change anything.
  
**Final Output:** `26`

---

### **Example 3: `"(("`**

- Left-to-right: No closing `)`, so no balanced substring.
- Right-to-left: No closing `)`, so no balanced substring.
  
**Final Output:** `0`

---

## **Time Complexity**
- Each scan is **O(N)**, so total complexity is **O(N)**.

## **Space Complexity**
- **O(1)** (only uses a few variables).

"""
