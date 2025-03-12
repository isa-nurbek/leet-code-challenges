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

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The time complexity of the `longest_balanced_substring` function is **O(n)**, where `n` is the length of the input string.
This is because the function iterates through the string once, performing constant-time operations (pushing and popping
from the stack) for each character.

### Space Complexity:

The space complexity is **O(n)** in the worst case. This occurs when the stack grows to store indices of all opening
parentheses in the string (e.g., for a string like `(((((`). However, in balanced cases, the stack size remains small.

### Final Answer:
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### Explanation of `longest_balanced_substring` Function

The function `longest_balanced_substring(string)` finds the length of the longest contiguous balanced substring
of parentheses. A balanced substring consists of properly nested and matched `(` and `)`. 

---
## **Step-by-Step Breakdown**
### **1. Initial Setup**
```
max_length = 0
idx_stack = []
idx_stack.append(-1)
```
- `max_length` stores the length of the longest balanced substring found so far.
- `idx_stack` is a stack that stores indices of unmatched parentheses. It helps in tracking the start of a valid balanced substring.
- `idx_stack.append(-1)`: This is an important trick! It helps calculate the length correctly when a balanced substring starts
from index `0`.

---
### **2. Iterating Through the String**
```
for i in range(len(string)):
```
- We loop through each character in `string`, tracking its index `i`.

#### **Case 1: If Current Character is `(`**
```
if string[i] == "(":
    idx_stack.append(i)
```
- If `(` is encountered, we store its index in the stack. It might be a potential start of a balanced substring.

#### **Case 2: If Current Character is `)`**
```
else:
    idx_stack.pop()
```
- If `)` is encountered, we remove (pop) the most recent `(` (if any) from the stack, because it forms a pair.

---
### **3. Handling the Stack after `pop()`**
```
if len(idx_stack) == 0:
    idx_stack.append(i)
```
- If the stack becomes empty after popping, it means the `)` we encountered does not have a matching `(` before it.
- We push the index `i` of this unmatched `)` into the stack to serve as a new "starting boundary" for future balanced substrings.

---
### **4. Updating Maximum Length**
```
else:
    balanced_substring_start_idx = idx_stack[len(idx_stack) - 1]
    current_length = i - balanced_substring_start_idx
    max_length = max(max_length, current_length)
```
- If the stack is not empty, the top of the stack contains the last unmatched `)` (or the `-1` we initially added).
- The start index of the current balanced substring is found using:
  ```
  balanced_substring_start_idx = idx_stack[len(idx_stack) - 1]
  ```
- The length of the current balanced substring is:
  ```
  current_length = i - balanced_substring_start_idx
  ```
- We update `max_length` if `current_length` is greater than the previous max.

---
### **5. Returning the Result**
```
return max_length
```
- Finally, we return the maximum balanced substring length found.

---
## **Example Walkthrough**

### **Example 1: `"(()))("`**

#### **Initial Values**
- `max_length = 0`
- `idx_stack = [-1]`

#### **Processing Each Character**

| Index | Char | Stack Before | Stack After  | max_length     | Explanation                                      |
|-------|------|--------------|--------------|----------------|--------------------------------------------------|
| 0     | `(`  | `[-1]`       | `[-1, 0]`    | `0`            | Push `0` (index of `(`)                          |
| 1     | `(`  | `[-1, 0]`    | `[-1, 0, 1]` | `0`            | Push `1`                                         |
| 2     | `)`  | `[-1, 0, 1]` | `[-1, 0]`    | `2 - 0 = 2`    | Pop `1`, valid substring `( )`, length = 2       |
| 3     | `)`  | `[-1, 0]`    | `[-1]`       | `3 - (-1) = 4` | Pop `0`, valid substring `( ( ) )`, length = 4   |
| 4     | `)`  | `[-1]`       | `[4]`        | `4`            | Stack empty, push `4`                            |
| 5     | `(`  | `[4]`        | `[4, 5]`     | `4`            | Push `5`                                         |

#### **Final Result**
- `max_length = 4`
- **Output: `4`**

---
### **Example 2: `"((()))()()()()()()()()()()"`**

- The entire string is balanced.
- **Output: `26`** (since the full length of the string is 26).

---
### **Example 3: `"(("`**

- No `)` is present, so no balanced substring can be formed.
- **Output: `0`**.

---
## **Time and Space Complexity**
- **Time Complexity:** O(n), since we traverse the string once.
- **Space Complexity:** O(n), due to the stack storing indices.

---
### **Final Summary**
- Uses a stack to track unmatched `(` and `)`.
- Updates max balanced substring length dynamically.
- Handles edge cases like unmatched `)` and `(` at the beginning or end.

This is an efficient and optimal way to find the longest balanced substring of parentheses. 

"""
