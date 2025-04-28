# Problem Description:

"""

                                                # Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function
should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these
quadruplets in no particular order.

If no four numbers sum up to the target sum, the function should return an empty array.


## Sample Input:
```
array = [7, 6, 4, -1, 1, 2]
target_sum = 16
```

## Sample Output:
```
[[7, 6, 4, -1], [7, 6, 1, 2]] 

// The quadruplets could be ordered differently
```

## Optimal Time & Space Complexity:
```
Average: O(n^2) time | O(n^2) space - where `n` is the length of the input array.
Worst: O(n^3) time | O(n^2) space - where `n` is the length of the input array.
```

"""

# =========================================================================================================================== #

# Solution:


# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(1) space
def four_number_sum_sorted(array, target_sum):
    # Sort the array to make it easier to find quadruplets and avoid duplicates
    array.sort()

    # Initialize an empty list to store the quadruplets that sum up to the target
    quadruplets = []

    # Iterate through the array, leaving room for the other three numbers in the quadruplet
    for i in range(len(array) - 3):
        # Iterate through the array starting from the next element after i
        for j in range(i + 1, len(array) - 2):
            # Initialize two pointers, one at the start (left) and one at the end (right) of the remaining array
            left, right = j + 1, len(array) - 1

            # Use a two-pointer approach to find pairs that, along with array[i] and array[j], sum to the target
            while left < right:
                # Calculate the current sum of the four numbers
                current_sum = array[i] + array[j] + array[left] + array[right]

                # If the current sum matches the target, add the quadruplet to the list
                if current_sum == target_sum:
                    quadruplets.append([array[i], array[j], array[left], array[right]])
                    # Move both pointers to find other possible quadruplets
                    left += 1
                    right -= 1
                # If the current sum is less than the target, move the left pointer to the right to increase the sum
                elif current_sum < target_sum:
                    left += 1
                # If the current sum is greater than the target, move the right pointer to the left to decrease the sum
                else:
                    right -= 1

    # Return the list of quadruplets that sum up to the target
    return quadruplets


# Test Cases:

array = [7, 6, 4, -1, 1, 2]
target_sum = 16

array_2 = [1, 2, 3, 4, 5, 6, 7]
target_sum_2 = 10

array_3 = [1, 2, 3, 4, 5]
target_sum_3 = 100

print(four_number_sum_sorted(array, target_sum))
# Output: [[7, 6, 4, -1], [7, 6, 1, 2]]

print(four_number_sum_sorted(array_2, target_sum_2))
# Output: [[1, 2, 3, 4]]

print(four_number_sum_sorted(array_3, target_sum_3))
# Output: []

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis:

The time complexity of the `four_number_sum_sorted` function can be broken down as follows:

1. **Sorting the Array**:
   - Sorting the array takes O(n log n)) time, where `n` is the length of the array.

2. **Nested Loops**:
   - The outer loop runs from i = 0 to i = n - 4, which is O(n).
   - The middle loop runs from j = i + 1 to j = n - 3, which is also O(n).
   - The inner while loop runs from `left = j + 1` to `right = n - 1`, which is O(n) in the worst case.

   Therefore, the nested loops contribute O(n^3) time complexity.

3. **Overall Time Complexity**:
   - The dominant term is O(n^3), so the overall time complexity is:

        O(n log n) + O(n^3) = O(n^3)

---

### Space Complexity Analysis:

1. **Output Space**:
   - The space required for the `quadruplets` list depends on the number of valid quadruplets found. In the worst case,
   the number of quadruplets can be O(n^3), but this is rare and depends on the input.

2. **Auxiliary Space**:
   - The sorting is done in-place, so it uses O(1) additional space.
   - The pointers (`i`, `j`, `left`, `right`) and temporary variables use O(1) space.

3. **Overall Space Complexity**:
   - If we ignore the space required for the output, the auxiliary space complexity is O(1).
   - If we include the output space, the worst-case space complexity is O(n^3).

### Summary:
- **Time Complexity**: O(n^3)
- **Space Complexity**: O(1) (excluding output) or O(n^3) (including output)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Explanation of the Code**

The function `four_number_sum_sorted(array, target_sum)` finds all unique quadruplets (sets of four numbers) that sum to
`target_sum`. It uses **sorting** and a **two-pointer technique** to efficiently search for these quadruplets.

---

## **Step-by-Step Breakdown**

### **1. Sorting the Array**
```
array.sort()
```
- Sorting the array first ensures that we can efficiently find pairs using **two pointers**.
- **Time complexity:** `O(N log N)`

---

### **2. Iterating Over the Array**
```
for i in range(len(array) - 3):
    for j in range(i + 1, len(array) - 2):
```
- We **fix** two numbers in the quadruplet:
  - `i`: First number (`0` to `len(array) - 4`)
  - `j`: Second number (`i+1` to `len(array) - 3`)
  
- The remaining **two numbers** will be found using the **two-pointer approach**.

---

### **3. Using Two Pointers**
```
left, right = j + 1, len(array) - 1

while left < right:
```
- `left` starts **right after `j`**.
- `right` starts **at the last element**.
- The **goal** is to find two numbers (`array[left]` and `array[right]`) such that their sum, when added to
`array[i]` and `array[j]`, equals `target_sum`.

---

### **4. Calculating the Current Sum**
```
current_sum = array[i] + array[j] + array[left] + array[right]
```
- This checks whether the sum of the **four numbers** matches the target.

---

### **5. Adjusting Pointers Based on `current_sum`**
```
if current_sum == target_sum:
    quadruplets.append([array[i], array[j], array[left], array[right]])
    left += 1
    right -= 1
```
- If `current_sum == target_sum`, we found a valid quadruplet.
- **Move both pointers** to search for more pairs.

```
elif current_sum < target_sum:
    left += 1
```
- If `current_sum` is **too small**, move `left` **rightward** (increase the sum).

```
else:
    right -= 1
```
- If `current_sum` is **too large**, move `right` **leftward** (decrease the sum).

---

### **6. Returning the List of Quadruplets**
```
return quadruplets
```
- Returns a **list of all unique quadruplets**.

---

## **Example Walkthrough**

### **Test Case 1**
```
array = [7, 6, 4, -1, 1, 2]
target_sum = 16
```

#### **Step 1: Sorting**
```
[-1, 1, 2, 4, 6, 7]
```
#### **Step 2: Iteration and Pointer Adjustment**

| `i` | `j` | `left` | `right` | `current_sum` | Action                      |
|-----|-----|--------|---------|---------------|-----------------------------|
| -1  | 1   | 2      | 7       | 9             | Move `left`                 |
| -1  | 1   | 4      | 7       | 11            | Move `left`                 |
| -1  | 1   | 6      | 7       | 13            | Move `left`                 |
| -1  | 2   | 4      | 7       | 12            | Move `left`                 |
| -1  | 2   | 6      | 7       | 14            | Move `left`                 |
| -1  | 4   | 6      | 7       | 16            | **Found:** `[-1, 4, 6, 7]`  |
| 1   | 2   | 4      | 7       | 14            | Move `left`                 |
| 1   | 2   | 6      | 7       | 16            | **Found:** `[1, 2, 6, 7]`   |

#### **Final Output**
```
[[7, 6, 4, -1], [7, 6, 1, 2]]
```

---

### **Test Case 2**
```
array_2 = [1, 2, 3, 4, 5, 6, 7]
target_sum_2 = 10
```
- Sorting: `[1, 2, 3, 4, 5, 6, 7]`
- **Valid Quadruplet:** `[1, 2, 3, 4]`

**Output:**
```
[[1, 2, 3, 4]]
```

---

### **Test Case 3**
```
array_3 = [1, 2, 3, 4, 5]
target_sum_3 = 100
```
- No valid quadruplets exist.

**Output:**
```
[]
```

---

## **Comparison with Hash Table Approach**

| Approach                   | Time Complexity     | Space Complexity | Best When?                  |
|----------------------------|---------------------|------------------|-----------------------------|
| **Sorting + Two Pointers** | `O(N^3)`            | `O(1)`           | When memory is a concern    |
| **Hash Table Method**      | `O(N^2)`            | `O(N^2)`         | When we need faster results |

The **sorting + two-pointer method** is **more space-efficient** but slightly **slower** than the hash table approach.

---

## **Summary**
- **Sort the array** first.
- **Use nested loops to fix two numbers (`i` and `j`).**
- **Use the two-pointer technique** to find the remaining two numbers.
- **Move `left` and `right` accordingly** to adjust the sum.
- **Time Complexity:** `O(N^3)`, **Space Complexity:** `O(1)`.
- **Alternative method (hash table approach) is faster (`O(N^2)`) but uses more space.**

"""
