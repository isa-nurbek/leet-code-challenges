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


# O(n) time | O(1) space
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

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The time complexity of the `longest_balanced_substring` function is **O(n)**, where `n` is the length of the input string.
This is because the function iterates through the string twice:
1. Once from the beginning to the end.
2. Once from the end to the beginning.

Each iteration takes **O(n)** time, and since we perform two passes, the total time complexity remains **O(n)**.

### Space Complexity:

The space complexity of the function is **O(1)**, which means it uses constant extra space. The function only uses a few
variables (`max_length`, `opening_count`, `closing_count`) to keep track of counts and the maximum length, regardless
of the input size. No additional data structures (like stacks or arrays) are used that grow with the input size.

### Summary:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This function, `longest_balanced_substring`, finds the length of the longest balanced substring of parentheses in a given string.
A balanced substring consists of an equal number of opening `(` and closing `)` parentheses, arranged correctly.

---

### **Explanation of the Code**
The function uses two **passes** over the string:
1. **Left-to-right scan**
2. **Right-to-left scan**

Each pass ensures that we correctly count matching pairs of parentheses while preventing cases where closing parentheses `)`
appear before their matching opening `(`.

---

## **Step-by-Step Breakdown**
### **1. Initialization**
```
max_length = 0
opening_count = 0
closing_count = 0
```
- `max_length`: Stores the maximum length of a balanced substring found so far.
- `opening_count`: Tracks the number of `(` encountered.
- `closing_count`: Tracks the number of `)` encountered.

---

## **2. First Pass: Left-to-Right Traversal**
```
for char in string:
    if char == "(":
        opening_count += 1
    else:
        closing_count += 1
```
- If we encounter `(`, we increase `opening_count`.
- If we encounter `)`, we increase `closing_count`.

### **Checking for Balanced Substrings**
```
if opening_count == closing_count:
    max_length = max(max_length, closing_count * 2)
elif closing_count > opening_count:
    opening_count = 0
    closing_count = 0
```
- If `opening_count == closing_count`, it means we have a balanced substring, so we update `max_length`.
- If `closing_count > opening_count`, it means there are more `)` than `(`, making the substring invalid.
We reset both counters to `0`.

### **Why Reset When `closing_count > opening_count`?**
This ensures that any unmatched `)` do not interfere with future valid substrings. Resetting the counters allows us
to start fresh from a new potential balanced sequence.

---

## **3. Second Pass: Right-to-Left Traversal**
```
opening_count = 0
closing_count = 0

for i in reversed(range(len(string))):
    char = string[i]

    if char == "(":
        opening_count += 1
    else:
        closing_count += 1
```
- We now traverse the string **backward**.
- The logic is the same as before, but this time we handle cases where `(` appears before a matching `)`, which might
have been missed in the first pass.

### **Checking for Balanced Substrings in Reverse**
```
if opening_count == closing_count:
    max_length = max(max_length, opening_count * 2)
elif opening_count > closing_count:
    opening_count = 0
    closing_count = 0
```
- If `opening_count == closing_count`, update `max_length`.
- If `opening_count > closing_count`, reset both counters. This ensures that any extra `(` doesn’t interfere with
future valid substrings.

---

## **4. Returning the Maximum Length**
```
return max_length
```
- After both passes, `max_length` holds the length of the longest balanced substring.

---

## **Example Walkthrough**

### **Example 1**

#### **Input:**
```
s = "(()))("
```
#### **First Pass (Left-to-Right)**

| Index | Char | `(` Count | `)` Count | `max_length` | Action                    |
|-------|------|-----------|-----------|------------- |---------------------------|
| 0     | `(`  | 1         | 0         | 0            | Continue                  |
| 1     | `(`  | 2         | 0         | 0            | Continue                  |
| 2     | `)`  | 2         | 1         | 0            | Continue                  |
| 3     | `)`  | 2         | 2         | 4            | Found valid (max updated) |
| 4     | `)`  | 2         | 3         | 4            | Reset counts              |
| 5     | `(`  | 1         | 0         | 4            | Continue                  |

#### **Second Pass (Right-to-Left)**

| Index | Char | `(` Count | `)` Count | `max_length` | Action                      |
|-------|------|-----------|-----------|--------------|-----------------------------|
| 5     | `(`  | 1         | 0         | 4            | Continue                    |
| 4     | `)`  | 1         | 1         | 4            | Found valid (max unchanged) |
| 3     | `)`  | 1         | 2         | 4            | Continue                    |
| 2     | `)`  | 1         | 3         | 4            | Continue                    |
| 1     | `(`  | 2         | 3         | 4            | Continue                    |
| 0     | `(`  | 3         | 3         | 6            | Found valid (max updated)   |

#### **Final Output:**
```
max_length = 4
```
- The longest balanced substring is `"()"`, appearing twice, but the longest continuous balanced sequence is `"(()))"` of length `4`.

---

## **Time & Space Complexity**
- **Time Complexity:** O(N) because we iterate over the string twice.
- **Space Complexity:** O(1) since we use only a few integer variables.

---

## **Why Two Passes?**
1. The **left-to-right pass** handles cases where extra `)` appear before `(`.
2. The **right-to-left pass** ensures extra `(` are handled correctly.
3. This avoids using a **stack**, making the approach efficient in both time and space.

---

## **Alternative Approach: Stack Method**
Another way to solve this is by using a **stack** to track indices of unmatched `(` and `)`, which helps
calculate valid substring lengths. However, the two-pass counting method in this code is more space-efficient.

---

## **Conclusion**
This function efficiently finds the longest balanced substring of parentheses using a two-pass approach:
1. **Left-to-right** pass to catch unmatched `)`.
2. **Right-to-left** pass to catch unmatched `(`.

This ensures that **all valid substrings are considered**, yielding an optimized solution in **O(N) time and O(1) space**.

"""
