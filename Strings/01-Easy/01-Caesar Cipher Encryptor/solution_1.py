# Description:

"""
                                    Caesar Cipher Encryptor

Given a non-empty string of lowercase letters and a non-negative integer representing a key, write
a function that returns a new string obtained by shifting every letter in the input string by k positions
in the alphabet, where k is the key.

Note that letters should "wrap" around the alphabet; in other words, the letter `z` shifted by one returns the letter `a`.

## Sample Input:

```
string = "xyz"
key = 2
```

## Sample Output:

```
"zab"
```

## Optimal Space & Time Complexity:

```
`O(n)` time | `O(n)` space - where `n` is the length of the input string.
```

"""

# =============================================================================================== #

# Solution:


# O(n)time | O(n) space
def get_new_letter(letter, key):
    new_letter_code = ord(letter) + key
    return (
        chr(new_letter_code)
        if new_letter_code <= 122
        else chr(96 + new_letter_code % 122)
    )


def caesar_cipher_encryptor(str, key):
    new_letters = []
    new_key = key % 26

    for letter in str:
        new_letters.append(get_new_letter(letter, new_key))
    return "".join(new_letters)


# Test Cases
print(caesar_cipher_encryptor("abc", 2))  # Output: "cde"
print(caesar_cipher_encryptor("xyz", 3))  # Output: "abc"
print(caesar_cipher_encryptor("abc", 28))  # Output: "cde"
print(caesar_cipher_encryptor("abcdefghijklmnopqrstuvwxyz", 1))
# Output: "bcdefghijklmnopqrstuvwxyza"
print(caesar_cipher_encryptor("hello", 0))  # Output: "hello"

# =============================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

Let's analyze the time and space complexity of the `caesar_cipher_encryptor` function.

### Time Complexity:
1. **Loop through the input string**: The function iterates over each character in the input string `str`.
If the length of the string is `n`, this loop runs `n` times.
2. **`get_new_letter` function**: Inside the loop, the `get_new_letter` function is called for each character.
This function performs a constant amount of work:
   - It calculates the new character code using `ord(letter) + key`.
   - It checks if the new character code is within the range of lowercase letters (97 to 122) and adjusts it if necessary.
   - It converts the new character code back to a character using `chr()`.
   
   All these operations are constant time, so the time complexity of `get_new_letter` is `O(1)`.

3. **Appending to the list**: Appending each new character to the `new_letters` list is also a constant time operation, `O(1)`.

4. **Joining the list into a string**: After the loop, the list `new_letters` is joined into a single string using `"".join
(new_letters)`. This operation takes `O(n)` time, where `n` is the length of the string.

**Overall Time Complexity**: 
- The loop runs `n` times, and each iteration takes `O(1)` time.
- The final join operation takes `O(n)` time.
- Therefore, the total time complexity is `O(n)`.

### Space Complexity:
1. **List `new_letters`**: The function creates a list `new_letters` to store the new characters. This list will have
the same length as the input string, so it requires `O(n)` space.
2. **Other variables**: The variables `new_key`, `letter`, and the return value of `get_new_letter` all use constant space, `O(1)`.

**Overall Space Complexity**: 
- The dominant space usage is the `new_letters` list, which requires `O(n)` space.
- Therefore, the total space complexity is `O(n)`.

### Summary:
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

Where `n` is the length of the input string `str`.

"""

# Code Explanation:

"""
The given code implements a **Caesar cipher encryptor**, a basic encryption technique where each letter
in a string is shifted by a fixed number of positions in the alphabet.
Here's a detailed breakdown of the code and how it works:

---

### **Function 1: `get_new_letter`**

```
def get_new_letter(letter, key):
    new_letter_code = ord(letter) + key
    return (
        chr(new_letter_code)
        if new_letter_code <= 122
        else chr(96 + new_letter_code % 122)
    )
```

**Purpose:**  
This function shifts a single letter forward by a given `key` in the alphabet, ensuring the result 
wraps around to the start of the alphabet if it exceeds `'z'`.

- **Input Parameters:**
  - `letter`: A single lowercase character (`'a'` to `'z'`).
  - `key`: An integer representing how many positions to shift the letter.

- **Explanation of Logic:**
  1. `ord(letter)` converts the letter into its ASCII value (e.g., `'a'` → 97, `'z'` → 122).
  2. `new_letter_code = ord(letter) + key` adds the shift (`key`) to the ASCII value.
  3. If `new_letter_code <= 122` (within `'a'` to `'z'` range), convert it back to a character using `chr(new_letter_code)`.
  4. If `new_letter_code > 122`, the letter has passed `'z'`. To wrap around:
     - Calculate the offset beyond `'z'` using `new_letter_code % 122`.
     - Add this offset to `96` (ASCII value before `'a'`) to get the wrapped-around character.

---

### **Function 2: `caesar_cipher_encryptor`**

```
def caesar_cipher_encryptor(str, key):
    new_letters = []
    new_key = key % 26

    for letter in str:
        new_letters.append(get_new_letter(letter, new_key))
    return "".join(new_letters)
```

**Purpose:**  
This function applies the Caesar cipher to an entire string, shifting all characters by a specified key.

- **Input Parameters:**
  - `str`: A string of lowercase letters to be encrypted.
  - `key`: An integer representing how many positions to shift the letters.

- **Explanation of Logic:**
  1. `new_key = key % 26`: The alphabet has 26 letters, so taking the modulus ensures the key is within
  the range `[0, 25]`. This avoids unnecessary large shifts (e.g., shifting by 52 is equivalent to shifting by 0).
  2. Create an empty list `new_letters` to store the shifted characters.
  3. Iterate through each `letter` in the input `string`:
     - Use `get_new_letter(letter, new_key)` to calculate the shifted letter.
     - Append the shifted letter to `new_letters`.
  4. Combine the shifted letters into a single string using `"".join(new_letters)` and return it.

---

### **Test Cases**

#### **Test Case 1: Basic Shift**
```
print(caesar_cipher_encryptor("abc", 2))  # Output: "cde"
```
- `'a'` → `'c'` (shift by 2)
- `'b'` → `'d'`
- `'c'` → `'e'`

---

#### **Test Case 2: Wrapping Around**
```
print(caesar_cipher_encryptor("xyz", 3))  # Output: "abc"
```
- `'x'` → `'a'` (wraps around after `'z'`)
- `'y'` → `'b'`
- `'z'` → `'c'`

---

#### **Test Case 3: Large Key**
```
print(caesar_cipher_encryptor("abc", 28))  # Output: "cde"
```
- `key = 28 % 26 = 2` (equivalent shift is 2)
- `'a'` → `'c'`
- `'b'` → `'d'`
- `'c'` → `'e'`

---

#### **Test Case 4: Entire Alphabet**
```
print(caesar_cipher_encryptor("abcdefghijklmnopqrstuvwxyz", 1))  
# Output: "bcdefghijklmnopqrstuvwxyza"
```
- All letters shift by 1, with `'z'` wrapping to `'a'`.

---

#### **Test Case 5: No Shift**
```
print(caesar_cipher_encryptor("hello", 0))  # Output: "hello"
```
- No shift occurs when the key is `0`.

---

### **Key Points**
1. The Caesar cipher is case-sensitive in this implementation (works only for lowercase letters).
2. Non-alphabetic characters are not handled and would need extra logic for validation if required.
3. The modulo operation ensures efficiency for large keys.

This implementation demonstrates a simple yet effective approach to encryption using basic
string manipulation and ASCII value calculations.

"""
