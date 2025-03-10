# Description:

"""
                                         Palindrome Check

Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

## Sample Input:

```
string = "abcdcba"
```

## Sample Output:

```
true // it's written the same forward and backward
```

## Optimal Space & Time Complexity:

```
O(n) time | O(1) space - where `n` is the length of the input string.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n)time | O(1) space
def isPalindrome(string):
    left_idx = 0
    right_idx = len(string) - 1

    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False

        left_idx += 1
        right_idx -= 1

    return True


# Test Cases
print(isPalindrome("madam"))  # True
print(isPalindrome("hello"))  # False
print(isPalindrome("a"))  # True
print(isPalindrome(""))  # True
print(isPalindrome("Madam"))  # False

# =========================================================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity:
The time complexity of the `isPalindrome` function is **O(n)**, where `n` is the length of the input string.
This is because the function iterates through the string from both ends (left and right) towards the center,
comparing characters at each step. In the worst case, it will perform `n/2` comparisons, which simplifies to **O(n)**.

### Space Complexity:
The space complexity of the `isPalindrome` function is **O(1)**. This is because the function uses a constant 
amount of extra space (variables like `left_idx`, `right_idx`, and the input string itself) regardless of the
size of the input string. No additional data structures or memory allocations are used that depend on the input size.

### Summary:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

"""

# =========================================================================================================================== #

# Code Explanation:

"""
Here's a detailed explanation of the provided code and how it works:

#### Function Signature:
```
def isPalindrome(string):
```
This function checks if the input string is a **palindrome**. A palindrome is a string that reads the same
forward and backward (e.g., "madam" is a palindrome, but "hello" is not).

#### Initial Variable Setup:
```
    left_idx = 0
    right_idx = len(string) - 1
```
- `left_idx` is initialized to `0`, representing the starting index of the string.
- `right_idx` is initialized to `len(string) - 1`, the last index of the string. 

These variables are used to compare characters from the beginning and end of the string, moving inward.

#### While Loop:
```
    while left_idx < right_idx:
```
The loop runs as long as `left_idx` is less than `right_idx`, ensuring comparisons are only made for
the relevant parts of the string.

#### Character Comparison:
```
    if string[left_idx] != string[right_idx]:
        return False
```
- The characters at the positions `left_idx` and `right_idx` are compared.
- If the characters are **not equal**, the function immediately returns `False`, as the string cannot be a palindrome.

#### Increment and Decrement:
```
    left_idx += 1
    right_idx -= 1
```
- After a successful comparison (where the characters are equal), the `left_idx` is incremented to move
to the next character on the left, and `right_idx` is decremented to move to the next character on the right.

#### End of Loop:
```
    return True
```
If the loop completes without finding a mismatch, the function returns `True`, indicating the string is a palindrome.

---

### Example Walkthroughs

1. **Input: "madam"**
    - `left_idx = 0, right_idx = 4`: Compare `string[0]` ('m') and `string[4]` ('m') → equal.
    - Increment `left_idx` to 1, decrement `right_idx` to 3.
    - `left_idx = 1, right_idx = 3`: Compare `string[1]` ('a') and `string[3]` ('a') → equal.
    - Increment `left_idx` to 2, decrement `right_idx` to 2.
    - Loop ends (`left_idx = right_idx`), return `True`.

2. **Input: "hello"**
    - `left_idx = 0, right_idx = 4`: Compare `string[0]` ('h') and `string[4]` ('o') → not equal.
    - Return `False`.

3. **Input: "a"**
    - Single-character strings are trivially palindromes because there is no mismatch possible.
    - Loop doesn't run (`left_idx = 0, right_idx = 0`), return `True`.

4. **Input: ""**
    - An empty string is considered a palindrome by definition.
    - Loop doesn't run (`left_idx = 0, right_idx = -1`), return `True`.

5. **Input: "Madam"**
    - `left_idx = 0, right_idx = 4`: Compare `string[0]` ('M') and `string[4]` ('m') → not equal (case-sensitive comparison).
    - Return `False`.

"""
