# Problem Description:

"""

                                        Generate Document

You're given a string of available characters and a string representing a document that you need to generate. Write a function
that determines if you can generate the document using the available characters. If you can generate the document, your
function should return `True`; otherwise, it should return `False`.

You're only able to generate the document if the frequency of unique characters in the characters string is greater than or
equal to the frequency of unique characters in the document string. For example, if you're given `characters = "abcabc"`
and `document = "aabbccc"` you cannot generate the document because you're missing one `c`.

The document that you need to create may contain any characters, including special characters, capital letters, numbers,
and spaces.

Note: you can always generate the empty string (`""`).


## Sample Input:
```
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
```

## Sample Output:
```
True
```

## Optimal Time & Space Complexity
```
O(n + m) time | O(c) space - where `n` is the number of characters, `m` is the length of the document,
and `c` is the number of unique characters in the characters string
```

"""

# =========================================================================================================================== #

# Solution:


# O(c * (n + m)) time | O(c) space
def generate_document(characters, document):
    # A set to keep track of characters that have already been counted
    alreadyCounted = set()

    # Iterate through each character in the document
    for character in document:
        # If the character has already been counted, skip it
        if character in alreadyCounted:
            continue

        # Count the frequency of the current character in the document
        document_frequency = count_character_frequency(character, document)
        # Count the frequency of the current character in the characters string
        characters_frequency = count_character_frequency(character, characters)

        # If the character appears more frequently in the document than in the characters string,
        # it means we don't have enough characters to generate the document, so return False
        if document_frequency > characters_frequency:
            return False

        # Mark the character as counted by adding it to the set
        alreadyCounted.add(character)

    # If all characters in the document can be generated from the characters string, return True
    return True


def count_character_frequency(character, target):
    # Initialize a counter for the frequency of the character
    frequency = 0

    # Iterate through each character in the target string
    for char in target:
        # If the current character matches the target character, increment the frequency counter
        if char == character:
            frequency += 1

    # Return the total count of the character in the target string
    return frequency


# Test Cases
print(generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))  # True
print(generate_document("A", "a"))  # False
print(generate_document("a hsgalhsa sanbjksbdkjba kjx", ""))  # True
print(generate_document("", "hello"))  # False

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

#### **Time Complexity**

Let:
- `n` be the length of `characters`
- `m` be the length of `document`

The function `generate_document()` iterates through every character in `document` `O(m)` and calls
`count_character_frequency()` twice for each unique character. 

The function `count_character_frequency()` itself iterates through `target`, which could be either
`characters` or `document`. 
In the worst case:
- It takes `O(n)` time when called on `characters`
- It takes `O(m)` time when called on `document`

Since `generate_document()` calls `count_character_frequency()` twice per unique character in `document`,
and in the worst case, every character in `document` is unique, the total worst-case time complexity is:

    O(m * (n + m)) = `O(mn + m^2)`

This is inefficient, especially for large inputs.

#### **Space Complexity**
- The `alreadyCounted` set stores unique characters from `document`, which takes at most `O(m)` space.
- `count_character_frequency()` uses only a few integer variables (constant space, `O(1)`).

- Overall, the function uses **`O(m)` additional space** for `alreadyCounted`.

Thus, the space complexity is: `O(m)`

### Summary

- **Time Complexity**: O(mn + m^2)
- **Space Complexity**: O(m)

### **Optimized Approach**

A more efficient approach would be to precompute character frequencies using hash maps (dictionaries).
This would reduce the time complexity to `O(n + m)`, making it much more scalable.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""

The `generate_document` function checks whether a given `document` string can be generated using the characters
provided in the `characters` string. It does this by comparing the frequency of each character in the `document`
with the frequency of the same character in the `characters` string. If the frequency of any character in the
`document` exceeds its frequency in the `characters` string, the function returns `False`. Otherwise, it returns `True`.

### How the Function Works:
1. **Initialization**:
   - The function starts by initializing an empty set called `alreadyCounted` to keep track of characters that have
   already been processed.

2. **Iterate Through the Document**:
   - The function iterates through each character in the `document` string.
   - If the character has already been processed (i.e., it is in the `alreadyCounted` set), the function skips further
   processing for that character using `continue`.

3. **Count Frequencies**:
   - For each unique character in the `document`, the function calculates its frequency in both the `document` and
   the `characters` strings using the `count_character_frequency` function.
   - The `count_character_frequency` function counts how many times a specific character appears in a given string.

4. **Comparison**:
   - If the frequency of the character in the `document` is greater than its frequency in the `characters` string,
   the function immediately returns `False`, indicating that the `document` cannot be generated using the given `characters`.

5. **Update Already Counted Set**:
   - If the character's frequency in the `document` is less than or equal to its frequency in the `characters` string,
   the character is added to the `alreadyCounted` set to avoid redundant processing.

6. **Final Return**:
   - If the function completes the loop without finding any character in the `document` that exceeds its frequency in the
   `characters` string, it returns `True`, indicating that the `document` can be generated using the given `characters`.

### Test Case Analysis:
1. **Test Case 1**:
   ```
   print(generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))  # True
   ```
   - The `characters` string contains all the necessary characters to generate the `document` string.
   - The function returns `True` because the frequency of each character in the `document` is less than or equal to
   its frequency in the `characters` string.

2. **Test Case 2**:
   ```
   print(generate_document("A", "a"))  # False
   ```
   - The `characters` string contains only the character `'A'`, but the `document` string contains `'a'`.
   - Since `'a'` is not present in the `characters` string, the function returns `False`.

3. **Test Case 3**:
   ```
   print(generate_document("a hsgalhsa sanbjksbdkjba kjx", ""))  # True
   ```
   - The `document` string is empty, so no characters are needed to generate it.
   - The function returns `True` because an empty `document` can always be generated.

4. **Test Case 4**:
   ```
   print(generate_document("", "hello"))  # False
   ```
   - The `characters` string is empty, but the `document` string contains characters (`'h'`, `'e'`, `'l'`, `'o'`).
   - Since there are no characters available in the `characters` string to generate the `document`, the function returns `False`.

### Explanation of the Last Test Case:
- **Input**:
  - `characters = ""` (empty string)
  - `document = "hello"` (non-empty string)
- **Process**:
  - The function iterates through each character in the `document` string.
  - For each character, it checks if the character exists in the `characters` string.
  - Since the `characters` string is empty, the frequency of any character in the `characters` string is `0`.
  - The frequency of each character in the `document` string is greater than `0`, so the function returns `False`.
- **Conclusion**:
  - The `document` cannot be generated because there are no characters available in the `characters` string to form the `document`.

This function is useful for scenarios where you need to verify if a document can be constructed from a given set of characters,
such as in word games or text generation tasks.

"""
