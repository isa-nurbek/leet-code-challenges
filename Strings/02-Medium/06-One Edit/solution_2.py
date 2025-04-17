# Problem Description:

"""
                                    One Edit

You're given two strings `string_one` and `string_two`. Write a function that determines if these two
strings can be made equal using only one edit.

There are 3 possible edits:

- **Replace:** One character in one string is swapped for a different character.
- **Add:** One character is added at any index in one string.
- **Remove:** One character is removed at any index in one string.

Note that both strings will contain at least one character. If the strings are the same, your function should return true.


## Sample Input:
```
string_one = "hello"
string_two = "hollo"
```

## Sample Output:
```
True // A single replace at index 1 of either string can make the strings equal
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the length of the shorter string.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space - where `n` is the length of shorter string
def one_edit(string_one, string_two):
    # Get the lengths of both strings
    length_one, length_two = len(string_one), len(string_two)

    # If the difference in lengths is more than 1, more than one edit is needed
    if abs(length_one - length_two) > 1:
        return False

    # Initialize a flag to track if an edit has been made
    made_edit = False

    # Initialize indices to traverse both strings
    index_one = 0
    index_two = 0

    # Loop through both strings while there are characters left to compare
    while index_one < length_one and index_two < length_two:
        # If the current characters of both strings don't match
        if string_one[index_one] != string_two[index_two]:
            # If an edit has already been made, return False
            if made_edit:
                return False

            # Mark that an edit has been made
            made_edit = True

            # If string_one is longer, move its index forward (simulating a deletion)
            if length_one > length_two:
                index_one += 1
            # If string_two is longer, move its index forward (simulating a deletion)
            elif length_two > length_one:
                index_two += 1
            # If the lengths are the same, move both indices forward (simulating a replacement)
            else:
                index_one += 1
                index_two += 1
        else:
            # If the characters match, move both indices forward
            index_one += 1
            index_two += 1

    # If the loop completes without finding more than one edit, return True
    return True


# Test Case 1
print(one_edit("hello", "hollo"))  # Output: True

# Test Case 2
print(one_edit("abc", "b"))  # Output: False

# Test Case 3
print(one_edit("abcdefghijk", "abcdefghijk"))  # Output: True

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity

The time complexity of the `one_edit` function is **O(n)**, where **n** is the length of the shorter string.
Here's why:

1. **Initial Length Check**: The function starts by comparing the lengths of the two strings.
This operation takes **O(1)** time.

2. **While Loop**: The main logic is inside the `while` loop, which iterates through both strings.
The loop runs until one of the strings is fully traversed. In the worst case, it will iterate through
the entire shorter string, which takes **O(n)** time.

3. **Conditional Checks**: Inside the loop, the function checks if the characters at the current indices are different.
If they are, it checks if an edit has already been made. These checks are **O(1)** operations.

4. **Index Updates**: Depending on the lengths of the strings, the indices are incremented appropriately.
This is also an **O(1)** operation.

Since the loop runs in linear time relative to the length of the shorter string, the overall time complexity is **O(n)**.

### Space Complexity

The space complexity of the `one_edit` function is **O(1)**, which means it uses constant space.
Here's why:

1. **Variables**: The function uses a few variables (`length_one`, `length_two`, `made_edit`, `index_one`, `index_two`),
but the number of variables does not depend on the input size. These variables take up a constant amount of space.

2. **No Additional Data Structures**: The function does not use any additional data structures like arrays, lists,
or dictionaries that grow with the input size.

Since the space used by the function does not scale with the input size, the space complexity is **O(1)**.

### Summary

- **Time Complexity**: **O(n)**, where **n** is the length of the shorter string.
- **Space Complexity**: **O(1)**, constant space.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of `one_edit` Function**

The function `one_edit` determines whether two strings are at most **one edit away** from each other.
An **edit** can be:

1. **Insertion** of a single character.
2. **Deletion** of a single character.
3. **Replacement** of a single character.

If more than one edit is needed to make the two strings identical, the function returns `False`. 
Otherwise, it returns `True`.

---

### **Step-by-Step Explanation**
1. **Calculate the Lengths of Both Strings**  
   ```
   length_one, length_two = len(string_one), len(string_two)
   ```
   This gets the lengths of both input strings.

2. **Check if the Length Difference is Greater Than 1**  
   ```
   if abs(length_one - length_two) > 1:
       return False
   ```
   - If the difference in lengths is greater than 1, more than one edit would be required (because you can
   only insert or delete **one** character per edit).
   - Example: `"abc"` and `"a"` (length difference = 2) → `False`

3. **Initialize Tracking Variables**
   ```
   made_edit = False
   index_one = 0
   index_two = 0
   ```
   - `made_edit` keeps track of whether we've already made an edit.
   - `index_one` and `index_two` are used to traverse the two strings.

4. **Iterate Over Both Strings Character by Character**
   ```
   while index_one < length_one and index_two < length_two:
   ```
   - This loop ensures we don't go out of bounds while comparing characters.

5. **Character Mismatch Handling**
   ```
   if string_one[index_one] != string_two[index_two]:
   ```
   - If we find a mismatch between characters in the two strings, we must decide how to handle it.

6. **Check If We Already Made an Edit**
   ```
   if made_edit:
       return False
   ```
   - If we've already modified a character before and we find another mismatch, we return `False`
   (because we would need more than one edit).

7. **Mark That We've Made an Edit**
   ```
   made_edit = True
   ```

8. **Adjust Indexes Based on Lengths**
   ```
   if length_one > length_two:
       index_one += 1  # Deletion in string_one
   elif length_two > length_one:
       index_two += 1  # Insertion in string_one
   else:
       index_one += 1
       index_two += 1  # Replacement case
   ```
   - **Case 1: `length_one > length_two`**  
     - This means `string_one` is longer, so a deletion must have occurred in `string_one`. Move `index_one` ahead.
   - **Case 2: `length_two > length_one`**  
     - This means `string_two` is longer, so an insertion must have happened in `string_one`. Move `index_two` ahead.
   - **Case 3: `length_one == length_two`**  
     - This means a replacement has occurred. Move both indices ahead.

9. **If No More Mismatches are Found, Return True**
   ```
   return True
   ```
   - If we complete the loop without finding more than one edit, we return `True`.

---

### **Test Cases and Walkthrough**

#### **Test Case 1**
```
one_edit("hello", "hollo")
```
**Explanation:**
- `"hello"` → `"hollo"`  
- The second character `'e'` is replaced with `'o'`. **One replacement (valid edit).**
- **Output:** `True`

---

#### **Test Case 2**
```
one_edit("abc", "b")
```
**Explanation:**
- `"abc"` → `"b"`
- Two deletions are needed (`"abc" → "bc"` and `"bc" → "b"`), which is **more than one edit**.
- **Output:** `False`

---

#### **Test Case 3**
```
one_edit("abcdefghijk", "abcdefghijk")
```
**Explanation:**
- The strings are already identical, meaning **zero edits are required**.
- **Output:** `True`

---

### **Final Summary**

- **Handles insertions, deletions, and replacements.**
- **Ensures only one edit is allowed.**
- **Runs efficiently in O(N) time.**

"""
