# Problem Description:

"""
                            Group Anagrams

Write a function that takes in an array of strings and groups anagrams together.

Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example,
"cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your function should return a list of anagram groups in no particular order.


## Sample Input:
```
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
```

## Sample Output:
```
[["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
```

## Optimal Time & Space Complexity:
```
O(w * n * log(n)) time | O(wn) space - where `w` is the number of words
and `n` is the length of the longest word.
```

"""

# =========================================================================================================================== #

# Solution:


# O(w * n * log(n)) time | O(w * n) space - where `w` is the number of words
# and `n` is the length of the longest word
def group_anagrams(words):
    # Create a dictionary to store groups of anagrams.
    # The key will be the sorted version of the word, and the value will be a list of anagrams.
    anagrams = {}

    # Iterate through each word in the input list.
    for word in words:
        # Sort the characters of the word and join them back into a string.
        # This sorted version will be the same for all anagrams.
        sorted_word = "".join(sorted(word))

        # Check if the sorted word is already a key in the dictionary.
        if sorted_word in anagrams:
            # If it is, append the current word to the list of anagrams.
            anagrams[sorted_word].append(word)
        else:
            # If it is not, create a new entry in the dictionary with the sorted word as the key
            # and a list containing the current word as the value.
            anagrams[sorted_word] = [word]

    # Return the values of the dictionary, which are lists of grouped anagrams.
    return list(anagrams.values())


# Test Cases
words_1 = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
words_2 = ["abc", "dabd", "bca", "cab", "ddba"]
words_3 = []

# Test Case 1
print(group_anagrams(words_1))
# Expected Output: [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

# Test Case 2
print(group_anagrams(words_2))
# Expected Output: [['abc', 'bca', 'cab'], ['dabd', 'ddba']]

# Test Case 3 (Empty Input)
print(group_anagrams(words_3))
# Expected Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity**

1. **Sorting each word**: 
   - Sorting a word of length `k` takes `O(k log k)` time.
   - If there are `n` words, and the average length of a word is `k`, the total time for sorting
   all words is `O(n * k log k)`.

2. **Inserting into the dictionary**:
   - Inserting a word into the dictionary (hash map) takes `O(1)` on average.
   - Since there are `n` words, this step takes `O(n)` time.

3. **Overall Time Complexity**:
   - The dominant factor is the sorting step, so the total time complexity is `O(n * k log k)`.

---

### **Space Complexity**

1. **Dictionary storage**:
   - The dictionary stores all the words. If there are `n` words, and the average length of a word is `k`,
   the space required is `O(n * k)`.

2. **Output list**:
   - The output list also stores all the words, so it requires `O(n * k)` space.

3. **Overall Space Complexity**:
   - The total space complexity is `O(n * k)`.

---

### **Summary**
- **Time Complexity**: `O(n * k log k)`
- **Space Complexity**: `O(n * k)`

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### Explanation of the `group_anagrams` Function

The `group_anagrams` function takes a list of words and groups together words that are anagrams of each other.

#### **Step-by-Step Breakdown**
1. **Initialize a Dictionary (`anagrams`)**  
   ```
   anagrams = {}
   ```
   This dictionary will store sorted versions of words as keys and a list of anagrams as values.

2. **Iterate Through Each Word in the Input List (`words`)**  
   ```
   for word in words:
   ```
   This loop goes through each word in the list.

3. **Sort the Characters of Each Word**  
   ```
   sorted_word = "".join(sorted(word))
   ```
   - The `sorted(word)` function sorts the letters of `word` in alphabetical order.
   - `"".join(sorted(word))` joins the sorted characters back into a string.
   - This ensures that all anagrams (which have the same characters in different orders)
   will have the same sorted representation.

4. **Group Anagrams in the Dictionary**  
   ```
   if sorted_word in anagrams:
       anagrams[sorted_word].append(word)
   else:
       anagrams[sorted_word] = [word]
   ```
   - If the sorted word already exists in the dictionary, we append the original word to the corresponding list.
   - If it doesn't exist, we create a new list with the word.

5. **Return the Values (Lists of Anagram Groups)**
   ```
   return list(anagrams.values())
   ```
   - The dictionary values (which are lists of grouped anagrams) are returned as a list.

---

### **Example Walkthrough**
#### **Example 1**
```
words_1 = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
```
| Word   | Sorted Word | Dictionary After Processing                                                                    |
|--------|-------------|------------------------------------------------------------------------------------------------|
| "yo"   | "oy"        | `{"oy": ["yo"]}`                                                                               |
| "act"  | "act"       | `{"oy": ["yo"], "act": ["act"]}`                                                               |
| "flop" | "flop"      | `{"oy": ["yo"], "act": ["act"], "flop": ["flop"]}`                                             |
| "tac"  | "act"       | `{"oy": ["yo"], "act": ["act", "tac"], "flop": ["flop"]}`                                      |
| "foo"  | "foo"       | `{"oy": ["yo"], "act": ["act", "tac"], "flop": ["flop"], "foo": ["foo"]}`                      |
| "cat"  | "act"       | `{"oy": ["yo"], "act": ["act", "tac", "cat"], "flop": ["flop"], "foo": ["foo"]}`               |
| "oy"   | "oy"        | `{"oy": ["yo", "oy"], "act": ["act", "tac", "cat"], "flop": ["flop"], "foo": ["foo"]}`         |
| "olfp" | "flop"      | `{"oy": ["yo", "oy"], "act": ["act", "tac", "cat"], "flop": ["flop", "olfp"], "foo": ["foo"]}` |

**Final Output:**
```
[['yo', 'oy'], ['act', 'tac', 'cat'], ['flop', 'olfp'], ['foo']]
```

---

#### **Example 2**
```
words_2 = ["abc", "dabd", "bca", "cab", "ddba"]
```
| Word   | Sorted Word | Dictionary After Processing                                |
|--------|-------------|------------------------------------------------------------|
| "abc"  | "abc"       | `{"abc": ["abc"]}`                                         |
| "dabd" | "abdd"      | `{"abc": ["abc"], "abdd": ["dabd"]}`                       |
| "bca"  | "abc"       | `{"abc": ["abc", "bca"], "abdd": ["dabd"]}`                |
| "cab"  | "abc"       | `{"abc": ["abc", "bca", "cab"], "abdd": ["dabd"]}`         |
| "ddba" | "abdd"      | `{"abc": ["abc", "bca", "cab"], "abdd": ["dabd", "ddba"]}` |

**Final Output:**
```
[['abc', 'bca', 'cab'], ['dabd', 'ddba']]
```

---

#### **Example 3 (Empty Input)**
```
words_3 = []
```
- Since the input list is empty, there are no words to process.
- The dictionary remains empty.
- The function returns an empty list.

**Final Output:**
```
[]
```
"""
