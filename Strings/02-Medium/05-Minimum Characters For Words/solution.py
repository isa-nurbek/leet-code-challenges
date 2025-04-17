# Problem Description:

"""
                                       Minimum Characters For Words

Write a function that takes in an array of words and returns the smallest array of characters needed to form
all of the words. The characters don't need to be in any particular order.

For example, the characters `["y", "r", "o", "u"]` are needed to form the words `["your", "you", "or", "yo"]`.

Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.


## Sample Input:
```
words = ["this", "that", "did", "deed", "them!", "a"]
```

## Sample Output:
```
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
// The characters could be ordered differently.
```

## Optimal Time & Space Complexity:
```
O(n * l) time | O(c) space - where `n` is the number of words, `l` is the length of the longest word,
and `c` is the number of unique characters across all words.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * l) time | O(c) space
def minimum_characters_for_words(words):
    # Dictionary to store the maximum frequency of each character across all words
    maximum_character_frequencies = {}

    # Iterate through each word in the list
    for word in words:
        # Calculate the frequency of each character in the current word
        character_frequencies = count_character_frequencies(word)

        # Update the global maximum frequencies with the frequencies from the current word
        update_maximum_frequencies(character_frequencies, maximum_character_frequencies)

    # Convert the maximum frequencies dictionary into a list of characters
    return make_array_from_character_frequencies(maximum_character_frequencies)


def count_character_frequencies(string):
    # Dictionary to store the frequency of each character in the given string
    character_frequencies = {}

    # Iterate through each character in the string
    for character in string:
        # If the character is not in the dictionary, initialize its frequency to 0
        if character not in character_frequencies:
            character_frequencies[character] = 0

        # Increment the frequency of the current character
        character_frequencies[character] += 1

    # Return the dictionary containing character frequencies
    return character_frequencies


def update_maximum_frequencies(frequencies, maximum_frequencies):
    # Iterate through each character in the frequencies dictionary
    for character in frequencies:
        frequency = frequencies[character]

        # If the character is already in the maximum frequencies dictionary,
        # update its frequency to the maximum between the current and new frequency
        if character in maximum_frequencies:
            maximum_frequencies[character] = max(
                frequency, maximum_frequencies[character]
            )
        else:
            # If the character is not in the maximum frequencies dictionary, add it
            maximum_frequencies[character] = frequency


def make_array_from_character_frequencies(character_frequencies):
    # List to store the final characters based on their frequencies
    characters = []

    # Iterate through each character in the frequencies dictionary
    for character in character_frequencies:
        frequency = character_frequencies[character]

        # Append the character to the list as many times as its frequency
        for _ in range(frequency):
            characters.append(character)

    # Return the list of characters
    return characters


# Test Case 1
print(minimum_characters_for_words(["this", "that", "did", "deed", "them!", "a"]))
# Output: ['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']

# Test Case 2
print(minimum_characters_for_words(["a", "abc", "ab", "boo"]))
# Output: ['a', 'b', 'c', 'o', 'o']

# Test Case 3
print(minimum_characters_for_words(["!!!2", "234", "222", "432"]))
# Output: ['!', '!', '!', '2', '2', '2', '3', '4']

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity

1. **`count_character_frequencies(string)`**:
   - This function iterates over each character in the string, which takes `O(n)` time, where `n`
   is the length of the string.
   - Inserting or updating a character in the dictionary takes `O(1)` on average.
   - **Overall time complexity**: `O(n)`.

2. **`update_maximum_frequencies(frequencies, maximum_frequencies)`**:
   - This function iterates over each character in the `frequencies` dictionary, which has at most `k`
   unique characters (where `k` is the number of unique characters in the word).
   - For each character, it performs a lookup and update in the `maximum_frequencies` dictionary, which
   takes `O(1)` on average.
   - **Overall time complexity**: `O(k)`.

3. **`make_array_from_character_frequencies(character_frequencies)`**:
   - This function iterates over each character in the `character_frequencies` dictionary, which has
   at most `m` unique characters (where `m` is the total number of unique characters across all words).
   - For each character, it appends the character to the list `frequency` times, where `frequency` is the
   count of that character.
   - The total number of append operations is equal to the sum of all frequencies, which is `O(M)`,
   where `M` is the total number of characters across all words.
   - **Overall time complexity**: `O(M)`.

4. **`minimum_characters_for_words(words)`**:
   - For each word in the list `words`, it calls `count_character_frequencies` and `update_maximum_frequencies`.
   - Let `N` be the total number of characters across all words, and `W` be the number of words.
   - The total time complexity for all calls to `count_character_frequencies` is `O(N)`.
   - The total time complexity for all calls to `update_maximum_frequencies` is `O(M)`, where `M` is
   the total number of unique characters across all words.
   - Finally, `make_array_from_character_frequencies` takes `O(M)` time.
   - **Overall time complexity**: `O(N + M)`.

### Space Complexity

1. **`count_character_frequencies(string)`**:
   - The space used by the `character_frequencies` dictionary is proportional to the number of unique
   characters in the string, which is `O(k)`, where `k` is the number of unique characters in the string.
   - **Overall space complexity**: `O(k)`.

2. **`update_maximum_frequencies(frequencies, maximum_frequencies)`**:
   - The `maximum_frequencies` dictionary grows as new characters are added, but it does not use additional
   space beyond what is already allocated.
   - **Overall space complexity**: `O(1)` (no additional space is used beyond the input).

3. **`make_array_from_character_frequencies(character_frequencies)`**:
   - The space used by the `characters` list is proportional to the total number of characters
   across all words, which is `O(M)`.
   - **Overall space complexity**: `O(M)`.

4. **`minimum_characters_for_words(words)`**:
   - The `maximum_character_frequencies` dictionary stores the maximum frequency of each unique character 
   across all words, which takes `O(M)` space.
   - The `characters` list returned by `make_array_from_character_frequencies` also takes `O(M)` space.
   - **Overall space complexity**: `O(M)`.

### Summary

- **Time Complexity**: `O(N + M)`, where `N` is the total number of characters across all words, and `M`
is the total number of unique characters across all words.

- **Space Complexity**: `O(M)`, where `M` is the total number of unique characters across all words.

This analysis assumes that the number of unique characters `M` is relatively small compared to the total
number of characters `N`, which is typically the case for most natural languages.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This Python program determines the minimum set of characters needed to construct all words from a given list.
The key idea is to compute the maximum frequency of each character across all words and then return an array
containing those characters, repeated according to their maximum frequency.

---

## **Code Breakdown**
### **1. `minimum_characters_for_words(words)` (Main Function)**
```
def minimum_characters_for_words(words):
    maximum_character_frequencies = {}

    for word in words:
        character_frequencies = count_character_frequencies(word)
        update_maximum_frequencies(character_frequencies, maximum_character_frequencies)

    return make_array_from_character_frequencies(maximum_character_frequencies)
```
#### **What It Does**
- Initializes `maximum_character_frequencies` as an empty dictionary to keep track of the highest
count of each character across all words.
- Iterates through each word in the input list and:
  - Calls `count_character_frequencies(word)` to get a dictionary with character counts for the word.
  - Calls `update_maximum_frequencies()` to update `maximum_character_frequencies` with the highest frequency
  of each character found so far.
- Finally, `make_array_from_character_frequencies()` converts the dictionary into an array where each character
appears according to its highest recorded frequency.

---

### **2. `count_character_frequencies(string)`**
```
def count_character_frequencies(string):
    character_frequencies = {}

    for character in string:
        if character not in character_frequencies:
            character_frequencies[character] = 0

        character_frequencies[character] += 1

    return character_frequencies
```
#### **What It Does**
- Takes a string as input and returns a dictionary where:
  - Keys are characters in the string.
  - Values are their frequencies (how many times they appear).
- Iterates through each character in the string:
  - If it's not in the dictionary, it initializes its count to `0`.
  - Increments its count.

#### **Example**
```
count_character_frequencies("deed") 
# Output: {'d': 2, 'e': 2}
```

---

### **3. `update_maximum_frequencies(frequencies, maximum_frequencies)`**
```
def update_maximum_frequencies(frequencies, maximum_frequencies):
    for character in frequencies:
        frequency = frequencies[character]

        if character in maximum_frequencies:
            maximum_frequencies[character] = max(
                frequency, maximum_frequencies[character]
            )
        else:
            maximum_frequencies[character] = frequency
```
#### **What It Does**
- Takes two dictionaries:
  1. `frequencies`: Character frequencies of the current word.
  2. `maximum_frequencies`: Stores the highest frequency encountered for each character.
- Iterates over `frequencies`:
  - If the character already exists in `maximum_frequencies`, updates it to the maximum value
  between the existing and new frequency.
  - Otherwise, adds the character to `maximum_frequencies` with its frequency.

#### **Example**

Suppose `maximum_frequencies = {'d': 2, 'e': 2}` and `frequencies = {'t': 1, 'h': 1, 'a': 1, 't': 1}`.
After calling `update_maximum_frequencies`, `maximum_frequencies` becomes:
```
{'d': 2, 'e': 2, 't': 2, 'h': 1, 'a': 1}
```
This ensures that each character is stored with its highest occurrence across all words.

---

### **4. `make_array_from_character_frequencies(character_frequencies)`**
```
def make_array_from_character_frequencies(character_frequencies):
    characters = []

    for character in character_frequencies:
        frequency = character_frequencies[character]

        for _ in range(frequency):
            characters.append(character)

    return characters
```
#### **What It Does**
- Converts the `maximum_character_frequencies` dictionary into an array.
- Iterates through each character and appends it to `characters` as many times as its frequency.

#### **Example**
If `character_frequencies = {'d': 2, 'e': 2, 't': 2, 'h': 1, 'a': 1, 'm': 1, '!': 1}`, the output array will be:
```
['d', 'd', 'e', 'e', 't', 't', 'h', 'a', 'm', '!']
```

---

## **Example Execution**

### **Input**
```
print(minimum_characters_for_words(["this", "that", "did", "deed", "them!", "a"]))
```

### **Step-by-Step Execution**
1. **First word: `"this"`**
   - Character frequencies: `{'t': 1, 'h': 1, 'i': 1, 's': 1}`
   - Updates `maximum_character_frequencies`: `{'t': 1, 'h': 1, 'i': 1, 's': 1}`

2. **Second word: `"that"`**
   - Character frequencies: `{'t': 2, 'h': 1, 'a': 1}`
   - Updates `maximum_character_frequencies`: `{'t': 2, 'h': 1, 'i': 1, 's': 1, 'a': 1}`

3. **Third word: `"did"`**
   - Character frequencies: `{'d': 1, 'i': 1}`
   - Updates `maximum_character_frequencies`: `{'t': 2, 'h': 1, 'i': 1, 's': 1, 'a': 1, 'd': 1}`

4. **Fourth word: `"deed"`**
   - Character frequencies: `{'d': 2, 'e': 2}`
   - Updates `maximum_character_frequencies`: `{'t': 2, 'h': 1, 'i': 1, 's': 1, 'a': 1, 'd': 2, 'e': 2}`

5. **Fifth word: `"them!"`**
   - Character frequencies: `{'t': 1, 'h': 1, 'e': 1, 'm': 1, '!': 1}`
   - Updates `maximum_character_frequencies`: `{'t': 2, 'h': 1, 'i': 1, 's': 1, 'a': 1, 'd': 2, 'e': 2, 'm': 1, '!': 1}`

6. **Sixth word: `"a"`**
   - No change since `a` is already in `maximum_character_frequencies`.

7. **Convert dictionary to list**
   - `['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']`

### **Final Output**
```
['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']
```

---

## **Conclusion**
This function effectively determines the minimum set of characters required to form all words
in the input list. It does so efficiently using dictionaries to track maximum frequencies and 
constructs the final list accordingly.

"""
