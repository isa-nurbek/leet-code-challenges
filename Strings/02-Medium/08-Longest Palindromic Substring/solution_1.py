# Description:

"""
                            Longest Palindromic Substring

Write a function that, given a string, returns its longest palindromic substring.

A palindrome is defined as a string that's written the same forward and backward. Note that
single-character strings are palindromes.

You can assume that there will only be one longest palindromic substring.


## Sample Input:

```
string = "abaxyzzyxf"
```

## Sample Output:

```
"xyzzyx"
```

## Optimal Time & Space Complexity:

```
`O(n^2)` time | `O(n)` space - where `n` is the length of the input string.
```

"""

# =============================================================================================== #

# Solution


# O(n^3) time | O(n) space
def longest_palindromic_substring(string):
    # Initialize a variable to store the longest palindromic substring found so far
    longest = ""

    # Loop through each character in the string as a potential starting point
    for i in range(len(string)):
        # Loop through each character from the current starting point to the end of the string
        for j in range(i, len(string)):
            # Extract the substring from index i to j (inclusive)
            substring = string[i : j + 1]

            # Check if the current substring is longer than the longest found so far
            # and if it is a palindrome
            if len(substring) > len(longest) and is_palindrome(substring):
                # Update the longest palindromic substring
                longest = substring

    # Return the longest palindromic substring found
    return longest


def is_palindrome(string):
    # Initialize two pointers, one at the start of the string and one at the end
    left_idx = 0
    right_idx = len(string) - 1

    # Loop until the two pointers meet or cross each other
    while left_idx < right_idx:
        # If the characters at the current pointers are not the same, it's not a palindrome
        if string[left_idx] != string[right_idx]:
            return False
        # Move the left pointer to the right and the right pointer to the left
        left_idx += 1
        right_idx -= 1

    # If the loop completes without finding any mismatches, the string is a palindrome
    return True


# Test Cases
print(longest_palindromic_substring("abaxyzzyxf"))  # xyzzyx
print(longest_palindromic_substring("it's highnoon"))  # noon
print(longest_palindromic_substring("aca"))  # aca

# =============================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity:
1. **Outer Loop**:
   - The outer loop runs `n` times, where `n` is the length of the input string.

2. **Inner Loop**:
   - For each iteration of the outer loop, the inner loop runs `n - i` times, where `i` is the current index of the outer loop.
   - In the worst case, the inner loop runs approximately `n` times for each iteration of the outer loop.

3. **Palindrome Check**:
   - For each substring, the `is_palindrome` function checks if it is a palindrome. This function runs in `O(m)` time,
   where `m` is the length of the substring.
   - In the worst case, `m` can be up to `n` (the length of the entire string).

4. **Total Time Complexity**:
   - The outer loop runs `n` times.
   - The inner loop runs `n` times for each outer loop iteration.
   - For each substring, the palindrome check takes `O(n)` time.
   - Therefore, the total time complexity is:
     
        O(n) * O(n) * O(n) = O(n^3)
     
---

### Space Complexity:
1. **Substring Storage**:
   - The `substring` variable stores a substring of the input string. In the worst case, this substring can be
   up to `n` characters long.
   - The `longest` variable also stores a substring of up to `n` characters.

2. **Auxiliary Space**:
   - The `is_palindrome` function uses constant space `O(1)` as it only uses pointers and does not store additional data.

3. **Total Space Complexity**:
   - The space used by the `substring` and `longest` variables dominates the space complexity.
   - Therefore, the total space complexity is: `O(n)`

---

### Summary:
- **Time Complexity**: `O(n^3)` 
- **Space Complexity**: `O(n) `

---

### Optimized Approach:
The above solution is not efficient for large inputs. A more efficient approach to solve this problem is
using **dynamic programming** or **Manacher's algorithm**, which can reduce the time complexity to O(n^2) or O(n), respectively.

"""

# Code Explanation:

"""
This Python code finds the **longest palindromic substring** within a given string using a brute-force approach.
Let's break it down step by step.

---

## **Understanding the Code**
The code consists of two functions:

1. `longest_palindromic_substring(string)`:  
   - This function iterates over all possible substrings of the given string.
   - It checks whether a substring is a **palindrome** using the `is_palindrome` function.
   - It keeps track of the longest palindrome found so far and returns it.

2. `is_palindrome(string)`:  
   - This function checks if a given string is a **palindrome** (i.e., it reads the same forward and backward).
   - It does so by comparing characters from both ends of the string moving toward the center.

---

## **Detailed Walkthrough**

### **1. `longest_palindromic_substring(string)`**
```
def longest_palindromic_substring(string):
    longest = ""  # Stores the longest palindrome found
```
- `longest` is initialized as an empty string.
- It will store the longest palindromic substring found.

```
    for i in range(len(string)):  # Iterate over every starting index of the substring
        for j in range(i, len(string)):  # Iterate over every ending index of the substring
            substring = string[i : j + 1]  # Extract substring from index i to j (inclusive)
```
- The **outer loop** iterates over all possible **starting indices** (`i`).
- The **inner loop** iterates over all possible **ending indices** (`j`).
- `substring = string[i : j + 1]` extracts the substring from `i` to `j`.

```
    if len(substring) > len(longest) and is_palindrome(substring):
        longest = substring  # Update the longest palindrome found
```
- If `substring` is **longer** than `longest` **and** is a **palindrome**, we update `longest`.

```
    return longest  # Return the longest palindromic substring
```
- Finally, the function returns the longest palindromic substring found.

---

### **2. `is_palindrome(string)`**
This function checks whether a string is a palindrome.

```
def is_palindrome(string):
    left_idx = 0  # Pointer at the start of the string
    right_idx = len(string) - 1  # Pointer at the end of the string
```
- `left_idx` starts from the **leftmost** character.
- `right_idx` starts from the **rightmost** character.

```
    while left_idx < right_idx:  # Loop until the pointers meet or cross
        if string[left_idx] != string[right_idx]:  # If characters don’t match, it's not a palindrome
            return False  
        left_idx += 1  # Move left pointer forward
        right_idx -= 1  # Move right pointer backward
```
- The function **compares characters** from both ends of the string.
- If any character pair doesn't match, the function returns `False` immediately.
- If all characters match, the function continues until the pointers meet in the middle.

```
    return True  # If loop completes, the string is a palindrome
```
- If no mismatches are found, the function returns `True`.

---

## **Example Execution**

Let's go through each test case in detail to see how the function `longest_palindromic_substring` works.

---

## **Test Case 1**
```
print(longest_palindromic_substring("abaxyzzyxf"))  # Expected Output: "xyzzyx"
```
### **Step-by-step Execution**
1. The function generates all possible substrings of `"abaxyzzyxf"`.
2. It checks each substring to see if it is a palindrome.
3. The longest palindrome found in this string is `"xyzzyx"`, which appears in the middle of the string.

### **Why is "xyzzyx" the longest palindrome?**
- "xyzzyx" is symmetrical and reads the same forward and backward.
- There are other palindromes in the string, such as "aba" and "zz", but none are as long as "xyzzyx".

---

## **Test Case 2**
```
print(longest_palindromic_substring("it's highnoon"))  # Expected Output: "noon"
```
### **Step-by-step Execution**
1. The function extracts all substrings of `"it's highnoon"`.
2. It checks each substring to see if it is a palindrome.
3. The longest palindrome found is `"noon"`.

### **Why is "noon" the longest palindrome?**
- "noon" is a 4-letter palindrome.
- Other smaller palindromes like "h", "i", "g", and "oo" exist, but they are shorter than "noon".

### **Note:**  
- The function is case-sensitive and treats spaces and punctuation as characters.
- If spaces were removed before processing, "highnoon" would still have "noon" as the longest palindrome.

---

## **Test Case 3**
```
print(longest_palindromic_substring("aca"))  # Expected Output: "aca"
```
### **Step-by-step Execution**
1. The function checks substrings of `"aca"`.
2. The entire string `"aca"` itself is a palindrome.
3. There are other smaller palindromes ("a", "c"), but `"aca"` is the longest.

### **Why is "aca" the longest palindrome?**
- "aca" reads the same forward and backward.
- Since the entire string is a palindrome, it is naturally the longest palindromic substring.

---

## **Summary**
- The function finds the longest palindromic substring by checking all substrings.
- It uses a nested loop to generate all substrings (**O(n²)** complexity).
- It checks if each substring is a palindrome using two-pointer comparison (**O(n)** complexity).
- The overall time complexity is **O(n³)**, making it inefficient for large inputs.

"""
