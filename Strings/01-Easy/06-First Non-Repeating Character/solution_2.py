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
1 // The first non-repeating character is "b" and is found at index 1.
```

## Optimal Time & Space Complexity
```
O(n) time | O(1) space - where `n` is the length of the input string The constant space is
because the input string only has lowercase English-alphabet letters; thus, our hash table will
never have more than 26 character frequencies.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def first_non_repeating_character(string):
    # Create a dictionary to store the frequency of each character in the string
    character_frequencies = {}

    # Iterate through each character in the string to populate the frequency dictionary
    for character in string:
        # Use the get() method to retrieve the current count of the character.
        # If the character is not in the dictionary, return 0 as the default value.
        # Then, increment the count by 1 and store it back in the dictionary.
        character_frequencies[character] = character_frequencies.get(character, 0) + 1

    # Iterate through the string again, this time by index
    for idx in range(len(string)):
        # Get the character at the current index
        character = string[idx]

        # Check if the frequency of this character is 1 (i.e., it's non-repeating)
        if character_frequencies[character] == 1:
            # If it is, return the current index as it's the first non-repeating character
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

### Time Complexity:

1. **First Loop (Counting Frequencies):**
   - The first loop iterates over each character in the string to count the frequency of each character.
   - This loop runs in **O(n)** time, where `n` is the length of the string.

2. **Second Loop (Finding the First Non-Repeating Character):**
   - The second loop iterates over the string again to find the first character with a frequency of 1.
   - This loop also runs in **O(n)** time.

3. **Overall Time Complexity:**
   - The total time complexity is **O(n) + O(n) = O(n)**.

---

### Space Complexity:

1. **Character Frequency Dictionary:**
   - The `character_frequencies` dictionary stores the frequency of each character in the string.
   - In the worst case, if all characters are unique, the dictionary will store `n` key-value pairs.
   - Thus, the space complexity is **O(n)**.

2. **Overall Space Complexity:**
   - The space complexity is **O(n)** due to the dictionary.

---

### Summary:
- **Time Complexity:** **O(n)**
- **Space Complexity:** **O(n)**

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### Explanation of the Code

The function `first_non_repeating_character(string)` is designed to find the index of the first non-repeating
character in a given string. If all characters repeat, it returns `-1`.

---

### Step-by-Step Breakdown:

#### 1. **Initialize a Dictionary to Store Character Frequencies**
```
character_frequencies = {}
```
- This dictionary will store each character in the string as a key and its frequency (count of occurrences) as the value.

#### 2. **Count Character Frequencies**
```
for character in string:
    character_frequencies[character] = character_frequencies.get(character, 0) + 1
```
- The function iterates through the string, updating the frequency count of each character.
- `character_frequencies.get(character, 0)` retrieves the current frequency of `character` (defaulting to `0` if it does not exist).
- The `+1` increments the count.

#### 3. **Find the First Non-Repeating Character**
```
for idx in range(len(string)):
    character = string[idx]
    if character_frequencies[character] == 1:
        return idx
```
- The function iterates through the string a second time.
- It checks if the frequency of the current character is `1` (i.e., it appears only once in the string).
- If such a character is found, its index is returned immediately.

#### 4. **Return `-1` if No Unique Character Exists**
```
return -1
```
- If the loop completes without finding a unique character, `-1` is returned.

---

### Test Cases and Outputs

#### 1. **Example:** `"abcdcaf"`
**Step 1:** Character frequencies:
```
{'a': 2, 'b': 1, 'c': 2, 'd': 1, 'f': 1}
```
**Step 2:** The first character with a frequency of `1` is `'b'`, at index **1**.

**Output:** `1`

---

#### 2. **Example:** `"faadabcbbebdf"`
**Character frequencies:**
```
{'f': 2, 'a': 3, 'd': 2, 'b': 3, 'c': 1, 'e': 1}
```
- First non-repeating character: `'c'` at index **6**.

**Output:** `6`

---

#### 3. **Example:** `"a"`
- Only one character, which is unique.
- **Output:** `0`

---

#### 4. **Example:** `""` (Empty string)
- Since there are no characters, the function directly returns `-1`.

---

### Summary
- The function efficiently finds the first non-repeating character using a dictionary for frequency counting.
- It ensures an **O(n)** time complexity.
- It works for empty strings, single-character strings, and cases where no non-repeating character exists.

"""
