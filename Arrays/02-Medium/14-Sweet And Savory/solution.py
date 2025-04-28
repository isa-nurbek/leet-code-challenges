# Problem Description:

"""

                                                # Sweet And Savory

You're hosting an event at a food festival and want to showcase the best possible pairing of two dishes from the festival that
complement each other's flavor profile.

Each dish has a flavor profile represented by an integer. A negative integer means a dish is sweet, while a positive integer
means a dish is savory. The absolute value of that integer represents the intensity of that flavor. For example, a flavor profile
of `-3` is slightly sweet, one of `-10` is extremely sweet, one of `2` is mildly savory, and one of `8` is significantly savory.

You're given an array of these dishes and a target combined flavor profile. Write a function that returns the best possible pairing
of two dishes (the pairing with a total flavor profile that's closest to the target one). Note that this pairing must include one
sweet and one savory dish. You're also concerned about the dish being too savory, so your pairing should never be more savory than
the target flavor profile.

All dishes will have a positive or negative flavor profile; there are no dishes with a 0 value. For simplicity, you can assume that
there will be at most one best solution. If there isn't a valid solution, your function should return `[0, 0]`. The returned array
should be sorted, meaning the sweet dish should always come first.


## Sample Input:
```
dishes = [-3, -5, 1, 7]
target = 8
```

## Sample Output:
```
[-3, 7] 

// The combined profile of 4 is closest without going over
```

## Optimal Time & Space Complexity:
```
O(n * log(n)) time | O(n) space - where `n` is number of dishes.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * log(n)) time | O(n) space
def sweet_and_savory(dishes, target):
    # Separate the dishes into sweet (negative values) and savory (positive values)
    # Sort sweet dishes in ascending order of their absolute values (closest to zero first)
    sweet_dishes = sorted([dish for dish in dishes if dish < 0], key=abs)

    # Sort savory dishes in ascending order (smallest positive first)
    savory_dishes = sorted([dish for dish in dishes if dish > 0])

    # Initialize the best_pair to store the best combination of sweet and savory dishes
    best_pair = [0, 0]

    # Initialize the best_difference to store the smallest difference between the sum and the target
    best_difference = float("inf")

    # Initialize pointers for sweet_dishes and savory_dishes
    sweet_index, savory_index = 0, 0

    # Use a two-pointer technique to find the best pair
    while sweet_index < len(sweet_dishes) and savory_index < len(savory_dishes):
        # Calculate the current sum of the sweet and savory dishes at the current indices
        current_sum = sweet_dishes[sweet_index] + savory_dishes[savory_index]

        # Check if the current sum is less than or equal to the target
        if current_sum <= target:
            # Calculate the difference between the target and the current sum
            current_difference = target - current_sum

            # If this difference is smaller than the best_difference found so far,
            # update the best_difference and best_pair
            if current_difference < best_difference:
                best_difference = current_difference
                best_pair = [sweet_dishes[sweet_index], savory_dishes[savory_index]]

            # Move the savory_index pointer to the right to try a larger savory dish
            savory_index += 1
        else:
            # If the current sum is greater than the target, move the sweet_index pointer
            # to the right to try a smaller sweet dish (since sweet dishes are negative)
            sweet_index += 1

    # Return the best pair of sweet and savory dishes that sum closest to the target
    return best_pair


# Test Cases:

dishes = [-3, -5, 1, 7]
target = 8

dishes_2 = [3, 5, 7, 2, 6, 8, 1]
target_2 = 10

dishes_3 = [2, 5, -4, -7, 12, 100, -25]
target_3 = -20

dishes_4 = []
target_4 = 10

print(sweet_and_savory(dishes, target))
# Output: [-3, 7]

print(sweet_and_savory(dishes_2, target_2))
# Output: [0, 0]

print(sweet_and_savory(dishes_3, target_3))
# Output: [-25, 5]

print(sweet_and_savory(dishes_4, target_4))
# Output: [0, 0]

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

1. **Sorting the Dishes:**
   - Sorting the `sweet_dishes` and `savory_dishes` lists takes O(n log n) time, where `n` is the number of dishes.
   This is because sorting is the most expensive operation in the algorithm.

2. **Two-pointer Traversal:**
   - The while loop iterates over the `sweet_dishes` and `savory_dishes` lists using two pointers (`sweet_index` and
   `savory_index`). In the worst case, this loop runs O(n) times, where `n` is the total number of dishes.

Thus, the overall time complexity is dominated by the sorting step: O(n log n)

---

### Space Complexity Analysis

1. **Additional Space for Sorting:**
   - The `sweet_dishes` and `savory_dishes` lists require O(n) space in total, where `n` is the number of dishes.

2. **Constant Space for Variables:**
   - The variables `best_pair`, `best_difference`, `sweet_index`, and `savory_index` use O(1) space.

Thus, the overall space complexity is: O(n)

---

### Summary

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

This algorithm is efficient for finding the best sweet and savory dish pair that sums closest to the target value.
The sorting step is the bottleneck, but the two-pointer traversal ensures that the search is linear after sorting.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**

The function `sweet_and_savory(dishes, target)` is designed to find the best combination of one **sweet** and one **savory**
dish such that their sum is **as close as possible to the given target without exceeding it**.

---

### **Step-by-Step Breakdown**

#### **1. Categorize Dishes into Sweet and Savory**
```
sweet_dishes = sorted([dish for dish in dishes if dish < 0], key=abs)
savory_dishes = sorted([dish for dish in dishes if dish > 0])
```
- **Sweet dishes** (negative values) are extracted and sorted by absolute value.
- **Savory dishes** (positive values) are extracted and sorted in ascending order.
- The sorting ensures we start with the least absolute sweet dish and the smallest savory dish, making it easier
to find the closest sum.

**Example:**  

For `dishes = [-3, -5, 1, 7]`, after sorting:  
- `sweet_dishes = [-3, -5]`
- `savory_dishes = [1, 7]`

---

#### **2. Initialize Best Pair and Best Difference**

```
best_pair = [0, 0]
best_difference = float("inf")
```
- `best_pair`: Stores the best combination found.
- `best_difference`: Tracks the smallest difference between `target` and the sum of the selected dishes.

---

#### **3. Use Two-Pointer Approach**

```
sweet_index, savory_index = 0, 0
```
- **`sweet_index`** starts at the first element of `sweet_dishes`.
- **`savory_index`** starts at the first element of `savory_dishes`.

```
while sweet_index < len(sweet_dishes) and savory_index < len(savory_dishes):
```
- The loop continues as long as there are **both** sweet and savory dishes to consider.

---

#### **4. Calculate Current Sum and Update Best Pair**

```
current_sum = sweet_dishes[sweet_index] + savory_dishes[savory_index]
```
- Computes the sum of the current sweet and savory dish.

##### **4.1. If the Sum is Within Target**

```
if current_sum <= target:
    current_difference = target - current_sum

    if current_difference < best_difference:
        best_difference = current_difference
        best_pair = [sweet_dishes[sweet_index], savory_dishes[savory_index]]

    savory_index += 1
```
- If `current_sum` is **≤ target**, update `best_difference` and `best_pair` if it's the closest sum found.
- Move the `savory_index` **right** (i.e., to a larger savory dish) to try and get closer to `target`.

##### **4.2. If the Sum Exceeds the Target**

```
else:
    sweet_index += 1
```
- If `current_sum` is **greater than target**, move the `sweet_index` **right** to use a sweeter dish with a smaller absolute value.

---

#### **5. Return the Best Found Pair**

```
return best_pair
```
- The loop continues until all possible dish pairs have been considered, and the best combination is returned.

---

### **Test Cases and Outputs**

#### **1. Example Case: `[-3, -5, 1, 7]` with `target = 8`**
```
sweet_and_savory([-3, -5, 1, 7], 8)
```
- `sweet_dishes = [-3, -5]`
- `savory_dishes = [1, 7]`
- Best pair: `[-3, 7]` (sum = `4`, closest to `8` without exceeding it)

**Output:** `[-3, 7]`

---

#### **2. No Sweet Dishes: `[3, 5, 7, 2, 6, 8, 1]` with `target = 10`**
```
sweet_and_savory([3, 5, 7, 2, 6, 8, 1], 10)
```
- No negative numbers, so `sweet_dishes = []`
- Since a valid sweet & savory pair isn't possible, default `[0, 0]` is returned.

**Output:** `[0, 0]`

---

#### **3. Example Case: `[2, 5, -4, -7, 12, 100, -25]` with `target = -20`**
```
sweet_and_savory([2, 5, -4, -7, 12, 100, -25], -20)
```
- `sweet_dishes = [-4, -7, -25]`
- `savory_dishes = [2, 5, 12, 100]`
- Best pair: `[-25, 5]` (sum = `-20`)

**Output:** `[-25, 5]`

---

#### **4. Empty List: `[]` with `target = 10`**
```
sweet_and_savory([], 10)
```
- No dishes available, so return `[0, 0]`.

**Output:** `[0, 0]`

---

### **Alternative Approach**
If we assume a dish list always contains at least one sweet and one savory dish, we could **skip sorting** and use a **hash set**
for lookup, reducing complexity to `O(n)`. But sorting ensures a clear approach for finding the closest sum efficiently.

---

### **Conclusion**

- The function effectively finds the closest sum **without exceeding the target** using sorting and a **two-pointer** approach.
- The approach is efficient and works well for different inputs, including edge cases.
- If there are **no valid pairs**, it defaults to `[0, 0]`.

This method balances **efficiency** and **clarity**, making it a strong solution for the problem. 

"""
