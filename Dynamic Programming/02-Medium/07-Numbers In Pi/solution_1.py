# Problem Description:

"""
                                            Numbers In Pi

Given a string representation of the first `n` digits of `Pi` and a list of positive integers (all in string format), write a
function that returns the smallest number of spaces that can be added to the `n` digits of `Pi` such that all resulting numbers
are found in the list of integers.

> Note that a single number can appear multiple times in the resulting numbers.

For example, if `Pi` is `"3141"` and the numbers are `["1", "3", "4"]`, the number `"1"` is allowed to appear twice in the list
of resulting numbers after three spaces are added: `"3 | 1 | 4 | 1"`.

If no number of spaces to be added exists such that all resulting numbers are found in the list of integers, the function should
return `-1`.


## Sample Input:
```
pi = "3141592653589793238462643383279",
numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
```

## Sample Output:
```
2

// "314159265 | 35897932384626433832 | 79"
```

## Optimal Time & Space Complexity:
```
O(n³ + m) time | O(n + m) space - where `n` is the number of digits in `Pi` and `m` is the number of favorite numbers.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n³ + m) time | O(n + m) space
def numbersInPi(pi, numbers):
    # Convert the list of numbers into a set for O(1) lookups
    numbersTable = {number for number in numbers}

    # Start the recursive process from index 0 with an empty cache
    minSpaces = getMinSpaces(pi, numbersTable, 0, {})

    # Return the result (or -1 if no valid split was found)
    return minSpaces if minSpaces != float("inf") else -1


def getMinSpaces(pi, numbersTable, idx, cache):
    # Base case: if we've reached the end of the string, return -1
    # (we'll add 1 to this later, making it 0 spaces for the last number)
    if idx == len(pi):
        return -1

    # If we've already computed the result for this index, return it
    if idx in cache:
        return cache[idx]

    # Initialize minimum spaces to infinity (indicating no valid split found yet)
    minSpaces = float("inf")

    # Try all possible prefixes starting at current index
    for i in range(idx, len(pi)):
        prefix = pi[idx : i + 1]  # Get the substring from idx to i

        # If this prefix is one of our target numbers
        if prefix in numbersTable:
            # Recursively find the minimum spaces for the remaining string
            spacesInSuffix = getMinSpaces(pi, numbersTable, i + 1, cache)

            # Update the minimum spaces if this split leads to a better solution
            # We add 1 because each split adds one space between numbers
            minSpaces = min(minSpaces, spacesInSuffix + 1)

    # Store the computed result in cache before returning
    cache[idx] = minSpaces

    return minSpaces


# Test Case:

pi = "3141592653589793238462643383279"
numbers = [
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79",
]

print(numbersInPi(pi, numbers))
# Output: 2

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

## Time Complexity Analysis

The time complexity of the given algorithm can be analyzed as follows:

1. **Initial Setup**: Converting the `numbers` list into a set (`numbersTable`) takes O(n) time, where n is the number
of elements in `numbers`. This is because set insertion is O(1) on average for each element.

2. **Recursive Function (`getMinSpaces`)**:
   - The function is called recursively for each index in the string `pi` (length m), and the results are memoized using
   `cache` to avoid redundant calculations.
   - For each index `idx`, the function checks all possible prefixes starting at `idx` (i.e., `pi[idx : i + 1]` for `i` from
   `idx` to `m-1`). This leads to O(m) operations per call in the worst case (when no early termination occurs).
   - With memoization, each of the m indices is computed only once, and each computation involves O(m) work (checking all
   possible prefixes). Thus, the total time for the recursive part is O(m²).

3. **Overall Time Complexity**: 
   - The dominant term is O(m²) from the recursive function, and the O(n) from the set creation is negligible if n is small
   compared to m².
   - Thus, the total time complexity is **O(m² + n)**, where m is the length of `pi` and n is the number of elements in `numbers`.

### Space Complexity Analysis

The space complexity is determined by the following components:

1. **Set (`numbersTable`)**: This requires O(n) space to store all the numbers in the input list.

2. **Memoization Cache (`cache`)**: 
   - The cache stores results for each index in `pi`, so it can grow up to O(m) in the worst case (one entry per index).
   - Each cache entry stores an integer (the minimum spaces), so the space per entry is O(1).

3. **Recursive Call Stack**:
   - In the worst case (without memoization), the recursion depth could be O(m) (e.g., when no valid splits are found,
   and the function recurses until `idx == len(pi)`).
   - With memoization, the recursion depth is effectively limited by the cache, so the stack space is O(m).

4. **Additional Space**:
   - The slicing operation (`pi[idx : i + 1]`) creates substrings of `pi`. In Python, strings are immutable, and slicing creates
   new string objects. In the worst case, this could involve O(m²) space (e.g., if all possible substrings are stored temporarily).
   However, in practice, these substrings are short-lived and garbage-collected, so the peak additional space is O(m)
   (for the current prefix being checked).

5. **Overall Space Complexity**:
   - The dominant terms are the set O(n) and the cache O(m).
   - Thus, the total space complexity is **O(m + n)**.

### Summary
- **Time Complexity**: O(m² + n), where m is the length of `pi` and n is the number of elements in `numbers`.
- **Space Complexity**: O(m + n), due to the cache and the set of numbers.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go through the code **step by step** to understand how it works.

---

### 🔍 **Goal:**

You are given:

* A string `pi` (representing digits of π),
* A list of strings `numbers` (substrings allowed to be used).

The goal is:

> To split the string `pi` into a sequence of numbers from the list `numbers`, using as **few splits as possible**, and
return the number of **spaces (splits)** needed.

---

### 🧠 High-Level Idea:

The function finds a **minimal way to segment the `pi` string** using only substrings from the `numbers` list.

* If it's **not possible**, return `-1`.
* If it is, return the **minimum number of splits** needed.

---

### 🔁 Function Breakdown

#### 1. **Top-Level Function**

```
def numbersInPi(pi, numbers):
    numbersTable = {number for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, 0, {})
    return minSpaces if minSpaces != float("inf") else -1
```

* Converts the list `numbers` into a **set** `numbersTable` for **O(1) lookup time**.
* Calls a recursive helper `getMinSpaces` starting at index `0`.
* If a solution is found (`minSpaces != inf`), return it. Otherwise, return `-1`.

---

#### 2. **Recursive Function**

```
def getMinSpaces(pi, numbersTable, idx, cache):
```

##### 🔹 Parameters:

* `pi`: The full pi string.
* `numbersTable`: Set of valid numbers.
* `idx`: Current position in `pi`.
* `cache`: Memoization dictionary to store results for subproblems.

---

#### ✅ Base Case

```
    if idx == len(pi):
        return -1
```

* If you've reached the **end of the string**, you don’t need more spaces.
* Returns `-1` because the final split **doesn't count as a space** (a common trick in this kind of problem).

---

#### ♻️ Memoization

```
    if idx in cache:
        return cache[idx]
```

* If you’ve already computed the answer for this index, return it to avoid recomputation.

---

#### 🔄 Loop to Try Prefixes

```
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx : i + 1]
        if prefix in numbersTable:
            spacesInSuffix = getMinSpaces(pi, numbersTable, i + 1, cache)
            minSpaces = min(minSpaces, spacesInSuffix + 1)
```

* Loop through all substrings starting at `idx`.
* If the current `prefix` is a valid number:

  * Recursively compute `spacesInSuffix` for the rest of the string.
  * Add `1` to account for the current split.
  * Track the **minimum number of splits** found.

---

#### 🧠 Store in Cache

```
    cache[idx] = minSpaces
```

* Store the result before returning it to **speed up future calls**.

---

#### 🔚 Return Result

```
    return minSpaces
```

---

### 🧪 Test Case:

```
pi = "3141592653589793238462643383279"
numbers = [
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79",
]
```

Let’s break down how it finds a result of **2**:

One optimal segmentation:

1. `"314159265"` (from numbers)
2. `"35897932384626433832"` (from numbers)
3. `"79"` (from numbers)

This makes **2 splits**: after the 1st and 2nd segments.

---

### 🔁 Time Complexity

* Worst-case: exponential due to many ways to split.
* But thanks to **memoization**, it's brought down to:

  * **O(n²)** where `n = len(pi)` (all possible substrings),
  * And each state is cached.

---

### ✅ Summary:

This code:

* Tries every valid split of the string,
* Uses memoization to avoid recomputation,
* Minimizes the number of splits (spaces),
* Returns `-1` if no valid split is possible.

---

Let's visualize the **recursive exploration and optimal split** of the string `pi = "3141592653589793238462643383279"` with
the given list of valid `numbers`.

We want to split `pi` into substrings that are in the list, using the **fewest number of spaces**.

---

### 🧪 Given:

```
pi:      3141592653589793238462643383279
numbers: {
    "314159265358979323846",
    "26433",
    "8",
    "3279",
    "314159265",
    "35897932384626433832",
    "79"
}
```

---

### ✅ ASCII Visualization of Optimal Path:

```
3141592653589793238462643383279
|         |                     |
314159265 35897932384626433832 79
```

### ➕ Explanation:

* `314159265` — in numbers ✅
* `35897932384626433832` — in numbers ✅
* `79` — in numbers ✅

We insert **2 spaces**, which results in **3 substrings**, and that's the minimum possible.

---

### 🔁 How recursion explores:

The recursive function tries to match prefixes from left to right, like this:

```
idx = 0
Try: 3        ❌ Not in list
Try: 31       ❌
Try: 314      ❌
...
Try: 314159265 ✅ → Recurse on idx = 9

    idx = 9
    Try: 3            ❌
    Try: 35           ❌
    ...
    Try: 35897932384626433832 ✅ → Recurse on idx = 30

        idx = 30
        Try: 7     ❌
        Try: 79    ✅ → Recurse on idx = 32

            idx = 32 → End of string, return -1 (no space needed here)
```

Then unwind:

```
spacesInSuffix = -1 → +1 → +1 → total = 2 spaces
```

---

### 🧠 Final Result:

```
print(numbersInPi(pi, numbers))  # Output: 2
```

"""
