# Description:

"""
                                Longest Substring Without Duplication

Write a function that takes in a string and returns its longest substring without duplicate characters.

You can assume that there will only be one longest substring without duplication.


## Sample Input:
```
string = "kilimandjaro"
```

## Sample Output:
```
"limandj"
```

## Optimal Time & Space Complexity:
```
`O(n)` time | `O(min(n, a))` space - where `n` is the length of the input string
and `a` is the length of the character alphabet represented in the input string.
```

"""

# =========================================================================================================================== #

# Solution:


# `O(n)` time | `O(1)` space - where `n` is the length of shorter string
def longest_substring_without_duplication(string):
    # Dictionary to store the last seen index of each character
    last_seen = {}

    # List to store the start and end indices of the longest substring without duplication
    # Initialize with [0, 1] which represents the first character
    longest = [0, 1]

    # Variable to keep track of the starting index of the current substring without duplicates
    start_idx = 0

    # Loop through each character in the string along with its index
    for i, char in enumerate(string):
        # If the character has been seen before, update the start_idx to be the maximum of
        # the current start_idx and the index right after the last occurrence of the character
        if char in last_seen:
            start_idx = max(start_idx, last_seen[char] + 1)

        # If the current substring (from start_idx to i+1) is longer than the previously
        # recorded longest substring, update the longest substring indices
        if longest[1] - longest[0] < i + 1 - start_idx:
            longest = [start_idx, i + 1]

        # Update the last seen index of the current character
        last_seen[char] = i

    # Return the substring using the indices stored in 'longest'
    return string[longest[0] : longest[1]]


# Test Case 1
print(longest_substring_without_duplication("kilimandjaro"))  # Output: limandj

# Test Case 2
print(longest_substring_without_duplication("abacacacaaabacaaaeaaafa"))  # Output: bac

# Test Case 3
print(longest_substring_without_duplication("a"))  # Output: a

# =========================================================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The time complexity of the `longest_substring_without_duplication` function is **O(n)**,
where `n` is the length of the input string.

- **Explanation**:
  - The function iterates through the string once using a single loop (`for i, char in enumerate(string)`).
  
  - Inside the loop, each operation (checking if a character exists in `last_seen`, updating `start_idx`, 
  and updating `longest`) takes constant time **O(1)**.
  
  - Therefore, the overall time complexity is linear, **O(n)**.

---

### Space Complexity:

The space complexity of the function is **O(min(n, m))**, where:
- `n` is the length of the input string.
- `m` is the size of the character set (e.g., 26 for lowercase English letters, 256 for ASCII characters, etc.).

- **Explanation**:
  - The `last_seen` dictionary stores the most recent index of each character in the string. In the worst case,
  it will store all unique characters in the string.
  
  - The size of `last_seen` is bounded by the size of the character set (`m`). For example, if the string contains
  only lowercase English letters, the maximum size of `last_seen` is 26.
  
  - If the character set is very large (e.g., Unicode), the space complexity is bounded by the length of the
  string (`n`), as the dictionary cannot store more than `n` unique characters.
  
  - Therefore, the space complexity is **O(min(n, m))**.

---

### Summary:
- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(min(n, m))**

"""

# =========================================================================================================================== #

# Code Explanation:

"""
### Explanation of the `longest_substring_without_duplication` Function

This function finds the **longest substring** in a given string where **no character repeats**. 
It efficiently tracks character occurrences using a **hash map** (`last_seen`) and a **sliding window** approach.

---

### **Code Breakdown**
#### **1. Initialize Variables**
```
last_seen = {}
longest = [0, 1]
start_idx = 0
```
- `last_seen`: A dictionary that stores the **last seen index** of each character in the string.
- `longest`: A list storing the **starting and ending indices** of the longest substring found so far.
- `start_idx`: The starting index of the current substring being considered.

---

#### **2. Iterate Over the String**
```
for i, char in enumerate(string):
```
- The function loops through each character in the string.
- `i` is the **index**, and `char` is the **character** at that index.

---

#### **3. Update `start_idx` if Character is Repeated**
```
if char in last_seen:
    start_idx = max(start_idx, last_seen[char] + 1)
```
- If `char` was seen before (`char in last_seen`), it means we have encountered a duplicate.
- We **update** `start_idx` to the maximum of:
  - The current `start_idx`
  - The **next** position after the last occurrence of `char` (`last_seen[char] + 1`).
- This ensures that `start_idx` moves past the **last occurrence** of the repeated character,
maintaining a substring with **no duplicates**.

---

#### **4. Update `longest` If Current Substring is Longer**
```
if longest[1] - longest[0] < i + 1 - start_idx:
    longest = [start_idx, i + 1]
```
- **Calculate the current substring length**: `i + 1 - start_idx`
- If this is **longer** than the longest substring found so far, update `longest` to **store the new indices**.

---

#### **5. Update `last_seen`**
```
last_seen[char] = i
```
- Store the **current index** of `char` in `last_seen`, so we can track when it was last seen.

---

#### **6. Return the Longest Substring**
```
return string[longest[0] : longest[1]]
```
- Extract the **longest substring** using `longest[0]` (start index) and `longest[1]` (end index).

---

### **Example Walkthrough**

#### **Input**: `"kilimandjaro"`

| i  | char|     last_seen                                    | start_idx | longest     | Current Substring |
|----|-----|--------------------------------------------------|-----------|-------------|-------------------|
| 0  | k   | {k: 0}                                           | 0         | [0, 1]      | "k"               |
| 1  | i   | {k: 0, i: 1}                                     | 0         | [0, 2]      | "ki"              |
| 2  | l   | {k: 0, i: 1, l: 2}                               | 0         | [0, 3]      | "kil"             |
| 3  | i   | {k: 0, i: 3, l: 2}                               | 2         | [0, 3]      | "li"              |
| 4  | m   | {k: 0, i: 3, l: 2, m: 4}                         | 2         | [2, 5]      | "lim"             |
| 5  | a   | {k: 0, i: 3, l: 2, m: 4, a: 5}                   | 2         | [2, 6]      | "lima"            |
| 6  | n   | {k: 0, i: 3, l: 2, m: 4, a: 5, n: 6}             | 2         | [2, 7]      | "liman"           |
| 7  | d   | {k: 0, i: 3, l: 2, m: 4, a: 5, n: 6, d: 7}       | 2         | [2, 8]      | "limand"          |
| 8  | j   | {k: 0, i: 3, l: 2, m: 4, a: 5, n: 6, d: 7, j: 8} | 2         | [2, 9]      | "limandj"         |
| 9  | a   | {k: 0, i: 3, l: 2, m: 4, a: 9, n: 6, d: 7, j: 8} | 6         | [2, 9]      | "andja"           |

**Final Output:** `"limandj"`

---

This function efficiently finds the **longest substring without duplicate characters** using
a **sliding window** and a **hash map** for quick lookups.

"""
