# Description:

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

## Optimal Space & Time Complexity:

```
O(n * m) time | O(m) space - where `n` is the number of strings, and `m` is the length of the longest string.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * m) time | O(c) space - where `n`` is the number of strings, `m` is the
# length of the longest string, and `c` is the number of unique characters across
# all strings
def common_characters(strings):
    character_counts = {}

    for string in strings:
        unique_string_characters = set(string)

        for character in unique_string_characters:
            if character not in character_counts:
                character_counts[character] = 0
            character_counts[character] += 1

    final_characters = []
    for character, count in character_counts.items():
        if count == len(strings):
            final_characters.append(character)

    return final_characters


# Test Cases
print(common_characters(["abc", "bcd", "cbad"]))  # Output: ['b', 'c']
print(common_characters(["a", "b", "c"]))  # Output: []
print(common_characters(["aaaa", "a"]))  # Output: ['a']
print(
    common_characters(["*abc!d", "de!f*", "**!!!****d*****"])
)  # Output: ['d', '!', '*']

# =========================================================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity:

1. **Loop through each string**: The outer loop iterates over each string in the `strings` list.
If there are `n` strings, this loop runs `n` times.

2. **Convert each string to a set**: For each string, converting it to a set takes `O(m)` time,
where `m` is the length of the string. This is because each character in the string needs to be added to the set.

3. **Loop through unique characters in the set**: For each unique character in the set, the inner loop runs.
In the worst case, this could be `O(m)` times if all characters in the string are unique.

4. **Update character counts**: The operation of checking if a character is in the `character_counts` dictionary and
updating its count is `O(1)` on average, thanks to the hash table implementation of Python dictionaries.

5. **Final loop to find common characters**: The final loop iterates over the `character_counts` dictionary, which has
at most `k` entries, where `k` is the number of unique characters across all strings. This loop runs in `O(k)` time.

### Overall Time Complexity:
- The dominant part of the time complexity comes from the nested loops. For each string (of length `m`), we perform `O(m)`
operations to convert it to a set and then `O(m)` operations to update the character counts. Since this is done
for `n` strings, the total time complexity is:
  
    `O(n * m)`
  
where `n` is the number of strings and `m` is the average length of the strings.

### Space Complexity:

1. **`character_counts` dictionary**: This dictionary stores counts for each unique character across all strings.
In the worst case, if all characters in all strings are unique, this dictionary could have up to `k` entries,
where `k` is the total number of unique characters across all strings.

2. **`final_characters` list**: This list stores the characters that are common to all strings. In the worst case,
this list could have up to `k` entries, but typically it will be much smaller.

### Overall Space Complexity:
- The space complexity is dominated by the `character_counts` dictionary, which can have up to `k` entries. Therefore,
the space complexity is: `O(k)`
  
where `k` is the number of unique characters across all strings.

### Summary:
- **Time Complexity**: `O(n * m)`
- **Space Complexity**: `O(k)`

Here, `n` is the number of strings, `m` is the average length of the strings, and `k` is the number of unique characters
across all strings.

"""

# =========================================================================================================================== #

# Code Explanation:

"""

This function, `common_characters`, identifies characters that are common across all strings in the input list.
Let's break it down step by step:

### Code Breakdown
#### 1. **Initialization**:
```
character_counts = {}
```
This dictionary keeps track of how many strings each character appears in.

---

#### 2. **Iterate Through the Strings**:
```
for string in strings:
    unique_string_characters = set(string)
```
- Each string is processed one at a time.
- **`set(string)`** ensures only unique characters from the current string are considered. This avoids counting
duplicate characters in a single string.

---

#### 3. **Update Character Counts**:
```
for character in unique_string_characters:
    if character not in character_counts:
        character_counts[character] = 0
    character_counts[character] += 1
```
- For each unique character in the current string:
  - If the character is not already in `character_counts`, initialize its count to `0`.
  - Increment the count to indicate that this character appears in the current string.

At the end of this loop, `character_counts` contains a mapping of each character to the number of strings in which it appears.

---

#### 4. **Filter Common Characters**:
```
final_characters = []
for character, count in character_counts.items():
    if count == len(strings):
        final_characters.append(character)
```
- The function loops through the `character_counts` dictionary.
- If a character's count equals the total number of strings (`len(strings)`), it means the character is present in every string.
- Such characters are added to the `final_characters` list.

---

#### 5. **Return the Result**:
```
return final_characters
```
The `final_characters` list, containing the common characters, is returned.

---

### Example Walkthroughs

#### Example 1:
```
print(common_characters(["abc", "bcd", "cbad"]))  # Output: ['b', 'c']
```
1. **Unique Characters**:
   - `"abc"` → `{'a', 'b', 'c'}`
   - `"bcd"` → `{'b', 'c', 'd'}`
   - `"cbad"` → `{'a', 'b', 'c', 'd'}`

2. **Character Counts**:
   - `'a': 2`, `'b': 3`, `'c': 3`, `'d': 2`

3. **Final Characters**:
   - Only `'b'` and `'c'` have a count of `3` (equal to the number of strings), so they are returned.

---

#### Example 2:
```
print(common_characters(["a", "b", "c"]))  # Output: []
```
- Each string has only one unique character.
- No character is common across all strings, so the output is an empty list.

---

#### Example 3:
```
print(common_characters(["aaaa", "a"]))  # Output: ['a']
```
- `"aaaa"` → `{'a'}`
- `"a"` → `{'a'}`
- `'a': 2` (matches the number of strings), so `'a'` is returned.

---

#### Example 4:
```
print(common_characters(["*abc!d", "de!f*", "**!!!****d*****"]))  # Output: ['d', '!', '*']
```
1. **Unique Characters**:
   - `"*abc!d"` → `{'*', 'a', 'b', 'c', '!', 'd'}`
   - `"de!f*"` → `{'*', 'e', 'f', '!', 'd'}`
   - `"**!!!****d*****"` → `{'*', '!', 'd'}`

2. **Character Counts**:
   - `'*': 3`, `'!': 3`, `'d': 3`, `'a': 1`, `'b': 1`, `'c': 1`, `'e': 1`, `'f': 1`

3. **Final Characters**:
   - Only `'*'`, `'!'`, and `'d'` have a count of `3` (equal to the number of strings), so they are returned.

---

### Summary
The function effectively finds common characters by leveraging a dictionary to count occurrences and
filtering based on the number of strings. It ensures efficiency by processing only unique characters
in each string and avoids unnecessary space usage by focusing on characters common across all inputs.

"""
