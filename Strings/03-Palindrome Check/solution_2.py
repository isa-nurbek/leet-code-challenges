# Description:
"""
                                         Palindrome Check

Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

Sample Input:
string = "abcdcba"

Sample Output:
true // it's written the same forward and backward


Optimal Space & Time Complexity:
`O(n)` time | `O(1)` space - where `n` is the length of the input string.

"""


# O(n)time | O(n) space
def isPalindrome(string):
    reversed_chars = []
    for i in reversed(range(len(string))):
        reversed_chars.append(string[i])
    return string == "".join(reversed_chars)


print(isPalindrome("madam"))  # True
print(isPalindrome("hello"))  # False
print(isPalindrome("a"))  # True
print(isPalindrome(""))  # True
print(isPalindrome("Madam"))  # False


# Big O:
"""

### **Time Complexity**
- The loop iterates through all `n` characters of the input string, where `n` is the length of the string.
- The `.join()` operation also takes O(n) time to construct the reversed string.
- Total Time Complexity: **O(n)**.

### **Space Complexity**
- The `reversed_chars` list requires space proportional to the input string’s length, i.e., O(n).
- Total Space Complexity: **O(n)**.

---

### **Important Notes**
1. **Case-Sensitivity:** 
   The comparison is case-sensitive, meaning `"Madam"` is not considered a palindrome, as `"M"` and `"m"` are different.

2. **Optimization:** 
   This implementation is simple but can be optimized to use O(1) space. For example, you could compare characters
   directly by iterating from both ends toward the center without building an extra list.
   
---

"""

# Code Explanation:
"""
### Code Breakdown and Explanation

This Python code checks whether a given string is a **palindrome**. A palindrome is a string that reads the same
backward as forward, such as "madam" or "racecar".

Here’s a detailed breakdown of how the code works:

---

### **Code Walkthrough**

#### **1. Function Definition**
```
def isPalindrome(string):
```
The function `isPalindrome` takes one argument, `string`, which is the input string to be checked for palindrome properties.

---

#### **2. Reversing the String**
```
reversed_chars = []
for i in reversed(range(len(string))):
    reversed_chars.append(string[i])
```

- **`reversed(range(len(string)))`:**
  - Generates indices in reverse order for the input string. For example, if the string is `"hello"`, the range
  will produce the indices `4, 3, 2, 1, 0`.
  - The `reversed` function ensures we iterate backward over the string.

- **`reversed_chars.append(string[i])`:**
  - For each index `i` from the reversed range, the character at that index in the original string is added
  to the `reversed_chars` list.
  - This effectively builds a reversed version of the input string in the `reversed_chars` list.

For example:
- If `string = "madam"`, after the loop, `reversed_chars = ['m', 'a', 'd', 'a', 'm']`.

---

#### **3. Join Reversed Characters**
```
return string == "".join(reversed_chars)
```

- The `reversed_chars` list is converted back into a string using `"".join(reversed_chars)`.
  - For example, if `reversed_chars = ['m', 'a', 'd', 'a', 'm']`, the result of `"".join(reversed_chars)` is `"madam"`.

- Finally, the function checks if the original string (`string`) is equal to the reversed string. If they are the same,
the string is a palindrome, and the function returns `True`; otherwise, it returns `False`.

---

### **Example Walkthroughs**

1. **Input: `"madam"`**
   - Reversed string: `"madam"`
   - Original == Reversed: `True`
   - Output: `True`

2. **Input: `"hello"`**
   - Reversed string: `"olleh"`
   - Original != Reversed: `False`
   - Output: `False`

3. **Input: `"a"`**
   - Single character is always a palindrome.
   - Output: `True`

4. **Input: `""` (empty string)**
   - An empty string is trivially a palindrome.
   - Output: `True`

5. **Input: `"Madam"`**
   - Reversed string: `"madaM"`
   - Original != Reversed (case-sensitive): `False`
   - Output: `False`

"""
