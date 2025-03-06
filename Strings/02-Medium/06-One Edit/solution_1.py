# Description:

"""
                                    One Edit

You're given two strings `stringOne` and `stringTwo`. Write a function that determines if these two
strings can be made equal using only one edit.

There are 3 possible edits:

- **Replace:** One character in one string is swapped for a different character.
- **Add:** One character is added at any index in one string.
- **Remove:** One character is removed at any index in one string.

Note that both strings will contain at least one character. If the strings are the same, your function should return true.


## Sample Input:
```
stringOne = "hello"
stringTwo = "hollo"
```

## Sample Output:
```
True // A single replace at index 1 of either string can make the strings equal
```

## Optimal Time & Space Complexity:
```
`O(n)` time | `O(1)` space - where `n` is the length of the shorter string.
```

"""

# =============================================================================================== #

# Solution


# `O(n + m)` time | `O(1)` space - where `n` is the length of stringOne, and
# `m` is the length of stringTwo
def one_edit(string_one, string_two):
    # Get the lengths of both strings
    length_one, length_two = len(string_one), len(string_two)

    # If the difference in lengths is more than 1, more than one edit is needed
    if abs(length_one - length_two) > 1:
        return False

    # Iterate through the characters of the shorter string
    for i in range(min(length_one, length_two)):
        # If characters at the current position are different
        if string_one[i] != string_two[i]:
            # If string_one is longer, check if the rest of string_one matches string_two from this point
            if length_one > length_two:
                return string_one[i + 1 :] == string_two[i:]
            # If string_two is longer, check if the rest of string_two matches string_one from this point
            elif length_two > length_one:
                return string_one[i:] == string_two[i + 1 :]
            # If lengths are equal, check if the rest of the strings match after this point
            else:
                return string_one[i + 1 :] == string_two[i + 1 :]

    # If no differences are found, the strings are either identical or one edit away
    return True


# Test Case 1
print(one_edit("hello", "hollo"))  # Output: True

# Test Case 2
print(one_edit("abc", "b"))  # Output: False

# Test Case 3
print(one_edit("abcdefghijk", "abcdefghijk"))  # Output: True


# =============================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity

The time complexity of the `one_edit` function is **O(n)**, where **n** is the length of the shorter string.
Here's why:

1. **Loop through characters**: The function iterates through the characters of the shorter string using
a `for` loop. In the worst case, it will compare all characters of the shorter string.
2. **String slicing**: When a mismatch is found, the function performs string slicing (`string_one[i + 1:]`
or `string_two[i + 1:]`). String slicing in Python takes **O(k)** time, where **k** is the length of the
sliced string. However, in this case, the sliced string is at most one character shorter than the original
string, so the slicing operation is still **O(n)** in the worst case.

Since the loop and the slicing operations are both linear in terms of the input size, the overall time complexity is **O(n)**.

---

### Space Complexity

The space complexity of the `one_edit` function is **O(1)** (constant space).
Here's why:

1. **No additional data structures**: The function does not use any additional data structures 
(like lists, dictionaries, etc.) that grow with the input size.
2. **String slicing**: While string slicing creates new strings, these slices are temporary and do not 
grow with the input size. They are discarded after comparison.

Thus, the space complexity is constant, **O(1)**.

---

### Summary

- **Time Complexity**: **O(n)**, where **n** is the length of the shorter string.
- **Space Complexity**: **O(1)** (constant space).

This implementation is efficient for checking if two strings are one edit apart.

"""

# Code Explanation:

"""
This function `one_edit` checks whether two strings are at most **one edit apart**. An edit can be:
1. **Insertion** of a character.
2. **Deletion** of a character.
3. **Replacement** of a character.

If more than one edit is required to make the strings equal, the function returns `False`. Otherwise, it returns `True`.

---

## **Step-by-step Explanation of the Code**

### **Step 1: Compute Lengths and Check for Large Differences**
```
length_one, length_two = len(string_one), len(string_two)

if abs(length_one - length_two) > 1:
    return False
```
- First, the function calculates the lengths of both input strings.
- If the difference in their lengths is greater than **1**, it returns `False` immediately. 
  - This is because a single edit cannot convert a string of length 5 into a string of length 7 
  (since at least 2 edits would be required).

---

### **Step 2: Compare Characters One by One**
```
for i in range(min(length_one, length_two)):
    if string_one[i] != string_two[i]:  # Found a difference
```
- We iterate through both strings up to the length of the shorter string.
- If we find a character that does **not** match, we need to determine whether this is the **only edit** needed.

---

### **Step 3: Handle the Three Edit Cases**
#### **Case 1: Deletion from `string_one`**
```
if length_one > length_two:
    return string_one[i + 1 :] == string_two[i:]
```
- If `string_one` is longer, this means that we need to remove one character from `string_one` to match `string_two`.
- We check whether removing `string_one[i]` (by slicing from `i+1`) makes it equal to `string_two[i:]`.

#### **Case 2: Insertion into `string_one`**
```
elif length_two > length_one:
    return string_one[i:] == string_two[i + 1 :]
```
- If `string_two` is longer, this means that we need to insert one character into `string_one`.
- We check whether skipping `string_two[i]` (by slicing from `i+1`) makes `string_two` equal to `string_one`.

#### **Case 3: Replacement**
```
else:
    return string_one[i + 1 :] == string_two[i + 1 :]
```
- If both strings are of equal length, then a mismatch means a **replacement** is needed.
- We check whether the strings are identical **after skipping the mismatched character**.

---

### **Step 4: Handle the Case When No Edits Are Needed**
```
return True
```
- If no differences are found during iteration, the strings are either identical or differ only by an optional last character.
- In either case, they are **one edit away or already equal**, so we return `True`.

---

## **Test Cases & Expected Output**
```
print(one_edit("hello", "hollo"))  # Output: True  (Replace 'e' with 'o')
print(one_edit("abc", "b"))        # Output: False (Need to delete 'a' and 'c')
print(one_edit("abcdefghijk", "abcdefghijk"))  # Output: True (No edits needed)
```

### **Breakdown of Each Test Case**
1. **"hello" vs. "hollo"**  
   - Only one replacement (`e` → `o`), so it returns `True`.

2. **"abc" vs. "b"**  
   - The difference in length is `2`, so it's impossible to fix in one edit. Returns `False`.

3. **"abcdefghijk" vs. "abcdefghijk"**  
   - The strings are identical, so it returns `True`.

---

## **Edge Cases**
1. **Empty strings:**
   ```
   print(one_edit("", ""))  # True (no edits needed)
   print(one_edit("", "a"))  # True (one insertion)
   print(one_edit("a", ""))  # True (one deletion)
   print(one_edit("", "ab"))  # False (needs two insertions)
   ```
2. **Strings with only one character difference at the end:**
   ```
   print(one_edit("test", "tes"))  # True (one deletion)
   print(one_edit("tes", "test"))  # True (one insertion)
   print(one_edit("test", "best")) # True (one replacement)
   ```
3. **Strings with multiple differences:**
   ```
   print(one_edit("cat", "dog"))  # False (needs 3 edits)
   ```

---

## **Summary**
- **Handles all three edit cases:** insertion, deletion, and replacement.
- **Early exit optimization:** If the length difference is greater than 1, it returns `False` immediately.
- **Efficient comparison using slicing.**
- **Time complexity is `O(N)`.**
- **Space complexity is `O(1)`.**

"""
