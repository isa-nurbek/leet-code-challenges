# Problem Description:

"""

                                            Product Sum

Write a function that takes in a "special" array and returns its product sum.

A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a "special"
array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth.

The depth of a "special" array is how far nested it is. For instance, the depth of `[]` is `1`; the depth of the inner array
in `[[]]` is `2`; the depth of the innermost array in `[[[]]]` is `3`.

Therefore, the product sum of `[x, y]` is `x + y`; the product sum of `[x, [y, z]]` is `x + 2 * (y + z)`; the product sum of
`[x, [y, [z]]]` is `x + 2 * (y + 3z)`.


## Sample Input
```
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
```

## Sample Output
```
12 // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
```

## Optimal Time & Space Complexity:
```
O(n) time | O(d) space - where `n` is the total number of elements in the array, including sub-elements,
and `d` is the greatest depth of "special" arrays in the array.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(d) space
def product_sum(array, multiplier=1):
    # Initialize sum to accumulate all elements' values
    sum = 0

    # Iterate through each element in the array
    for element in array:
        # If the element is a list (nested array), recursively calculate its product sum
        if type(element) is list:
            # For nested arrays, increment the multiplier (depth) by 1
            sum += product_sum(element, multiplier + 1)
        else:
            # For regular numbers, simply add them to the sum
            sum += element

    # Multiply the accumulated sum by the current depth level
    return sum * multiplier


# Test Cases:

print(product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
# Output: 12

print(product_sum([1, 2, 3, 4, 5]))
# Output: 15

print(product_sum([[1, 2], 3, [4, 5]]))
# Output: 27

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:

- **Definition**: The function calculates a "product sum" of a special array (which may contain nested lists) where
each element is summed, but nested lists contribute to the sum multiplied by their depth level.
- **Approach**: The function processes each element of the array exactly once. For each element, it checks whether
the element is a list or not. 
  - If it's a list, the function recursively processes that list with an incremented `multiplier`.
  - If it's not a list, the element is added to the sum directly.
- **Recurrence Relation**: If we denote `n` as the total number of elements in the array (including all nested elements),
the time complexity can be expressed as `O(n)`, because each element is processed exactly once, regardless of its depth.

- **Conclusion**: The time complexity is **O(n)**, where `n` is the total number of elements (including all nested elements).

### Space Complexity:

- **Definition**: The space complexity is determined by the maximum depth of the recursion stack.
- **Approach**: The function uses recursion to handle nested lists. The recursion depth is equal to the maximum depth of
nesting in the array. For example:
  - `[1, 2, [3, [4]]]` has a maximum depth of 3 (the element `4` is nested 3 levels deep).
- **Auxiliary Space**: For each recursive call, a new stack frame is created, but no additional data structures are used that
grow with the input size.
- **Conclusion**: The space complexity is **O(d)**, where `d` is the maximum depth of nesting in the array. In the worst case, if
the array is a linear chain of nested lists (e.g., `[[[[]]]`), then `d = n`, making the space complexity **O(n)** in the worst case.

### Summary:
- **Time Complexity**: **O(n)** (where `n` is the total number of elements, including all nested elements).
- **Space Complexity**: **O(d)** (where `d` is the maximum depth of nesting, with a worst-case of **O(n)** if the array
is deeply nested).

This analysis assumes that checking `type(element) is list` and arithmetic operations are constant-time operations,
which is reasonable in Python.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go through the code step by step and understand how the `product_sum` function works.

### 🔍 **Function Purpose:**

The function `product_sum` **recursively sums a special array** that may contain **nested arrays (lists within lists)**. The key
point is that the **deeper** the nesting level, the **more weight (multiplier)** that sub-array's sum contributes to the total sum.

---

### 📌 **Function Definition:**
```
def product_sum(array, multiplier=1):
```
- **`array`**: The input list which may include both integers and nested lists.
- **`multiplier`**: Tracks how deep we are in the nesting. It starts at 1 for the top level and increases by 1 with each level
of nesting.

---

### ⚙️ **Inside the function:**

```
sum = 0
```
- Initialize a local variable `sum` to keep the running total.

```
for element in array:
```
- Loop through every element in the input array.

```
if type(element) is list:
    sum += product_sum(element, multiplier + 1)
```
- If the element is a **list**, it's a **nested structure**. So we **call `product_sum` recursively** on this sub-array.
- We increase the `multiplier` by 1 because we're one level deeper.

```
else:
    sum += element
```
- If the element is an **integer**, simply add it to the running total.

```
return sum * multiplier
```
- Once all elements are processed, return the `sum` multiplied by the current level's multiplier.

---

### 🔢 **Example 1:**
```
product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])
```

Let’s break it down step-by-step:

**Level 1 (multiplier = 1):**
- Elements: 5, 2, [7, -1], 3, [6, [-13, 8], 4]
- Direct integers: 5 + 2 + 3 = 10
- [7, -1] → Recurse into level 2
- [6, [-13, 8], 4] → Recurse into level 2

---

**Level 2 (multiplier = 2):**
- [7, -1] → 7 + (-1) = 6 → 6 × 2 = 12
- [6, [-13, 8], 4] → 
  - 6 and 4 → sum = 6 + 4 = 10
  - [-13, 8] → Recurse into level 3

---

**Level 3 (multiplier = 3):**
- [-13, 8] → -13 + 8 = -5 → -5 × 3 = -15

Back to level 2:
- sum for [6, [-13, 8], 4] = 10 + (-15) = -5 → -5 × 2 = -10

---

Final sum at level 1:
- Direct elements: 10
- From [7, -1] = 12
- From [6, [-13, 8], 4] = -10

→ Total = 10 + 12 + (-10) = **12**

✅ Output: `12`

---

### ✅ **Other Examples:**

#### Example 2:
```
product_sum([1, 2, 3, 4, 5])
```
No nested lists, so:
1 + 2 + 3 + 4 + 5 = 15  
→ 15 × 1 = ✅ `15`

---

#### Example 3:
```
product_sum([[1, 2], 3, [4, 5]])
```

**Level 1 (multiplier = 1):**
- [1, 2] → Level 2 = 1 + 2 = 3 → 3 × 2 = 6
- 3 → stays as 3
- [4, 5] → Level 2 = 4 + 5 = 9 → 9 × 2 = 18

Total: 6 + 3 + 18 = ✅ `27`

---

### 💡 Summary:

- The function **recursively computes a weighted sum**.
- **Deeper nested lists are multiplied** by a higher `multiplier`.
- This is similar to a depth-weighted sum.

---

Let’s do a **visual breakdown** of this input:

```
product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])
```

We’ll show the **nesting levels** like a tree and annotate each level with its multiplier and intermediate sums.

### 🌳 **Visual Tree Breakdown**

```
Level 1 (multiplier = 1)
└── [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
     ├── 5                         → +5
     ├── 2                         → +2
     ├── [7, -1]         (Level 2, multiplier = 2)
     │    ├── 7                   → +7
     │    └── -1                  → -1
     │    => subtotal = 6 × 2     → +12
     ├── 3                         → +3
     └── [6, [-13, 8], 4] (Level 2, multiplier = 2)
          ├── 6                   → +6
          ├── [-13, 8]   (Level 3, multiplier = 3)
          │     ├── -13          → -13
          │     └── 8            → +8
          │     => subtotal = (-5) × 3 → -15
          └── 4                   → +4
          => subtotal = (6 + -15 + 4) = -5 × 2 → -10

Final Calculation:
→ Level 1: 5 + 2 + 3 = 10
→ Level 2: +12 (from [7, -1]) + (-10) (from [6, [-13, 8], 4])
→ Total = 10 + 12 - 10 = ✅ **12**
```

---

### 🧠 Conceptual Analogy:
You can think of each list as a **folder** that contains either:
- Numbers (add them directly), or
- Other folders (go inside, sum their contents, and multiply that sum based on how deep you are).

"""
