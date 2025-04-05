# Problem Description:

"""
                                            # Apartment Hunting

You're looking to move into a new apartment on specific street, and you're given a list of contiguous blocks on that street
where each block contains an apartment that you could move into.

You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school
and a gym near your apartment. The list of blocks that you have contains information at every block about all of the buildings that
are present and absent at the block in question. For instance, for every block, you might know whether a school, a pool, an office,
and a gym are present.

In order to optimize your life, you want to pick an apartment block such that you minimize the farthest distance you'd have to walk
from your apartment to reach any of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street and a list of your required buildings and that
returns the location (the index) of the block that's most optimal for you.

If there are multiple most optimal blocks, your function can return the index of any one of them.


## Sample Input:
```
blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]

reqs = ["gym", "school", "store"]
```

## Sample Output:
```
3 // at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index,
  you'd have to walk farther
```

## Optimal Time & Space Complexity:
```
O(b * r) time | O(b) space - where `b` is the number of blocks and `r` is the number of requirements.
```

"""

# =========================================================================================================================== #

# Solution:


# O(b * r) time | O(b) space
def apartment_hunting(blocks, reqs):
    # Initialize a dictionary to store minimum distances for each requirement
    # For each requirement, create a list to store min distances for each block
    num_blocks = len(blocks)
    min_distances = {req: [float("inf")] * num_blocks for req in reqs}

    # First pass: Left to Right
    # For each requirement, calculate the closest instance to the left of each block
    for req in reqs:
        closest_req = float("inf")  # Tracks the closest requirement seen so far
        for i in range(num_blocks):
            if blocks[i][req]:  # If current block has the requirement
                closest_req = i  # Update closest requirement position
            # Store distance to closest requirement (left if not found yet)
            min_distances[req][i] = (
                abs(i - closest_req) if closest_req != float("inf") else float("inf")
            )

    # Second pass: Right to Left
    # For each requirement, calculate the closest instance to the right of each block
    # and keep the minimum of left and right distances
    for req in reqs:
        closest_req = float("inf")  # Reset closest requirement tracker
        for i in range(num_blocks - 1, -1, -1):  # Iterate from right to left
            if blocks[i][req]:  # If current block has the requirement
                closest_req = i  # Update closest requirement position
            # Compare with left pass result and store the minimum distance
            min_distances[req][i] = min(
                min_distances[req][i],
                abs(i - closest_req) if closest_req != float("inf") else float("inf"),
            )

    # Calculate the maximum distance across all requirements for each block
    max_distances_at_blocks = [
        max(
            min_distances[req][i] for req in reqs
        )  # Max distance for this block across all reqs
        for i in range(num_blocks)
    ]

    # Return the index of the block with the smallest maximum distance
    return max_distances_at_blocks.index(min(max_distances_at_blocks))


# Test Cases:

blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]

reqs = ["gym", "school", "store"]

blocks_2 = [
    {"gym": False, "office": True, "school": True, "store": False},
    {"gym": True, "office": False, "school": False, "store": False},
    {"gym": True, "office": False, "school": True, "store": False},
    {"gym": False, "office": False, "school": True, "store": False},
    {"gym": False, "office": False, "school": True, "store": True},
]

reqs_2 = ["gym", "office", "school", "store"]

print(apartment_hunting(blocks, reqs))  # Output: 3
print(apartment_hunting(blocks_2, reqs_2))  # Output: 2

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

### **Time Complexity Analysis**

1. **Initialization of `min_distances`:**
   - We initialize a dictionary `min_distances` where each key is a requirement (`req`) and the value is a list of size
   `num_blocks` (initialized to `inf`).
   - This takes **O(R × B)** time, where:
     - `R` = number of requirements (`len(reqs)`).
     - `B` = number of blocks (`num_blocks`).

2. **First Pass (Left to Right):**
   - For each requirement (`req`), we iterate over all blocks (`B` times).
   - For each block, we perform **O(1)** operations (checking if the requirement is present and updating `min_distances`).
   - This pass takes **O(R × B)** time.

3. **Second Pass (Right to Left):**
   - Similar to the first pass, we iterate over each requirement and each block in reverse.
   - Again, this takes **O(R × B)** time.

4. **Compute `max_distances_at_blocks`:**
   - For each block (`B` iterations), we compute the maximum distance across all requirements (`R` operations per block).
   - This takes **O(B × R)** time.

5. **Finding the Minimum Maximum Distance:**
   - We find the index of the minimum value in `max_distances_at_blocks` (which is **O(B)** time).

**Total Time Complexity**:
- The dominant operations are the two passes and the computation of `max_distances_at_blocks`, each taking **O(R × B)** time.
- Thus, the total time complexity is:
  
  O(R * B) + O(R * B) + O(R * B) + O(B) = O(R * B)
  

### **Space Complexity Analysis**

1. **`min_distances` Dictionary:**
   - Stores `R` keys, each mapping to a list of size `B`.
   - This takes **O(R × B)** space.

2. **`max_distances_at_blocks` List:**
   - A list of size `B` (stores the maximum distance for each block).
   - This takes **O(B)** space.

3. **Other Variables:**
   - `closest_req`, loop counters, etc., use **O(1)** space.

**Total Space Complexity**:
- The dominant term is the `min_distances` dictionary, which takes **O(R × B)** space.
- Thus, the total space complexity is: O(R * B)

### **Final Answer**
- **Time Complexity:** **O(R × B)**
- **Space Complexity:** **O(R × B)**

Where:
- `R` = number of requirements (`len(reqs)`).
- `B` = number of blocks (`len(blocks)`).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through the `apartment_hunting` function step by step. The goal of this function is to find the **best block** to
live in such that the **maximum distance** to any required building (like a gym, school, or store) is **minimized**.

### 📌 Problem Definition

Given:
- `blocks`: A list of dictionaries where each dictionary represents a block and keys represent building types (e.g., "gym",
"school") with boolean values (`True` = has the facility, `False` = doesn't).
- `reqs`: A list of required buildings.

We want to choose the **block index** such that the **furthest** you would have to walk to reach any required building is
as short as possible.

---

### 🔍 Step-by-Step Explanation

#### Step 1: Initialize `min_distances` Dictionary
```
min_distances = {req: [float("inf")] * num_blocks for req in reqs}
```
- We create a dictionary where each key is a requirement (e.g., "gym") and the value is a list of size `num_blocks`.
- Each element of the list will eventually store the **minimum distance** from that block to the closest block that satisfies
the requirement.

Initially, we set all distances to infinity because we haven't done any calculations yet.

---

### ➡️ Forward Pass (Left to Right)

```
for req in reqs:
    closest_req = float("inf")
    for i in range(num_blocks):
        if blocks[i][req]:
            closest_req = i
        min_distances[req][i] = abs(i - closest_req) if closest_req != float("inf") else float("inf")
```

For each requirement:
- Walk through the blocks from **left to right**.
- Keep track of the last block index `closest_req` that satisfied the requirement.
- At each step, calculate how far the current block is from the nearest **seen-so-far** satisfying block.

This gives us **minimum distances to the requirement when looking from the left side**.

---

### ⬅️ Backward Pass (Right to Left)

```
for req in reqs:
    closest_req = float("inf")
    for i in range(num_blocks - 1, -1, -1):
        if blocks[i][req]:
            closest_req = i
        min_distances[req][i] = min(min_distances[req][i], abs(i - closest_req) if closest_req != float("inf") else float("inf"))
```

This does the same thing, but in **reverse**:
- Walking from right to left.
- Checks whether there's a closer requirement behind (to the right), and takes the **minimum** between both directions.

After this step, `min_distances[req][i]` contains the **true shortest distance** from block `i` to the closest block that
satisfies the requirement `req`.

---

### 🔢 Find Max Distance Per Block

```
max_distances_at_blocks = [max(min_distances[req][i] for req in reqs) for i in range(num_blocks)]
```

Now, for each block `i`, we:
- Find the **maximum** distance among all requirements from that block.
- Why max? Because we want to minimize the **worst-case distance** to any requirement.

This gives us a list of "worst-case" distances from each block.

---

### ✅ Find Optimal Block

```
return max_distances_at_blocks.index(min(max_distances_at_blocks))
```

Finally:
- We find the **block with the smallest worst-case distance**.
- Return its index.

---

### 📦 Example Breakdown

```
blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]

reqs = ["gym", "school", "store"]
```

The result is `3`, because from block 3:
- Closest gym is at block 2 (distance 1)
- School is at block 3 (distance 0)
- Store is at block 4 (distance 1)

Max of those = 1 → Best worst-case!

---

### 🔄 Second Test Case

```
blocks_2 = [
    {"gym": False, "office": True, "school": True, "store": False},
    {"gym": True, "office": False, "school": False, "store": False},
    {"gym": True, "office": False, "school": True, "store": False},
    {"gym": False, "office": False, "school": True, "store": False},
    {"gym": False, "office": False, "school": True, "store": True},
]

reqs_2 = ["gym", "office", "school", "store"]
```

The result is `2`, which again is the block with the lowest max distance to all requirements.

### ✅ Summary

This function uses **dynamic programming + two sweeps** (forward and backward) to efficiently calculate shortest distances to required buildings from each block. Then it selects the block where the worst distance to any requirement is minimized.

---

## Visual Diagram of an example

Let’s go through a **step-by-step visual walkthrough** for the **first test case** with this input:

### 🧱 Blocks

Each block has three possible facilities: **gym**, **school**, and **store**.

```
blocks = [
    {"gym": False, "school": True,  "store": False},  # 0
    {"gym": True,  "school": False, "store": False},  # 1
    {"gym": True,  "school": True,  "store": False},  # 2
    {"gym": False, "school": True,  "store": False},  # 3
    {"gym": False, "school": True,  "store": True},   # 4
]

reqs = ["gym", "school", "store"]
```

We want to find the best block where the **maximum distance to any requirement is minimized**.

---

## 🔍 Step 1: Distance Tables for Each Requirement

### 🔹 Forward Pass: Left ➡️ Right

Let’s compute the distances to the **nearest gym** from the left:

| Block | Has Gym? | Closest Gym Index | Distance |
|-------|----------|-------------------|----------|
| 0     | ❌       | ∞                 | ∞        |
| 1     | ✅       | 1                 | 0        |
| 2     | ✅       | 2                 | 0        |
| 3     | ❌       | 2                 | 1        |
| 4     | ❌       | 2                 | 2        |

Same for **school**:

| Block | Has School? | Closest School Index | Distance |
|-------|-------------|----------------------|----------|
| 0     | ✅          | 0                    | 0        |
| 1     | ❌          | 0                    | 1        |
| 2     | ✅          | 2                    | 0        |
| 3     | ✅          | 3                    | 0        |
| 4     | ✅          | 4                    | 0        |

And for **store**:

| Block | Has Store? | Closest Store Index | Distance |
|-------|------------|---------------------|----------|
| 0     | ❌         | ∞                   | ∞        |
| 1     | ❌         | ∞                   | ∞        |
| 2     | ❌         | ∞                   | ∞        |
| 3     | ❌         | ∞                   | ∞        |
| 4     | ✅         | 4                   | 0        |

---

### 🔹 Backward Pass: Right ⬅️ Left

Now we scan right to left and update distances **if closer**:

#### For Gym:
| Block | Closest Gym Index (Back) | Final Distance |
|-------|---------------------------|----------------|
| 4     | ∞                         | 2              |
| 3     | 2                         | 1              |
| 2     | 2                         | 0              |
| 1     | 1                         | 0              |
| 0     | 1                         | 1              |

#### For School (already minimum in forward pass):
Final: `[0, 1, 0, 0, 0]`

#### For Store:
| Block | Closest Store Index (Back) | Final Distance |
|-------|-----------------------------|----------------|
| 4     | 4                           | 0              |
| 3     | 4                           | 1              |
| 2     | 4                           | 2              |
| 1     | 4                           | 3              |
| 0     | 4                           | 4              |

---

## 📊 Step 2: Maximum Distance Per Block

Now we combine the distances at each block:

| Block | To Gym | To School | To Store | Max Distance |
|-------|--------|-----------|----------|--------------|
| 0     | 1      | 0         | 4        | **4**        |
| 1     | 0      | 1         | 3        | **3**        |
| 2     | 0      | 0         | 2        | **2**        |
| 3     | 1      | 0         | 1        | **1** ✅     |
| 4     | 2      | 0         | 0        | **2**        |

✅ **Block 3 is optimal**, with the smallest max distance of 1.

---

## ✅ Final Answer: `3`

"""
