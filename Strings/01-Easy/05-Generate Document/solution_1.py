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

## Optimal Space & Time Complexity
```
O(n + m) time | O(c) space - where `n` is the number of characters, `m` is the length of the document,
and `c` is the number of unique characters in the characters string.
```

"""

# =========================================================================================================================== #

# Solution:


# O(m * (n + m)) time | O(1) space - where `n` is the number
# of characters, `m` is the length of the document
def generate_document(characters, document):
    # Iterate through each character in the document
    for character in document:
        # Count how many times the current character appears in the document
        document_frequency = count_character_frequency(character, document)

        # Count how many times the current character appears in the given characters
        character_frequency = count_character_frequency(character, characters)

        # If the character appears more frequently in the document than in the given characters,
        # it means we don't have enough characters to generate the document
        if document_frequency > character_frequency:
            return False  # Return False, indicating the document cannot be generated

    # If all characters in the document have sufficient frequency in the given characters,
    # return True, indicating the document can be generated
    return True


# Helper function to count the frequency of a specific character in a target string
def count_character_frequency(character, target):
    frequency = 0  # Initialize frequency counter

    # Iterate through each character in the target string
    for char in target:
        # If the current character matches the one we're counting, increment the frequency
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

Let's analyze the time and space complexity of the provided code.

### Code Breakdown

1. **`count_character_frequency(character, target)`**:
   - This function iterates through the `target` string and counts how many times the `character` appears.
   
   - Time Complexity: `O(n)`, where `n` is the length of the `target` string.
   - Space Complexity: `O(1)`, as it only uses a single integer variable (`frequency`) to store the count.

2. **`generate_document(characters, document)`**:
   - This function iterates through each character in the `document` string.
   - For each character, it calls `count_character_frequency` twice:
     - Once to count the frequency of the character in the `document`.
     - Once to count the frequency of the character in the `characters`.
   - It then compares the two frequencies and returns `False` if the frequency in the `document` is greater than
   the frequency in `characters`.
   - If all characters pass the check, it returns `True`.

### Time Complexity

- Let `n` be the length of the `document` string.
- Let `m` be the length of the `characters` string.
- For each character in the `document`:
  - `count_character_frequency(character, document)` takes `O(n)` time.
  - `count_character_frequency(character, characters)` takes `O(m)` time.
  
- Since these operations are performed for each character in the `document`, the total time complexity is:
  
    `O(n * (n + m))`
  
- In the worst case, this simplifies to `O(n^2 + nm)`.

### Space Complexity

- The space complexity is determined by the additional space used by the functions.
- Both `count_character_frequency` and `generate_document` use a constant amount of extra space (e.g., the `frequency` variable).

- Therefore, the space complexity is `O(1)`.

### Summary

- **Time Complexity**: `O(n^2 + nm)`
- **Space Complexity**: `O(1)`

### Optimization Consideration

The current implementation is inefficient because it repeatedly counts the frequency of characters in the `document` and 
`characters` strings. A more efficient approach would be to precompute the frequency of each character in both strings 
using a hash map (dictionary), which would reduce the time complexity to `O(n + m)`.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### Explanation of the Code

The code defines two functions: `generate_document` and `count_character_frequency`. The purpose of the code is
to determine whether a given `document` string can be generated using the characters provided in the `characters` string.
Here's a detailed breakdown of how it works:

---

### 1. **`count_character_frequency` Function**
This function calculates the frequency of a specific character in a given string (`target`).

- **Parameters:**
  - `character`: The character whose frequency needs to be counted.
  - `target`: The string in which the frequency of the character is to be counted.

- **Logic:**
  - Initialize a counter `frequency` to 0.
  - Iterate through each character in the `target` string.
  - If the current character matches the `character` being counted, increment the `frequency` counter.
  - Return the final count of the character.

- **Example:**
  - `count_character_frequency("a", "apple")` returns `1` because "a" appears once in "apple".

---

### 2. **`generate_document` Function**
This function checks whether the `document` string can be generated using the characters provided in the `characters` string.

- **Parameters:**
  - `characters`: A string containing the available characters.
  - `document`: The string that needs to be generated using the characters.

- **Logic:**
  - Iterate through each character in the `document` string.
  - For each character, calculate:
    - `document_frequency`: The frequency of the character in the `document`.
    - `character_frequency`: The frequency of the character in the `characters` string.
  - If the `document_frequency` of any character exceeds its `character_frequency`, it means there are not enough characters
  in `characters` to generate the `document`. In this case, return `False`.
  - If all characters in the `document` have sufficient frequency in `characters`, return `True`.

- **Edge Cases:**
  - If the `document` is an empty string, it can always be generated, so return `True`.
  - If the `characters` string is empty but the `document` is not, it cannot be generated, so return `False`.

---

### 3. **Test Cases**

#### Test Case 1:
```
print(generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))  # True
```
- **Explanation:**
  - The `characters` string contains all the necessary characters to generate the `document` string.
  - For example, "A", "l", "g", "o", etc., all appear in sufficient quantities in `characters`.
  - Therefore, the function returns `True`.

#### Test Case 2:
```
print(generate_document("A", "a"))  # False
```
- **Explanation:**
  - The `characters` string contains "A", but the `document` string contains "a".
  - Since the function is case-sensitive, "A" and "a" are treated as different characters.
  - Therefore, the function returns `False`.

#### Test Case 3:
```
print(generate_document("a hsgalhsa sanbjksbdkjba kjx", ""))  # True
```
- **Explanation:**
  - The `document` string is empty, so it can always be generated.
  - Therefore, the function returns `True`.

#### Test Case 4:
```
print(generate_document("", "hello"))  # False
```
- **Explanation:**
  - The `characters` string is empty, but the `document` string is not.
  - Since there are no characters available to generate the `document`, the function returns `False`.

---

### 4. **Key Points**
- The function is **case-sensitive**. For example, "A" and "a" are treated as different characters.
- The function assumes that the order of characters does not matter. It only checks the frequency of characters.
- The time complexity of the function is **O(n * m)**, where:
  - `n` is the length of the `document` string.
  - `m` is the length of the `characters` string.
  - This is because the `count_character_frequency` function is called for each character in the `document`.

---

### 5. **Optimization**
The current implementation is not optimal because it repeatedly counts the frequency of characters in the `characters` string.
A more efficient approach would be to:
1. Use a dictionary to store the frequency of each character in the `characters` string.
2. Iterate through the `document` string and decrement the frequency in the dictionary.
3. If any character's frequency becomes negative, return `False`.

"""
