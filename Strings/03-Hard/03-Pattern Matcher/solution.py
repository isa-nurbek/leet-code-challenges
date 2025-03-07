# Description:

"""
                                        Pattern Matcher

You're given two non-empty strings. The first one is a pattern consisting of only `"x"`s and / or `"y"`s; the other
one is a normal string of alphanumeric characters. Write a function that checks whether the normal string matches the pattern.

A string `S0` is said to match a pattern if replacing all `"x"`s in the pattern with some non-empty substring `S1` of `S0`
and replacing all `"y"`s in the pattern with some non-empty substring `S2` of `S0` yields the same string `S0`.

If the input string doesn't match the input pattern, the function should return an empty array; otherwise, it should return
an array holding the strings `S1` and `S2` that represent `"x"` and `"y"` in the normal string, in that order. If the pattern
doesn't contain any `"x"`s or `"y"`s, the respective letter should be represented by an empty string in the final array that
you return.

You can assume that there will never be more than one pair of strings `S1` and `S2` that appropriately represent `"x"` and
`"y"` in the normal string.


## Sample Input:
```
pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"
```

## Sample Output:
```
["go", "powerranger"]
```

## Optimal Time & Space Complexity:
```
`O(n^2 + m)` time | `O(n + m)` space - where `n` is the length of the main string and
`m` is the length of the pattern.
```

"""

# =============================================================================================== #

# Solution:


# `O(n^2 + m)` time | `O(n + m)` space
def pattern_matcher(pattern, string):
    # If the pattern is longer than the string, it's impossible to match, so return an empty list.
    if len(pattern) > len(string):
        return []

    # Normalize the pattern to start with 'x' to simplify processing.
    new_pattern = get_new_pattern(pattern)
    # Check if the pattern was switched (i.e., originally started with 'y').
    did_switch = new_pattern[0] != pattern[0]

    # Initialize counts for 'x' and 'y' in the pattern.
    counts = {"x": 0, "y": 0}
    # Get the counts of 'x' and 'y' and the position of the first 'y' in the pattern.
    first_y_pos = get_counts_and_first_y_pos(new_pattern, counts)

    # If there are 'y's in the pattern, we need to find lengths for both 'x' and 'y'.
    if counts["y"] != 0:
        # Iterate over possible lengths for 'x'.
        for len_of_x in range(1, len(string)):
            # Calculate the required length for 'y' based on the current length of 'x'.
            len_of_y = (len(string) - len_of_x * counts["x"]) / counts["y"]

            # If the length of 'y' is invalid (negative or not an integer), skip this iteration.
            if len_of_y <= 0 or len_of_y % 1 != 0:
                continue

            # Convert len_of_y to an integer.
            len_of_y = int(len_of_y)
            # Calculate the starting index of 'y' in the string.
            y_idx = first_y_pos * len_of_x

            # Extract 'x' and 'y' from the string based on the calculated lengths.
            x = string[:len_of_x]
            y = string[y_idx : y_idx + len_of_y]

            # Construct a potential match by mapping the pattern to the extracted 'x' and 'y'.
            potential_match = map(lambda char: x if char == "x" else y, new_pattern)

            # If the constructed string matches the input string, return the result.
            if string == "".join(potential_match):
                # Return [x, y] if the pattern was not switched, otherwise [y, x].
                return [x, y] if not did_switch else [y, x]
    else:
        # If there are no 'y's in the pattern, only 'x' needs to be considered.
        len_of_x = len(string) / counts["x"]

        # If the length of 'x' is valid (integer), proceed.
        if len_of_x % 1 == 0:
            len_of_x = int(len_of_x)

            # Extract 'x' from the string.
            x = string[:len_of_x]
            # Construct a potential match by mapping the pattern to 'x'.
            potential_match = map(lambda char: x, new_pattern)

            # If the constructed string matches the input string, return the result.
            if string == "".join(potential_match):
                # Return [x, ""] if the pattern was not switched, otherwise ["", x].
                return [x, ""] if not did_switch else ["", x]

    # If no match is found, return an empty list.
    return []


def get_new_pattern(pattern):
    # Convert the pattern into a list of characters.
    pattern_letters = list(pattern)

    # If the pattern starts with 'x', return it as is.
    if pattern[0] == "x":
        return pattern_letters
    else:
        # If the pattern starts with 'y', swap 'x' and 'y' to normalize it.
        return list(map(lambda char: "x" if char == "y" else "y", pattern_letters))


def get_counts_and_first_y_pos(pattern, counts):
    # Initialize the position of the first 'y' as None.
    first_y_pos = None

    # Iterate over the pattern to count 'x' and 'y' and find the first 'y' position.
    for i, char in enumerate(pattern):
        counts[char] += 1

        # If this is the first 'y', record its position.
        if char == "y" and first_y_pos is None:
            first_y_pos = i

    # Return the position of the first 'y'.
    return first_y_pos


# Test Cases:
pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"

pattern_2 = "xyx"
string_2 = "thisshouldobviouslybewrong"

pattern_3 = "xxxx"
string_3 = "testtesttesttest"

print(pattern_matcher(pattern, string))
# Output: ['go', 'powerranger']

print(pattern_matcher(pattern_2, string_2))
# Output: []

print(pattern_matcher(pattern_3, string_3))
# Output: ['test', '']

# =============================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity

1. **Pattern Transformation (`get_new_pattern`)**:
   - This function iterates over the pattern to convert it to a new pattern where the first character is always 'x'.
   - Time complexity: **O(n)**, where `n` is the length of the pattern.

2. **Counting and First 'y' Position (`get_counts_and_first_y_pos`)**:
   - This function iterates over the pattern to count the occurrences of 'x' and 'y' and find the first position of 'y'.
   - Time complexity: **O(n)**, where `n` is the length of the pattern.

3. **Main Logic (`pattern_matcher`)**:
   - If the pattern contains 'y':
     - The outer loop runs for `len_of_x` from 1 to `len(string) - 1`. This is **O(m)**, where `m` is the length of the string.
     - Inside the loop, the `map` operation and string concatenation take **O(m)** time.
     - Total time complexity for this case: **O(m²)**.
   - If the pattern contains only 'x':
     - The `map` operation and string concatenation take **O(m)** time.
     - Total time complexity for this case: **O(m)**.

   - Overall, the worst-case time complexity is **O(m²)** when the pattern contains 'y'.

### Space Complexity

1. **Pattern Transformation (`get_new_pattern`)**:
   - This function creates a new list of the same size as the pattern.
   - Space complexity: **O(n)**, where `n` is the length of the pattern.

2. **Counting and First 'y' Position (`get_counts_and_first_y_pos`)**:
   - This function uses a constant amount of extra space (a dictionary and a variable).
   - Space complexity: **O(1)**.

3. **Main Logic (`pattern_matcher`)**:
   - The main logic uses additional space for the `potential_match` list, which can be up to the size of the string.
   - Space complexity: **O(m)**, where `m` is the length of the string.

   - Overall, the space complexity is **O(n + m)**, where `n` is the length of the pattern and `m` is the length of the string.

### Summary

- **Time Complexity**: **O(m²)** in the worst case (when the pattern contains 'y'), otherwise **O(m)**.
- **Space Complexity**: **O(n + m)**, where `n` is the length of the pattern and `m` is the length of the string.

This analysis assumes that the pattern and string are of reasonable lengths and that the operations like string slicing
and concatenation are efficient.

"""

# Code Explanation:

"""
### **Pattern Matcher: Detailed Explanation**

The function `pattern_matcher(pattern, string)` is designed to find the substrings that correspond to
`x` and `y` in the given pattern such that when the pattern is expanded, it reconstructs the given `string`.

---

## **Step-by-Step Breakdown of the Code**
### **Step 1: Handle Edge Cases**
```
if len(pattern) > len(string):
    return []
```
- If the pattern is longer than the string, it is **impossible** to form the string using the pattern,
so return an empty list.

---

### **Step 2: Normalize the Pattern**
```
new_pattern = get_new_pattern(pattern)
did_switch = new_pattern[0] != pattern[0]
```
- The function `get_new_pattern(pattern)` ensures that the pattern always starts with `"x"`.
If the pattern starts with `"y"`, it swaps `"x"` and `"y"` to maintain consistency.
- The `did_switch` flag tracks whether the pattern was modified so that we can swap `x` and `y` back later if needed.

#### **Example:**
```
pattern = "yxyy"
new_pattern = get_new_pattern(pattern)  # Returns ['x', 'y', 'x', 'x']
did_switch = True
```

---

### **Step 3: Count Occurrences of "x" and "y"**
```
counts = {"x": 0, "y": 0}
first_y_pos = get_counts_and_first_y_pos(new_pattern, counts)
```
- The function `get_counts_and_first_y_pos(new_pattern, counts)` counts how many times `"x"` and `"y"`
appear in `new_pattern` and also finds the first occurrence of `"y"` (if it exists).
- This helps in calculating potential lengths of `x` and `y`.

#### **Example:**
```
pattern = "xxyxxy"
counts = {"x": 4, "y": 2}
first_y_pos = 2  # (First occurrence of 'y' is at index 2)
```

---

### **Step 4: Find Possible Lengths of "x" and "y"**
```
if counts["y"] != 0:
    for len_of_x in range(1, len(string)):
        len_of_y = (len(string) - len_of_x * counts["x"]) / counts["y"]
```
- If `"y"` exists in the pattern, we iterate over **possible lengths for `"x"`**, calculating the length of `"y"` accordingly.
- The formula:

        Length of `y` = Total String Length - (Count of `x` * Length of `x`) / Count of `y`
  
- If `len_of_y` is a **valid integer**, we proceed with checking the substrings.

---

### **Step 5: Extract "x" and "y" and Validate the Match**
```
if len_of_y > 0 and len_of_y % 1 == 0:
    len_of_y = int(len_of_y)
    y_idx = first_y_pos * len_of_x
    x = string[:len_of_x]
    y = string[y_idx : y_idx + len_of_y]
```
- We find the **starting index of `"y"`** using `first_y_pos * len_of_x`.
- Extract potential values for `"x"` and `"y"` from `string`.

#### **Example Calculation:**
For `pattern = "xxyxxy"` and `string = "gogopowerrangergogopowerranger"`:

- Let’s say `len_of_x = 2`:
  - `len_of_y = (30 - 2 × 4) / 2 = 10`
  - `x = "go"`
  - `y = "powerranger"`

```
potential_match = map(lambda char: x if char == "x" else y, new_pattern)
if string == "".join(potential_match):
```
- This reconstructs the string from the pattern using the extracted `"x"` and `"y"` values and checks if it matches `string`.

- If there's a match, it **returns `[x, y]` or `[y, x]`** (if `did_switch` was `True`).

---

### **Step 6: Special Case When There is No "y"**
```
else:
    len_of_x = len(string) / counts["x"]
    if len_of_x % 1 == 0:
        len_of_x = int(len_of_x)
        x = string[:len_of_x]
        potential_match = map(lambda char: x, new_pattern)
```
- If there is **no "y"** in the pattern:
  - The entire string should be **divisible by the count of "x"**.
  - Extract `x` accordingly.
  - If `string` matches the reconstructed pattern, return `[x, ""]`.

---

## **Test Cases & Execution**
```
pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"
print(pattern_matcher(pattern, string))
# Output: ['go', 'powerranger']
```
- `"x"` maps to `"go"`, `"y"` maps to `"powerranger"`, and the pattern reconstructs the string.

---

```
pattern_2 = "xyx"
string_2 = "thisshouldobviouslybewrong"
print(pattern_matcher(pattern_2, string_2))
# Output: []
```
- No valid `x` and `y` pairs exist that satisfy the pattern.

---

```
pattern_3 = "xxxx"
string_3 = "testtesttesttest"
print(pattern_matcher(pattern_3, string_3))
# Output: ['test', '']
```
- Only `"x"` is present in the pattern.
- `"x"` maps to `"test"` (since `string` is evenly divided into four `"test"` parts).
- `"y"` is an empty string since it's not in the pattern.

---

## **Summary**
- **Convert pattern** to always start with `"x"`.
- **Count occurrences of "x" and "y"** and identify the first position of `"y"`.
- **Iterate over possible lengths** of `"x"` and calculate `"y"` accordingly.
- **Extract substrings and validate** the pattern.
- **Handle special case** where `"y"` is absent.

This approach ensures an **efficient** pattern-matching process, avoiding brute-force substring searches. 

"""
