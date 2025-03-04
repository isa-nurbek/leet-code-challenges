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

# Solution


# O(n)time | O(n) space
def get_new_letter(letter, key, alphabet):
    new_letter_code = alphabet.index(letter) + key
    return alphabet[new_letter_code % 26]


def caesar_cipher_encryptor(str, key):
    new_letters = []
    new_key = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for letter in str:
        new_letters.append(get_new_letter(letter, new_key, alphabet))
    return "".join(new_letters)


# Test Cases
print(caesar_cipher_encryptor("abc", 2))  # Outputs: "cde"
print(caesar_cipher_encryptor("xyz", 28))  # Outputs: "zab"
print(caesar_cipher_encryptor("hello", 52))  # Outputs: "hello"
print(caesar_cipher_encryptor("abc", 0))  # Outputs: "abc"
print(caesar_cipher_encryptor("a", 1))  # Outputs: "b"
print(caesar_cipher_encryptor("z", 1))  # Outputs: "a"

# =============================================================================================== #

# Big O:

"""

### **Time and Space Complexity**

- **Time Complexity:**
  - Processing each letter in the string takes O(1) for indexing and shifting.
  - Total time is O(n), where `n` is the length of the string.

- **Space Complexity:**
  - The `alphabet` list takes O(26), which is constant.
  - The `new_letters` list takes O(n) to store the result.
  - Total space complexity is O(n).

This implementation is both time and space efficient for the Caesar cipher.

"""

# Code Explanation:

"""

This code implements a **Caesar cipher encryptor**, which is a simple substitution cipher that shifts letters
in the alphabet by a fixed number of places. Here's an in-depth explanation of how it works:

---

### **Functions and Main Logic**

#### 1. **`get_new_letter(letter, key, alphabet)`**
   - **Purpose:** Computes the new letter after shifting the given letter by `key` positions in the alphabet.
   - **Parameters:**
     - `letter`: A single character to be shifted.
     - `key`: The number of positions to shift.
     - `alphabet`: A list of lowercase English letters (`a-z`).

   - **Process:**
     1. `alphabet.index(letter)` finds the index of `letter` in the alphabet list.
     2. `new_letter_code = alphabet.index(letter) + key` computes the new index after adding the key.
     3. `alphabet[new_letter_code % 26]` ensures that if the index exceeds 25 (end of the alphabet), it
     wraps around using the modulo operation `% 26`.

---

#### 2. **`caesar_cipher_encryptor(str, key)`**
   - **Purpose:** Encrypts a string using the Caesar cipher with the given key.
   - **Parameters:**
     - `str`: The input string to be encrypted.
     - `key`: The shift value for the cipher.

   - **Process:**
     1. `new_key = key % 26` ensures that the key is reduced to a value within the bounds of the alphabet (0-25),
     optimizing performance.
     2. `alphabet = list("abcdefghijklmnopqrstuvwxyz")` creates the reference list of lowercase letters.
     3. A loop processes each `letter` in the `string`:
        - Calls `get_new_letter()` to compute the encrypted version of `letter`.
        - Appends the new letter to the `new_letters` list.
     4. `''.join(new_letters)` combines the encrypted letters into a single string and returns it.

---

### **Example Outputs**

1. **`caesar_cipher_encryptor("abc", 2)`**
   - Explanation:
     - Key: 2, so each letter is shifted by 2 positions.
     - `"a"` becomes `"c"`, `"b"` becomes `"d"`, `"c"` becomes `"e"`.
   - Output: `"cde"`

2. **`caesar_cipher_encryptor("xyz", 28)`**
   - Explanation:
     - Key: 28. Since `28 % 26 = 2`, the effective key is 2.
     - `"x"` becomes `"z"`, `"y"` becomes `"a"`, `"z"` becomes `"b"`.
   - Output: `"zab"`

3. **`caesar_cipher_encryptor("hello", 52)`**
   - Explanation:
     - Key: 52. Since `52 % 26 = 0`, the effective key is 0.
     - All letters remain the same (`"hello"`).
   - Output: `"hello"`

4. **`caesar_cipher_encryptor("abc", 0)`**
   - Explanation:
     - Key: 0. No shift occurs.
     - Output: `"abc"`

5. **`caesar_cipher_encryptor("a", 1)`**
   - Explanation:
     - Key: 1. `"a"` shifts to `"b"`.
   - Output: `"b"`

6. **`caesar_cipher_encryptor("z", 1)`**
   - Explanation:
     - Key: 1. `"z"` shifts to `"a"` because of the modulo wrap-around.
   - Output: `"a"`

---

### **Key Concepts in the Code**

1. **Modulo Operation:** Ensures that indices wrap around when they exceed the alphabet bounds (e.g., `"z"` to `"a"`).
2. **Efficiency:** By reducing the key modulo 26 (`key % 26`), the function avoids unnecessary calculations for very large keys.
3. **Separation of Concerns:** The function `get_new_letter` handles letter-specific logic, making the main function (`caesar_cipher_encryptor`) cleaner and more focused on processing the entire string.

"""
