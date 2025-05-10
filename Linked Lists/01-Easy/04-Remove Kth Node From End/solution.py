# Problem Description:

"""
                                            Remove `K`th Node From End

Write a function that takes in the head of a `Singly Linked List` and an integer `k` and removes the kth node from the end of
the list.

The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).

Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done, even if the head
is the node that's supposed to be removed. In other words, if the head is the node that's supposed to be removed, your function
should simply mutate its `value` and `next` pointer.

> Note that your function doesn't need to return anything.

You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

## Sample Input:
```
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
k = 4
```

## Sample Output:
```
// No output required
// The 4th node from the end of the list (the node with value 6) is removed.

0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 -> None
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


# Function to remove kth node from end
# O(n) time | O(1) space
def remove_kth_node_from_end(head, k):
    # Initialize two pointers, both starting at the head of the linked list
    counter = 1
    first = head  # This will eventually point to the node BEFORE the one to remove
    second = head  # This will be used to create the proper distance between pointers

    # Move the second pointer k nodes ahead of the first pointer
    while counter <= k:
        second = second.next
        counter += 1

    # If second has reached the end (None), this means we need to remove the head
    if second is None:
        # Copy the value from the next node to effectively remove the head
        head.value = head.next.value
        # Skip over the next node (which now has the head's original value)
        head.next = head.next.next
        return  # Early return since we've handled the special case

    # Move both pointers until second reaches the last node
    # This maintains the k node gap between them
    while second.next is not None:
        second = second.next
        first = first.next

    # Now first points to the node before the one to remove
    # Skip over the kth node from end by pointing first.next to first.next.next
    first.next = first.next.next


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
linked_list_dict = {
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "6", "value": 5},
        {"id": "6", "next": "7", "value": 6},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": "9", "value": 8},
        {"id": "9", "next": None, "value": 9},
    ],
}

# Test Case:

# Build the linked list from dictionary
linked_list = build_linked_list(linked_list_dict)

# Remove 4th node from end
remove_kth_node_from_end(linked_list, 4)  # This modifies the linked_list in place

# Print the modified linked list
print_linked_list(linked_list)
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `remove_kth_node_from_end` function.

### Time Complexity:

The function uses a two-pointer technique to remove the k-th node from the end of a linked list. 

Here's the breakdown:

1. **Initialization**: O(1) - Just setting up `counter`, `first`, and `second`.
2. **First while loop**: O(k) - Moves the `second` pointer `k` nodes ahead.
3. **Check if `second` is None**: O(1) - Checks if `second` has reached the end (this happens when `k` equals the length of the
list, meaning we need to remove the head).
4. **Second while loop**: O(n - k) - Moves both `first` and `second` until `second.next` is `None`. This means `first` will be at
the node just before the one to be removed.
5. **Removing the node**: O(1) - Adjusts the `next` pointer to skip the node to be removed.

- **Total time complexity**: O(k) + O(n - k) = O(n), where `n` is the number of nodes in the linked list.
This is because we traverse the list at most twice (once to move `second` and once to move both pointers).

### Space Complexity:

The function uses a constant amount of extra space (only a few pointers like `counter`, `first`, and `second`). It does not use
any additional data structures that grow with the input size.

- **Total space complexity**: O(1) (constant space).

### Summary:
- **Time Complexity**: O(n) (linear time).
- **Space Complexity**: O(1) (constant space).

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Here’s a **detailed explanation** of how the entire code works, broken down into sections:

---

## ✅ 1. `LinkedList` Class

```
class LinkedList:
    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.next = None    # Pointer to the next node (initially None)
```

This class defines a node in a singly linked list. Each node holds:

* `value`: The data it stores.
* `next`: A reference (pointer) to the next node in the list.

---

## ✅ 2. `build_linked_list(data)` Function

This function **constructs a linked list** from a dictionary format. The input dictionary looks like:

```
{
    "head": "0",          # ID of the head node
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        ...
    ]
}
```

### Step-by-step:

```
nodes = {}
for node_data in data["nodes"]:
    node = LinkedList(node_data["value"])
    nodes[node_data["id"]] = node
```

* Creates all nodes and stores them in a dictionary using their `"id"` as keys.
* This allows easy access for linking later.

```
for node_data in data["nodes"]:
    if node_data["next"] is not None:
        nodes[node_data["id"]].next = nodes[node_data["next"]]
```

* Sets the `.next` pointer of each node to point to the node with the `"next"` ID.

```
return nodes[data["head"]]
```

* Returns the **head node** of the constructed linked list.

---

## ✅ 3. `remove_kth_node_from_end(head, k)` Function

Removes the **k-th node from the end** of a singly linked list **in one pass (O(n) time)** and **O(1) space**.

### Key Idea:

* Use two pointers: `first` and `second`
* Move `second` **k steps** ahead of `first`
* Then move both together until `second` hits the end
* Now `first` is just before the node to delete

---

### Detailed Steps:

#### 🔹 Step 1: Initialize pointers

```
first = head
second = head
```

#### 🔹 Step 2: Move `second` k steps ahead

```
while counter <= k:
    second = second.next
    counter += 1
```

* After this loop, `second` is `k` nodes ahead of `first`.

#### 🔹 Step 3: Edge Case – `k` equals length of list

```
if second is None:
    head.value = head.next.value
    head.next = head.next.next
    return
```

* If `second` is `None`, it means we must delete the **head** node.
* To do this in place (since we can't change `head` pointer), we **copy the next node’s value** and **skip the next node**.

#### 🔹 Step 4: Move both pointers until `second.next` is None

```
while second.next is not None:
    second = second.next
    first = first.next
```

* Now, `first.next` is the node to delete.

#### 🔹 Step 5: Skip the target node

```
first.next = first.next.next
```

* This deletes the node by skipping it in the link.

---

## ✅ 4. `print_linked_list(linked_list)` Function

Simple utility to print the values of the list:

```
0 -> 1 -> 2 -> ... -> None
```

It loops through the list using `.next` and prints the `value`.

---

## ✅ 5. Test Data and Output

### Initial Linked List:

```
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
```

### Operation:

```
remove_kth_node_from_end(linked_list, 4)
```

This removes the **4th node from the end**, which is `6` (position index 6, value 6).

### Final Linked List:

```text
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9 -> None
```

✅ Node with value `6` is gone!

---

Here's a **step-by-step ASCII visualization** of how the two-pointer technique removes the **4th node from the end** in the given
linked list:

---

### 🔗 Initial Linked List

```
HEAD
 ↓
[0] → [1] → [2] → [3] → [4] → [5] → [6] → [7] → [8] → [9] → None
```

---

### 🎯 Goal

Remove the **4th node from the end**, which is the node with value **6**.

---

### 🧭 Step 1: Move `second` k=4 nodes ahead

```
first
 ↓
[0] → [1] → [2] → [3] → [4] → [5] → [6] → [7] → [8] → [9] → None
         ↑
       second (4 steps ahead of first)
```

* `second` is 4 steps ahead of `first`.

---

### 🚶 Step 2: Move both `first` and `second` forward together until `second.next == None`

Repeat until `second.next == None`:

1st iteration:

```
       first
        ↓
[0] → [1] → [2] → [3] → [4] → [5] → [6] → [7] → [8] → [9] → None
                                ↑
                              second
```

2nd iteration:

```
             first
              ↓
[0] → [1] → [2] → [3] → [4] → [5] → [6] → [7] → [8] → [9] → None
                                        ↑
                                      second
```

3rd iteration:

```
                   first
                    ↓
[0] → [1] → [2] → [3] → [4] → [5] → [6] → [7] → [8] → [9] → None
                                                ↑
                                              second
```

Now `second.next == None`, so stop.

---

### ✂️ Step 3: Delete the node after `first`

`first` is at node with value **5**, so `first.next` (which is **6**) is deleted:

```
first.next = first.next.next
```

---

### ✅ Final Linked List

```
[0] → [1] → [2] → [3] → [4] → [5] → [7] → [8] → [9] → None
```

Node `[6]` has been removed.

---

Let's visualize the **edge case** where the **head node is removed** — specifically, when `k` equals the length of the list.

---

### 🧪 Example

Let’s say the original linked list is:

```
[0] → [1] → [2] → [3] → [4] → None
```

If `k = 5` (length of list), we are being asked to **remove the 5th node from the end**, which is the **head node [0]**.

---

### 🧭 Step 1: Move `second` k=5 steps ahead

```
first
 ↓
[0] → [1] → [2] → [3] → [4] → None
                         ↑
                      second (after 5 steps)
```

After moving `second` 5 steps forward, it becomes `None`.

---

### ⚠️ Special Case Triggered

```
if second is None:
    head.value = head.next.value
    head.next = head.next.next
```

Because `second` is `None`, we cannot move both pointers anymore.

So, we do this:

### ✂️ Step 2: Copy value from head.next into head

```
Copy value from [1] → into [0] → becomes:

[1] → [1] → [2] → [3] → [4] → None
```

Now remove original [1] by skipping it:

```
head.next = head.next.next
```

---

### ✅ Final Linked List

```
[1] → [2] → [3] → [4] → None
```

So effectively, **the head node was replaced** by its successor — a **common trick** when you must delete a node but can't
update external references to it (e.g., in-place deletion).

"""
