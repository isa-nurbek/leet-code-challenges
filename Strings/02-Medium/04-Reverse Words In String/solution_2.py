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

# =========================================================================================================================== #

# Solution:


# O(n) time | O(n) space - where `n` is the length of the string.
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

# Test Case 3
print(reverse_words_in_string("his      string     has a     lot of   whitespace"))
# Output: "whitespace   of lot     a has     string      his"

# =========================================================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity

1. **Splitting the String into Words:**
   - The loop iterates over each character in the string exactly once.
   - Inside the loop, the operations are constant time (`O(1)`), such as checking
   if a character is a space or appending to the list.
   - Therefore, the time complexity for this part is `O(n)`, where `n` is the length of the string.

2. **Reversing the List of Words:**
   - The `reverse_list` function reverses the list in place.
   - It swaps elements from the start and end of the list, moving towards the center.
   - This operation takes `O(m)` time, where `m` is the number of words in the list.
   - In the worst case, `m` can be proportional to `n` (e.g., if the string consists of single characters
   separated by spaces), so this part is also `O(n)`.

3. **Joining the Words into a String:**
   - The `join` operation concatenates all the words in the list into a single string.
   - This operation takes `O(n)` time because it involves copying each character from the list into the final string.

### Space Complexity

1. **Storing the Words:**
   - The `words` list stores all the words and spaces from the original string.
   - In the worst case, this list could have `O(n)` elements (e.g., if the string consists
   of single characters separated by spaces).
   - Therefore, the space complexity for storing the words is `O(n)`.

2. **Reversing the List:**
   - The `reverse_list` function operates in place and does not use any additional space proportional to the input size.
   - Therefore, the space complexity for reversing the list is `O(1)`.

3. **Joining the Words:**
   - The `join` operation creates a new string that is the same size as the original string.
   - Therefore, the space complexity for joining the words is `O(n)`.

### Summary

- **Time Complexity:** `O(n)`
  - The function processes each character in the string a constant number of times.
  
- **Space Complexity:** `O(n)`
  - The function uses additional space proportional to the size of the input string
  to store the words and the final reversed string.

### Final Answer

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

"""

# =========================================================================================================================== #

# Code Explanation:

"""
This function `reverse_words_in_string(string)` reverses the order of words in a given string while keeping
the spaces intact. Let's go step by step through how it works.

---

## **Function Breakdown**
### **1. `reverse_words_in_string(string)`**
This is the main function that processes the input string.

#### **Step 1: Convert the string into a list of characters**
```
characters = [char for char in string]
```
Strings in Python are immutable, so we first convert the string into a list of characters. This allows us to 
modify the string in place.

#### **Step 2: Reverse the entire string**
```
reverse_list_range(characters, 0, len(characters) - 1)
```
We use the helper function `reverse_list_range()` to reverse the entire string. This means all characters,
including words and spaces, get reversed.

For example:
```
Original string: "AlgoExpert is the best!"
After reversing: "!tseb eht si trepxEoglA"
```

#### **Step 3: Reverse each word individually**
Now, we need to reverse each word back to its original form but in the new order.

```
start_of_word = 0
while start_of_word < len(characters):
    end_of_word = start_of_word

    while end_of_word < len(characters) and characters[end_of_word] != " ":
        end_of_word += 1

    reverse_list_range(characters, start_of_word, end_of_word - 1)
    start_of_word = end_of_word + 1
```
- We iterate over the reversed list and find each word.
- We determine the start and end index of each word.
- We call `reverse_list_range()` on each word to correct its order.
- We move to the next word by skipping the spaces.

**Example Execution**
```
Reversed string: "!tseb eht si trepxEoglA"
Word-by-word reversal:
1. "!tseb" → "best!"
2. "eht" → "the"
3. "si" → "is"
4. "trepxEoglA" → "AlgoExpert"

Final Output: "best! the is AlgoExpert"
```

---

### **2. `reverse_list_range(my_list, start, end)`**
This helper function reverses a portion of a list **in place**.
```
while start < end:
    my_list[start], my_list[end] = my_list[end], my_list[start]
    start += 1
    end -= 1
```
It swaps elements from `start` to `end` progressively until they meet in the middle.

---

## **Edge Case Handling**

### **1. Multiple Spaces Between Words**

For example:
```
reverse_words_in_string("his      string     has a     lot of   whitespace")
```
- The function correctly reverses the entire string first:
  ```
  "whitespace   of lot     a has     string      his"
  ```
- Then it reverses each word while maintaining spaces.

The function **does not remove** extra spaces; it preserves them as they are.

---

This method is efficient and does not require additional space beyond the input list.

### **Final Thoughts**

This is an elegant approach to reversing words in a string while preserving spaces. It efficiently
uses in-place reversal to minimize memory usage.

"""
