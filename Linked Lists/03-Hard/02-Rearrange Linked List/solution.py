# Problem Description:

"""
                                            Rearrange Linked List

Write a function that takes in the head of a Singly Linked List and an integer `k`, rearranges the list in place (i.e., doesn't
create a brand new list) around nodes with value `k`, and returns its new head.

Rearranging a Linked List around nodes with value `k` means moving all nodes with a value smaller than `k` before all nodes with
value `k` and moving all nodes with a value greater than `k` after all nodes with value `k`.

All moved nodes should maintain their original relative ordering if possible.

Note that the linked list should be rearranged even if it doesn't have any nodes with value `k`.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
head = 3 -> 0 -> 5 -> 2 -> 1 -> 4 -> None
k = 3

// The head node with value 3
```

## Sample Output:
```
0 -> 2 -> 1 -> 3 -> 5 -> 4 -> None

// The new head node with value 0
// Note that the nodes with values 0, 2, and 1 have maintained their original relative ordering,
and so have the nodes with values 5 and 4.
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


# O(n) time | O(1) space
def rearrange_linked_list(head, k):
    # Initialize pointers for three separate linked lists:
    # 1. Nodes with values smaller than k
    # 2. Nodes with values equal to k
    # 3. Nodes with values greater than k
    smaller_list_head = None
    smaller_list_tail = None

    equal_list_head = None
    equal_list_tail = None

    greater_list_head = None
    greater_list_tail = None

    # Traverse the original linked list
    node = head
    while node is not None:
        # Determine which list the current node belongs to based on its value
        if node.value < k:
            # Add to smaller values list
            smaller_list_head, smaller_list_tail = grow_linked_list(
                smaller_list_head, smaller_list_tail, node
            )
        elif node.value > k:
            # Add to greater values list
            greater_list_head, greater_list_tail = grow_linked_list(
                greater_list_head, greater_list_tail, node
            )
        else:
            # Add to equal values list
            equal_list_head, equal_list_tail = grow_linked_list(
                equal_list_head, equal_list_tail, node
            )

        # Move to next node after disconnecting current node from original list
        prev_node = node
        node = node.next
        prev_node.next = None  # Disconnect the node from original list

    # First, connect the smaller and equal lists
    connected_head, connected_tail = connect_linked_lists(
        smaller_list_head, smaller_list_tail, equal_list_head, equal_list_tail
    )

    # Then connect the combined list with the greater list
    final_head, _ = connect_linked_lists(
        connected_head, connected_tail, greater_list_head, greater_list_tail
    )

    return final_head


def grow_linked_list(head, tail, node):
    """
    Helper function to append a node to a linked list.
    Returns the new head and tail of the linked list.
    If the list was empty, the new node becomes both head and tail.
    Otherwise, the node is appended to the end of the list.
    """
    new_head = head
    new_tail = node

    if new_head is None:
        new_head = node  # First node in the list

    if tail is not None:
        tail.next = node  # Append to existing list

    return (new_head, new_tail)


def connect_linked_lists(head_one, tail_one, head_two, tail_two):
    """
    Helper function to connect two linked lists.
    Returns the head and tail of the combined list.
    If either list is empty, returns the other list.
    Otherwise, connects tail of first list to head of second list.
    """
    if head_one is None:
        return head_two, tail_two

    if head_two is None:
        return head_one, tail_one

    # Connect the two lists
    tail_one.next = head_two

    # Return head of first list and tail of second list
    return head_one, tail_two


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
    "head": "3",
    "nodes": [
        {"id": "3", "next": "0", "value": 3},
        {"id": "0", "next": "5", "value": 0},
        {"id": "5", "next": "2", "value": 5},
        {"id": "2", "next": "1", "value": 2},
        {"id": "1", "next": "4", "value": 1},
        {"id": "4", "next": None, "value": 4},
    ],
}

k = 3

# Test Case:

# Build the linked list from dictionary
linked_list = build_linked_list(linked_list_dict)

# Result
result = rearrange_linked_list(linked_list, 3)

print_linked_list(result)
# Output: 0 -> 2 -> 1 -> 3 -> 5 -> 4 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `rearrange_linked_list` function.

### Time Complexity:

1. **Initialization**: The initialization of the six pointers (`smaller_list_head`, `smaller_list_tail`, etc.) is done
in constant time, O(1).
2. **Traversing the Linked List**: The `while` loop iterates over each node in the original linked list exactly once. If there
are `n` nodes in the linked list, this loop runs in O(n) time.
   - Inside the loop, each operation (checking the value, calling `grow_linked_list`, updating `prev_node` and `node`) is done
   in constant time, O(1).
3. **Connecting the Lists**: The `connect_linked_lists` function is called twice, and each call is done in constant time, O(1),
as it just involves updating a few pointers.
   
Overall, the time complexity is dominated by the traversal of the linked list, so the total time complexity is **O(n)**.

### Space Complexity:

1. **Additional Pointers**: The algorithm uses a constant number of additional pointers (like `smaller_list_head`,
`smaller_list_tail`, etc.), which does not depend on the input size. Thus, the space used for these is O(1).
2. **Input and Output**: The input is the linked list of size `n`, and the output is a rearranged linked list of the same size.
However, the rearrangement is done in-place by reusing the existing nodes and only modifying their `next` pointers.
No additional data structures (like arrays or hash maps) are used.

Thus, the space complexity is **O(1)** (constant extra space), as the algorithm does not use any additional space proportional
to the input size.

### Summary:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) (in-place rearrangement)

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through the entire code and understand it **step by step**—what each part does and how the pieces work together
to solve the problem of **rearranging a linked list around a pivot value `k`**.

---

### 🧱 1. **LinkedList Node Class**

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

* This defines a simple **singly linked list node**:

  * `value`: holds the integer value of the node.
  * `next`: a pointer to the next node in the list (default is `None`).

---

### 🏗️ 2. **`build_linked_list` Function**

```
def build_linked_list(data):
    ...
```

* This function **constructs a linked list** from a dictionary containing:

  * `head`: the ID of the head node.
  * `nodes`: a list of dictionaries, where each dictionary represents a node with:

    * `id`: node's unique identifier (used for linking).
    * `value`: the integer value of the node.
    * `next`: the ID of the next node (or `None`).

#### Example Input:

```
{
    "head": "3",
    "nodes": [
        {"id": "3", "next": "0", "value": 3},
        ...
    ]
}
```

#### How it works:

1. **Creates node instances** for each dictionary entry and stores them in a `nodes` dict using their `id`.
2. **Links nodes** using the `next` field by updating the `.next` pointer of each node.
3. **Returns the head node** of the built linked list using the `head` ID.

---

### 🔀 3. **`rearrange_linked_list(head, k)`**

This is the main logic to **rearrange the linked list** so that:

* All nodes with values **less than `k`** come first.
* Then nodes **equal to `k`**.
* Then nodes **greater than `k`**.

And **the relative order in each group is preserved**.

#### Step-by-step logic:

1. **Initialize three separate lists**:

   * `smaller_list_head` and `smaller_list_tail`: for values `< k`
   * `equal_list_head` and `equal_list_tail`: for values `== k`
   * `greater_list_head` and `greater_list_tail`: for values `> k`

2. **Traverse the original list**, and place each node into one of the three lists using the `grow_linked_list()` helper.

3. **Break the original list** by setting `prev_node.next = None` to avoid unwanted links.

4. **Connect the three lists together** using `connect_linked_lists()`:

   * First connect smaller + equal
   * Then connect that result with greater

5. **Return the new head** of the rearranged list.

---

### 🌿 4. **`grow_linked_list(head, tail, node)`**

```
def grow_linked_list(head, tail, node):
    new_head = head
    new_tail = node

    if new_head is None:
        new_head = node

    if tail is not None:
        tail.next = node

    return (new_head, new_tail)
```

* Adds a `node` to the end of a list.
* Returns the new head and tail after adding.

---

### 🔗 5. **`connect_linked_lists(head_one, tail_one, head_two, tail_two)`**

* Concatenates two linked lists:

  * If the first list is empty, return the second.
  * Otherwise, connect `tail_one.next` to `head_two`.

---

### 🖨️ 6. **`print_linked_list(head)`**

* Utility function to **print the linked list** for visual verification.

---

### 🧪 Test Case

Given the dictionary input and `k = 3`:

**Original List** (based on the IDs and values):

```
3 -> 0 -> 5 -> 2 -> 1 -> 4 -> None
```

**Values and groups:**

* `< 3`: 0, 2, 1
* `== 3`: 3
* `> 3`: 5, 4

**Rearranged List:**

```
0 -> 2 -> 1 -> 3 -> 5 -> 4 -> None
```

Which is exactly what the function prints.

---

### ✅ Summary

This code:

* **Parses a dictionary representation** of a linked list.
* **Rearranges nodes** into three parts based on a pivot value `k`.
* **Preserves the relative order** in each group.
* **Returns the new head** of the reordered list.

---

Here’s an **ASCII diagram** to help you **visualize how the linked list is rearranged around `k = 3`**, based on the test case provided.

---

### 🔢 Input Dictionary Data (Visualized)

**Node Definitions** from the input:

```
{
    "head": "3",
    "nodes": [
        {"id": "3", "next": "0", "value": 3},
        {"id": "0", "next": "5", "value": 0},
        {"id": "5", "next": "2", "value": 5},
        {"id": "2", "next": "1", "value": 2},
        {"id": "1", "next": "4", "value": 1},
        {"id": "4", "next": None, "value": 4},
    ]
}
```

### 🧭 Original Linked List:

```
[3] --> [0] --> [5] --> [2] --> [1] --> [4] --> None
```

### 📊 Partition Based on `k = 3`:

Split into three buckets:

**< 3 (Smaller):**

```
[0] --> [2] --> [1] --> None
```

**== 3 (Equal):**

```
[3] --> None
```

**> 3 (Greater):**

```
[5] --> [4] --> None
```

---

### 🔗 After Rearranging (Merged Lists):

Merge order:

1. Smaller + Equal → `[0] --> [2] --> [1] --> [3]`
2. Result + Greater → `[0] --> [2] --> [1] --> [3] --> [5] --> [4]`

### ✅ Final Output:

```
[0] --> [2] --> [1] --> [3] --> [5] --> [4] --> None
```

---

### 🔁 Node Flow Visualization:

```
Original:
  [3] --> [0] --> [5] --> [2] --> [1] --> [4] --> None

After Rearranging with k=3:
       +---------+
       |         |
       v         v
<k:  [0] --> [2] --> [1]
==k:                        [3]
>k:                                 [5] --> [4]

Merged Final:
[0] --> [2] --> [1] --> [3] --> [5] --> [4] --> None
```

"""
