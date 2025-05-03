# Problem Description:

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
True

// It's written the same forward and backward
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the input string.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n)time | O(n) space
def isPalindrome(string):
    reversed_chars = []

    for i in reversed(range(len(string))):
        reversed_chars.append(string[i])

    return string == "".join(reversed_chars)


# Test Cases
print(isPalindrome("madam"))  # True
print(isPalindrome("hello"))  # False
print(isPalindrome("a"))  # True
print(isPalindrome(""))  # True
print(isPalindrome("Madam"))  # False

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:
1. **Reversing the string**: The `for` loop iterates over the string in reverse order, which takes `O(n)` time,
where `n` is the length of the string.
2. **Appending characters**: Appending each character to the `reversed_chars` list also takes `O(n)` time in total.
3. **Joining the list**: The `"".join(reversed_chars)` operation concatenates the characters in the list, which takes `O(n)` time.
4. **Comparison**: The final comparison `string == "".join(reversed_chars)` takes `O(n)` time.

Thus, the overall time complexity is:

    O(n) + O(n) + O(n) + O(n) = `O(n)`

### Space Complexity:
1. **Reversed characters list**: The `reversed_chars` list stores all the characters of the string, which requires `O(n)` space.
2. **Joined string**: The `"".join(reversed_chars)` operation creates a new string, which also requires `O(n)` space.

Thus, the overall space complexity is:

    O(n) + O(n) = `O(n)`

### **Final Answer**
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

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
