# Problem Description:

"""

                                            Permutations

Write a function that takes in an array of unique integers and returns an array of all `permutations` of those integers in
no particular order.

If the input array is empty, the function should return an empty array.


## Sample Input
```
array = [1, 2, 3]
```

## Sample Output
```
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Optimal Time & Space Complexity:
```
O(n * n!) time | O(n * n!) space - where `n` is the length of the input array.
```
"""

# =========================================================================================================================== #

# Solution:


# Upper Bound: O(n² * n!) time | O(n * n!) space
# Roughly: O(n * n!) time | O(n * n!) space
def get_permutations(array):
    """Main function to get all permutations of an array.

    Args:
        array: The input array to generate permutations for

    Returns:
        A list of all possible permutations of the input array
    """
    permutations = []  # This will store all the permutations we generate
    permutations_helper(array, [], permutations)  # Start the recursive process
    return permutations


def permutations_helper(array, current_permutation, permutations):
    """Recursive helper function to generate permutations.

    Args:
        array: The remaining elements to permute
        current_permutation: The permutation being built in the current recursion path
        permutations: The list that accumulates all complete permutations
    """
    # Base case: if array is empty
    if not len(array):
        # Add the completed permutation to our results
        permutations.append(current_permutation)
    else:
        # Recursive case: build permutations by choosing each remaining element
        for i in range(len(array)):
            # Create new array without the current element (array[i])
            new_array = array[:i] + array[i + 1 :]

            # Add current element to the permutation we're building
            new_permutation = current_permutation + [array[i]]

            # Recurse with the remaining elements and updated permutation
            permutations_helper(new_array, new_permutation, permutations)


# Test Cases:

print(get_permutations([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

print(get_permutations([1]))
# Output: [[1]]

print(get_permutations([]))
# Output: [[]]

# =========================================================================================================================== #

# Big O Analysis:

"""

## Time and Space Complexity Analysis

### Time Complexity:

The algorithm generates all permutations of an input array. For an array of size `n`, there are `n!` (n factorial) permutations.

1. **Base Case**: When the array is empty, it adds the current permutation to the result list (`permutations`). This operation
is `O(1)` per permutation, but since there are `n!` permutations, this contributes `O(n!)` in total.
2. **Recursive Case**: For each element in the array, the algorithm:
   - Creates a new array without the current element (`array[:i] + array[i + 1:]`), which takes `O(n)` time (since slicing and
   concatenating lists is linear).
   - Creates a new permutation by appending the current element (`current_permutation + [array[i]]`), which also takes `O(n)` time
   (since appending to a list is amortized `O(1)`, but creating a new list is `O(n)`).
   - Makes a recursive call with the new array and new permutation.

At each level of recursion, the work done is proportional to the size of the current array. The recursion tree has `n` levels
(since the array shrinks by 1 element at each level), and at the `k-th` level, there are `n! / (n - k)!` nodes (each representing
a partial permutation). The total work is the sum over all levels of the work done at each level, which is `O(n * n!)`.

Thus, the **time complexity is `O(n * n!)`**.

### Space Complexity:

The space complexity is determined by:
1. **Output Space**: The `permutations` list stores all `n!` permutations, each of size `n`, so this takes `O(n * n!)` space.
2. **Recursion Stack**: The maximum depth of the recursion is `n` (since the array shrinks by 1 element at each level). At each
level, the algorithm creates new arrays and permutations, but these are not all stored simultaneously (they are created and
discarded as the recursion proceeds). The recursion stack itself uses `O(n)` space.
3. **Auxiliary Space**: The `current_permutation` and `new_array` are temporary and take `O(n)` space at each level, but they
are not all stored simultaneously. The total auxiliary space is `O(n)` (dominated by the recursion stack).

Thus, the **space complexity is `O(n * n!)`** (dominated by the output storage).

### Summary:
- **Time Complexity**: `O(n * n!)` (since we generate `n!` permutations, and each permutation takes `O(n)` time to construct).
- **Space Complexity**: `O(n * n!)` (to store all permutations, each of size `n`). The recursion stack and auxiliary space
are `O(n)`, which is dominated by the output.

This is optimal for generating all permutations, as the output itself is of size `n * n!`.

"""


"""
Let's walk through your `get_permutations` function step by step and break it down in detail.

### **Goal:**
Generate all **permutations** of a given list of elements.

A **permutation** is a rearrangement of the elements in a list. For example, the permutations of `[1, 2, 3]` are:

```
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
```

---

### **Function Structure:**

```
def get_permutations(array):
    permutations = []
    permutations_helper(array, [], permutations)
    return permutations
```

- `array`: The input list whose permutations we want to generate.
- `permutations`: A list that will store all the final permutations.
- `permutations_helper`: A recursive helper function that does the actual work.

---

### **Helper Function:**

```
def permutations_helper(array, current_permutation, permutations):
    if not len(array):
        permutations.append(current_permutation)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i + 1 :]
            new_permutation = current_permutation + [array[i]]
            permutations_helper(new_array, new_permutation, permutations)
```

Let’s break this down.

---

### 🔁 **Recursive Idea:**

1. **Base Case:**
```
if not len(array):
    permutations.append(current_permutation)
```
- This means: "If there are no more elements left in the input `array` *and* `current_permutation` is not empty, we’ve built
a complete permutation."
- We then add `current_permutation` to the final `permutations` list.

---

2. **Recursive Case:**
```
for i in range(len(array)):
    new_array = array[:i] + array[i + 1 :]
    new_permutation = current_permutation + [array[i]]
    permutations_helper(new_array, new_permutation, permutations)
```

- Loop through each element in the array:
    - Choose one element (`array[i]`)
    - Remove it from the array: `new_array = array[:i] + array[i+1:]`
        - For example, if `array = [1,2,3]` and `i = 0`, then `new_array = [2,3]`
    - Add it to the current permutation: `new_permutation = current_permutation + [array[i]]`
    - Recurse with the smaller array and the updated permutation.

---

### 🧠 Example Walkthrough: `get_permutations([1, 2])`

Let’s see what happens step-by-step:

1. First call:  
   `array = [1, 2]`, `current_permutation = []`

2. Loop starts:
   - **i = 0**:
     - Take `1`
     - `new_array = [2]`, `new_permutation = [1]`
     - Recurse

3. Inside recursion:
   - `array = [2]`, `current_permutation = [1]`
   - **i = 0**:
     - Take `2`
     - `new_array = []`, `new_permutation = [1, 2]`
     - Recurse

4. Inside recursion:
   - `array = []`, `current_permutation = [1, 2]`
   - Base case met → add `[1, 2]` to permutations

5. Backtrack, now **i = 1** in step 2:
   - Take `2`
   - `new_array = [1]`, `new_permutation = [2]`
   - Recurse → leads to `[2, 1]`

---

### ✅ Output:

```
print(get_permutations([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

Each time, it picks an element, removes it from the list, builds up a permutation, and continues recursively until the permutation is complete.

---

Let's visualize how the recursive function works step-by-step for a small input, like `[1, 2, 3]`.

We'll show the **call stack** as a tree, where each level is a recursive call and we track how permutations are built.  

---

### Initial Call:
```
get_permutations([1, 2, 3])
```
This calls:
```
permutations_helper([1, 2, 3], [], [])
```

Let’s visualize this as a tree:

---

### 📈 Recursive Tree for `[1, 2, 3]`:

Each node shows:  
`array`, `current_permutation`

```
                          [1,2,3], []
                         /     |     \
                      /        |        \
          [2,3],[1]  [1,3],[2]  [1,2],[3]
           /    \       /   \       /   \
        [3],[1,2] [2],[1,3] [3],[2,1] [1],[2,3] [2],[3,1] [1],[3,2]
          |         |         |         |         |         |
         [],[1,2,3] [],[1,3,2] [],[2,1,3] [],[2,3,1] [],[3,1,2] [],[3,2,1]
```

---

### 🧠 How It Works:

#### Level 0 (start):
- Start with `[1,2,3]`, `[]`

#### Level 1 (choose first element):
- Pick `1`: Remaining `[2,3]`, New permutation `[1]`
- Pick `2`: Remaining `[1,3]`, New permutation `[2]`
- Pick `3`: Remaining `[1,2]`, New permutation `[3]`

#### Level 2 (choose second element):
- If you picked `1` → `[2,3]`, `[1]`:
  - Pick `2`: → `[3]`, `[1,2]`
  - Pick `3`: → `[2]`, `[1,3]`

...and so on, until the array is empty and the current permutation is full.

---

### ✅ When base case is hit:

When `array == []`, for example:
```
permutations_helper([], [1, 2, 3], permutations)
```

Now `[1,2,3]` is a full permutation → it gets added to the result list.

---

### Final Result:
```
[
 [1, 2, 3],
 [1, 3, 2],
 [2, 1, 3],
 [2, 3, 1],
 [3, 1, 2],
 [3, 2, 1]
]
```

"""
