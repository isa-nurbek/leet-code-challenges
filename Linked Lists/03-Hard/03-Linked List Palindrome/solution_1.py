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


# O(n) time | O(n) space
def linkedList_palindrome(head):
    """
    Main function to check if a linked list is a palindrome.
    Args:
        head: The head node of the linked list
    Returns:
        bool: True if the linked list is a palindrome, False otherwise
    """
    # Start the recursive process with the head node as both left and right pointers
    is_palindrome_results = is_palindrome(head, head)
    # Return the final result which indicates if all outer pairs were equal
    return is_palindrome_results.outer_nodes_are_equal


def is_palindrome(left_node, right_node):
    """
    Recursive helper function to check palindrome property.
    Uses recursion to reach the end of the list and then compares nodes
    while unwinding the recursion stack.

    Args:
        left_node: The node moving forward from the start (left side)
        right_node: The node moving backward from the end (right side)
    Returns:
        LinkedListInfo: An object containing comparison results and next node
    """
    # Base case: we've reached the end of the list
    if right_node is None:
        # When we hit the end, return True (base case) and the left node to compare
        return LinkedListInfo(True, left_node)

    # Recursive case: go all the way to the end of the list first
    recursive_call_results = is_palindrome(left_node, right_node.next)

    # Unpack the results from the recursive call
    left_node_to_compare = recursive_call_results.left_node_to_compare
    outer_nodes_are_equal = recursive_call_results.outer_nodes_are_equal

    # The current comparison result is True only if:
    # 1. All previous outer comparisons were equal (outer_nodes_are_equal)
    # 2. The current left and right nodes have the same value
    recursive_is_equal = (
        outer_nodes_are_equal and left_node_to_compare.value == right_node.value
    )

    # Move the left pointer forward for the next comparison
    next_left_node_to_compare = left_node_to_compare.next

    # Return the current comparison result and the next left node to compare
    return LinkedListInfo(recursive_is_equal, next_left_node_to_compare)


class LinkedListInfo:
    """
    Helper class to store information about the palindrome check:
    - Whether all outer node comparisons so far have been equal
    - The next left node to compare in the next step
    """

    def __init__(self, outer_nodes_are_equal, left_node_to_compare):
        self.outer_nodes_are_equal = outer_nodes_are_equal
        self.left_node_to_compare = left_node_to_compare


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

Let's analyze the time and space complexity of the given `linkedList_palindrome` function.

### **Time Complexity: O(n)**

- The function `is_palindrome` is called recursively for each node in the linked list (once per `right_node` traversal).
- Each recursive call performs a constant amount of work (comparisons and pointer updates).
- Since we traverse the entire linked list once, the time complexity is **O(n)**, where `n` is the number of nodes in the linked list.

### **Space Complexity: O(n)**

- The recursion stack grows proportionally to the length of the linked list because we make a recursive call for each node
(until `right_node` becomes `None`).
- In the worst case (when the list is not a palindrome), we reach the end of the list before unwinding the stack, leading to
**O(n)** space usage.
- If the list is a palindrome, we still use **O(n)** space due to the recursion depth.

### **Summary**
- **Time Complexity:** **O(n)** (linear time, as we visit each node once).
- **Space Complexity:** **O(n)** (due to recursion stack; not constant space because we don’t modify the list in-place).

### **Optimization Note**

This approach uses recursion, which inherently uses **O(n)** space. An alternative **O(1)** space solution (but still **O(n)** time)
would involve:
1. Finding the middle of the linked list (using slow & fast pointers).
2. Reversing the second half in-place.
3. Comparing the first half with the reversed second half.
4. Restoring the list (if required).

This would avoid recursion and reduce space complexity to **O(1)**.
However, the given solution is correct and efficiently solves the problem in **O(n)** time.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code checks whether a given **singly linked list** is a **palindrome**—that is, whether it reads the same forwards and
backwards. Here's a detailed explanation of each part of the code, its structure, and how it works step by step.

---

## 🔧 1. **LinkedList Node Definition**

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

* This is a **custom singly linked list node class**.
* Each node holds a `value` and a reference to the `next` node (`None` by default).

---

## 🏗️ 2. **build_linked_list(data)**

```
def build_linked_list(data):
```

This function constructs the linked list from a **dictionary format** like:

```
{
    "head": "0",
    "nodes": [
        {"id": "0", "next": "1", "value": 0},
        ...
    ]
}
```

### 🔍 How it works:

1. **Create a dictionary of node instances** keyed by their IDs:

   ```
   nodes = {}
   for node_data in data["nodes"]:
       node = LinkedList(node_data["value"])
       nodes[node_data["id"]] = node
   ```

2. **Connect the nodes** using the `next` references:

   ```
   for node_data in data["nodes"]:
       if node_data["next"] is not None:
           nodes[node_data["id"]].next = nodes[node_data["next"]]
   ```

3. **Return the head node**:

   ```
   return nodes[data["head"]]
   ```

---

## 🔁 3. **Recursive Palindrome Check**

### Main function:

```
def linkedList_palindrome(head):
    is_palindrome_results = is_palindrome(head, head)
    return is_palindrome_results.outer_nodes_are_equal
```

* This calls the recursive `is_palindrome` helper to check if the linked list is a palindrome.
* It passes the `head` node twice:

  * One will stay at the front (`left_node`)
  * The other will recurse to the end (`right_node`)

---

## 🔄 4. **Recursive Helper: `is_palindrome()`**

```
def is_palindrome(left_node, right_node):
    if right_node is None:
        return LinkedListInfo(True, left_node)
```

### 🔁 Key idea: **Recursive reverse traversal**

* The recursion **goes to the end of the list** (`right_node` moves to `None`), then
* As it **unwinds**, it compares values from **both ends** inward:

  * `right_node` comes from the **back**
  * `left_node_to_compare` comes from the **front**

### Step-by-step:

1. **Base Case**:

   * When `right_node` is `None`, return:

     ```
     LinkedListInfo(True, left_node)
     ```

     * This means we're at the end, and comparison can begin.

2. **Recursive Call**:

   ```
   recursive_call_results = is_palindrome(left_node, right_node.next)
   ```

   * This walks all the way to the end.

3. **Check value equality while unwinding**:

   ```
   recursive_is_equal = (
       outer_nodes_are_equal and left_node_to_compare.value == right_node.value
   )
   ```

4. **Advance the left pointer (towards center)**:

   ```
   next_left_node_to_compare = left_node_to_compare.next
   ```

5. **Return new `LinkedListInfo` object**:

   ```
   return LinkedListInfo(recursive_is_equal, next_left_node_to_compare)
   ```

---

## 🧱 5. **Support Class: `LinkedListInfo`**

```
class LinkedListInfo:
    def __init__(self, outer_nodes_are_equal, left_node_to_compare):
        self.outer_nodes_are_equal = outer_nodes_are_equal
        self.left_node_to_compare = left_node_to_compare
```

* A container to hold two values:

  * `outer_nodes_are_equal`: Are the outer nodes matched up to this point?
  * `left_node_to_compare`: Move this forward on each recursive return.

---

## 🖨️ 6. **Print Utility Function**

```
def print_linked_list(linked_list):
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
```

* Just prints the list nicely: `0 -> 1 -> 2 -> 2 -> 1 -> 0 -> None`

---

## 🧪 7. **Test Case Input**

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

* This builds the list: `0 -> 1 -> 2 -> 2 -> 1 -> 0`
* This is a **palindrome**, so the output will be:

```
Is palindrome? True
```

---

## ⏱️ Time and Space Complexity

### Time Complexity: **O(n)**

* Each node is visited exactly once during recursion.

### Space Complexity: **O(n)**

* Due to the **recursive call stack** holding `n` frames (1 per node).

---

## ✅ Summary

This code:

* Builds a linked list from a dictionary format.
* Checks if the list is a palindrome using a clever **recursive approach**.
* Uses an inner class to pass multiple values back during recursion.
* Has O(n) time and space complexity.

---

Let's visualize the linked list and how the **recursive palindrome check** works in ASCII.

## 🔗 Linked List Structure

Given this input:

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

### ➤ ASCII Diagram of the Linked List

```
[0] --> [1] --> [2] --> [2] --> [1] --> [0] --> None
 ^                                     ^
Head                                   Tail
```

---

## 🔁 Recursive Palindrome Check (Step-by-Step)

The recursion starts with both `left_node` and `right_node` pointing to the **head**.

### ➤ Step 1: Traverse to the end (recursion goes deep)

Call Stack builds like this:

```
is_palindrome(0, 0)    # right_node = 0
└─ is_palindrome(0, 1)    # right_node = 1
   └─ is_palindrome(0, 2)
      └─ is_palindrome(0, 2)
         └─ is_palindrome(0, 1)
            └─ is_palindrome(0, 0)
               └─ is_palindrome(0, None)  # Base case
```

At the base case:

* `right_node` is `None`
* Return `LinkedListInfo(True, left_node = 0)`

---

### ⬅ Step 2: Backtrack and Compare Values

Now, as the stack unwinds, we compare values from **outside inward**:

```
Unwinding order (right_node):
0  ←  left = 0  →  MATCH
1  ←  left = 1  →  MATCH
2  ←  left = 2  →  MATCH
2  ←  left = 2  →  MATCH
1  ←  left = 1  →  MATCH
0  ←  left = 0  →  MATCH
```

### ASCII Tracking:

```
Comparisons:
[0] == [0]  ✔
 [1] == [1] ✔
  [2] == [2] ✔

Halfway reached, all values match. ✅
```

---

## ✅ Final Result

```
Is palindrome? True
```

"""
