# Problem Description:

"""
                                        Semordnilap

Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.

A semordnilap pair is defined as a set of different strings where the reverse of one word is the same as
the forward version of the other. For example the words "diaper" and "repaid" are a semordnilap pair, as
are the words "palindromes" and "semordnilap".

The order of the returned pairs and the order of the strings within each pair does not matter.


## Sample Input:
```
words = ["diaper", "abc", "test", "cba", "repaid"]
```

## Sample Output:
```
[["diaper", "repaid"], ["abc", "cba"]]
```

## Optimal Time & Space Complexity:
```
O(n * m) time | O(n) space - where `n` is the number of words and `m` is the length of the longest word.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * m) time | O(n) space
def semordnilap(words):
    # Convert the list of words to a set for O(1) look-up times
    words_set = set(words)

    # Initialize an empty list to store the semordnilap pairs
    semordnilap_pairs = []

    # Iterate through each word in the original list
    for word in words:
        # Reverse the current word
        reverse = word[::-1]

        # Check if the reversed word exists in the set and is not the same as the original word
        if reverse in words_set and reverse != word:
            # If it is a valid semordnilap pair, add it to the list
            semordnilap_pairs.append([word, reverse])

            # Remove both the original word and its reverse from the set to avoid duplicate pairs
            words_set.remove(word)
            words_set.remove(reverse)

    # Return the list of semordnilap pairs
    return semordnilap_pairs


words_1 = ["diaper", "abc", "test", "cba", "repaid"]
words_2 = ["aaa", "bbbb"]
words_3 = ["dog", "desserts", "god", "stressed"]

# Test Cases
print(semordnilap(words_1))  # [['diaper', 'repaid'], ['abc', 'cba']]
print(semordnilap(words_2))  # []
print(semordnilap(words_3))  # [['dog', 'god'], ['desserts', 'stressed']]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity Analysis

1. **Creating the Set**: 
   - Converting the list of words into a set (`words_set = set(words)`) takes `O(n)` time,
   where `n` is the number of words in the list.

2. **Iterating Through Words**:
   - The loop iterates through each word in the list, which is `O(n)` time.

3. **Reversing Each Word**:
   - Reversing a word (`word[::-1]`) takes `O(m)` time, where `m` is the length of the word. In the worst case,
   if the longest word has length `m`, this operation is `O(m)`.

4. **Checking if the Reversed Word Exists in the Set**:
   - Checking if the reversed word exists in the set (`reverse in words_set`) is an average-case `O(1)` operation for a set.

5. **Appending to the Result List**:
   - Appending a pair to the `semordnilap_pairs` list is `O(1)`.

6. **Removing Words from the Set**:
   - Removing a word from the set (`words_set.remove(word)` and `words_set.remove(reverse)`) is an average-case `O(1)` operation.

### Overall Time Complexity
- The dominant operation is the loop that iterates through each word and performs operations that are `O(m)`
(reversing the word) and `O(1)` (set operations). Therefore, the overall time complexity is:
 
    `O(n * m)`

where `n` is the number of words and `m` is the length of the longest word.

### Space Complexity Analysis

1. **Set Storage**:
   - The set `words_set` stores all the words, which takes `O(n)` space.

2. **Result List**:
   - The `semordnilap_pairs` list stores pairs of words. In the worst case, if all words form semordnilap pairs,
   the space required is `O(n)`.

3. **Auxiliary Space**:
   - The space used for the reversed word (`reverse`) is `O(m)`, where `m` is the length of the longest word.

### Overall Space Complexity
- The dominant space usage is from the set and the result list, both of which are `O(n)`. Therefore,
the overall space complexity is: `O(n)`
  

### Summary
- **Time Complexity**: O(n * m)
- **Space Complexity**: O(n)

Where:
- `n` is the number of words in the input list.
- `m` is the length of the longest word in the input list.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The function `semordnilap(words)` finds all **semordnilap** word pairs in a given list of words. A **semordnilap**
is a word that forms a different valid word when reversed (unlike a palindrome, which remains the same when reversed).
Let's go through the function step by step.

---

### **Step-by-Step Explanation**

#### **1. Convert the List into a Set**
```
words_set = set(words)
```
- The given list `words` is converted into a **set** (`words_set`). 
- This helps in **O(1) average-time complexity** lookups instead of O(n) when checking for reversed words.
- This also ensures that duplicate words are handled correctly.

---

#### **2. Initialize an Empty List for Storing Pairs**
```
semordnilap_pairs = []
```
- This list will store the **valid semordnilap pairs**.

---

#### **3. Iterate Over Each Word in the List**
```
for word in words:
```
- We iterate through each word in the original list `words`.

---

#### **4. Compute the Reversed Word**
```
reverse = word[::-1]
```
- The word is reversed using Python slicing `[::-1]`.
- Example: `"diaper"` → `"repaid"`

---

#### **5. Check If the Reverse Exists in the Set**
```
if reverse in words_set and reverse != word:
```
- `reverse in words_set`: This ensures that the reversed word exists in the original list.
- `reverse != word`: This ensures that we do not mistakenly count palindromes (e.g., `"racecar"` should not be a semordnilap).

---

#### **6. Add the Pair and Remove Processed Words**
```
semordnilap_pairs.append([word, reverse])
words_set.remove(word)
words_set.remove(reverse)
```
- The found pair `[word, reverse]` is added to the result list.
- We **remove both words** from `words_set` to prevent counting the same pair twice.

---

#### **7. Return the List of Pairs**
```
return semordnilap_pairs
```
- Finally, the function returns the list of valid semordnilap pairs.

---

## **Example Walkthrough**
Let's analyze how the function works for different inputs.

### **Test Case 1**
```
words_1 = ["diaper", "abc", "test", "cba", "repaid"]
print(semordnilap(words_1))  
# Output: [['diaper', 'repaid'], ['abc', 'cba']]
```
**Step-by-step execution:**
1. Convert to set: `{"diaper", "abc", "test", "cba", "repaid"}`
2. `"diaper"` → `"repaid"` found in set → Add `["diaper", "repaid"]`
   - Remove `"diaper"` and `"repaid"` from the set.
3. `"abc"` → `"cba"` found in set → Add `["abc", "cba"]`
   - Remove `"abc"` and `"cba"` from the set.
4. `"test"` → `"tset"` (not in set) → Ignore.

Final Output: `[['diaper', 'repaid'], ['abc', 'cba']]`

---

### **Test Case 2**
```
words_2 = ["aaa", "bbbb"]
print(semordnilap(words_2))  
# Output: []
```
- `"aaa"` reversed is `"aaa"` (a palindrome, not a semordnilap).
- `"bbbb"` reversed is `"bbbb"` (same reason).
- **No valid semordnilap pairs** → Return `[]`.

---

### **Test Case 3**
```
words_3 = ["dog", "desserts", "god", "stressed"]
print(semordnilap(words_3))  
# Output: [['dog', 'god'], ['desserts', 'stressed']]
```
1. Convert to set: `{"dog", "desserts", "god", "stressed"}`
2. `"dog"` → `"god"` found in set → Add `["dog", "god"]`
   - Remove `"dog"` and `"god"` from the set.
3. `"desserts"` → `"stressed"` found in set → Add `["desserts", "stressed"]`
   - Remove `"desserts"` and `"stressed"` from the set.

Final Output: `[['dog', 'god'], ['desserts', 'stressed']]`

---

## **Summary**
- Uses a **set** for **fast lookups**.
- Ensures **words are only counted once**.
- Handles **palindromes correctly**.
- **Efficient (O(n) time complexity)**.

"""
