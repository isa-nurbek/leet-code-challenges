# Description:

"""
                                       Reverse Words In String

Write a function that takes in a string of words separated by one or more whitespaces and returns a string that
has these words in reverse order. For example, given the string `"tim is great"`, your function should return `"great is tim"`.

For this problem, a word can contain special characters, punctuation, and numbers. The words in the string will be
separated by one or more whitespaces, and the reversed string must contain the same whitespaces as the original string.
For example, given the string `"whitespaces    4"` you would be expected to return `"4    whitespaces"`.

Note that you're not allowed to to use any built-in `split` or `reverse` methods/functions. However, you are allowed
to use a built-in `join` method/function.

Also note that the input string isn't guaranteed to always contain words.


## Sample Input:
```
string = "AlgoExpert is the best!"
```

## Sample Output:
```
"best! the is AlgoExpert"
```

## Optimal Time & Space Complexity:
```
`O(n)` time | `O(n)` space - where `n` is the length of the string.
```

"""

# =============================================================================================== #

# Solution


# `O(n)` time | `O(n)` space - where `n` is the length of the string.
def reverse_words_in_string(string):
    # Initialize an empty list to store individual words and spaces
    words = []
    # Track the starting index of the current word
    start_of_word = 0

    # Iterate through each character in the string
    for idx in range(len(string)):
        character = string[idx]

        # If the current character is a space, it means we've reached the end of a word
        if character == " ":
            # Append the word (from start_of_word to idx) to the words list
            words.append(string[start_of_word:idx])
            # Update start_of_word to the current index (start of the next word or space)
            start_of_word = idx
        # If the character at start_of_word is a space, it means we've encountered a new word
        elif string[start_of_word] == " ":
            # Append the space to the words list
            words.append(" ")
            # Update start_of_word to the current index (start of the new word)
            start_of_word = idx

    # Append the last word (or space) to the words list
    words.append(string[start_of_word:])

    # Reverse the order of words in the list
    reverse_list(words)
    # Join the reversed list into a single string and return it
    return "".join(words)


def reverse_list(my_list):
    # Initialize two pointers: start at the beginning and end at the end of the list
    start, end = 0, len(my_list) - 1

    # Swap elements from the start and end until the pointers meet in the middle
    while start < end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        # Move the start pointer forward
        start += 1
        # Move the end pointer backward
        end -= 1


# Test Case 1
print(reverse_words_in_string("AlgoExpert is the best!"))
# Output: "best! the is AlgoExpert"

# Test Case 2
print(reverse_words_in_string("Reverse These Words"))
# Output: "Words These Reverse"

# Test Case 2
print(reverse_words_in_string("his      string     has a     lot of   whitespace"))
# Output: "whitespace   of lot     a has     string      his"

# =============================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity

1. **Splitting the String into Words**: The loop that iterates through the string to split it into words
runs in `O(n)` time, where `n` is the length of the string. This is because each character is processed once.

2. **Reversing the List of Words**: The `reverse_list` function reverses the list of words in place. This
operation takes `O(m)` time, where `m` is the number of words in the list. In the worst case, `m` can be
proportional to `n` (e.g., when each word is a single character), so this step is also `O(n)`.

3. **Joining the Words into a String**: The `join` operation to concatenate the reversed list of words into
a single string takes `O(n)` time, as it needs to iterate through all characters in the list.

**Overall Time Complexity**: `O(n)`, where `n` is the length of the input string.


### Space Complexity

1. **Storing the Words**: The `words` list stores all the words and spaces from the input string. In the
worst case, this list can have `O(n)` elements (e.g., when each word is a single character).

2. **Reversing the List**: The `reverse_list` function operates in place and does not use additional space
proportional to the input size.

3. **Output String**: The final output string requires `O(n)` space.

**Overall Space Complexity**: `O(n)`, where `n` is the length of the input string.

### Summary

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

"""

# Code Explanation:

"""
This function, `reverse_words_in_string`, reverses the order of words in a given string while preserving
spaces between them. Let's break it down step by step.

---

## **Understanding the Code**

### **1. Function: `reverse_words_in_string(string)`**
This function processes the input string and extracts words while keeping spaces intact. Then, it reverses
the extracted elements and joins them back into a string.

#### **Step 1: Initialize Variables**
```
words = []
start_of_word = 0
```
- `words`: A list to store words and spaces separately.
- `start_of_word`: Keeps track of the starting index of the current word or space.

#### **Step 2: Iterate Over the String**
```
for idx in range(len(string)):
    character = string[idx]
```
- This loop iterates over every character in the input string.
- The variable `idx` represents the current character index.

#### **Step 3: Extract Words and Spaces**
```
if character == " ":
    words.append(string[start_of_word:idx])
    start_of_word = idx
```
- If a space `" "` is encountered, the substring from `start_of_word` to `idx` (which represents a word)
is added to the `words` list.
- `start_of_word` is updated to `idx`, indicating the beginning of a space sequence.

```
elif string[start_of_word] == " ":
    words.append(" ")
    start_of_word = idx
```
- If `start_of_word` is a space, that means we are entering a new word after spaces.
- It appends `" "` to the list separately to preserve spaces.
- Then, `start_of_word` is updated to the index of the first character of the next word.

#### **Step 4: Add the Last Word or Space**
```
words.append(string[start_of_word:])
```
- At the end of the loop, the last word or space sequence (from `start_of_word` to the end of the string)
is appended to the `words` list.

---

### **2. Function: `reverse_list(my_list)`**
This helper function reverses the order of elements in a list using a two-pointer approach.

#### **Step 1: Initialize Pointers**
```
start, end = 0, len(my_list) - 1
```
- `start`: Points to the first element.
- `end`: Points to the last element.

#### **Step 2: Swap Elements**
```
while start < end:
    my_list[start], my_list[end] = my_list[end], my_list[start]
    start += 1
    end -= 1
```
- Swap the elements at the `start` and `end` positions.
- Move `start` forward and `end` backward.
- This continues until `start` is greater than or equal to `end`, meaning the list is fully reversed.

---

### **3. Returning the Final String**
```
reverse_list(words)
return "".join(words)
```
- The `words` list (which contains words and spaces) is reversed.
- `"".join(words)` converts the list back into a string while maintaining spacing.

---

## **Example Walkthrough**

### **Example 1**
```
reverse_words_in_string("AlgoExpert is the best!")
```

**Step 1: Extract Words and Spaces**
```
words = ['AlgoExpert', ' ', 'is', ' ', 'the', ' ', 'best!']
```

**Step 2: Reverse the List**
```
words = ['best!', ' ', 'the', ' ', 'is', ' ', 'AlgoExpert']
```

**Step 3: Join the List**
```
"best! the is AlgoExpert"
```

---

### **Example 2**
```
reverse_words_in_string("his      string     has a     lot of   whitespace")
```

**Step 1: Extract Words and Spaces**
```
words = ['his', '      ', 'string', '     ', 'has', ' ', 'a', '     ', 'lot', ' ', 'of', '   ', 'whitespace']
```

**Step 2: Reverse the List**
```
words = ['whitespace', '   ', 'of', ' ', 'lot', '     ', 'a', ' ', 'has', '     ', 'string', '      ', 'his']
```

**Step 3: Join the List**
```
"whitespace   of lot     a has     string      his"
```

This output maintains all spaces from the original string while reversing only the words.

---

## **Key Takeaways**

1. **Preserves spaces**: Spaces are stored separately and kept intact after reversing.
2. **Two-pass approach**:
   - First pass: Extract words and spaces.
   - Second pass: Reverse the order.
3. **Efficient reversal**: The `reverse_list` function swaps elements in `O(n)` time complexity.

"""
