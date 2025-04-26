# Problem Description:

"""

                                            Generate Div Tags

Write a function that takes in a positive integer `number_of_tags` and returns a list of all the valid strings that you can generate
with that number of matched `<div></div>` tags.

A string is valid and contains matched `<div></div>` tags if for every opening tag `<div>`, there's a closing tag `</div>` that
comes after the opening tag and that isn't used as a closing tag for another opening tag. Each output string should contain exactly
`number_of_tags` opening tags and `number_of_tags` closing tags.

For example, `given number_of_tags = 2`, the valid strings to return would be: `["<div></div><div></div>", "<div><div></div></div>"]`.

Note that the output strings don't need to be in any particular order.


## Sample Input
```
number_of_tags = 3
```

## Sample Output
```
[
    "<div><div><div></div></div></div>",
    "<div><div></div><div></div></div>",
    "<div><div></div></div><div></div>",
    "<div></div><div><div></div></div>",
    "<div></div><div></div><div></div>",
]
// The strings could be ordered differently.
```

## Optimal Time & Space Complexity:
```
O(4ⁿ / √n) time | O(n · 4ⁿ / √n) space - where `n` is the input number.
```
"""

# =========================================================================================================================== #

# Solution:


# O(4ⁿ / √n) time | O(n · 4ⁿ / √n) space
def generate_div_tags(number_of_tags):
    """
    Generates all possible valid combinations of a given number of div tags.

    Args:
        number_of_tags (int): The number of div tag pairs to generate

    Returns:
        list: A list of strings containing all valid div tag combinations
    """
    matched_div_tags = []
    # Start the recursive generation with full count of opening and closing tags needed
    generate_div_tags_from_prefix(number_of_tags, number_of_tags, "", matched_div_tags)
    return matched_div_tags


def generate_div_tags_from_prefix(
    opening_tags_needed, closing_tags_needed, prefix, result
):
    """
    Recursively generates valid div tag combinations by building them character by character.

    The approach uses backtracking to explore all possible valid sequences where:
    1. We never close a tag that hasn't been opened
    2. We end with all tags properly closed

    Args:
        opening_tags_needed (int): How many more opening <div> tags we can add
        closing_tags_needed (int): How many more closing </div> tags we can add
        prefix (str): The current string being built
        result (list): Accumulator for valid complete strings
    """

    # Base case: all tags have been properly opened and closed
    if closing_tags_needed == 0:
        result.append(prefix)
        return

    # If we can still open more tags (more <div> available)
    if opening_tags_needed > 0:
        # Add an opening tag and recurse, decreasing opening tags needed
        new_prefix = prefix + "<div>"
        generate_div_tags_from_prefix(
            opening_tags_needed - 1, closing_tags_needed, new_prefix, result
        )

    # We can add a closing tag if we have unclosed opening tags
    # (opening_tags_needed < closing_tags_needed means we have open tags to close)
    if opening_tags_needed < closing_tags_needed:
        # Add a closing tag and recurse, decreasing closing tags needed
        new_prefix = prefix + "</div>"
        generate_div_tags_from_prefix(
            opening_tags_needed, closing_tags_needed - 1, new_prefix, result
        )


# Test Cases:

print(generate_div_tags(3))
# Output:
"""
[
    "<div><div><div></div></div></div>",
    "<div><div></div><div></div></div>",
    "<div><div></div></div><div></div>",
    "<div></div><div><div></div></div>",
    "<div></div><div></div><div></div>",
] 
"""

print(generate_div_tags(1))
# Output: ["<div></div>"]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### 🔍 Time Complexity

The total number of valid combinations of `n` pairs of div tags is given by the **Catalan number**:


    Cₙ = 1 / n + 1 (2n / n)


So, for each of those combinations, you're constructing a string of length `5n` for each `<div>` and `6n` for each `</div>`,
roughly O(n) characters per result.

- Number of valid strings = **O(Cₙ)**  
- Time to construct each string = **O(n)**  
- Recursive branching structure also explores all valid states, each state doing constant work aside from recursion.

So the time complexity is approximately: O(4ⁿ / √n)

---

### 🧠 Space Complexity

There are two main components:

1. **Call stack (recursion depth):** At most `2n` recursive calls deep  
   → **O(n)**

2. **Result list:** Holds `Cₙ` strings, each of length O(n)  
   → **O(n · Cₙ) = O(n · 4ⁿ / √n)**

**👉 Total space complexity:** O(n · 4ⁿ / √n)

### Summary:
- **Time Complexity**: O(4ⁿ / √n)
- **Space Complexity**: O(n · 4ⁿ / √n)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code generates **all valid combinations of HTML `<div>` tags** for a given number. Each combination must be *well-formed*,
meaning every `<div>` has a matching `</div>`, and tags are nested properly (like in valid HTML).

---

### 🔍 What is the Goal?

Given a number `n`, we want to generate all valid strings containing exactly `n` opening `<div>` tags and `n` closing `</div>` tags,
where:

- Every opening `<div>` has a matching `</div>`.
- The tags are properly nested like parentheses in an arithmetic expression.

---

### 📘 Analogy: Parentheses Generation

This is **identical in structure** to the classic _"Generate Valid Parentheses"_ problem. Instead of `"("` and `")"`, we're
using `"<div>"` and `"</div>"`.

---

### 🧠 Core Idea: Backtracking

We use **recursion and backtracking** to try out all valid sequences by adding one tag at a time, ensuring at every step that
we maintain validity:
- You can't close more tags than you've opened.
- You can only add a closing tag if there's already an unmatched opening tag.

---

### 🧱 Code Breakdown

#### 1. `generate_div_tags(number_of_tags)`

This is the main function that sets things up.

```
def generate_div_tags(number_of_tags):
    matched_div_tags = []
    generate_div_tags_from_prefix(number_of_tags, number_of_tags, "", matched_div_tags)
    return matched_div_tags
```

- `number_of_tags`: total number of `<div>` tags to be used (also same number of `</div>` tags).
- `matched_div_tags`: list that will collect all valid sequences.
- It calls the helper recursive function `generate_div_tags_from_prefix`.

---

#### 2. `generate_div_tags_from_prefix(opening_tags_needed, closing_tags_needed, prefix, result)`

This recursive function builds up valid sequences step-by-step.

Parameters:
- `opening_tags_needed`: how many opening tags `<div>` are still left to add.
- `closing_tags_needed`: how many closing tags `</div>` are still left to add.
- `prefix`: the string built so far.
- `result`: reference to the list that will hold all complete valid combinations.

Let’s break down the logic:

##### ✅ If we still need opening tags:
```
if opening_tags_needed > 0:
```
We can always add an opening tag if we haven’t used all of them yet:
```
new_prefix = prefix + "<div>"
generate_div_tags_from_prefix(
    opening_tags_needed - 1, closing_tags_needed, new_prefix, result
)
```

##### ✅ If we can legally add a closing tag:
```
if opening_tags_needed < closing_tags_needed:
```
Only add a closing tag if there's at least one unmatched `<div>` tag. That is, more opening tags have been used than closing ones.
```
new_prefix = prefix + "</div>"
generate_div_tags_from_prefix(
    opening_tags_needed, closing_tags_needed - 1, new_prefix, result
)
```

##### 🎯 Base Case – no tags left to add:
```
if closing_tags_needed == 0:
    result.append(prefix)
```
Once both opening and closing tags are used up, add the complete string to the result list.

---

### 🧪 Example: `generate_div_tags(1)`

Only one valid possibility:
```
["<div></div>"]
```

---

### 🧪 Example: `generate_div_tags(3)`

Valid outputs (exactly 3 `<div>`s and 3 `</div>`s, properly nested):

1. `<div><div><div></div></div></div>`
2. `<div><div></div><div></div></div>`
3. `<div><div></div></div><div></div>`
4. `<div></div><div><div></div></div>`
5. `<div></div><div></div><div></div>`

---

### 🧠 Time Complexity

This is a **Catalan Number** problem:
- Number of valid sequences = Catalan(n)
- Catalan(n) = (2n)! / ((n+1)! * n!) → grows exponentially.

So, **Time Complexity = O(Catalan(n))**


### Space Complexity:

O(Catalan(n) * n) - total
O(n) - for recursion stack

---

Here's an ASCII diagram showing the **recursion tree** for `generate_div_tags(2)`. It demonstrates how each step adds either
`<div>` or `</div>`, and how valid sequences are formed:

---

### 🌳 **Recursion Tree for `generate_div_tags(2)`**

```
Start: ""
|
├── Add <div> → "<div>"
|   |
|   ├── Add <div> → "<div><div>"
|   |   |
|   |   ├── Add </div> → "<div><div></div>"
|   |   |   |
|   |   |   └── Add </div> → "<div><div></div></div>" ✅
|   |
|   └── Add </div> → "<div></div>"
|       |
|       └── Add <div> → "<div></div><div>"
|           |
|           └── Add </div> → "<div></div><div></div>" ✅
```

---

### ✅ Final Valid Outputs for `n=2`

1. `<div><div></div></div>`
2. `<div></div><div></div>`

---

This tree shows how the function explores all valid sequences **by tracking available opening and closing tags** and only taking
valid paths. Each branch is a function call, and each leaf where both counts reach zero is a valid sequence.

"""
