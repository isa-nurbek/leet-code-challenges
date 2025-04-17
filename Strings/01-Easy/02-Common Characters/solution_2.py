# Problem Description:

"""

                                    Common Characters

Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common
to all strings in the list, ignoring multiplicity.

Note that the strings are not guaranteed to only contain alphanumeric characters. The list you return can be in any order.


## Sample Input:
```
strings = ["abc", "bcd", "cbaccd"]
```

## Sample Output:
```
["b", "c"] // The characters could be ordered differently.
```

## Optimal Time & Space Complexity:
```
O(n * m) time | O(m) space - where `n` is the number of strings, and `m` is the length of the longest string.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * m) time | O(m) space
def common_characters(strings):
    # Step 1: Find the smallest string in the list of strings.
    # This is done to minimize the number of potential common characters we need to check.
    smallest_string = get_smallest_string(strings)

    # Step 2: Convert the smallest string into a set of characters.
    # This gives us the initial set of potential common characters.
    potential_common_characters = set(smallest_string)

    # Step 3: Iterate through each string in the list.
    # For each string, we will remove characters from the potential_common_characters set
    # that are not present in the current string.
    for string in strings:
        remove_nonexistent_characters(string, potential_common_characters)

    # Step 4: After processing all strings, the remaining characters in the set
    # are the common characters across all strings.
    return list(potential_common_characters)


def get_smallest_string(strings):
    # Initialize the smallest string as the first string in the list.
    smallest_string = strings[0]

    # Iterate through each string in the list to find the smallest one.
    for string in strings:
        if len(string) < len(smallest_string):
            smallest_string = string

    # Return the smallest string found.
    return smallest_string


def remove_nonexistent_characters(string, potential_common_characters):
    # Convert the current string into a set of unique characters.
    unique_string_characters = set(string)

    # Iterate through a copy of the potential_common_characters set.
    # We use list() to create a copy because we cannot modify a set while iterating over it.
    for character in list(potential_common_characters):
        # If the character is not in the current string's set of characters,
        # remove it from the potential_common_characters set.
        if character not in unique_string_characters:
            potential_common_characters.remove(character)


# Test Cases
print(common_characters(["abc", "bcd", "cbad"]))  # Output: ['b', 'c']
print(common_characters(["a", "b", "c"]))  # Output: []
print(common_characters(["aaaa", "a"]))  # Output: ['a']
print(
    common_characters(["*abc!d", "de!f*", "**!!!****d*****"])
)  # Output: ['d', '!', '*']

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

Let's analyze the time and space complexity of the `common_characters` function and its helper functions.

### 1. `get_smallest_string(strings)`:

- **Time Complexity**: This function iterates through the list of strings once to find the smallest string.
If there are `n` strings and the average length of the strings is `m`, the time complexity is `O(n * m)`.

- **Space Complexity**: This function only stores the smallest string, so the space complexity is `O(m)`.

### 2. `remove_nonexistent_characters(string, potential_common_characters)`:

- **Time Complexity**: This function iterates through the `potential_common_characters` set and checks if each character
exists in the `unique_string_characters` set. The size of `potential_common_characters` is at most `m`
(the length of the smallest string), and checking membership in a set is `O(1)`.

Therefore, the time complexity is `O(m)`.

- **Space Complexity**: This function creates a set `unique_string_characters` from the input string, which takes `O(k)`
space where `k` is the length of the string. However, since this set is temporary, the overall space complexity is `O(1)`
if we consider the input and output space.

### 3. `common_characters(strings)`:

- **Time Complexity**:
  - `get_smallest_string` takes `O(n * m)`.
  
  - The `remove_nonexistent_characters` function is called `n` times, and each call takes `O(m)`. Therefore,
  the total time complexity for this part is `O(n * m)`.
  
  - Overall, the time complexity is `O(n * m)`.
  
- **Space Complexity**:
  - The `potential_common_characters` set takes `O(m)` space.
  - The `unique_string_characters` set in `remove_nonexistent_characters` is temporary and does not add
  to the overall space complexity.
  
  - Therefore, the space complexity is `O(m)`.

### Summary
- **Time Complexity**: `O(n * m)`
- **Space Complexity**: `O(m)`

Where:
- `n` is the number of strings in the input list.
- `m` is the length of the smallest string in the list.

This analysis assumes that the operations on sets (like membership checks and removals) are `O(1)`, 
which is generally true for Python's set implementation.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""

The given code finds the common characters present in all strings in a list. Let's break it down step-by-step:

---

## **How it works**

### **1. Main Function: `common_characters(strings)`**
This is the main function, which takes a list of strings (`strings`) as input and returns the list of characters 
that are common to all strings.

---

### **Function Purpose**
The `common_characters(strings)` function identifies the characters that are common to all strings in the input
list `strings`. The result is returned as a list of unique characters. 

---

### **Detailed Explanation**

#### **1. Finding the Smallest String**
```
smallest_string = get_smallest_string(strings)
```

- The first step is to find the smallest string (in terms of length) from the input list of strings.
- Why?
  - The characters in the smallest string act as the starting point for potential common characters. If a character
  is not in the smallest string, it cannot possibly be common to all strings. This optimization reduces unnecessary checks.

Example:  
If `strings = ["abc", "bcd", "cbad"]`, the smallest string is `"abc"`.

---

#### **2. Initializing Potential Common Characters**
```
potential_common_characters = set(smallest_string)
```

- The characters of the smallest string are converted into a set. This set will hold the characters that are
**potentially** common across all strings.
  - A set is used because checking for membership (`if character in set`) and removing elements is efficient
  (both are O(1).
- Why start with the smallest string?
  - If a character is not in the smallest string, it doesn't need to be checked in the other strings. This step
  ensures the algorithm processes only the minimal number of characters needed.

Example:  
If `smallest_string = "abc"`, the initial `potential_common_characters` is `{'a', 'b', 'c'}`.

---

#### **3. Iterating Through Each String**
```
for string in strings:
    remove_nonexistent_characters(string, potential_common_characters)
```

- This loop processes each string in the input list to check if the characters in `potential_common_characters` are
present in the string.
- For every string, the helper function `remove_nonexistent_characters` is called to refine the set of `potential_common_characters`.

---

#### **4. Refining Potential Common Characters**
```
remove_nonexistent_characters(string, potential_common_characters)
```

- The purpose of this helper function is to progressively remove characters from `potential_common_characters` that 
are not present in the current string.
  
How it works:
1. **Convert the string to a set of unique characters:**
   ```
   unique_string_characters = set(string)
   ```
   This allows efficient membership checks.

2. **Iterate through the potential common characters:**
   ```
   for character in list(potential_common_characters):
   ```
   A list copy of the set is used for iteration to avoid modifying the set while looping.

3. **Remove non-existent characters:**
   ```
   if character not in unique_string_characters:
       potential_common_characters.remove(character)
   ```
   If a character is not in the current string, it is removed from the set of `potential_common_characters`.

Example:  
- Suppose `potential_common_characters = {'a', 'b', 'c'}` and the current string is `"bcd"`.  
  - `'a'` is not in `"bcd"`, so it is removed.  
  - The updated `potential_common_characters` becomes `{'b', 'c'}`.

---

#### **5. Return the Result**
```
return list(potential_common_characters)
```

- After iterating through all strings, `potential_common_characters` contains only the characters that are common to all strings.
- This set is converted to a list and returned as the result.

Example:  
If `potential_common_characters = {'b', 'c'}`, the final result is `['b', 'c']`.

---

### **Example Walkthrough**

#### Input: `common_characters(["abc", "bcd", "cbad"])`

1. **Find the smallest string:**  
   `smallest_string = "abc"`

2. **Initialize potential common characters:**  
   `potential_common_characters = {'a', 'b', 'c'}`

3. **Process each string:**
   - For `"abc"`:  
     - All characters `'a', 'b', 'c'` are in `"abc"`. No changes to the set.  
     `potential_common_characters = {'a', 'b', 'c'}`

   - For `"bcd"`:  
     - `'a'` is not in `"bcd"`, so remove `'a'`.  
     `potential_common_characters = {'b', 'c'}`

   - For `"cbad"`:  
     - All characters `'b', 'c'` are in `"cbad"`. No changes to the set.  
     `potential_common_characters = {'b', 'c'}`

4. **Return the result:**  
   Convert `{'b', 'c'}` to a list: `['b', 'c']`

---

### **Why This Approach Works**
- By starting with the smallest string, the algorithm minimizes the initial set of characters to consider.
- The use of sets ensures efficient operations for membership checks and removals.
- Iterating through each string refines the set of potential common characters step by step.
- The final set represents the characters that are present in all strings.

---

### **Key Points**
- **Efficiency:** The algorithm ensures minimal computation by focusing only on characters from the smallest string
and refining the set of potential common characters as it processes each string.
- **Simplicity:** The logic is broken into clear steps, making it easy to follow and maintain.
- **Robustness:** The function handles edge cases like strings with no common characters or strings with repeated
characters effectively.

---

### **2. Helper Function: `get_smallest_string(strings)`**
This function returns the smallest string (in terms of length) from the input list of strings.

---

Let's break down the function `get_smallest_string(strings)` in detail:

---

### **Purpose**
The function identifies the shortest string (in terms of length) from a given list of strings and returns it.
This is an important optimization step because the shortest string is used as the initial reference for finding
common characters across all strings.

---

### **Detailed Explanation**

#### **Input**
The function takes one argument:
- `strings`: A list of strings. For example, `["abc", "bcd", "cbad"]`.

#### **Output**
The function returns:
- The shortest string in the list. For example, `"abc"` if the input is `["abc", "bcd", "cbad"]`.

---

### **Code Walkthrough**

#### **1. Initialize the Smallest String**
```
smallest_string = strings[0]
```
- The function begins by assuming the first string in the list (`strings[0]`) is the smallest string.
- **Why start with the first string?**
  - There must always be at least one string in the list (since no empty input list is handled in this function).
  - Starting with the first string ensures we have a valid initial reference to compare against other strings.

For example:
- If `strings = ["abc", "bcd", "cbad"]`, `smallest_string` is initially `"abc"`.

---

#### **2. Loop Through All Strings**
```
for string in strings:
```
- The function iterates through each string in the list. This ensures every string is considered when determining the smallest one.

---

#### **3. Compare String Lengths**
```
if len(string) < len(smallest_string):
    smallest_string = string
```
- For each string in the list, its length is compared to the current `smallest_string`.
- **If the current string's length is shorter, update `smallest_string`:**
  - `smallest_string` is updated to hold the current string.
  - This ensures that by the end of the loop, `smallest_string` holds the shortest string in the list.

**Why compare lengths?**
- The function is designed to find the **shortest** string, so the length of each string is the deciding factor.

---

#### **4. Return the Smallest String**
```
return smallest_string
```
- After the loop completes, `smallest_string` holds the shortest string in the list. This is returned as the final result.

---

### **Example Walkthrough**

#### **Example 1:**
```
strings = ["abc", "bcd", "cbad"]
```

1. **Initialize `smallest_string`:**
   - `smallest_string = "abc"`

2. **Iterate Through Strings:**
   - **Compare "abc" with itself:**  
     `len("abc") == len("abc")`. No change (`smallest_string` remains `"abc"`).
   - **Compare "bcd" with "abc":**  
     `len("bcd") == len("abc")`. No change (`smallest_string` remains `"abc"`).
   - **Compare "cbad" with "abc":**  
     `len("cbad") > len("abc")`. No change (`smallest_string` remains `"abc"`).

3. **Result:**  
   `return "abc"`

---

#### **Example 2:**
```
strings = ["longest", "mid", "tiny"]
```

1. **Initialize `smallest_string`:**
   - `smallest_string = "longest"`

2. **Iterate Through Strings:**
   - **Compare "longest" with itself:**  
     `len("longest") == len("longest")`. No change (`smallest_string` remains `"longest"`).
   - **Compare "mid" with "longest":**  
     `len("mid") < len("longest")`. Update `smallest_string = "mid"`.
   - **Compare "tiny" with "mid":**  
     `len("tiny") > len("mid")`. No change (`smallest_string` remains `"mid"`).

3. **Result:**  
   `return "mid"`

---

#### **Example 3:**
```
strings = ["a", "abc", "ab"]
```

1. **Initialize `smallest_string`:**
   - `smallest_string = "a"`

2. **Iterate Through Strings:**
   - **Compare "a" with itself:**  
     `len("a") == len("a")`. No change (`smallest_string` remains `"a"`).
   - **Compare "abc" with "a":**  
     `len("abc") > len("a")`. No change (`smallest_string` remains `"a"`).
   - **Compare "ab" with "a":**  
     `len("ab") > len("a")`. No change (`smallest_string` remains `"a"`).

3. **Result:**  
   `return "a"`

---

### **Why This Works**

The algorithm systematically checks every string in the list and keeps track of the shortest one. By comparing 
lengths one by one, it ensures that no shorter string is overlooked.

---

### **Edge Cases**

#### 1. **Single String in List:**
Input: `["abc"]`  
- The loop runs once, and the single string is returned: `"abc"`.

#### 2. **All Strings Are Equal in Length:**
Input: `["abc", "def", "ghi"]`  
- The function returns the first string: `"abc"`, as all strings are equally short.

#### 3. **Empty Input List (Not Handled):**
Input: `[]`  
- This case would raise an `IndexError` because the code assumes the list is non-empty (`strings[0]` is accessed
without checking if the list is empty). To handle this, you could add a check:
  ```
  if not strings:
      return None
  ```
  
---

### **Key Takeaways**
- **Purpose:** Find the shortest string in a list of strings by comparing lengths.
- **Efficiency:** The function ensures only one pass through the list, making it fast and memory-efficient.
- **Limitations:** Assumes the input list is non-empty.

---

### **3. Helper Function: `remove_nonexistent_characters(string, potential_common_characters)`**
This function removes characters from the set `potential_common_characters` if they are not present in the given `string`.

---

### **Purpose**
This function refines the set of potential common characters by removing characters from it that are not present in a given string.

---

### **Detailed Explanation**

#### **Input**
The function takes two arguments:
1. `string`: A string from the list being processed.
2. `potential_common_characters`: A set of characters that are potentially common across all strings.

#### **Output**
The function modifies `potential_common_characters` **in place** by removing any characters that are not found in `string`.
This step ensures that `potential_common_characters` only contains characters that are present in all strings processed so far.

---

### **Code Walkthrough**

#### **1. Create a Set of Unique Characters from the String**
```
unique_string_characters = set(string)
```

- Converts the characters in the string into a set (`unique_string_characters`).
- **Why convert to a set?**
  - A set allows for efficient membership checks (e.g., `character in unique_string_characters` is O(1).
  - This step eliminates duplicate characters from the string, which is unnecessary to process multiple times.

Example:  
If `string = "bcd"`, then `unique_string_characters = {'b', 'c', 'd'}`.

---

#### **2. Iterate Over `potential_common_characters`**
```
for character in list(potential_common_characters):
```

- **Why `list(potential_common_characters)`?**
  - The function iterates over a copy of the set (using `list()`), rather than the original set itself.
  - This is important because modifying a set (removing elements) while iterating over it directly raises a `RuntimeError` in Python.

Example:  
If `potential_common_characters = {'a', 'b', 'c'}`, the `list()` function creates a temporary copy: `['a', 'b', 'c']`.

---

#### **3. Check If a Character Is Missing**
```
if character not in unique_string_characters:
    potential_common_characters.remove(character)
```

- For each character in the `potential_common_characters`, it checks if that character is **not** present in
`unique_string_characters` (the set of characters in the current string).
- If the character is missing, it is removed from `potential_common_characters`.

---

### **Example Walkthrough**

#### Input: 
```
string = "bcd"
potential_common_characters = {'a', 'b', 'c'}
```

1. **Create a Set of Unique Characters from the String:**  
   `unique_string_characters = {'b', 'c', 'd'}`.

2. **Iterate Over `potential_common_characters`:**  
   - `list(potential_common_characters) = ['a', 'b', 'c']`.

3. **Check Each Character:**  
   - `'a'` is **not** in `unique_string_characters`, so remove it from `potential_common_characters`.  
     Updated `potential_common_characters = {'b', 'c'}`.
   - `'b'` **is** in `unique_string_characters`, so keep it in the set.
   - `'c'` **is** in `unique_string_characters`, so keep it in the set.

4. **Result:**  
   After processing, `potential_common_characters = {'b', 'c'}`.

---

### **Why This Works**

This function works by progressively refining the set of potential common characters, ensuring that only characters 
present in all processed strings are retained.

- If a character is missing from any string, it cannot be a common character and is immediately removed from
`potential_common_characters`.

---

### **Edge Cases**

#### 1. **Empty String**
If the input `string` is empty (`""`), then `unique_string_characters = set()`.  
- Every character in `potential_common_characters` will fail the check (`character not in unique_string_characters`)
and be removed.  
- Result: `potential_common_characters` becomes an empty set (`set()`).

#### 2. **Empty `potential_common_characters`**
If `potential_common_characters` is already empty, the function has no work to do.  
- Result: The function immediately returns with no changes.

#### 3. **No Overlap Between `string` and `potential_common_characters`**
If `string` contains no characters in `potential_common_characters`, all characters will be removed.  
- Example:  
  - Input: `string = "xyz"`, `potential_common_characters = {'a', 'b', 'c'}`.  
  - Result: `potential_common_characters = set()`.

---

### **Key Takeaways**
1. **Purpose:** Refines `potential_common_characters` by removing characters not present in a given string.
2. **Efficiency:** Uses sets for fast membership checks and in-place modification of the input set.
3. **Robustness:** Handles edge cases like empty strings or no overlap effectively.

---

### **Test Cases**

#### **Input 1: `common_characters(["abc", "bcd", "cbad"])`**
1. **Find smallest string:**  
   The smallest string is `"abc"` (length 3).  

2. **Initialize potential common characters:**  
   `potential_common_characters = {'a', 'b', 'c'}` (set of characters from `"abc"`).

3. **Process each string:**  
   - For `"abc"`, no characters are removed (`{'a', 'b', 'c'}` remains unchanged).
   - For `"bcd"`, `'a'` is not in `"bcd"`, so it is removed. Now `{'b', 'c'}` remains.
   - For `"cbad"`, no additional characters are removed. Final set: `{'b', 'c'}`.

4. **Result:**  
   Convert `{'b', 'c'}` to a list and return: `['b', 'c']`.

---

#### **Input 2: `common_characters(["a", "b", "c"])`**
1. **Find smallest string:**  
   The smallest string is `"a"`.  

2. **Initialize potential common characters:**  
   `potential_common_characters = {'a'}`.

3. **Process each string:**  
   - For `"a"`, no changes.
   - For `"b"`, `'a'` is removed because it is not in `"b"`. Now the set is empty.
   - For `"c"`, no changes (the set is already empty).

4. **Result:**  
   Return an empty list: `[]`.

---

#### **Input 3: `common_characters(["aaaa", "a"])`**
1. **Find smallest string:**  
   The smallest string is `"a"`.  

2. **Initialize potential common characters:**  
   `potential_common_characters = {'a'}`.

3. **Process each string:**  
   - For `"aaaa"`, no changes (all characters are `'a'`).
   - For `"a"`, no changes.

4. **Result:**  
   Return `['a']`.

---

#### **Input 4: `common_characters(["*abc!d", "de!f*", "**!!!****d*****"])`**
1. **Find smallest string:**  
   The smallest string is `"de!f*"` (length 5).  

2. **Initialize potential common characters:**  
   `potential_common_characters = {'d', 'e', '!', 'f', '*'}`.

3. **Process each string:**  
   - For `"*abc!d"`, remove `'e'` and `'f'`. Remaining: `{'d', '!', '*'}`.
   - For `"de!f*"`, no changes.
   - For `"**!!!****d*****"`, no changes.

4. **Result:**  
   Return `['d', '!', '*']`.

---

### **Key Points**
- The algorithm optimizes checks by focusing on the smallest string.
- It uses sets for efficient membership checks and updates.
- The function ensures that only characters present in all strings are returned.

"""
