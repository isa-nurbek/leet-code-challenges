# Problem Description:

"""
                                             Remove Duplicates From Linked List

You're given the head of a Singly Linked List whose nodes are in `sorted or unsorted order` with respect to their values. Write
a function that returns a modified version of the linked list where `all nodes with duplicate values are removed`, leaving only
distinct values. Modify the list in place (do not create a new list). The relative order of the remaining nodes should preserve
their original order (whether sorted or unsorted).

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

## Sample Input With Sorted Linked List:
```
sorted_linked_list_dict = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 3},
        {"id": "3", "next": "3-2", "value": 4},
        {"id": "3-2", "next": "3-3", "value": 4},
        {"id": "3-3", "next": "4", "value": 4},
        {"id": "4", "next": "5", "value": 5},
        {"id": "5", "next": "5-2", "value": 6},
        {"id": "5-2", "next": None, "value": 6},
    ],
}

// The List Looks Like: [1] -> [1] -> [3] -> [4] -> [4] -> [4] -> [5] -> [6] -> [6] -> None 
// The head node with value 1
```

## Sample Output With Sorted Linked List:
```
1 -> 3 -> 4 -> 5 -> 6 -> None 

// The head node with value 1
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the number of nodes in the Linked List.
```

"""

# =========================================================================================================================== #

# Solution:


# Linked List Class
class LinkedList:
    def __init__(self, value):
        self.value = value  # Store the value of this node
        self.next = None  # Pointer to the next node (initially None)


# Helper function to convert dictionary to LinkedList
def build_linked_list(data):
    """Builds a linked list from a dictionary representation.

    Args:
        data: Dictionary containing 'head' (id of head node) and 'nodes' (list of node dictionaries)

    Returns:
        The head node of the constructed linked list
    """
    if not data:
        return None

    # Create all nodes first and store them in a dictionary by their IDs
    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    # Connect the nodes by setting the next pointers based on the 'next' IDs
    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    # Return the head node (the starting point of the linked list)
    return nodes[data["head"]]


# Function to remove duplicates from sorted list
# O(n) time | O(1) space
def remove_duplicates_from_linked_list(linked_list):
    """Removes consecutive duplicate values from a sorted linked list in-place.

    Args:
        linked_list: The head node of the linked list to process

    Returns:
        The head node of the modified linked list
    """
    current_node = linked_list
    while current_node is not None:
        # Find the next node with a different value
        next_distinct_node = current_node.next
        while (
            next_distinct_node is not None
            and next_distinct_node.value == current_node.value
        ):
            next_distinct_node = next_distinct_node.next

        # Skip over all duplicates and point to the next distinct node
        current_node.next = next_distinct_node

        # Move to the next distinct node for next iteration
        current_node = next_distinct_node

    return linked_list  # Return the head of the modified list


# Function to print the linked list (for verification)
def print_linked_list(linked_list):
    """Prints the linked list in a readable format.

    Args:
        linked_list: The head node of the linked list to print
    """
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Input data
sorted_linked_list_dict = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 3},
        {"id": "3", "next": "3-2", "value": 4},
        {"id": "3-2", "next": "3-3", "value": 4},
        {"id": "3-3", "next": "4", "value": 4},
        {"id": "4", "next": "5", "value": 5},
        {"id": "5", "next": "5-2", "value": 6},
        {"id": "5-2", "next": None, "value": 6},
    ],
}

# Test Case:

# Build the linked list from dictionary
linked_list = build_linked_list(sorted_linked_list_dict)

# Remove duplicates
result = remove_duplicates_from_linked_list(linked_list)

print_linked_list(result)
# Output: 1 -> 3 -> 4 -> 5 -> 6 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `remove_duplicates_from_linked_list` function.

### Time Complexity:

The function processes each node in the linked list exactly once in the outer while loop. For each node, it may also
traverse some subsequent nodes in the inner while loop to skip duplicates. 

In the worst case (when all nodes are unique), the inner loop doesn't do any work (just one comparison per node),
resulting in O(n) time. 

In the case where there are many duplicates, each node is still only processed once by either the outer or inner loop. 
For example, if all nodes are the same value, the inner loop will traverse all nodes once, and the outer loop will only run once.

Thus, the time complexity is **O(n)**, where n is the number of nodes in the linked list.

### Space Complexity:

The function uses a constant amount of additional space (only a few pointers like `current_node` and `next_distinct_node` are used).
It modifies the linked list in-place without using any additional data structures that grow with input size.

Thus, the space complexity is **O(1)** (constant space).

### Summary:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through the code in detail and explain each part of it so you fully understand how everything works — from
the data setup to removing duplicates in the linked list.

### 🔹 PART 1: `LinkedList` Class

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

This defines a **node** in a singly linked list.

- `value`: stores the value for that node (like 1, 3, 4, etc.).
- `next`: points to the **next node** in the list. It's initialized as `None`.

Example:
```
node = LinkedList(5)
```
This creates a node like:
```
[5] -> None
```

---

### 🔹 PART 2: `build_linked_list(data)` Function

```
def build_linked_list(data):
    if not data:
        return None
```
This function takes a dictionary (`data`) and builds the linked list from it.

#### ✅ Step 1: Create All Nodes
```
nodes = {}
for node_data in data["nodes"]:
    node = LinkedList(node_data["value"])
    nodes[node_data["id"]] = node
```

- It goes through every node in the `data["nodes"]` list.
- For each node, it creates a `LinkedList` object using its `value`.
- It stores these nodes in a dictionary `nodes` using their `id` as key, for easy access later.

#### ✅ Step 2: Connect the Nodes
```
for node_data in data["nodes"]:
    if node_data["next"] is not None:
        nodes[node_data["id"]].next = nodes[node_data["next"]]
```
- Now it connects each node’s `next` pointer using the `id` of the next node.

#### ✅ Step 3: Return Head
```
return nodes[data["head"]]
```
- It returns the head node, i.e., the start of the linked list.

---

### 🔹 PART 3: `remove_duplicates_from_linked_list(linked_list)`

```
def remove_duplicates_from_linked_list(linked_list):
    current_node = linked_list
```
This function **removes duplicate values** from a **sorted** linked list.

Let’s step through this:

#### ✅ Outer While Loop
```
while current_node is not None:
```
Iterate through the list from start to end.

#### ✅ Inner While Loop
```
next_distinct_node = current_node.next
while (next_distinct_node is not None and 
        next_distinct_node.value == current_node.value):
    next_distinct_node = next_distinct_node.next
```
- `next_distinct_node` starts as the next node.
- It skips over all nodes that have the **same value** as the current node.
- When it finds a node with a **different value**, it stops.

#### ✅ Update the `next` pointer
```
current_node.next = next_distinct_node
current_node = next_distinct_node
```
- It connects the current node directly to the next distinct node.
- Then it moves on to the next node and repeats.

🔁 This process continues until the end of the list.

---

### 🔹 PART 4: `print_linked_list(linked_list)`

```
def print_linked_list(linked_list):
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
```

- This is a helper function to print the list in a readable format.
- Example output:  
  ```
  1 -> 3 -> 4 -> 5 -> 6 -> None
  ```

---

### 🔹 PART 5: The Input Data

```
linked_list_dict = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "1-2", "value": 1},
        {"id": "1-2", "next": "1-3", "value": 1},
        {"id": "1-3", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 3},
        {"id": "3", "next": "3-2", "value": 4},
        {"id": "3-2", "next": "3-3", "value": 4},
        {"id": "3-3", "next": "4", "value": 4},
        {"id": "4", "next": "5", "value": 5},
        {"id": "5", "next": "5-2", "value": 6},
        {"id": "5-2", "next": None, "value": 6},
    ],
}
```

This dictionary defines the linked list. It mimics the structure:
```
1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 -> None
```

---

### 🔹 PART 6: Full Flow

```
linked_list = build_linked_list(linked_list_dict)      # Build the list
deduped_list = remove_duplicates_from_linked_list(linked_list)  # Remove duplicates
print_linked_list(deduped_list)                        # Print result
```

---

### ✅ Final Output:

```
1 -> 3 -> 4 -> 5 -> 6 -> None
```

Because duplicates like the extra 1s, 4s, and 6s were removed.

---

### Recap

| Step              | Description                                         |
|-------------------|-----------------------------------------------------|
| Build list        | Converts a structured dictionary into a linked list |
| Remove duplicates | Scans the sorted list and skips repeated values     |
| Print list        | Displays values in order from head to end           |

---


## Visual Diagram (Before & After)

Here’s what the list looks like **before removing duplicates**:

```
[1] → [1] → [1] → [3] → [4] → [4] → [4] → [5] → [6] → [6] → None
```

Since the list is sorted, all duplicate values are **next to each other**.

### 🧠 `remove_duplicates_from_linked_list`

The function checks:

- Is current node value same as next?
- If yes, skip the next node (unlink it)
- Continue until values differ.

**Step-by-step:**

```
[1] → [1] → [1]         # all these 1s get collapsed into one
 ↓
[1] → [3] → [4] → [4] → [4]  → [5] → [6] → [6] → None
              ↓
[4] gets collapsed into one

Final:
[1] → [3] → [4] → [5] → [6] → None
```

Duplicates are removed *in place*, so no extra memory is used (other than some pointers).

"""
