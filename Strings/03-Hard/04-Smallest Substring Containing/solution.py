# Description:

"""
                                    Smallest Substring Containing

You're given two non-empty strings: a big string and a small string. Write a function that returns the smallest
substring in the big string that contains all of the small string's characters.

Note that:

- The substring can contain other characters not found in the small string.

- The characters in the substring don't have to be in the same order as they appear in the small string.

- If the small string has duplicate characters, the substring has to contain those duplicate characters
(it can also contain more, but not fewer).

You can assume that there will only be one relevant smallest substring.


## Sample Input:
```
bigString = "abcd$ef$axb$c$"
smallString = "$$abf"
```

## Sample Output:
```
"f$axb$"
```

## Optimal Time & Space Complexity:
```
`O(b + s)` time | `O(b + s)` space - where `b` is the length of the big input string
and `s` is the length of the small input string.
```

"""

# =============================================================================================== #

# Solution:


# `O(b + s)` time | `O(b + s)` space - where `b` is the length of the big
# input string and `s` is the length of the small input string
def smallest_substring_containing(big_string, small_string):
    # Step 1: Get the character counts for the small string
    target_char_counts = get_char_counts(small_string)

    # Step 2: Find the bounds of the smallest substring in the big string
    # that contains all characters of the small string
    substring_bounds = get_substring_bounds(big_string, target_char_counts)

    # Step 3: Extract and return the substring from the big string using the found bounds
    return get_string_from_bounds(big_string, substring_bounds)


def get_char_counts(string):
    # Initialize a dictionary to store character counts
    char_counts = {}

    # Iterate through each character in the string and update its count
    for char in string:
        increase_char_count(char, char_counts)

    return char_counts


def get_substring_bounds(string, target_char_counts):
    # Initialize the bounds of the substring with default values
    substring_bounds = [0, float("inf")]

    # Initialize a dictionary to store character counts for the current window
    substring_char_counts = {}

    # Calculate the number of unique characters in the small string
    num_unique_chars = len(target_char_counts.keys())

    # Initialize a counter to track how many unique characters have been matched
    num_unique_chars_done = 0

    # Initialize pointers for the sliding window
    left_idx = 0
    right_idx = 0

    # Iterate through the big string using the right pointer
    while right_idx < len(string):
        right_char = string[right_idx]

        # If the current character is not in the small string, move the right pointer
        if right_char not in target_char_counts:
            right_idx += 1
            continue

        # Update the character count for the current window
        increase_char_count(right_char, substring_char_counts)

        # If the count of the current character matches the target count, increment the matched counter
        if substring_char_counts[right_char] == target_char_counts[right_char]:
            num_unique_chars_done += 1

        # When all unique characters are matched, try to shrink the window from the left
        while num_unique_chars_done == num_unique_chars and left_idx <= right_idx:
            # Update the bounds if the current window is smaller than the previous best
            substring_bounds = get_closer_bounds(
                left_idx, right_idx, substring_bounds[0], substring_bounds[1]
            )

            left_char = string[left_idx]

            # If the left character is not in the small string, move the left pointer
            if left_char not in target_char_counts:
                left_idx += 1
                continue

            # If the count of the left character matches the target count, decrement the matched counter
            if substring_char_counts[left_char] == target_char_counts[left_char]:
                num_unique_chars_done -= 1

            # Decrease the count of the left character in the current window
            decrease_char_count(left_char, substring_char_counts)
            left_idx += 1

        # Move the right pointer to expand the window
        right_idx += 1

    return substring_bounds


def get_closer_bounds(idx_1, idx_2, idx_3, idx_4):
    # Return the bounds that represent the smaller substring
    return [idx_1, idx_2] if idx_2 - idx_1 < idx_4 - idx_3 else [idx_3, idx_4]


def get_string_from_bounds(string, bounds):
    start, end = bounds

    # If no valid substring was found, return an empty string
    if end == float("inf"):
        return ""

    # Extract and return the substring from the big string
    return string[start : end + 1]


def increase_char_count(char, char_counts):
    # Increase the count of the character in the dictionary
    if char not in char_counts:
        char_counts[char] = 0
    char_counts[char] += 1


def decrease_char_count(char, char_counts):
    # Decrease the count of the character in the dictionary
    char_counts[char] -= 1


# Test Cases:
big_string = "abcd$ef$axb$c$"
small_string = "$$abf"

big_string_2 = "abcdef"
small_string_2 = "fa"

big_string_3 = "a$fuu+afff+affaffa+a$Affab+a+a+$a$"
small_string_3 = "a+$aaAaaaa$++"

print(smallest_substring_containing(big_string, small_string))
# Output: "f$axb$"

print(smallest_substring_containing(big_string_2, small_string_2))
# Output: "abcdef"

print(smallest_substring_containing(big_string_3, small_string_3))
# Output: "affa+a$Affab+a+a+$a"

# =============================================================================================== #


# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity

1. **`get_char_counts(small_string)`**:
   - This function iterates over each character in `small_string` to count the occurrences.
   - Time complexity: **O(M)**, where `M` is the length of `small_string`.

2. **`get_substring_bounds(big_string, target_char_counts)`**:
   - This function uses a sliding window approach to find the smallest substring in `big_string` that
   contains all characters of `small_string`.
   - The `right_idx` pointer iterates over the entire `big_string` once, and the `left_idx` pointer moves
   forward only when a valid substring is found.
   - Each character in `big_string` is processed at most twice (once by `right_idx` and once by `left_idx`).
   - Time complexity: **O(N)**, where `N` is the length of `big_string`.

3. **`get_string_from_bounds(big_string, substring_bounds)`**:
   - This function simply extracts the substring from `big_string` using the bounds.
   - Time complexity: **O(K)**, where `K` is the length of the resulting substring.

4. **Overall Time Complexity**:
   - The dominant part is the sliding window algorithm in `get_substring_bounds`, which is **O(N)**.
   - Therefore, the total time complexity is **O(N + M)**.

---

### Space Complexity

1. **`get_char_counts(small_string)`**:
   - This function stores the character counts of `small_string` in a dictionary.
   - Space complexity: **O(M)**, where `M` is the number of unique characters in `small_string`.

2. **`get_substring_bounds(big_string, target_char_counts)`**:
   - This function uses a dictionary (`substring_char_counts`) to store the counts of characters in the current window.
   - The space required is proportional to the number of unique characters in `small_string`.
   - Space complexity: **O(M)**.

3. **`get_string_from_bounds(big_string, substring_bounds)`**:
   - This function does not use additional space proportional to the input size.
   - Space complexity: **O(1)**.

4. **Overall Space Complexity**:
   - The dominant space usage comes from the dictionaries used to store character counts.
   - Therefore, the total space complexity is **O(M)**.

---

### Summary

- **Time Complexity**: **O(N + M)**, where `N` is the length of `big_string` and `M` is the length of `small_string`.
- **Space Complexity**: **O(M)**, where `M` is the number of unique characters in `small_string`.

"""

# Code Explanation:

"""
### Explanation of the Code

The code provided is designed to find the smallest substring in a `big_string` that contains all the
characters of a `small_string`, including duplicates. The solution uses a sliding window approach
to efficiently find the smallest such substring.

### Key Functions

1. **`smallest_substring_containing(big_string, small_string)`**:
   - This is the main function that orchestrates the process.
   - It first calculates the character counts of the `small_string` using `get_char_counts`.
   - Then, it finds the bounds of the smallest substring in `big_string` that contains all characters 
   of `small_string` using `get_substring_bounds`.
   - Finally, it extracts and returns the substring using `get_string_from_bounds`.

2. **`get_char_counts(string)`**:
   - This function calculates the frequency of each character in the given string.
   - It returns a dictionary where keys are characters and values are their counts.

3. **`get_substring_bounds(string, target_char_counts)`**:

    Let’s break down the `get_substring_bounds` function step by step to understand how it works.
    This function is the core of the algorithm and uses a **sliding window** approach to find the smallest
    substring in `string` that contains all the characters of `small_string` (represented by `target_char_counts`).

    ---

    ### **Purpose of the Function**
    The function aims to find the **smallest substring** in `string` that contains all the characters in
    `target_char_counts` (which is derived from `small_string`). It returns the **bounds** (start and end indices) of this substring.

    ---

    ### **Key Variables**
    1. **`substring_bounds`**:
    - A list `[start, end]` that stores the indices of the smallest valid substring found so far.
    - Initialized to `[0, float("inf")]`, meaning no valid substring has been found yet.

    2. **`substring_char_counts`**:
    - A dictionary that keeps track of the counts of characters in the **current window** of `string`.

    3. **`num_unique_chars`**:
    - The number of unique characters in `target_char_counts` (derived from `small_string`).

    4. **`num_unique_chars_done`**:
    - A counter that tracks how many unique characters in `target_char_counts` have been **fully matched** in the current window.

    5. **`left_idx` and `right_idx`**:
    - Pointers that define the current window in `string`. The window is `[left_idx, right_idx]`.

    ---

    ### **How the Function Works**

    #### **Step 1: Initialize Variables**
    - `substring_bounds` is set to `[0, float("inf")]` (no valid substring found yet).
    - `substring_char_counts` is an empty dictionary to track character counts in the current window.
    - `num_unique_chars` is the number of unique characters in `target_char_counts`.
    - `num_unique_chars_done` is initialized to `0` (no characters matched yet).
    - `left_idx` and `right_idx` are set to `0` (start of the string).

    ---

    #### **Step 2: Expand the Window (Move `right_idx`)**
    - The outer `while` loop iterates over `string` using `right_idx`.
    - For each character at `right_idx`:
    - If the character is **not** in `target_char_counts`, it is ignored, and `right_idx` is incremented.
    - If the character is in `target_char_counts`:
        - Its count in `substring_char_counts` is incremented using `increase_char_count`.
        - If the count of this character in the current window matches its count in `target_char_counts`, increment
        `num_unique_chars_done`.

    ---

    #### **Step 3: Contract the Window (Move `left_idx`)**
    - When `num_unique_chars_done == num_unique_chars`, it means the current window contains all the required characters.
    - The inner `while` loop tries to **shrink the window** from the left to find a smaller valid substring:
    - Update `substring_bounds` using `get_closer_bounds` to keep track of the smallest valid window.
    - If the character at `left_idx` is **not** in `target_char_counts`, it is ignored, and `left_idx` is incremented.
    - If the character at `left_idx` is in `target_char_counts`:
        - If its count in the current window matches its count in `target_char_counts`, decrement `num_unique_chars_done`
        (since we are removing this character from the window).
        - Decrement its count in `substring_char_counts` using `decrease_char_count`.
        - Increment `left_idx` to shrink the window.

    ---

    #### **Step 4: Repeat Until the End of the String**
    - The outer loop continues to expand the window by moving `right_idx` until the end of `string`.
    - The inner loop contracts the window whenever a valid substring is found.

    ---

    #### **Step 5: Return the Bounds**
    - After processing the entire string, the function returns `substring_bounds`, which contains the indices 
    of the smallest valid substring.

    ---

    ### **Example Walkthrough**

    Let’s use an example to understand how this works:

    #### Input:
    - `string = "abcd$ef$axb$c$"`
    - `target_char_counts = {'$': 2, 'a': 1, 'b': 1, 'f': 1}` (derived from `small_string = "$$abf"`).

    #### Execution:
    1. **Initialization**:
    - `substring_bounds = [0, inf]`
    - `substring_char_counts = {}`
    - `num_unique_chars = 4` (`$`, `a`, `b`, `f`)
    - `num_unique_chars_done = 0`

    2. **Expand Window**:
    - `right_idx` moves from `0` to `len(string) - 1`.
    - When `right_idx` reaches `'$'` (index 4), `substring_char_counts = {'$': 1}`.
    - When `right_idx` reaches `'f'` (index 7), `substring_char_counts = {'$': 2, 'a': 1, 'b': 1, 'f': 1}`.
    - Now, `num_unique_chars_done = 4` (all characters matched).

    3. **Contract Window**:
    - The inner loop tries to shrink the window from the left.
    - The smallest valid substring found is `"f$axb$"` (indices `[7, 12]`).

    4. **Return Bounds**:
    - The function returns `[7, 12]`.

    ---

    ### **Key Points**
    1. **Sliding Window**:
    - The window expands to include new characters and contracts to find the smallest valid substring.

    2. **Character Count Matching**:
    - The function ensures that the current window contains all characters of `small_string` with the required counts.

    3. **Efficiency**:
    - The function processes each character in `string` at most twice (once by `right_idx` and once by `left_idx`),
    making it **O(n)** in time complexity.

    ---

    ### **Visualization**

    For `string = "abcd$ef$axb$c$"` and `small_string = "$$abf"`:

    | Step | `right_idx` | `left_idx` | Current Window  | `substring_char_counts`           | `num_unique_chars_done` | Action   |
    |------|-------------|------------|-----------------|-----------------------------------|-------------------------|----------|
    | 1    | 0           | 0          | "a"             | {'a': 1}                          | 0                       | Expand   |
    | 2    | 1           | 0          | "ab"            | {'a': 1, 'b': 1}                  | 0                       | Expand   |
    | 3    | 4           | 0          | "abcd$"         | {'$': 1}                          | 0                       | Expand   |
    | 4    | 7           | 0          | "abcd$ef"       | {'$': 2, 'a': 1, 'b': 1, 'f': 1}  | 4                       | Contract |
    | 5    | 7           | 7          | "f"             | {'f': 1}                          | 3                       | Expand   |
    | 6    | 12          | 7          | "f$axb$"        | {'$': 2, 'a': 1, 'b': 1, 'f': 1}  | 4                       | Contract |

    ---

    ### **Final Output**
    The function returns the bounds `[7, 12]`, which corresponds to the substring `"f$axb$"`.

    ---

4. **`get_closer_bounds(idx_1, idx_2, idx_3, idx_4)`**:
   - This helper function compares two pairs of indices and returns the pair that represents a smaller substring.

5. **`get_string_from_bounds(string, bounds)`**:
   - This function extracts the substring from `big_string` using the bounds provided.
   - If the bounds are invalid (i.e., `end` is infinity), it returns an empty string.

6. **`increase_char_count(char, char_counts)`**:
   - This helper function increments the count of a character in the `char_counts` dictionary.

7. **`decrease_char_count(char, char_counts)`**:
   - This helper function decrements the count of a character in the `char_counts` dictionary.

### Detailed Walkthrough

1. **Character Counting**:
   - The `get_char_counts` function is called to count the frequency of each character in `small_string`. 
   This gives us the target character counts that we need to match in the `big_string`.

2. **Sliding Window**:
   - The `get_substring_bounds` function initializes two pointers, `left_idx` and `right_idx`, to represent
   the current window in `big_string`.
   - It also initializes `substring_char_counts` to keep track of the character counts in the current window.
   - The function iterates over `big_string` using the `right_idx` pointer, expanding the window to include more characters.
   - For each character, it updates the `substring_char_counts` and checks if the current window contains all characters of `small_string` with the required counts.
   - When the current window contains all required characters, the function tries to contract the window from the left
   to find a smaller valid substring.

3. **Finding the Smallest Substring**:
   - The `get_closer_bounds` function is used to compare the current window with the smallest window found so far 
   and update the bounds if the current window is smaller.
   - This ensures that the function always keeps track of the smallest valid substring.

4. **Extracting the Result**:
   - Once the smallest bounds are found, the `get_string_from_bounds` function extracts the substring from `big_string`
   using these bounds.
   - If no valid substring is found, it returns an empty string.

### Example Walkthrough

Let's walk through the first test case:

- **Input**:
  - `big_string = "abcd$ef$axb$c$"`
  - `small_string = "$$abf"`

- **Step 1: Character Counting**:
  - `get_char_counts("$$abf")` returns `{'$': 2, 'a': 1, 'b': 1, 'f': 1}`.

- **Step 2: Sliding Window**:
  - The function iterates over `big_string` with `right_idx` and `left_idx`.
  - When `right_idx` reaches the character 'f', the current window contains all characters of `small_string`
  with the required counts.
  - The function then contracts the window from the left to find the smallest valid substring.

- **Step 3: Finding the Smallest Substring**:
  - The smallest valid substring found is "f$axb$".

- **Step 4: Extracting the Result**:
  - The function returns "f$axb$".

### Output

- For the first test case, the output is `"f$axb$"`.
- For the second test case, the output is `"abcdef"`.
- For the third test case, the output is `"affa+a$Affab+a+a+$a"`.

This approach ensures that the solution is efficient and works in linear time with respect to the length of `big_string`.

Here is detailed visualization of example:

| Step | `right_idx` Expands | `left_idx` Shrinks | Current Window |
|------|---------------------|--------------------|----------------|
| 1    | `"a"`               | -                  | `"a"`          |
| 2    | `"ab"`              | -                  | `"ab"`         |
| 3    | `"abc"`             | -                  | `"abc"`        |
| 4    | `"abcd"`            | -                  | `"abcd"`       |
| 5    | `"abcd$"`           | -                  | `"abcd$"`      |
| 6    | `"abcd$e"`          | -                  | `"abcd$e"`     |
| 7    | `"abcd$ef"`         | -                  | `"abcd$ef"`    |
| 8    | `"abcd$ef$"`        | Shrink from left   | `"f$axb$"` (Final Answer) 

---

## **Summary**
- The algorithm **uses the sliding window technique** to efficiently find the smallest substring.
- It **maintains a character frequency count** to ensure all characters from `small_string` are in the window.
- It **expands** when a needed character is missing and **shrinks** when a complete substring is found.
- The **resulting substring** is extracted from `big_string`.

This approach ensures **optimal performance** for large strings while correctly handling **duplicate characters**! 

"""
