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


# O(n)time | O(n) space
def isPalindrome(string):
    reversed_string = ""

    for i in reversed(range(len(string))):
        reversed_string += string[i]

    return string == reversed_string


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

### **Time Complexity**
1. The `reversed(range(len(string)))` operation iterates over the indices of the string in reverse order.
This takes `O(n)` time, where `n` is the length of the string.

2. The `for` loop iterates `n` times, and in each iteration, it appends a character to `reversed_string`.
Appending to a string in Python is `O(1)` on average, but in the worst case (due to string immutability and
potential reallocation), it can be `O(n)` for the entire loop.

3. The final comparison `string == reversed_string` takes `O(n)` time, as it compares each character of the two strings.

Thus, the **time complexity** is:

    O(n) + O(n) + O(n) = O(n)

---

### **Space Complexity**
1. The `reversed_string` variable stores a copy of the reversed string, which requires `O(n)` space.
2. No other significant additional space is used.

Thus, the **space complexity** is: `O(n)`

---

### **Final Answer**
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` (can be optimized to O(1))

"""

# =========================================================================================================================== #

# Code Explanation:

"""

Here is an explanation of the given code in detail, along with an example test case to demonstrate its functionality.

---

### Code Analysis

#### Function Definition
```
def isPalindrome(string):
```
- This function, `isPalindrome`, takes a single argument, `string`, which is expected to be a string.

#### Reversing the String
```
    reversed_string = ""
    for i in reversed(range(len(string))):
        reversed_string += string[i]
```
- **`reversed(range(len(string)))`**: This generates a sequence of indices in reverse order, from the last index to the first.
  - For example, if `string = "abc"`, `range(len(string))` produces `[0, 1, 2]`, and `reversed(range(len(string)))`
  produces `[2, 1, 0]`.
- **Loop (`for i in ...`)**: The loop iterates over each index `i` in this reversed sequence.
- **String Construction**: During each iteration, `string[i]` (the character at the current index) is appended to `reversed_string`.
  - If `string = "abc"`, `reversed_string` builds up as follows:
    1. Initially, `reversed_string = ""`.
    2. Append `string[2]` (i.e., `'c'`): `reversed_string = "c"`.
    3. Append `string[1]` (i.e., `'b'`): `reversed_string = "cb"`.
    4. Append `string[0]` (i.e., `'a'`): `reversed_string = "cba"`.

#### Comparison
```
    return string == reversed_string
```
- The original string `string` is compared with `reversed_string`.
- If they are equal, the function returns `True`, indicating the string is a palindrome.
- If they are not equal, the function returns `False`, indicating the string is not a palindrome.

---

### Test Cases

1. **Test Case 1: Palindrome String**
   ```
   print(isPalindrome("madam"))  # Expected output: True
   ```
   - Original string: `"madam"`.
   - Reversed string: `"madam"`.
   - Both are equal → **True**.

2. **Test Case 2: Non-Palindrome String**
   ```
   print(isPalindrome("hello"))  # Expected output: False
   ```
   - Original string: `"hello"`.
   - Reversed string: `"olleh"`.
   - Both are not equal → **False**.

3. **Test Case 3: Single-Character String**
   ```
   print(isPalindrome("a"))  # Expected output: True
   ```
   - A single-character string is always a palindrome since reversing it produces the same string.

4. **Test Case 4: Empty String**
   ```
   print(isPalindrome(""))  # Expected output: True
   ```
   - An empty string is trivially a palindrome as reversing it has no effect.

5. **Test Case 5: Case Sensitivity**
   ```
   print(isPalindrome("Madam"))  # Expected output: False
   ```
   - Original string: `"Madam"`.
   - Reversed string: `"madaM"`.
   - Both are not equal due to case differences → **False**.

"""
