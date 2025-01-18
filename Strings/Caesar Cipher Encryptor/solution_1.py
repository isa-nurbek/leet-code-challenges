# Description:
"""
                                    # Caesar Cipher Encryptor

Given a non-empty string of lowercase letters and a non-negative integer representing a key, write
a function that returns a new string obtained by shifting every letter in the input string by k positions
in the alphabet, where k is the key.

Note that letters should "wrap" around the alphabet; in other words, the letter `z` shifted by one returns the letter `a`.

## Sample Input

```plaintext
string = "xyz"
key = 2
```

## Sample Output

```plaintext
"zab"
```

## Optimal Space & Time Complexity

`O(n)` time | `O(n)` space - where `n` is the length of the input string.

"""


# O(n)time | O(n) space
def get_new_letter(letter, key):
    new_letter_code = ord(letter) + key
    return (
        chr(new_letter_code)
        if new_letter_code <= 122
        else chr(96 + new_letter_code % 122)
    )


def caesar_cipher_encryptor(string, key):
    new_letters = []
    new_key = key % 26

    for letter in string:
        new_letters.append(get_new_letter(letter, new_key))
    return "".join(new_letters)


print(caesar_cipher_encryptor("abc", 2))  # Output: "cde"
print(caesar_cipher_encryptor("xyz", 3))  # Output: "abc"
print(caesar_cipher_encryptor("abc", 28))  # Output: "cde"
print(caesar_cipher_encryptor("abcdefghijklmnopqrstuvwxyz", 1))
# Output: "bcdefghijklmnopqrstuvwxyza"
print(caesar_cipher_encryptor("hello", 0))  # Output: "hello"

# Big O:
"""
To determine the Big O complexity of the provided code, we analyze both the `get_new_letter` function
and the `caesar_cipher_encryptor` function.

### **`get_new_letter` function:**
- The function takes constant time to:
  - Convert a letter to its ASCII code using `ord`.
  - Perform arithmetic operations.
  - Convert the result back to a character using `chr`.
- The overall time complexity of `get_new_letter` is **O(1)**.

### **`caesar_cipher_encryptor` function:**
1. **Key calculation (`key % 26`)**:
   - Modulo operation takes **O(1)** time.

2. **Iterating through the string**:
   - The function iterates through each character in the input `string`. If the string has `n` characters,
   this loop runs `n` times.
   - For each character, it calls `get_new_letter`, which takes **O(1)** time.

3. **String concatenation (`"".join(new_letters)`)**:
   - Joining a list of `n` characters into a string takes **O(n)** time.

### **Total Time Complexity**:
- The loop iterates `n` times, and each iteration involves an **O(1)** operation from `get_new_letter`.
- The final string join also takes **O(n)** time.
- Therefore, the overall time complexity is:

  O(n) + O(n) = O(n)

### **Big O Complexity**:
The time complexity of the `caesar_cipher_encryptor` function is **O(n)**, where `n` is the length of the input string.

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
def caesar_cipher_encryptor(string, key):
    new_letters = []
    new_key = key % 26

    for letter in string:
        new_letters.append(get_new_letter(letter, new_key))
    return "".join(new_letters)
```

**Purpose:**  
This function applies the Caesar cipher to an entire string, shifting all characters by a specified key.

- **Input Parameters:**
  - `string`: A string of lowercase letters to be encrypted.
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
