# Description:

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
`O(n + m)` time | `O(c)` space - where `n` is the number of characters, `m` is the length of the document,
and `c` is the number of unique characters in the characters string
```

"""

# =============================================================================================== #

# Solution:


# O(n + m) time | O(c) space - where `n` is the number of characters, `m` is
# the length of the document, and `c` is the number of unique characters in the characters string
def generate_document(characters, document):
    character_counts = {}

    for character in characters:
        if character not in character_counts:
            character_counts[character] = 0

        character_counts[character] += 1

    for character in document:
        if character not in character_counts or character_counts[character] == 0:
            return False

        character_counts[character] -= 1

    return True


# Test Cases
print(generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))  # True
print(generate_document("A", "a"))  # False
print(generate_document("a hsgalhsa sanbjksbdkjba kjx", ""))  # True
print(generate_document("", "hello"))  # False

# =============================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### **Time Complexity Analysis:**
1. **First Loop (Building `character_counts`)**  
   - Iterates over all characters in `characters`.  
   - If `characters` has length `m`, this loop runs in **O(m)** time.

2. **Second Loop (Verifying `document` Against `character_counts`)**  
   - Iterates over all characters in `document`.  
   - If `document` has length `n`, this loop runs in **O(n)** time.

3. **Overall Complexity:**  
   - The total runtime is `O(m + n)`, since the two loops are independent.

---

### **Space Complexity Analysis:**
1. **Dictionary `character_counts` Storage**  
   - Stores counts for unique characters in `characters`.  
   - In the worst case (all unique characters), this takes **O(k)** space, where `k` is the number of unique characters.  
   - Since `k ≤ m` (bounded by the length of `characters`), the space complexity is **O(m)**.

2. **Other Variables**  
   - A few integer variables are used (constant space **O(1)**).

3. **Overall Complexity:**  
   - The space complexity is **O(m)**.

---

### **Final Complexity:**
- **Time Complexity:** `O(m + n)`
- **Space Complexity:** `O(m)`

"""

# Code Explanation:

"""
### **Detailed Explanation of the Code**

The function `generate_document(characters, document)` checks whether it is possible to generate the `document`
string using the available characters from the `characters` string. It ensures that the frequency of each
character in `characters` is sufficient to match the frequency of the same character in `document`.

---

### **Step-by-Step Breakdown**

#### **1. Understanding Inputs and Outputs**
- **Input:**  
  - `characters`: A string containing the available characters.
  - `document`: A string that we need to construct using `characters`.

- **Output:**  
  - `True` if the `document` can be formed using the characters (while considering the frequency of each character).
  - `False` otherwise.

---

### **2. Code Execution Steps**

#### **Step 1: Initialize a Dictionary to Count Characters**
```
character_counts = {}
```
- This dictionary (`character_counts`) will store the frequency of each character in the `characters` string.

#### **Step 2: Count the Frequency of Characters in `characters`**
```
for character in characters:
    if character not in character_counts:
        character_counts[character] = 0
    character_counts[character] += 1
```
- We iterate through each `character` in the `characters` string.
- If the character is not already in the dictionary, we initialize its count to 0.
- Then, we increment its count.

👉 **Example**  
If `characters = "Bste!hetsi ogEAxpelrt x "`, then after this step, `character_counts` will be:

```python
{
    'B': 1, 's': 2, 't': 3, 'e': 3, '!': 1, 'h': 1, 
    'i': 1, 'o': 1, 'g': 1, 'E': 1, 'A': 1, 'x': 2, 
    'p': 1, 'l': 1, 'r': 1, ' ': 4
}
```

---

#### **Step 3: Check if `document` Can Be Constructed**
```
for character in document:
    if character not in character_counts or character_counts[character] == 0:
        return False
    character_counts[character] -= 1
```
- We iterate through each `character` in `document`.
- If the character is either:
  - **Not in `character_counts`** → Return `False` (since the character is missing).
  - **Has a count of `0`** → Return `False` (since we have exhausted its occurrences).
- Otherwise, **decrement** the count of the character.

👉 **Example Execution for `document = "AlgoExpert is the Best!"`**  
- `'A'` is present in `character_counts`, so decrement its count.
- `'l'` is present, so decrement its count.
- `'g'` is present, so decrement its count.
- `'o'` is present, so decrement its count.
- `'E'` is present, so decrement its count.
- ... (continue for all characters)
- All characters are found with enough occurrences, so the function **returns `True`**.

---

#### **Step 4: If We Successfully Check All Characters, Return `True`**
```
return True
```
- If the loop completes without returning `False`, it means all characters in `document` were found with sufficient frequency.
- Hence, we return `True`.

---

### **Test Cases Walkthrough**
#### ✅ **Test Case 1**
```
print(generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))  # True
```
- Every character in `"AlgoExpert is the Best!"` is available in `"Bste!hetsi ogEAxpelrt x "` with enough frequency.
- **Output:** `True`

---

#### ❌ **Test Case 2**
```
print(generate_document("A", "a"))  # False
```
- `'A'` and `'a'` are different characters (case-sensitive).
- `'a'` is not in `characters`, so we return `False`.

---

#### ✅ **Test Case 3**
```
print(generate_document("a hsgalhsa sanbjksbdkjba kjx", ""))  # True
```
- The `document` is an empty string (`""`), which means we don't need any characters.
- An empty document can always be generated.
- **Output:** `True`

---

#### ❌ **Test Case 4**
```
print(generate_document("", "hello"))  # False
```
- The `characters` string is empty.
- We cannot form `"hello"` without any characters.
- **Output:** `False`

### **Final Thoughts**
- The approach efficiently determines whether a document can be created from a given set of characters.
- It properly considers **character frequency** and **case sensitivity**.
- Edge cases like **empty strings** and **different character cases** are handled correctly.

"""
