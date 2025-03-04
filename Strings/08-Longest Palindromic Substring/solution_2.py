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


# O(n^2) time | O(n) space
def longest_palindromic_substring(string):
    # Initialize the current longest palindrome substring indices.
    # The default is the first character, which is a palindrome of length 1.
    current_longest = [0, 1]

    # Iterate through the string to find the longest palindrome.
    for i in range(1, len(string)):
        # Check for the longest odd-length palindrome centered at `i`.
        odd = get_longest_palindrome_from(string, i - 1, i + 1)

        # Check for the longest even-length palindrome centered between `i-1` and `i`.
        even = get_longest_palindrome_from(string, i - 1, i)

        # Determine the longest palindrome between the odd and even cases.
        longest = max(odd, even, key=lambda x: x[1] - x[0])

        # Update the current longest palindrome if the newly found one is longer.
        current_longest = max(longest, current_longest, key=lambda x: x[1] - x[0])

    # Return the longest palindromic substring using the indices.
    return string[current_longest[0] : current_longest[1]]


def get_longest_palindrome_from(string, left_idx, right_idx):
    # Expand outwards from the center (defined by left_idx and right_idx)
    # to find the longest palindrome.
    while left_idx >= 0 and right_idx < len(string):
        # If the characters at the current indices don't match, stop expanding.
        if string[left_idx] != string[right_idx]:
            break
        # Move the left index to the left and the right index to the right.
        left_idx -= 1
        right_idx += 1

    # Return the indices of the longest palindrome found.
    # Note: `left_idx + 1` because the loop breaks when the characters don't match,
    # so the previous indices were the last valid palindrome indices.
    return [left_idx + 1, right_idx]


# Test Cases
print(longest_palindromic_substring("abaxyzzyxf"))  # Output: "xyzzyx"
print(longest_palindromic_substring("it's highnoon"))  # Output: "noon"
print(longest_palindromic_substring("aca"))  # Output: "aca"

# =============================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

- **Time Complexity**: O(n^2)

  - The outer loop in `longest_palindromic_substring` runs `n` times (where `n` is the length of the string).
  - For each character, the `get_longest_palindrome_from` function can expand up to `n` times in the worst case
  (e.g., when the entire string is a palindrome).
  - Therefore, the overall time complexity is - O(n^2).

- **Space Complexity**: O(1)

  - The algorithm uses a constant amount of extra space (only a few variables to store indices and the longest palindrome found).
  - The space complexity is O(1) because it does not use any additional data structures that grow with the input size.

### Summary

- **Time Complexity**: O(n^2)
- **Space Complexity**: O(1)

This algorithm is efficient for finding the longest palindromic substring in a string, and it works well for strings of
moderate length. For very large strings, more optimized algorithms (like Manacher's algorithm) can be used to 
achieve O(n) time complexity.

"""

# Code Explanation:

"""
This Python program efficiently finds the **longest palindromic substring** in a given string using the
**expand around center** approach. Let's break it down in detail.

---

## **Understanding the Code**
The main function is:
```
def longest_palindromic_substring(string):
```
It initializes `current_longest` as `[0, 1]`, representing the starting and ending indices of the longest palindromic
substring found so far.

### **1. Iterating Over the String**
```
for i in range(1, len(string)):
```
The function iterates through the string character by character, treating each character as a possible center of a palindrome.

### **2. Checking for Odd and Even Length Palindromes**
For each character at index `i`, two cases are considered:

- **Odd-length palindrome**: This means the palindrome is centered around one character. Example: `"racecar"`,
where `"e"` is the center.
  
  ```
  odd = get_longest_palindrome_from(string, i - 1, i + 1)
  ```
  Here, `i - 1` is the left pointer, and `i + 1` is the right pointer.

- **Even-length palindrome**: This means the palindrome has two centers. Example: `"abba"`, where `"bb"` is the center.
  
  ```
  even = get_longest_palindrome_from(string, i - 1, i)
  ```
  Here, `i - 1` is the left pointer, and `i` is the right pointer.

### **3. Finding the Longer Palindrome**
The function selects the longer palindrome from `odd` and `even`:
```
longest = max(odd, even, key=lambda x: x[1] - x[0])
```
It compares the lengths of the two palindromes by calculating `x[1] - x[0]`.

### **4. Updating the Longest Palindrome Found**
If the new palindrome is longer than the previously found longest palindrome, it updates `current_longest`:
```
current_longest = max(longest, current_longest, key=lambda x: x[1] - x[0])
```
Again, it compares by length (`x[1] - x[0]`).

### **5. Returning the Result**
After the loop finishes, the function extracts and returns the longest palindromic substring:
```
return string[current_longest[0] : current_longest[1]]
```
It slices the original string using the `current_longest` indices.

---

## **Understanding `get_longest_palindrome_from`**
This helper function expands outward from a given center to find the longest palindrome:

```
def get_longest_palindrome_from(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1
    return [left_idx + 1, right_idx]
```
### **How It Works**
1. It expands outward symmetrically from `left_idx` and `right_idx` **as long as** the characters at these indices are equal.
2. If it finds a mismatch, it stops.
3. It returns the indices of the longest palindromic substring found.

---

## **Example Walkthroughs**

### **Example 1: `"abaxyzzyxf"`**
#### **Step 1: Initialization**
- `current_longest = [0, 1]` (Initially, first character `"a"` is the longest)

#### **Step 2: Looping through the string**
At `i = 6`, the function detects `"xyzzyx"` as the longest palindrome and updates `current_longest = [3, 9]`.

#### **Final Output**
```
string[3:9] -> "xyzzyx"
```

---

### **Example 2: `"it's highnoon"`**
- The function finds `"noon"` at the end of the string.
- **Final Output:** `"noon"`

---

### **Example 3: `"aca"`**
- At `i = 1`, it expands around `"c"` to find `"aca"`.
- **Final Output:** `"aca"`

---

## **Final Thoughts**
- This approach **avoids checking all substrings explicitly**, unlike brute-force methods (**O(n³)**).
- It efficiently finds the longest palindromic substring in **O(n²)** time.
- The **expand-around-center** technique works well for problems like this!

"""
