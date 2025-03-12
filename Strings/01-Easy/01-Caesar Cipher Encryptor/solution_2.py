# Problem Description:

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

## Optimal Time & Space Complexity:
```
O(n) time | O(n) space - where `n` is the length of the input string.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n)time | O(n) space
# Function to calculate the new letter after shifting by the key
def get_new_letter(letter, key, alphabet):
    # Find the index of the current letter in the alphabet
    current_index = alphabet.index(letter)

    # Calculate the new index by adding the key (shift) to the current index
    new_letter_code = current_index + key

    # Use modulo 26 to wrap around the alphabet if the new index exceeds 25
    return alphabet[new_letter_code % 26]


# Function to encrypt a string using the Caesar Cipher
def caesar_cipher_encryptor(str, key):
    # List to store the new encrypted letters
    new_letters = []

    # Normalize the key to ensure it's within the range of 0-25
    new_key = key % 26

    # Define the alphabet as a list of lowercase letters
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    # Iterate over each letter in the input string
    for letter in str:
        # Get the new letter after shifting by the key and add it to the list
        new_letters.append(get_new_letter(letter, new_key, alphabet))

    # Join the list of new letters into a single string and return it
    return "".join(new_letters)


# Test Cases
print(caesar_cipher_encryptor("abc", 2))  # Outputs: "cde"
print(caesar_cipher_encryptor("xyz", 28))  # Outputs: "zab"
print(caesar_cipher_encryptor("hello", 52))  # Outputs: "hello"
print(caesar_cipher_encryptor("abc", 0))  # Outputs: "abc"
print(caesar_cipher_encryptor("a", 1))  # Outputs: "b"
print(caesar_cipher_encryptor("z", 1))  # Outputs: "a"

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

Let's analyze the time and space complexity of the provided `caesar_cipher_encryptor` function.

---

### **Time Complexity**
1. **`alphabet.index(letter)`**:
   - This operation searches for the index of `letter` in the `alphabet` list. Since `alphabet` is a list of 26 characters,
   this operation takes **O(1)** time because the size of the alphabet is fixed and small.

2. **`new_letter_code % 26`**:
   - The modulo operation is a constant-time operation, so this also takes **O(1)** time.

3. **Loop over `str`**:
   - The loop iterates over each character in the input string `str`. If the length of `str` is `n`, this loop runs **n times**.

4. **`alphabet[new_letter_code % 26]`**:
   - Accessing an element in a list by index is a constant-time operation, so this takes **O(1)** time.

5. **`"".join(new_letters)`**:
   - Joining a list of `n` characters into a string takes **O(n)** time.

---

#### **Overall Time Complexity**:
- The loop runs `n` times, and each iteration performs **O(1)** operations.
- The final `join` operation takes **O(n)** time.

- Therefore, the total time complexity is **O(n)**.

---

### **Space Complexity**
1. **`alphabet` list**:
   - The `alphabet` list has a fixed size of 26 characters, so it takes **O(1)** space.

2. **`new_letters` list**:
   - The `new_letters` list stores `n` characters, where `n` is the length of the input string `str`.
   This takes **O(n)** space.

3. **Other variables**:
   - Variables like `new_key`, `letter`, and `new_letter_code` use **O(1)** space.

---

#### **Overall Space Complexity**:
- The dominant space usage comes from the `new_letters` list, which takes **O(n)** space.

- Therefore, the total space complexity is **O(n)**.

---

### **Summary**
- **Time Complexity**: **O(n)**
- **Space Complexity**: **O(n)**

Where `n` is the length of the input string `str`.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

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
