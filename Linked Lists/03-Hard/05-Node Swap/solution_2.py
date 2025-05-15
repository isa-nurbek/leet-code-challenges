# Problem Description:

"""
                                            Node Swap

Write a function that takes in the head of a Singly Linked List, swaps every pair of adjacent nodes in place (i.e., doesn't create
a brand new list), and returns its new head.

If the input Linked List has an odd number of nodes, its final node should remain the same.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

// The head node with value 0
```

## Sample Output:
```
1 -> 0 -> 3 -> 2 -> 5 -> 4 -> None

// The new head node with value 1
```

## Optimal Time & Space Complexity:
```
O(n) time | O(1) space - where `n` is the number of nodes in the Linked List.
```

"""

# =========================================================================================================================== #

# Solution:


class LinkedList:
    def __init__(self, value):
        self.value = value  # Store the value of this node
        self.next = None  # Pointer to the next node (initially None)


# Helper function to convert dictionary to LinkedList
def build_linked_list(data):
    """Builds a linked list from dictionary representation.

    Args:
        data: Dictionary containing 'head' id and 'nodes' list with each node's
              id, value, and next node id.

    Returns:
        The head node of the constructed linked list.
    """
    if not data:
        return None

    # First create all nodes and store them in a dictionary by id
    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    # Then connect the nodes by setting next pointers
    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    return nodes[data["head"]]


# O(n) time | O(1) space
def node_swap(head):
    # Create a dummy node to serve as the new head's predecessor.
    # This helps handle edge cases where the original head is swapped.
    dummy = LinkedList(0)
    dummy.next = head
    prev = dummy  # 'prev' will track the node before the current pair

    while prev.next and prev.next.next:
        # There are at least two nodes left to swap
        first = prev.next  # First node in the pair to swap
        second = prev.next.next  # Second node in the pair to swap

        # Perform the swap:
        # 1. Connect previous node to the second node
        prev.next = second
        # 2. Connect first node to what comes after the second node
        first.next = second.next
        # 3. Connect second node back to the first node
        second.next = first

        # Move 'prev' forward to be before the next pair
        # (which is now the first node, since we just swapped)
        prev = first

    # Return the new head (what comes after dummy)
    return dummy.next


# Function to print the linked list (for verification)
def print_linked_list(linked_list):
    """Prints a linked list in arrow format.

    Args:
        linked_list: Head node of the linked list to print.
    """
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Test case
linked_list_dict = {
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": None, "value": 5},
    ],
}

# Build and print the linked list
linked_list = build_linked_list(linked_list_dict)

result = node_swap(linked_list)

print_linked_list(result)
# Output: 1 -> 0 -> 3 -> 2 -> 5 -> 4 -> None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `node_swap` function, which swaps every two adjacent nodes in a linked list.

### Time Complexity:

- The function iterates through the linked list once, processing nodes in pairs.
- For each pair of nodes, it performs a constant number of operations (pointer updates).
- If the linked list has `n` nodes, the loop runs approximately `n/2` times (since we process two nodes at a time).
- Thus, the time complexity is **O(n)**, where `n` is the number of nodes in the linked list.

### Space Complexity:

- The function uses a constant amount of extra space (`dummy`, `prev`, `first`, and `second` pointers), regardless of the input size.
- No additional data structures or recursive calls are used.
- Thus, the space complexity is **O(1)** (constant space).

### Summary:
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

This is an efficient in-place algorithm for swapping adjacent nodes in a linked list.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break down the code step by step to explain how everything works together to achieve **pairwise swapping of nodes in a linked list**.

---

## ✅ **1. Class Definition**

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

This is a simple `LinkedList` node class:

* Each node contains a `value`.
* And a `next` pointer that points to the **next node** in the linked list.
* Initially, `next` is set to `None`.

---

## ✅ **2. Building a Linked List from a Dictionary**

```
def build_linked_list(data):
    ...
```

This function converts a dictionary (like JSON data) into an actual linked list made of `LinkedList` objects.

### 🔹 Step-by-step:

Suppose we get this dictionary input:

```
{
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        ...
    ]
}
```

### 🔹 Step 1: Create all the nodes and store in a dictionary

```
nodes = {}
for node_data in data["nodes"]:
    node = LinkedList(node_data["value"])
    nodes[node_data["id"]] = node
```

* Creates a `LinkedList` object for each node.
* Maps each node's `id` to the node object.

### 🔹 Step 2: Connect the `next` pointers

```
for node_data in data["nodes"]:
    if node_data["next"] is not None:
        nodes[node_data["id"]].next = nodes[node_data["next"]]
```

* Sets the `next` attribute to the corresponding node using the `id`.

### 🔹 Step 3: Return the head node

```
return nodes[data["head"]]
```

* Returns the node corresponding to the `head` id.

---

## ✅ **3. Swapping Nodes in Pairs (`node_swap`)**

```
def node_swap(head):
    ...
```

This function swaps every **pair of adjacent nodes** in the linked list.

### 🔹 Example Before Swap:

```
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
```

### 🔹 After Swap:

```
1 -> 0 -> 3 -> 2 -> 5 -> 4 -> None
```

### 🔹 Step-by-step explanation:

#### 1. Dummy node

```
dummy = LinkedList(0)
dummy.next = head
prev = dummy
```

* A dummy node is used to simplify edge cases (like when head is being changed).
* `prev` is a pointer used to track the node **before the current pair**.

#### 2. Loop to iterate through pairs

```
while prev.next and prev.next.next:
```

* Loop as long as there are at least two nodes ahead to form a pair.

#### 3. Identify the two nodes in the pair

```
first = prev.next
second = prev.next.next
```

#### 4. Swap the nodes

```
prev.next = second          # previous node now points to second
first.next = second.next    # first now points to node after second
second.next = first         # second points to first (completing the swap)
```

This changes:

```
prev -> first -> second -> next_pair
```

To:

```
prev -> second -> first -> next_pair
```

#### 5. Move the `prev` pointer forward

```
prev = first
```

* `first` is now the second node in the pair after swapping, so `prev` moves to it.

---

## ✅ **4. Printing the Linked List**

```
def print_linked_list(linked_list):
    ...
```

This just traverses the linked list and prints:

```
value -> value -> ... -> None
```

---

## ✅ **5. Test Case**

```
linked_list_dict = {
    "head": "0",
    ...
}
```

You’re building a linked list of 6 nodes:

```
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
```

Then applying the `node_swap` function, the result becomes:

```
1 -> 0 -> 3 -> 2 -> 5 -> 4 -> None
```

---

## ✅ **Summary of Important Concepts**

| Concept                           | Description                                                              |
| --------------------------------- | ------------------------------------------------------------------------ |
| **Dummy Node**                    | Simplifies pointer updates at the head of the list.                      |
| **Two Pointers (first & second)** | Used to identify the pair to be swapped.                                 |
| **Pointer Manipulation**          | Rearranging `next` pointers to swap nodes without changing their values. |
| **O(n) Time**                     | Each node is visited once.                                               |
| **O(1) Space**                    | No extra data structures used, just a few pointers.                      |

---

Here's an **ASCII diagram** to visualize how the **pairwise node swapping** works.

### 🔰 Initial Linked List:

```
[0] -> [1] -> [2] -> [3] -> [4] -> [5] -> None
```

We want to swap every two adjacent nodes, so first `[0]` and `[1]`, then `[2]` and `[3]`, and so on.

---

### 🔄 Step-by-step Swap: First Pair (0 and 1)

**Pointers:**

* `prev` is a dummy node initially pointing to `[0]`.
* `first = [0]`, `second = [1]`

```
dummy -> [0] -> [1] -> [2] -> [3] -> [4] -> [5] -> None
   ^       ^      ^
 prev   first  second
```

**After swap:**

* `prev.next = second`
* `first.next = second.next`
* `second.next = first`

So now:

```
dummy -> [1] -> [0] -> [2] -> [3] -> [4] -> [5] -> None
             ^     ^
           second  first
```

`prev` moves to `first` (which is `[0]`), and the loop continues.

---

### 🔄 Second Pair (2 and 3)

**Pointers:**

* `prev = [0]`
* `first = [2]`, `second = [3]`

```
[0] -> [2] -> [3] -> [4] -> [5] -> None
         ^      ^
      first   second
```

**After swap:**

```
[0] -> [3] -> [2] -> [4] -> [5] -> None
         ^     ^
      second  first
```

---

### 🔄 Third Pair (4 and 5)

**Pointers:**

* `prev = [2]`
* `first = [4]`, `second = [5]`

```
[2] -> [4] -> [5] -> None
         ^      ^
      first   second
```

**After swap:**

```
[2] -> [5] -> [4] -> None
         ^     ^
      second  first
```

---

### ✅ Final List After All Swaps:

```
[1] -> [0] -> [3] -> [2] -> [5] -> [4] -> None
```

---

### 📌 Summary of Node Transitions:

| Original Pair | After Swap  |
| ------------- | ----------- |
| [0] → [1]     | [1] → [0]   |
| [2] → [3]     | [3] → [2]   |
| [4] → [5]     | [5] → [4]   |

"""
