# Problem Description:

"""

                                                # Best Seat

You walk into a theatre you're about to see a show in. The usher within the theatre walks you to your row and mentions you're
allowed to sit anywhere within the given row. Naturally you'd like to sit in the seat that gives you the most space. You also
would prefer this space to be evenly distributed on either side of you (e.g. if there are three empty seats in a row, you would
prefer to sit in the middle of those three seats).

Given the theatre row represented as an integer array, return the seat index of where you should sit. Ones represent occupied
seats and zeroes represent empty seats.

You may assume that someone is always sitting in the first and last seat of the row. Whenever there are two equally good seats,
you should sit in the seat with the lower index. If there is no seat to sit in, return -1. The given array will always have
a length of at least one and contain only ones and zeroes.


## Sample Input:
```
seats = [1, 0, 1, 0, 0, 0, 1]
```

## Sample Output:
```
4
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the number of seats.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(1) space
def best_seat(seats):
    # Initialize variables to track the best seat and the maximum available space
    best_seat = -1  # Default value if no suitable seat is found
    max_space = 0  # Tracks the largest continuous block of empty seats found

    # Start from the leftmost seat
    left = 0
    while left < len(seats):
        # Initialize the right pointer to the next seat
        right = left + 1

        # Move the right pointer as long as the seats are empty (0)
        while right < len(seats) and seats[right] == 0:
            right += 1

        # Calculate the available space between the left and right pointers
        # Subtract 1 because the space is between the seats, not including them
        available_space = right - left - 1

        # If this block of empty seats is larger than the previous maximum, update the best seat
        if available_space > max_space:
            best_seat = (left + right) // 2  # The middle seat in the block
            max_space = available_space

        # Move the left pointer to the current right pointer to check the next block
        left = right

    # Return the best seat found, or -1 if no suitable seat is available
    return best_seat


# Test Cases:

print(best_seat([1, 0, 1, 0, 0, 0, 1]))
# Output: 4

print(best_seat([1]))
# Output: -1

print(best_seat([1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]))
# Output: 3

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### Time Complexity Analysis

The time complexity of the `best_seat` function is **O(n)**, where `n` is the number of elements in the `seats` list.

#### Explanation:

1. The outer `while` loop iterates through the `seats` list once. The `left` pointer starts at 0 and increments
until it reaches the end of the list.

2. The inner `while` loop increments the `right` pointer as long as the current seat is `0` (available). This loop also
iterates through the list, but it does so in conjunction with the outer loop.

3. The key observation is that each element in the `seats` list is visited at most twice: once by the `left` pointer and
once by the `right` pointer. This results in a linear time complexity, **O(n)**.

---

### Space Complexity Analysis

The space complexity of the `best_seat` function is **O(1)**.

#### Explanation:

1. The function uses a constant amount of extra space, regardless of the input size. Variables like `best_seat`, `max_space`,
`left`, and `right` occupy a fixed amount of memory.

2. No additional data structures (e.g., arrays, hash maps) are used that grow with the input size. 
Thus, the space complexity is constant, **O(1)**.

---

### Summary
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

This makes the algorithm efficient for large inputs.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
The `best_seat` function determines the best seat in a row of seats based on maximizing the distance from occupied seats.

---

### **Understanding the Input and Output**
- The function takes a list `seats`, where:
  - `1` represents an **occupied** seat.
  - `0` represents an **empty** seat.
- The goal is to find the **index** of the seat that provides the **maximum** space from occupied seats.

---

### **Step-by-Step Explanation of the Code**

#### **1. Initialize Variables**
```
best_seat = -1
max_space = 0
```
- `best_seat`: Stores the index of the best seat found. Initialized to `-1`, meaning **no suitable seat** is found.
- `max_space`: Keeps track of the **maximum number of consecutive empty seats** found so far.

---

#### **2. Loop Through the List**
```
left = 0
while left < len(seats):
```
- `left` starts at **index 0** and moves through the list.

---

#### **3. Find the Right Boundary of an Empty Section**
```
right = left + 1
while right < len(seats) and seats[right] == 0:
    right += 1
```
- If `seats[right] == 0`, we **keep moving right** until we find a `1` (occupied seat).
- This process finds a **block of empty seats**.

---

#### **4. Calculate Available Space**
```
available_space = right - left - 1
```
- `available_space` represents the number of **empty seats** between `left` and `right`.

---

#### **5. Update Best Seat if Current Space is Greater**
```
if available_space > max_space:
    best_seat = (left + right) // 2
    max_space = available_space
```
- If the current `available_space` is **larger than** `max_space`, update:
  - `best_seat` to the **middle seat** of the empty block.
  - `max_space` to store the **new maximum empty space**.

---

#### **6. Move Left Pointer**
```
left = right
```
- Move `left` to `right` to **start searching for the next empty section**.

---

### **Example Walkthrough**

#### **Test Case 1**
```
seats = [1, 0, 1, 0, 0, 0, 1]
```
1. `left = 0`, `right = 1`, finds `available_space = 0` (ignored).
2. `left = 2`, `right = 3 → 4 → 5 → 6` finds `available_space = 3`
   - `best_seat = (2 + 6) // 2 = 4`
3. `left = 6`, no more empty blocks.

✅ **Output**: `4`

---

#### **Test Case 2**
```
seats = [1]
```
- No empty seats, so `best_seat` remains `-1`.

✅ **Output**: `-1`

---

#### **Test Case 3**
```
seats = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
```
1. `left = 3`, `right = 4`, finds `available_space = 1`
   - `best_seat = 3`
2. `left = 5`, `right = 6`, finds `available_space = 1` (same as max).
3. `left = 9`, `right = 10`, finds `available_space = 0`.

✅ **Output**: `3`

---

This approach is **efficient and optimal** for finding the best seat in a row. 🚀

"""
