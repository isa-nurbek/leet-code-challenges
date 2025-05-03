# Problem Description:

"""
                                        First Non-Repeating Character

Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's
first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string doesn't have any non-repeating characters, your function should return `-1`.


## Sample Input:
```
string = "abcdcaf"
```

## Sample Output:
```
1 

// The first non-repeating character is "b" and is found at index 1.
```

## Optimal Time & Space Complexity
```
O(n) time | O(1) space - where `n` is the length of the input string. The constant space is
because the input string only has lowercase English-alphabet letters; thus, our hash table will
never have more than 26 character frequencies.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n^2) time | O(1) space
def first_non_repeating_character(string):
    # Initialize a flag to track if a duplicate character is found
    found_duplicate = False

    # Outer loop: Iterate through each character in the string by index
    for idx in range(len(string)):
        # Reset the flag for each new character
        found_duplicate = False

        # Inner loop: Compare the current character with every other character in the string
        for idx_2 in range(len(string)):
            # Check if the characters are the same and the indices are different
            if string[idx] == string[idx_2] and idx != idx_2:
                # If a duplicate is found, set the flag to True and break out of the inner loop
                found_duplicate = True
                break

        # If no duplicate was found for the current character, return its index
        if not found_duplicate:
            return idx

    # If no non-repeating character is found, return -1
    return -1


# Test Cases
print(first_non_repeating_character("abcdcaf"))  # 1
print(first_non_repeating_character("faadabcbbebdf"))  # 6
print(first_non_repeating_character("a"))  # 0
print(first_non_repeating_character(""))  # -1

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity Analysis**

The function consists of a nested loop:
1. The **outer loop** iterates through each character in `string` → **O(n)**
2. The **inner loop** iterates through the entire string again to check for duplicates → **O(n)**

3. This results in a total time complexity of **O(n²)** in the worst case.

### **Space Complexity Analysis**

- The function only uses a few integer variables (`found_duplicate`, `idx`, `idx_2`), which all take **O(1)** space.
- No additional data structures (like a dictionary or list) are used to store frequency counts or other information.

Thus, the space complexity is **O(1)**.

### **Final Complexity:**
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

### **Optimized Approach**

A more efficient way to solve this problem would be to use a **hash map (dictionary)** to store character frequencies,
which reduces the time complexity to **O(n)**.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### Explanation of the Code

The function `first_non_repeating_character(string)` is designed to find the index of the first non-repeating 
character in a given string. If no such character exists, it returns `-1`.

---

### **Step-by-Step Breakdown**
#### **1. Function Definition and Initialization**
```
def first_non_repeating_character(string):
    found_duplicate = False
```
- The function takes a single input parameter, `string`, which is the text we will analyze.
- A boolean flag `found_duplicate` is initialized to `False`. This variable will help track whether the current
character has a duplicate.

---

#### **2. Outer Loop - Iterating Through Each Character**
```
for idx in range(len(string)):
    found_duplicate = False
```
- This `for` loop iterates through each character in the string using `idx` as an index.
- Before checking for duplicates, `found_duplicate` is reset to `False`.

---

#### **3. Inner Loop - Checking for Duplicates**
```
for idx_2 in range(len(string)):
    if string[idx] == string[idx_2] and idx != idx_2:
        found_duplicate = True
```
- The inner `for` loop iterates over the entire string again, using `idx_2` as an index.
- It checks if the character at `idx` is the same as the character at `idx_2` **and** if their indices are
different (`idx != idx_2`).
- If a duplicate is found, `found_duplicate` is set to `True`.

---

#### **4. Checking for a Unique Character**
```
if not found_duplicate:
    return idx
```
- If `found_duplicate` is still `False` after the inner loop completes, it means the character at `idx` does not have any duplicates.
- The function returns `idx`, which is the index of the first non-repeating character.

---

#### **5. No Unique Character Found**
```
return -1
```
- If the function completes both loops without finding a unique character, it returns `-1`, indicating that all characters
in the string are repeating.


### **Test Cases Execution**

#### **1st Test Case: `"abcdcaf"`**
```
print(first_non_repeating_character("abcdcaf"))
```
- 'a' (index 0) is repeated.
- 'b' (index 1) is **not repeated**.
- The function returns **1**.

---

#### **2nd Test Case: `"faadabcbbebdf"`**
```
print(first_non_repeating_character("faadabcbbebdf"))
```
- 'f' (index 0) is repeated.
- 'a' (index 1, 2) is repeated.
- 'd' (index 3, 11) is repeated.
- 'b' (index 4, 8) is repeated.
- 'c' (index 5) is **not repeated**.
- The function returns **6**.

---

#### **3rd Test Case: `"a"`**
```
print(first_non_repeating_character("a"))
```
- 'a' is the only character and is **not repeated**.
- The function returns **0**.

---

#### **4th Test Case: `""` (Empty String)**
```
print(first_non_repeating_character(""))
```
- The string is empty, so there are no characters to check.
- The function returns **-1**.

---

### **Optimized Approach (Using Hash Maps)**
The current approach is inefficient because of its **O(n²)** complexity. An improved approach would use a **hash map
(dictionary)** to count character occurrences in a single pass and then find the first non-repeating character
in another pass. This can be done in **O(n) time complexity**.

"""
