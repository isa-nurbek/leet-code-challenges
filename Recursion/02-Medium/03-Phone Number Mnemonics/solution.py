# Problem Description:

"""

                                        Phone Number Mnemonics

If you open the keypad of your mobile phone, it'll likely look like this:

```
   ----- ----- -----
  |     |     |     |
  |  1  |  2  |  3  |
  |     | abc | def |
   ----- ----- -----
  |     |     |     |
  |  4  |  5  |  6  |
  | ghi | jkl | mno |
   ----- ----- -----
  |     |     |     |
  |  7  |  8  |  9  |
  | pqrs| tuv | wxyz|
   ----- ----- -----
        |     |
        |  0  |
        |     |
         -----

Here's the mapping for clarity:

0: ["0"]

1: ["1"]

2: ["a", "b", "c"]

3: ["d", "e", "f"]

4: ["g", "h", "i"]

5: ["j", "k", "l"]

6: ["m", "n", "o"]

7: ["p", "q", "r", "s"]

8: ["t", "u", "v"]

9: ["w", "x", "y", "z"]
```

Almost every digit is associated with some letters in the alphabet; this allows certain phone numbers to spell out actual
words. For example, the phone number `8464747328` can be written as `timisgreat`; similarly, the phone number `2686463` can
be written as antoine or as `ant6463`.

It's important to note that a phone number doesn't represent a single sequence of letters, but rather multiple combinations
of letters. For instance, the digit `2` can represent three different letters (a, b, and c).

A mnemonic is defined as a pattern of letters, ideas, or associations that assist in remembering something. Companies oftentimes
use a mnemonic for their phone number to make it easier to remember.

Given a stringified phone number of any non-zero length, write a function that returns all mnemonics for this phone number,
in any order.

For this problem, a valid mnemonic may only contain letters and the digits `0` and `1`. In other words, if a digit is able
to be represented by a letter, then it must be. Digits `0` and `1` are the only two digits that don't have letter
representations on the keypad.

> Note that you should rely on the keypad illustrated above for digit-letter associations.


## Sample Input
```
phone_number = "1905"
```

## Sample Output
```
[
  "1w0j",
  "1w0k",
  "1w0l",
  "1x0j",
  "1x0k",
  "1x0l",
  "1y0j",
  "1y0k",
  "1y0l",
  "1z0j",
  "1z0k",
  "1z0l",
]
// The mnemonics could be ordered differently.
```

## Optimal Time & Space Complexity:
```
O(4ⁿ * n) time | O(4ⁿ * n) space - where `n` is the length of the phone number.
```
"""

# =========================================================================================================================== #

# Solution:


# O(4ⁿ * n) time | O(4ⁿ * n) space
def phone_number_mnemonics(phone_number):
    # Initialize a list to store all generated mnemonics
    mnemonics = []
    # Create a list to build each mnemonic, initialized with '0's as placeholders
    current_mnemonic = ["0"] * len(phone_number)

    # Define a recursive backtracking function to generate mnemonics
    def backtrack(index):
        # Base case: if we've processed all digits, add the complete mnemonic to results
        if index == len(phone_number):
            mnemonics.append("".join(current_mnemonic))
            return

        # Get the current digit from the phone number
        digit = phone_number[index]
        # For each letter mapped to the current digit:
        for letter in digit_to_letters[digit]:
            # Assign the letter to the current position
            current_mnemonic[index] = letter
            # Recursively process the next digit
            backtrack(index + 1)

    # Start the backtracking process from the first digit (index 0)
    backtrack(0)
    # Return all generated mnemonics
    return mnemonics


# Mapping of digits to their corresponding letters on a phone keypad
digit_to_letters = {
    "0": ["0"],  # 0 maps to 0
    "1": ["1"],  # 1 maps to 1
    "2": ["a", "b", "c"],  # 2 maps to a, b, c
    "3": ["d", "e", "f"],  # 3 maps to d, e, f
    "4": ["g", "h", "i"],  # 4 maps to g, h, i
    "5": ["j", "k", "l"],  # 5 maps to j, k, l
    "6": ["m", "n", "o"],  # 6 maps to m, n, o
    "7": ["p", "q", "r", "s"],  # 7 maps to p, q, r, s
    "8": ["t", "u", "v"],  # 8 maps to t, u, v
    "9": ["w", "x", "y", "z"],  # 9 maps to w, x, y, z
}

# Test Cases:

print(phone_number_mnemonics("1905"))
# ['1w0j', '1w0k', '1w0l', '1x0j', '1x0k', '1x0l', '1y0j', '1y0k', '1y0l', '1z0j', '1z0k', '1z0l']

print(phone_number_mnemonics("98"))
# ['wt', 'wu', 'wv', 'xt', 'xu', 'xv', 'yt', 'yu', 'yv', 'zt', 'zu', 'zv']

print(phone_number_mnemonics("0"))
# ['0']

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### **Time Complexity:**

1. **Digit to Letters Mapping:**
   - The digits `0` and `1` map to `["0"]` and `["1"]` respectively (only 1 choice per digit).
   - Digits `2` to `9` map to 3 or 4 letters each (e.g., `2` maps to `["a", "b", "c"]`).

2. **Worst Case:**
   - The worst case occurs when every digit in the phone number is from `7` or `9` (which map to 4 letters each). For example,
   if the input is `"9999"`, each digit has 4 choices.
   - Let `n` be the length of the phone number. If every digit has `4` choices, the recursion tree will have `4^n` leaves
   (since each of the `n` digits has 4 possibilities).
   
   - Thus, the total number of recursive calls is `O(4^n)`.

3. **Work per Recursive Call:**
   - At each recursive call, we append a letter to `current_mnemonic` (an `O(1)` operation for array assignment).
   - When we reach the base case (`index == len(phone_number)`), we join the `current_mnemonic` array into a string
   (an `O(n)` operation).
   - Since there are `O(4^n)` base cases, the total work for joining strings is `O(n * 4^n)`.

4. **Overall Time Complexity:**
   - The dominant term is `O(n * 4^n)` because of the string joining in the base case.
   

### **Space Complexity:**

1. **Recursion Stack:**
   - The maximum depth of the recursion is `n` (the length of the phone number), so the recursion stack uses `O(n)` space.

2. **Output Storage (`mnemonics`):**
   - In the worst case, there are `4^n` mnemonics, each of length `n`.
   - Thus, the space required to store all mnemonics is `O(n * 4^n)`.

3. **Auxiliary Space (`current_mnemonic`):**
   - The `current_mnemonic` array is of size `n` and is modified in-place during backtracking.

4. **Overall Space Complexity:**
   - The dominant term is `O(n * 4^n)` due to the output storage.


### **Final Answer:**
- **Time Complexity:** `O(n * 4ⁿ)`
- **Space Complexity:** `O(n * 4ⁿ)`

### **Explanation with Example:**
For a phone number like `"23"` (where `2` maps to `["a", "b", "c"]` and `3` maps to `["d", "e", "f"]`):
- The recursion tree has `3 * 3 = 9` leaves (mnemonics: `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`).
- The time complexity is `O(n * 3^n)` for this case (but `O(n * 4^n)` in the worst case).
- The space complexity is `O(n * 3^n)` for storing the output (but `O(n * 4^n)` in the worst case).

The worst-case scenario occurs when the phone number consists entirely of `7`s or `9`s (digits with 4 letters each).

"""

# Detailed Code Explanation:

"""
## 🎯 **Goal of the Code**

The function `phone_number_mnemonics(phone_number)` takes a string of digits (like a phone number) and returns **all possible 
letter combinations** that the number could represent based on the traditional phone keypad mapping.

---

## 📞 Phone Keypad Mapping

You’ve defined the mapping using a dictionary:

```
digit_to_letters = {
    "0": ["0"], 
    "1": ["1"],  
    "2": ["a", "b", "c"],  
    "3": ["d", "e", "f"],  
    "4": ["g", "h", "i"],  
    "5": ["j", "k", "l"], 
    "6": ["m", "n", "o"],  
    "7": ["p", "q", "r", "s"],  
    "8": ["t", "u", "v"],  
    "9": ["w", "x", "y", "z"],   
}
```

Each digit maps to a set of characters, just like on a mobile keypad.

---

## 🔁 How the Function Works

Here’s a breakdown of your function:

```
def phone_number_mnemonics(phone_number):
    mnemonics = []  # List to store all the valid mnemonics
    current_mnemonic = ["0"] * len(phone_number)  # Placeholder for one possible combination

    def backtrack(index):
        # Base case: If we’ve filled in all characters, save this combination
        if index == len(phone_number):
            mnemonics.append("".join(current_mnemonic))
            return

        digit = phone_number[index]  # Get the current digit
        for letter in digit_to_letters[digit]:  # Loop through each letter that maps to this digit
            current_mnemonic[index] = letter  # Replace character at current index
            backtrack(index + 1)  # Move to next digit

    backtrack(0)  # Start recursion from index 0
    return mnemonics
```

---

## 🔄 Example Walkthrough

Let’s walk through `phone_number_mnemonics("1905")`.

- **Input:** `"1905"`
- **Digits:**  
  - `"1"` → ["1"]  
  - `"9"` → ["w", "x", "y", "z"]  
  - `"0"` → ["0"]  
  - `"5"` → ["j", "k", "l"]  

So possible mnemonics are formed by taking one character from each list in sequence.

E.g.,  
`1w0j`, `1w0k`, `1w0l`,  
`1x0j`, `1x0k`, `1x0l`,  
...

Which results in:
```
['1w0j', '1w0k', '1w0l',
 '1x0j', '1x0k', '1x0l',
 '1y0j', '1y0k', '1y0l',
 '1z0j', '1z0k', '1z0l']
```

---

## 🔁 Backtracking Strategy

This is a classic **backtracking** approach, used for problems involving combinations, permutations, or exploring decision trees.

### Why It Works:

- The `backtrack` function explores **all paths recursively**.
- At each level, it tries every possible letter for that digit.
- When it reaches the end (`index == len(phone_number)`), it saves the full string.
- Backtracking ensures we explore **every valid combination**.

---

## ✅ Test Case Results

### `phone_number_mnemonics("0")`
→ ["0"]

### `phone_number_mnemonics("98")`
- 9 → [w, x, y, z]  
- 8 → [t, u, v]  
→ 4 * 3 = 12 combinations  
→ ["wt", "wu", ..., "zv"]

---

Let's visualize how the **backtracking tree** works for a small input — say:

---

### 📲 Input: `"23"`

Using the digit mapping:
- `"2"` → ["a", "b", "c"]
- `"3"` → ["d", "e", "f"]

---

### 🌳 Backtracking Tree Visualization

```
                        [ ]         ← Start with empty string
                       / | \
                     a   b   c      ← Choices for '2'
                   / | \ /|\ /|\
                 ad ae af bd be bf cd ce cf ← Choices for '3'
```

Each path from the root to a leaf gives you one complete **mnemonic** (a 2-letter string in this case).

---

### ✅ Final Results:

```
["ad", "ae", "af",
 "bd", "be", "bf",
 "cd", "ce", "cf"]
```

---

### 🌱 How This Grows for Larger Inputs

If you have `"203"`:
- `"2"` → ["a", "b", "c"]
- `"0"` → ["0"]
- `"3"` → ["d", "e", "f"]

Tree looks like:

```
                [ ]
               / | \
             a   b   c
             |   |   |
             0   0   0
           / | \ /|\ /|\
         d  e  f d e f d e f
```

Each level corresponds to one digit. The total number of leaves = product of letters for each digit.

"""
