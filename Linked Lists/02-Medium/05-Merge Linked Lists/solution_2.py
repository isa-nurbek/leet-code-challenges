# Problem Description:

"""
                                            Merge Linked Lists

Write a function that takes in the heads of two Singly Linked Lists that are in `sorted order`, respectively. The function should
merge the lists in place (i.e., it shouldn't create a brand new list) and return the head of the merged list; the merged list
should be in `sorted order`.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` if it's
the tail of the list.

You can assume that the input linked lists will always have at least one node; in other words, the heads will never be `None`.


## Sample Input:
```
head_one = 2 -> 6 -> 7 -> 8 -> None              // the head node with value 2
head_two = 1 -> 3 -> 4 -> 5 -> 9 -> 10 -> None   // the head node with value 1
```

## Sample Output:
```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None  // the new head node with value 1
```

## Optimal Time & Space Complexity:
```
O(n + m) time | O(1) space - where `n` is the number of nodes in the first Linked List and
`m` is the number of nodes in the second Linked List.

```

"""

# =========================================================================================================================== #

# Solution:


class LinkedList:
    """Node class for a singly linked list."""

    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.next = None  # Pointer to the next node (initially None)


# Helper function to convert dictionary to LinkedList
def build_linked_list(data):
    """Builds a linked list from a dictionary representation.

    Args:
        data: Dictionary with 'head' (id of head node) and 'nodes' (list of node dicts).

    Returns:
        The head node of the constructed linked list, or None if data is empty.
    """
    if not data:
        return None

    # Create all nodes and store them in a dictionary by ID
    nodes = {}
    for node_data in data["nodes"]:
        node = LinkedList(node_data["value"])
        nodes[node_data["id"]] = node

    # Connect nodes using 'next' pointers
    for node_data in data["nodes"]:
        if node_data["next"] is not None:
            nodes[node_data["id"]].next = nodes[node_data["next"]]

    return nodes[data["head"]]  # Return the head node

# O(n + m) time | O(1) space
def merge_linked_lists(head_one, head_two):
    """
    Merges two sorted linked lists into one sorted linked list.

    Args:
        head_one: Head node of the first sorted linked list
        head_two: Head node of the second sorted linked list

    Returns:
        Head node of the merged sorted linked list
    """

    # Edge case: If one list is empty, return the other
    if head_one is None:
        return head_two
    if head_two is None:
        return head_one

    # Determine which head should be the new head (the smaller one)
    if head_one.value < head_two.value:
        # Merge with head_one as the starting node
        recursive_merge(head_one, head_two, None)
        return head_one
    else:
        # Merge with head_two as the starting node
        recursive_merge(head_two, head_one, None)
        return head_two


def recursive_merge(p1, p2, p1_prev):
    """
    Recursively merges two linked lists by rearranging their nodes in sorted order.

    Args:
        p1: Current node from the primary list (the list we're merging into)
        p2: Current node from the secondary list (the list we're merging from)
        p1_prev: Previous node from the primary list (used to rewire pointers)
    """

    # Base case: If we've reached end of primary list, attach rest of secondary list
    if p1 is None:
        p1_prev.next = p2
        return

    # Base case: If we've reached end of secondary list, we're done
    if p2 is None:
        return

    if p1.value < p2.value:
        # p1 is smaller, keep it and move forward in primary list
        recursive_merge(p1.next, p2, p1)
    else:
        # p2 is smaller, we need to insert it before p1

        # First save p2's next node before we overwrite it
        new_p2 = p2.next

        # If there was a previous node in primary list, rewire it to point to p2
        if p1_prev is not None:
            p1_prev.next = p2

        # Insert p2 before p1 in the merged list
        p2.next = p1

        # Continue merging with p1 in its new position and new_p2 as next in secondary list
        recursive_merge(p1, new_p2, p2)


# Function to print the linked list (for verification)
def print_linked_list(head):
    """Prints the linked list in a readable format.

    Args:
        head: The head node of the linked list to print.
    """
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Test Case 1: Two non-empty sorted lists
linked_list_dict_one = {
    "head": "2",
    "nodes": [
        {"id": "2", "next": "6", "value": 2},
        {"id": "6", "next": "7", "value": 6},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": None, "value": 8},
    ],
}

linked_list_dict_two = {
    "head": "1",
    "nodes": [
        {"id": "1", "next": "3", "value": 1},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "9", "value": 5},
        {"id": "9", "next": "10", "value": 9},
        {"id": "10", "next": None, "value": 10},
    ],
}

# Build and merge the lists
list_one = build_linked_list(linked_list_dict_one)
list_two = build_linked_list(linked_list_dict_two)
merged_list = merge_linked_lists(list_one, list_two)

print("Merged List:")
print_linked_list(merged_list)
# Merged List: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → None

# Test Case 2: One list is empty
empty_list = None
merged_with_empty = merge_linked_lists(empty_list, list_two)

print("\nMerged with Empty List:")
print_linked_list(merged_with_empty)
# Merged with Empty List: 1 → 3 → 4 → 5 → 9 → 10 → None

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `merge_linked_lists` function and its helper `recursive_merge`.

### Time Complexity:

1. **Best Case**: When one list is empty - O(1) (just return the other list)
2. **Worst/Average Case**: 
   - The function processes each node of both lists exactly once.
   - If `n` is the length of the first list and `m` is the length of the second list, the time complexity is **O(n + m)**
   because each recursive call processes one node from either `p1` or `p2`.

### Space Complexity:

1. **Best Case**: When one list is empty - O(1) (no recursion needed)
2. **Worst/Average Case**:
   - The recursion depth is at most `n + m` (if we alternate between `p1` and `p2` in each call).
   - Thus, the space complexity is **O(n + m)** due to the recursion stack.


### Summary:
| Complexity  | Time     | Space    |
|-------------|----------|----------|
| **Best**    | O(1)     | O(1)     |
| **Worst**   | O(n + m) | O(n + m) |

### Optimization Note:
- This implementation uses **recursion**, which incurs additional space for the call stack. An **iterative approach** would
reduce the space complexity to **O(1)** (just a few pointers) while maintaining the same time complexity.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's break this code down step by step, starting from the class definition to the final test case. This code constructs **singly
linked lists**, merges two **sorted** linked lists, and prints them. The merge is done **recursively and in-place** (without
creating new nodes).

---

## 🔹 1. `LinkedList` Class

```
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
```

This defines a **node** in a singly linked list:

* `value`: holds the data (an integer).
* `next`: points to the next node in the list (`None` by default).

---

## 🔹 2. `build_linked_list(data)`

This function builds a linked list from a **dictionary representation**, which is useful for testing.

### Example input:

```
{
  "head": "2",
  "nodes": [
      {"id": "2", "next": "6", "value": 2},
      {"id": "6", "next": "7", "value": 6},
      {"id": "7", "next": "8", "value": 7},
      {"id": "8", "next": None, "value": 8},
  ]
}
```

### Steps:

1. **Create all nodes** using their `id` and `value`. Store them in a dictionary:

   ```
   nodes = {
       "2": LinkedList(2),
       "6": LinkedList(6),
       ...
   }
   ```
2. **Connect the nodes** using the `next` references (`id`s):

   ```
   nodes["2"].next = nodes["6"]
   nodes["6"].next = nodes["7"]
   ...
   ```
3. **Return the head node**:

   ```
   return nodes["2"]
   ```

---

## 🔹 3. `merge_linked_lists(head_one, head_two)`

Merges **two sorted linked lists** into one **sorted** list.

### Logic:

* If either list is empty (`None`), return the other.
* Compare the head values:

  * If `head_one.value < head_two.value`, use `head_one` as the base and call `recursive_merge`.
  * Otherwise, use `head_two` as the base and call `recursive_merge`.

### Example:

```
list_one: 2 → 6 → 7 → 8
list_two: 1 → 3 → 4 → 5 → 9 → 10
```

Since `1 < 2`, we call:

```
recursive_merge(p1=1, p2=2, p1_prev=None)
```

and return `list_two`'s head (`1`) as the merged list's head.

---

## 🔹 4. `recursive_merge(p1, p2, p1_prev)`

This function recursively merges the lists **in-place**, assuming `p1` is the current node in the base list and `p2` is from
the other list.

### Parameters:

* `p1`: current node in base list
* `p2`: current node from other list
* `p1_prev`: previous node before `p1` (helps in linking when `p2` needs to be inserted before `p1`)

### Cases:

1. **`p1` is `None`**: End of base list — attach remaining `p2` list to `p1_prev.next`.
2. **`p2` is `None`**: Nothing more to merge.
3. **If `p1.value < p2.value`**:

   * Move forward in base list: `recursive_merge(p1.next, p2, p1)`
4. **Else (`p2.value <= p1.value`)**:

   * Insert `p2` before `p1`.
   * Set `p1_prev.next = p2` (if `p1_prev` exists).
   * Save `p2.next` to `new_p2`.
   * Set `p2.next = p1`.
   * Recurse: `recursive_merge(p1, new_p2, p2)`

### Example Flow (Initial):

```
list1: 2 → 6 → 7 → 8
list2: 1 → 3 → 4 → 5 → 9 → 10

Start: merge_linked_lists(2, 1)
Result: merged head = 1
Now recursively insert 2, 6, 7, 8 into the proper places.
```

---

## 🔹 5. `print_linked_list(head)`

This utility function prints the linked list like:

```
1 -> 2 -> 3 -> ... -> None
```

---

## 🔹 6. Test Case 1

**Merging two non-empty sorted lists**

```
linked_list_dict_one = { ... }
linked_list_dict_two = { ... }
```

Build both linked lists and merge them:

```
list_one = build_linked_list(linked_list_dict_one)
list_two = build_linked_list(linked_list_dict_two)
merged_list = merge_linked_lists(list_one, list_two)
```

### Output:

```
Merged List:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
```

---

## 🔹 7. Test Case 2

**Merging an empty list with a non-empty list**

```
empty_list = None
merged_with_empty = merge_linked_lists(empty_list, list_two)
```

### Output:

```
Merged with Empty List:
1 -> 3 -> 4 -> 5 -> 9 -> 10 -> None
```

---

## ✅ Summary

| Component              | Purpose                                        |
| ---------------------- | ---------------------------------------------- |
| `LinkedList` class     | Represents a single node in a linked list      |
| `build_linked_list()`  | Converts a dictionary to an actual linked list |
| `merge_linked_lists()` | Entry point to merge two sorted lists          |
| `recursive_merge()`    | Recursively merges two lists in-place          |
| `print_linked_list()`  | Prints the list in a readable format           |

This is a clean, recursive, **in-place merge** of two sorted linked lists without creating new nodes.

"""
