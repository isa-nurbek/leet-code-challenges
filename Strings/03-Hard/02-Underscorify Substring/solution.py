# Problem Description:

"""
                                        Underscorify Substring

Write a function that takes in two strings: a main string and a potential substring of the main string. The
function should return a version of the main string with every instance of the substring in it wrapped between underscores.

If two or more instances of the substring in the main string overlap each other or sit side by side, the underscores
relevant to these substrings should only appear on the far left of the leftmost substring and on the far right of the rightmost
substring. If the main string doesn't contain the other string at all, the function should return the main string intact.


## Sample Input:
```
string = "testthis is a testtest to see if testestest it works"
substring = "test"
```

## Sample Output:
```
"_test_this is a _testtest_ to see if _testestest_ it works"
```

## Optimal Time & Space Complexity:
```
Average case: `O(n + m)` | `O(n)` space - where `n` is the length of the main string
and `m` is the length of the substring.
```

"""

# =========================================================================================================================== #

# Solution:


# Average case: `O(n + m)` | `O(n)` space - where `n` is the length
# of the main string and `m` is the length of the substring
def underscorify_substring(string, substring):
    """
    Main function to underscorify all occurrences of the substring in the string.

    Args:
        string (str): The original string.
        substring (str): The substring to be underscored.

    Returns:
        str: The modified string with underscores around the substrings.

    Raises:
        TypeError: If either argument is not a string.
    """
    if not isinstance(string, str) or not isinstance(substring, str):
        raise TypeError("Both arguments must be strings.")

    # Step 1: Get all locations where the substring occurs in the string.
    locations = get_locations(string, substring)

    # Step 2: Collapse overlapping or adjacent locations to avoid multiple underscores.
    locations = collapse(locations)

    # Step 3: Add underscores around the substrings in the original string.
    return underscorify(string, locations)


def get_locations(string, substring):
    """
    Finds all the start and end indices of the substring in the string.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        list: A list of lists, where each inner list contains the start and end indices of a substring occurrence.

    Raises:
        TypeError: If the first argument is not a string.
    """
    if not isinstance(string, str):
        raise TypeError("The first argument must be a string.")

    locations = []
    start_idx = 0

    # Loop through the string to find all occurrences of the substring.
    while start_idx < len(string):
        next_idx = string.find(substring, start_idx)

        if next_idx != -1:
            # If the substring is found, record its start and end indices.
            locations.append([next_idx, next_idx + len(substring)])
            start_idx = next_idx + 1
        else:
            # If no more occurrences are found, break the loop.
            break

    return locations


def collapse(locations):
    """
    Collapses overlapping or adjacent locations to avoid multiple underscores.

    Args:
        locations (list): A list of lists, where each inner list contains the start and end indices of a substring occurrence.

    Returns:
        list: A list of lists with overlapping or adjacent locations merged.
    """
    if not len(locations):
        return locations

    # Initialize the new_locations list with the first location.
    new_locations = [locations[0]]
    previous = new_locations[0]

    # Loop through the remaining locations and merge overlapping or adjacent ones.
    for i in range(1, len(locations)):
        current = locations[i]

        if current[0] <= previous[1]:
            # If the current location overlaps or is adjacent to the previous one, merge them.
            previous[1] = current[1]
        else:
            # If not, add the current location to the new_locations list.
            new_locations.append(current)
            previous = current

    return new_locations


def underscorify(string, locations):
    """
    Adds underscores around the substrings in the original string based on the locations.

    Args:
        string (str): The original string.
        locations (list): A list of lists, where each inner list contains the start and end indices of a substring occurrence.

    Returns:
        str: The modified string with underscores around the substrings.
    """
    locations_idx = 0
    string_idx = 0
    final_chars = []

    # Loop through the string and add underscores at the specified locations.
    while string_idx < len(string) and locations_idx < len(locations):
        current_location = locations[locations_idx]

        if string_idx == current_location[0]:
            # Add an underscore at the start of the substring.
            final_chars.append("_")

        # Add the current character to the final_chars list.
        final_chars.append(string[string_idx])

        if string_idx == current_location[1] - 1:
            # Add an underscore at the end of the substring.
            final_chars.append("_")
            locations_idx += 1

        string_idx += 1

    # If there are remaining locations, add an underscore.
    if locations_idx < len(locations):
        final_chars.append("_")

    # If there are remaining characters in the string, add them to the final_chars list.
    if string_idx < len(string):
        final_chars.append(string[string_idx:])

    # Join the characters to form the final string.
    return "".join(final_chars)


# Test Cases:
string = "testthis is a testtest to see if testestest it works"
substring = "test"

string_2 = "ttttttttttttttbtttttctatawtatttttastvb"
substring_2 = "ttt"

string_3 = "ababababababababababab"
substring_3 = "a"

print(underscorify_substring(string, substring))
# Output: "_test_this is a _testtest_ to see if _testestest_ it works"

print(underscorify_substring(string_2, substring_2))
# Output: "_tttttttttttttt_b_ttttt_ctatawta_ttttt_astvb"

print(underscorify_substring(string_3, substring_3))
# Output: "_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b"

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

Let's analyze the time and space complexity of the `underscorify_substring` function and its helper functions.

### 1. **`get_locations` Function**
   - **Time Complexity**: `O(n * m)`, where:
     - `n` is the length of the `string`.
     - `m` is the length of the `substring`.
     - This is because `string.find(substring, start_idx)` is called in a loop, and each call to `find` can
     take up to `O(m)` time in the worst case.
     
   - **Space Complexity**: `O(k)`, where `k` is the number of occurrences of the `substring` in the `string`.
   This is because we store the start and end indices of each occurrence in the `locations` list.

---

### 2. **`collapse` Function**
   - **Time Complexity**: `O(k)`, where `k` is the number of locations (occurrences of the `substring`).
   This is because we iterate through the `locations` list once.
   - **Space Complexity**: `O(k)`, as we create a new list `new_locations` to store the collapsed ranges.

---

### 3. **`underscorify` Function**
   - **Time Complexity**: `O(n)`, where `n` is the length of the `string`. This is because we iterate through
   the `string` once and append characters to the `final_chars` list.
   - **Space Complexity**: `O(n)`, as we store the final result in the `final_chars` list, which can grow up
   to the size of the input `string` plus the added underscores.

---

### 4. **Overall `underscorify_substring` Function**

   - **Time Complexity**: `O(n * m + k + n)`, which simplifies to O(n * m) in the worst case (since `k` can be up to `n/m`).
   
   - **Space Complexity**: `O(n + k)`, where:
     - `O(k)` comes from storing the locations.
     - `O(n)` comes from storing the final output.

---

### Summary
- **Time Complexity**: `O(n * m)`
- **Space Complexity**: `O(n + k)`

Where:
- `n` = length of the input `string`
- `m` = length of the `substring`
- `k` = number of occurrences of the `substring` in the `string` (can be up to `n/m`).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code defines a function, `underscorify_substring`, which takes a string and a substring as input and
returns a new string where all occurrences of the substring are surrounded by underscores (`_`).
The implementation follows a structured approach, breaking the problem into three main steps:

1. **Find all occurrences of the substring in the string.**
2. **Merge overlapping or adjacent occurrences.**
3. **Insert underscores at the correct positions.**

---

## **Detailed Breakdown of Each Function**
### **1. `underscorify_substring(string, substring)`**
This is the main function that orchestrates the process.

- **Step 1:** Calls `get_locations(string, substring)` to get all occurrences of `substring` within `string`.
- **Step 2:** Calls `collapse(locations)` to merge overlapping or adjacent occurrences.
- **Step 3:** Calls `underscorify(string, locations)` to insert underscores around the occurrences.

### **2. `get_locations(string, substring)`**
This function finds all starting and ending indices of `substring` in `string`.

#### **How It Works:**
- **It uses `string.find(substring, start_idx)`** to find occurrences of `substring`, starting from `start_idx`.
- **Each occurrence is stored as a list `[start, end]`** where:
  - `start`: index of the first character of `substring`
  - `end`: index of the last character of `substring` + 1
- **Moves `start_idx` forward by 1** to find overlapping occurrences.

#### **Example:**
For `string = "testtest"` and `substring = "test"`, this function finds:
```
[[0, 4], [4, 8]]
```
This means "test" appears at positions `[0:4]` and `[4:8]`.

---

### **3. `collapse(locations)`**
This function merges overlapping or adjacent occurrences of `substring`.

#### **How It Works:**
- If two intervals overlap or touch (i.e., `current[0] <= previous[1]`), they are merged into one.
- Otherwise, the interval is added separately.

#### **Example:**
For `[[0, 4], [4, 8], [10, 14]]`, after merging:
```
[[0, 8], [10, 14]]
```
- `[0,4]` and `[4,8]` are merged because `4 == 4`.
- `[10,14]` remains separate.

---

### **4. `underscorify(string, locations)`**
This function constructs the final string with underscores.

#### **How It Works:**
- Iterates through `string`, keeping track of `locations`.
- **When reaching `start` of a substring, inserts `_`.**
- **When reaching `end` of a substring, inserts another `_`.**
- Adds characters from `string` into `final_chars` (a list).
- Joins `final_chars` into a string.

#### **Example:**
For `string = "testthis is a testtest to see"` and `locations = [[0, 4], [14, 22]]`, output is:
```
"_test_this is a _testtest_ to see"
```

---

## **Example Walkthrough**
### **Example 1**
```
string = "testthis is a testtest to see if testestest it works"
substring = "test"
print(underscorify_substring(string, substring))
```
#### **Step 1: `get_locations()`**
Find occurrences:
```
[[0, 4], [14, 18], [18, 22], [26, 30], [30, 34], [32, 36]]
```
#### **Step 2: `collapse()`**
Merge overlapping/adjacent:
```
[[0, 4], [14, 22], [26, 36]]
```
#### **Step 3: `underscorify()`**
Insert underscores:
```
"_test_this is a _testtest_ to see if _testestest_ it works"
```

### **Example 2**
```
string = "ttttttttttttttbtttttctatawtatttttastvb"
substring = "ttt"
print(underscorify_substring(string, substring))
```
#### **Step 1: `get_locations()`**
Find occurrences:
```
[[0, 3], [1, 4], [2, 5], ..., [28, 31]]
```
#### **Step 2: `collapse()`**
Merge:
```
[[0, 14], [16, 19], [25, 31]]
```
#### **Step 3: `underscorify()`**
Output:
```
"_tttttttttttttt_b_ttttt_ctatawta_ttttt_astvb"
```

---

## **Conclusion**

This code efficiently finds and underscores substrings while handling overlaps, making it a useful text-processing algorithm.

"""
