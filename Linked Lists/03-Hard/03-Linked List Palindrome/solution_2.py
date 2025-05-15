# Problem Description:

"""
                                            Linked List Palindrome

Write a function that takes in the head of a Singly Linked List and returns a `boolean` representing whether the linked list's
nodes form a palindrome. Your function shouldn't make use of any auxiliary data structure.

A palindrome is usually defined as a string that's written the same `forward` and `backward`. For a linked list's nodes to form
a palindrome, their values must be the same when read from left to right and from right to left.
> Note that single-character strings are palindromes, which means that single-node linked lists form palindromes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input linked list will always have at least one node; in other words, the head will never be `None`.


## Sample Input:
```
head = 0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None

// The head node with value 0
```

## Sample Output:
```
True
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
def linkedList_palindrome(head):
    # Edge case: empty list or single node is always a palindrome
    if not head or not head.next:
        return True

    # Step 1: Find the middle of the linked list using slow and fast pointers
    # Slow moves 1 step at a time, fast moves 2 steps
    # When fast reaches end, slow will be at middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    # We'll reverse starting from the middle node (slow)
    prev = None
    current = slow
    while current:
        # Store next node before we overwrite current.next
        next_node = current.next
        # Reverse the link
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_node
    # After loop, prev will be the head of reversed second half

    # Step 3: Compare the first half with the reversed second half
    left = head  # Pointer to start of first half
    right = prev  # Pointer to start of reversed second half
    is_palindrome = True
    while right:
        if left.value != right.value:
            is_palindrome = False
            break
        left = left.next
        right = right.next

    # Step 4 (Optional): Restore the original list by reversing the second half back
    # This is good practice when you don't want to modify input data structure
    current = prev  # prev is head of reversed second half
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    # Reattach the restored second half to the middle node
    slow.next = prev

    return is_palindrome


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
        {"id": "2", "next": "2-2", "value": 2},
        {"id": "2-2", "next": "1-2", "value": 2},
        {"id": "1-2", "next": "0-2", "value": 1},
        {"id": "0-2", "next": None, "value": 0},
    ],
}

# Test Case:

# Build and print the linked list
linked_list = build_linked_list(linked_list_dict)

print("Linked list:")
print_linked_list(linked_list)

# Check if palindrome
is_palindrome = linkedList_palindrome(linked_list)
print("\nIs palindrome?", is_palindrome)

# Output:

"""
Linked list:
0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None

Is palindrome? True

"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the `linkedList_palindrome` function step by step.

### Time Complexity:

1. **Finding the middle of the linked list (Step 1):**
   - The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps at a time.
   - This takes `O(n/2)` time, which simplifies to `O(n)`.

2. **Reversing the second half of the linked list (Step 2):**
   - We reverse the second half of the list starting from the `slow` pointer.
   - This also takes `O(n/2)` time, which simplifies to `O(n)`.

3. **Comparing the first half with the reversed second half (Step 3):**
   - We compare up to `n/2` nodes in the worst case.
   - This takes `O(n/2)` time, which simplifies to `O(n)`.

4. **(Optional) Restoring the linked list (Step 4):**
   - We reverse the second half back to its original order.
   - This takes `O(n/2)` time, which simplifies to `O(n)`.

**Total Time Complexity:**
- `O(n) + O(n) + O(n) + O(n) = O(n)`.
- The dominant term is linear, so the overall time complexity is `O(n)`.

### Space Complexity:

- The algorithm uses a constant amount of extra space for pointers (`slow`, `fast`, `prev`, `current`, `next_node`, `left`, `right`, etc.).
- No additional data structures (like stacks or arrays) are used.
- Thus, the space complexity is `O(1)` (constant space).

### Summary:
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Note:
The optional step (Step 4) restores the linked list to its original state, which is good practice if you don't want to modify the
input data structure. However, if you don't care about restoring the list, you can omit Step 4, and the time complexity remains
`O(n)` (since `O(n)` still dominates). The space complexity remains `O(1)` either way.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Here’s a **detailed explanation** of how the given Python code works, broken down into components:

---

## 🧱 1. **LinkedList Class**

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

This defines a **Node** in a singly linked list:

* `value` stores the node's data.
* `next` is a pointer to the next node (initialized to `None`).

---

## 🔨 2. **build_linked_list(data)**

### Purpose:

Constructs a linked list from a dictionary that specifies:

* The ID of the `head` node.
* A list of node definitions, each with `id`, `value`, and `next`.

### Step-by-step:

```
def build_linked_list(data):
    if not data:
        return None
```

Returns `None` if the input is empty.

```
nodes = {}
for node_data in data["nodes"]:
    node = LinkedList(node_data["value"])
    nodes[node_data["id"]] = node
```

* Create all `LinkedList` nodes first and store them in a dictionary using their `id` as keys.
* This allows **random access** by ID when linking nodes.

```
for node_data in data["nodes"]:
    if node_data["next"] is not None:
        nodes[node_data["id"]].next = nodes[node_data["next"]]
```

* Connect each node’s `next` pointer using the ID from `next`.

```
return nodes[data["head"]]
```

* Returns the actual **head node** by looking it up using the `"head"` ID.

---

## 🧪 3. **Test Input Data**

```
linked_list_dict = {
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "2-2", "value": 2},
        {"id": "2-2", "next": "1-2", "value": 2},
        {"id": "1-2", "next": "0-2", "value": 1},
        {"id": "0-2", "next": None, "value": 0},
    ],
}
```

This represents the linked list:

```
0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None
```

Which **is a palindrome**: the list reads the same forward and backward.

---

## 🧠 4. **linkedList_palindrome(head)**

### Objective:

Checks whether the linked list is a **palindrome** using:

* O(n) time
* O(1) space (in-place operations)

### ✅ Steps:

#### **Step 1: Find the middle**

```
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

* Uses the **slow & fast pointer** technique.
* When `fast` reaches the end, `slow` will be at the **middle**.

For:

```
0 -> 1 -> 2 -> 2 -> 1 -> 0
```

`slow` ends on the **first 2** (the fourth node), which is the start of the second half.

---

#### **Step 2: Reverse the second half**

```
prev = None
current = slow
while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
```

* Reverses the second half of the list starting from `slow`.
* After reversing:

```
0 <- 1 <- 2   (prev points to 0, the new head of reversed half)
```

---

#### **Step 3: Compare first and second half**

```
left = head
right = prev
is_palindrome = True
while right:
    if left.value != right.value:
        is_palindrome = False
        break
    left = left.next
    right = right.next
```

* Compares values from the beginning (`left`) and from the reversed second half (`right`).
* If all values match, it’s a **palindrome**.

---

#### **Step 4 (Optional): Restore the original list**

```
current = prev
prev = None
while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
slow.next = prev
```

* Restores the second half to its original order to keep the input list unchanged.
* Optional but useful if you don't want to **mutate** the original list structure.

---

## 🖨️ 5. **print_linked_list(linked_list)**

Simple utility function to print the list in:

```
value -> value -> ... -> None
```

format for verification.

---

## ✅ Output:

```
Linked list:
0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None

Is palindrome? True
```

Correct! The list is a **palindrome**.

---

## 📌 Summary:

* The code constructs a linked list from a structured dictionary.
* It then checks if the list is a palindrome using an efficient in-place method.
* The `linkedList_palindrome` function works in **O(n)** time and **O(1)** space by reversing the second half of the list
temporarily for comparison.

---

Here’s a detailed **ASCII visualization** of how the code works at each step when checking whether the linked list is a palindrome:

### 📦 Input List (From `linked_list_dict`)

```
Step 0: Original Linked List

[0] -> [1] -> [2] -> [2] -> [1] -> [0] -> None
```

Each node points to the next node, forming a singly linked list.

---

### 🐢🐇 Step 1: Find the Middle (Slow & Fast Pointers)

```
Initial:
slow = [0]
fast = [0]

After 1st iteration:
slow = [1]
fast = [2]

After 2nd iteration:
slow = [2]       ← Middle of the list
fast = [1]

After 3rd iteration:
slow = [2]       ← (Already moved to middle)
fast = None      ← End reached
```

---

### 🔄 Step 2: Reverse the Second Half

Start from the middle node (`slow = [2]`) and reverse to the end.

```
Before Reversal:
[0] -> [1] -> [2] -> [2] -> [1] -> [0] -> None
                      ↑
                    slow

Reversing second half:
(1st step): [2] → None
(2nd step): [1] → [2]
(3rd step): [0] → [1] → [2]

After Reversal:
Reversed half:
[0] -> [1] -> [2] -> None
          ↑
        prev (new head of reversed second half)

Original first half (unchanged):
[0] -> [1] -> [2]
```

---

### 🔍 Step 3: Compare Both Halves

Compare:

* Left: [0] -> [1] -> [2]
* Right (reversed): [0] -> [1] -> [2]

```
Compare:
left:  [0] == right: [0] → match
left:  [1] == right: [1] → match
left:  [2] == right: [2] → match

→ All matched ⇒ It's a palindrome ✅
```

---

### 🔁 Step 4: Restore the List (Optional)

Reverse the second half **back** to original:

```
Before restoring:
First Half:  [0] -> [1] -> [2]
Second Half: [0] -> [1] -> [2]

Restoring:
(1st step): [1] → [0]
(2nd step): [2] → [1] → [0]

Reattached list:
[0] -> [1] -> [2] -> [2] -> [1] -> [0] -> None
```

Now the linked list is restored to its **original structure**.

---

### ✅ Final Output:

```
Linked list:
0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None

Is palindrome? True
```

"""
