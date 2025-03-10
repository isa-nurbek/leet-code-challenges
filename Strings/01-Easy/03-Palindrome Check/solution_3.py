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
def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)


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

### Time Complexity
- **Base Case:** The recursion stops when `i >= j`, which happens after approximately `n/2` comparisons,
where `n` is the length of the string.

- **Recursive Case:** In each recursive call, the function performs a constant amount of work (comparing two
characters and making a recursive call).

- **Total Work:** Since there are `n/2` recursive calls, and each call does constant work, the time complexity is **O(n)**.

### Space Complexity
- **Recursive Call Stack:** Each recursive call adds a new frame to the call stack. The maximum depth of the recursion is `n/2`,
so the space complexity is **O(n)** due to the call stack.

- **Auxiliary Space:** No additional data structures are used, so the auxiliary space is **O(1)**.

### Summary
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) (due to the call stack)

"""

# =========================================================================================================================== #

# Code Explanation:

"""
### Explanation of the Code:

#### 1. **Function Definition and Base Case**
```
def isPalindrome(string, i=0):
```
- This function checks if a given `string` is a palindrome using recursion.
- The optional parameter `i` starts at 0 and tracks the current index being checked from the start of the string.

#### 2. **Logic to Determine Corresponding Characters**
```
j = len(string) - 1 - i
```
- `j` is the index of the character being checked from the end of the string. It is computed by subtracting `i` from `len(string) - 1`.
- For example, if the string is `"madam"`:
  - When `i = 0`, `j = 4` (comparing first and last characters).
  - When `i = 1`, `j = 3` (comparing second and second-to-last characters).

#### 3. **Base Case for Recursion**
```
return True if i >= j
```
- If `i` is greater than or equal to `j`, all characters have been compared, and the function concludes the string is a palindrome.
- For example, in the case of `"madam"`, the recursion stops after comparing characters at indices `2` and `2` (middle of the string).

#### 4. **Recursive Step**
```
else string[i] == string[j] and isPalindrome(string, i + 1)
```
- The function checks if the characters at indices `i` and `j` are equal:
  - If not, it returns `False`.
  - If equal, the function calls itself with `i + 1` to check the next pair of characters.

#### 5. **Recursive Flow**
- The function continues comparing pairs of characters until:
  - A mismatch is found, in which case the function returns `False`.
  - All pairs are checked and match, in which case the function returns `True`.

---

### Example Walkthroughs

#### **Example 1: `"madam"`**
1. `isPalindrome("madam", i=0)`
   - `j = 4`, compare `string[0]` ('m') and `string[4]` ('m') → equal → call `isPalindrome("madam", i=1)`.
2. `isPalindrome("madam", i=1)`
   - `j = 3`, compare `string[1]` ('a') and `string[3]` ('a') → equal → call `isPalindrome("madam", i=2)`.
3. `isPalindrome("madam", i=2)`
   - `j = 2`, `i >= j` → return `True`.

Output: `True`

---

#### **Example 2: `"hello"`**
1. `isPalindrome("hello", i=0)`
   - `j = 4`, compare `string[0]` ('h') and `string[4]` ('o') → not equal → return `False`.

Output: `False`

---

#### **Example 3: `"a"`**
1. `isPalindrome("a", i=0)`
   - `j = 0`, `i >= j` → return `True`.

Output: `True`

---

#### **Example 4: `""` (Empty String)**
1. `isPalindrome("", i=0)`
   - `j = -1`, `i >= j` → return `True`.

Output: `True`

---

#### **Example 5: `"Madam"`**
1. `isPalindrome("Madam", i=0)`
   - `j = 4`, compare `string[0]` ('M') and `string[4]` ('m') → not equal → return `False`.

Output: `False`

"""
