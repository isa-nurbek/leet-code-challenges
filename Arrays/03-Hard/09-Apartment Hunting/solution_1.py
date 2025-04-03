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
O(br) time | O(br) space - where `b` is the number of blocks and `r` is the number of requirements.
```

"""

# =========================================================================================================================== #

# Solution:


# O(b² * r) time | O(b) space
def apartment_hunting(blocks, reqs):
    # Initialize an array to store the maximum distance needed for each block
    max_distances_at_blocks = [float("-inf") for block in blocks]

    # For each block in the neighborhood
    for i in range(len(blocks)):
        # For each requirement (gym, school, store, etc.)
        for req in reqs:
            closest_req_distance = float("inf")

            # Find the closest block with this requirement
            for j in range(len(blocks)):
                if blocks[j][req]:  # If this block has the requirement
                    # Calculate distance between current block and this block
                    closest_req_distance = min(
                        closest_req_distance, distance_between(i, j)
                    )

            # Track the worst-case distance for this requirement
            max_distances_at_blocks[i] = max(
                max_distances_at_blocks[i], closest_req_distance
            )

    # Return the block with the smallest maximum distance
    return get_idx_at_min_value(max_distances_at_blocks)


def get_idx_at_min_value(array):
    # Initialize variables to track the minimum value and its index
    idx_at_min_value = 0  # Start with index 0 as default

    # Initialize with infinity (so any real number will be smaller)
    min_value = float("inf")

    # Iterate through each element in the array
    for i in range(len(array)):
        current_value = array[i]  # Get the current element's value

        # Check if current value is smaller than the smallest found so far
        if current_value < min_value:
            min_value = current_value  # Update the smallest value
            idx_at_min_value = i  # Update the index of the smallest value

    # Return the index where the minimum value was found
    return idx_at_min_value


def distance_between(a, b):
    # Returns the absolute difference between two positions (blocks)
    # This represents the walking distance between them (Manhattan distance)
    return abs(a - b)


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

### Time Complexity:

1. **Outer Loop**: Iterates over each block (`for i in range(len(blocks))`). This runs `B` times, where `B` is the number of blocks.
2. **Middle Loop**: For each block, it iterates over each requirement (`for req in reqs`). This runs `R` times, where `R` is the
number of requirements.
3. **Inner Loop**: For each requirement, it checks every block again (`for j in range(len(blocks))`) to find the closest block
that satisfies the requirement. This runs `B` times.

Thus, the total time complexity is:
- **O(B * R * B) = O(B² * R)**.

### Space Complexity:

1. **max_distances_at_blocks**: This array stores one value per block, so it takes **O(B)** space.
2. Other variables (`i`, `req`, `j`, `closest_req_distance`, etc.) use constant space **O(1)**.

Thus, the total space complexity is:
- **O(B)**.

### Summary:
- **Time Complexity**: **O(B² * R)**
- **Space Complexity**: **O(B)**

### Notes:
- This is a brute-force approach. There are more optimized ways to solve this problem (e.g., precomputing closest distances
for each requirement using dynamic programming), which can reduce the time complexity to **O(B * R)**.
- The current approach recalculates distances redundantly, leading to the higher time complexity.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
### **Detailed Explanation of the Code**

This Python function, `apartment_hunting`, helps find the best apartment block to live in based on certain required amenities like
a gym, school, or store. It does so by determining the block where the maximum walking distance to any required amenity is minimized.

## **Code Walkthrough**

### **Step 1: Understanding the Input**

The function takes in:
1. `blocks`: A list of dictionaries where each dictionary represents an apartment block. The keys in each dictionary are amenities
(e.g., `"gym"`, `"school"`, `"store"`), and their values are `True` if the amenity is present and `False` otherwise.
2. `reqs`: A list of required amenities that the person wants near their apartment.

#### **Example Input**
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

---
### **Step 2: Initializing Maximum Distance Array**
```
max_distances_at_blocks = [float("-inf") for block in blocks]
```
- This array keeps track of the worst-case (maximum) distance for each block.
- It is initially set to negative infinity (`-inf`) to ensure any real number will be larger.

---
### **Step 3: Iterating Over Each Block**

The outer `for` loop iterates over each block `i`:
```
for i in range(len(blocks)):
```
For each block, we check every required amenity:

---
### **Step 4: Finding the Closest Requirement**
```
for req in reqs:
    closest_req_distance = float("inf")  # Start with infinity
```
- We initialize `closest_req_distance` as positive infinity (`inf`) because we want to find the minimum distance to an amenity.

Next, we iterate over all blocks `j` to find the closest one that has the required amenity:
```
for j in range(len(blocks)):
    if blocks[j][req]:  # If this block has the required amenity
        closest_req_distance = min(
            closest_req_distance, distance_between(i, j)
        )
```
- `blocks[j][req]` checks if block `j` has the required amenity (`True`).
- If it does, we compute the walking distance `distance_between(i, j)` using:
```
def distance_between(a, b):
    return abs(a - b)  # Manhattan distance between blocks
```
- We then update `closest_req_distance` to store the minimum distance encountered so far.

---
### **Step 5: Updating Maximum Distance**
```
max_distances_at_blocks[i] = max(
    max_distances_at_blocks[i], closest_req_distance
)
```
- For block `i`, we update `max_distances_at_blocks[i]` to store the **worst-case** distance for any required amenity.

---
### **Step 6: Finding the Optimal Block**

After calculating the maximum distances for all blocks, we call:
```
return get_idx_at_min_value(max_distances_at_blocks)
```
This function finds the index of the block with the **smallest** maximum distance:
```
def get_idx_at_min_value(array):
    idx_at_min_value = 0
    min_value = float("inf")

    for i in range(len(array)):
        if array[i] < min_value:
            min_value = array[i]
            idx_at_min_value = i

    return idx_at_min_value
```
- It iterates through the `max_distances_at_blocks` array to find the block with the smallest worst-case distance.

---

## **Example Walkthrough**

### **Given Blocks and Requirements**
```
blocks = [
    {"gym": False, "school": True, "store": False},  # Block 0
    {"gym": True, "school": False, "store": False},  # Block 1
    {"gym": True, "school": True, "store": False},   # Block 2
    {"gym": False, "school": True, "store": False},  # Block 3
    {"gym": False, "school": True, "store": True},   # Block 4
]

reqs = ["gym", "school", "store"]
```

### **Step-by-Step Calculation**

| Block  | Distance to Gym | Distance to School | Distance to Store | Max Distance   |
|--------|-----------------|--------------------|-------------------|----------------|
| 0      | 1 (Block 1)     | 0 (Itself)         | 4 (Block 4)       | **4**          |
| 1      | 0 (Itself)      | 1 (Block 0 or 2)   | 3 (Block 4)       | **3**          |
| 2      | 0 (Itself)      | 0 (Itself)         | 2 (Block 4)       | **2**          |
| 3      | 1 (Block 2)     | 0 (Itself)         | 1 (Block 4)       | **1**          |
| 4      | 2 (Block 2)     | 0 (Itself)         | 0 (Itself)        | **2**          |

### **Final Result**

The block with the smallest maximum distance is **Block 3**, so the function returns `3`.

---

For large neighborhoods, this solution can be slow. Optimized solutions use **prefix sums or two-pass scanning** to reduce 
complexity to O(B * R).

## **Final Thoughts**
The algorithm finds the most optimal apartment block by:
1. **Checking the distance** to every required amenity for each block.
2. **Tracking the worst-case distance** (max distance) for each block.
3. **Selecting the block with the smallest worst-case distance.**

This ensures that **the worst walk to any required place is as short as possible**, making it the best choice for living. 

"""
