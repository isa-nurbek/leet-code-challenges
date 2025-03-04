# Description:

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
`O(w * n * log(n))` time | `O(wn)` space - where `w` is the number of words
and `n` is the length of the longest word.
```

"""

# =============================================================================================== #

# Solution


# O(w * n * log(n) + n * w * log(w)) time | O(w * n) space - where `w` is the number of words
# and `n` is the length of the longest word
def group_anagrams(words):
    # If the input list is empty, return an empty list immediately
    if len(words) == 0:
        return []

    # Create a list of sorted versions of each word.
    # For example, "tac" becomes "act", "cat" becomes "act", etc.
    sorted_words = ["".join(sorted(w)) for w in words]

    # Create a list of indices corresponding to the original words list
    indices = [i for i in range(len(words))]

    # Sort the indices based on the sorted versions of the words.
    # This groups anagrams together in the indices list.
    indices.sort(key=lambda x: sorted_words[x])

    # Initialize the result list to store groups of anagrams
    result = []

    # Initialize a temporary list to store the current group of anagrams
    current_anagram_group = []

    # Set the current anagram to the sorted version of the first word
    current_anagram = sorted_words[indices[0]]

    # Iterate through the sorted indices
    for index in indices:
        word = words[index]  # Get the original word
        sorted_word = sorted_words[index]  # Get the sorted version of the word

        # If the sorted word matches the current anagram, add it to the current group
        if sorted_word == current_anagram:
            current_anagram_group.append(word)
            continue

        # If the sorted word doesn't match, it means we've reached a new group of anagrams.
        # Add the current group to the result list and start a new group.
        result.append(current_anagram_group)
        current_anagram_group = [word]
        current_anagram = sorted_word

    # Don't forget to add the last group of anagrams to the result list
    result.append(current_anagram_group)

    # Return the final list of anagram groups
    return result


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

# =============================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity:

1. **Sorting each word**: For each word in the list, we sort its characters. Sorting a word
of length `k` takes `O(k log k)` time. If the average length of the words is `k` and there are `n` words,
this step takes `O(n * k log k)` time.

2. **Sorting indices**: We sort the indices based on the sorted versions of the words.
Sorting `n` indices takes `O(n log n)` time.

3. **Grouping anagrams**: We iterate through the sorted indices and group words with the same sorted version.
This step takes `O(n)` time.

The overall time complexity is dominated by the sorting of the words and the indices:
    `O(n * k log k + n log n)`

### Space Complexity:

1. **Storing sorted words**: We store the sorted version of each word, which takes `O(n * k)` space.
2. **Storing indices**: We store the indices, which takes `O(n)` space.
3. **Result list**: The result list stores the grouped anagrams, which also takes `O(n * k)` space in the worst case.

The overall space complexity is: `O(n * k)`

### Summary:

- **Time Complexity**: `O(n * k log k + n log n)`
- **Space Complexity**: `O(n * k)`

"""

# Code Explanation:

"""
This function, `group_anagrams`, groups words that are anagrams of each other into separate lists. Here's
a detailed breakdown of how it works:

## **Understanding Anagrams**
An anagram is a word or phrase formed by rearranging the letters of a different word. For example:
- **"cat"** and **"tac"** are anagrams because they contain the same letters.
- **"flop"** and **"olfp"** are anagrams for the same reason.

---

## **Step-by-Step Explanation**
Let's go through the function's logic.

### **Step 1: Handle Edge Case (Empty List)**
```
if len(words) == 0:
    return []
```
- If the input list `words` is empty, we return an empty list immediately.

---

### **Step 2: Sort Each Word to Identify Anagrams**
```
sorted_words = ["".join(sorted(w)) for w in words]
```
- We create a new list called `sorted_words`, where each word is sorted alphabetically.
- This helps identify anagrams because all anagrams will have the same sorted representation.

#### Example:
For `words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]`,  
the `sorted_words` list will be:
```
["oy", "act", "flop", "act", "foo", "act", "oy", "flop"]
```

---

### **Step 3: Create a List of Indices and Sort by Sorted Words**
```
indices = [i for i in range(len(words))]
indices.sort(key=lambda x: sorted_words[x])
```
- We create a list of indices `[0, 1, 2, 3, 4, 5, 6, 7]`, representing the positions of words in the original list.
- We sort these indices based on the corresponding `sorted_words` values.

#### After sorting `indices` based on `sorted_words`, we get:
```
[0, 6, 1, 3, 5, 2, 7, 4]
```
- This means the words in `words` should now be processed in the order:
  `["yo", "oy", "act", "tac", "cat", "flop", "olfp", "foo"]`.

---

### **Step 4: Group Anagrams Together**
```
result = []
current_anagram_group = []
current_anagram = sorted_words[indices[0]]
```
- `result` will store the final grouped anagrams.
- `current_anagram_group` is a temporary list that holds words belonging to the same anagram group.
- `current_anagram` keeps track of the sorted representation of the anagram group being processed.

---

### **Step 5: Iterate Over Sorted Indices**
```
for index in indices:
    word = words[index]
    sorted_word = sorted_words[index]

    if sorted_word == current_anagram:
        current_anagram_group.append(word)
        continue

    result.append(current_anagram_group)
    current_anagram_group = [word]
    current_anagram = sorted_word
```
- We loop through the sorted indices and retrieve both the original word and its sorted version.
- If the current `sorted_word` matches `current_anagram`, we add the word to the `current_anagram_group`.
- If it's different, it means we've moved to a new anagram group:
  - We store the old group in `result`.
  - We reset `current_anagram_group` to start a new group.

---

### **Step 6: Add the Last Group**
```
result.append(current_anagram_group)
```
- After the loop, we append the last formed `current_anagram_group` to `result`.

---

## **Final Output Example**
For:
```
words_1 = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(group_anagrams(words_1))
```
The output is:
```
[['yo', 'oy'], ['act', 'tac', 'cat'], ['flop', 'olfp'], ['foo']]
```
---

## **Alternative Approach: Using a HashMap**

A more efficient approach would be using a dictionary (`defaultdict` from `collections`), where sorted
words are keys, and values are lists of words. This avoids sorting the indices explicitly.

"""
