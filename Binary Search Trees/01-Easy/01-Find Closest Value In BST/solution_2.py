# Problem Description:

"""
                                                Find Closest Value In BST

Write a function that takes in a `Binary Search Tree (BST)` and a target integer value and returns the closest value to that target
value contained in the BST.

You can assume that there will only be one closest value.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the BST property: its `value` is strictly greater than the values of every node to its left; its `value` is
less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or None.


## Sample Input:
```
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

target = 12
```

## Sample Output:
```
13
```

## Optimal Time & Space Complexity:
```
Average: O(log(n)) time | O(1) space - where `n` is the number of nodes in the BST.
Worst: O(n) time | O(1) space - where `n` is the number of nodes in the BST.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.left = None  # Reference to the left child node
        self.right = None  # Reference to the right child node


# Function to build a BST from dictionary data
def build_tree(data):
    if not data:  # If data is empty, return None (empty tree)
        return None

    nodes = {}  # Dictionary to store nodes by their IDs

    # First pass: create all node objects
    for node_data in data["nodes"]:
        node = BST(node_data["value"])  # Create new node with value
        nodes[node_data["id"]] = node  # Store node in dictionary with its ID as key

    # Second pass: connect child nodes to their parents
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]  # Get current node

        # If left child exists, connect it
        if node_data["left"] is not None:
            node.left = nodes[node_data["left"]]

        # If right child exists, connect it
        if node_data["right"] is not None:
            node.right = nodes[node_data["right"]]

    # Return the root node (first node in the nodes list)
    return nodes[data["nodes"][0]["id"]]


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def find_closest_value_in_bst(tree, target):
    """Find the value in a binary search tree (BST) that is closest to the target.

    Args:
        tree: The root node of the BST
        target: The target value we're trying to find a closest match for

    Returns:
        The value in the BST that is closest to the target
    """
    # Start the helper function with the tree's root value as initial closest
    return find_closest_value_in_bst_helper(tree, target, tree.value)


def find_closest_value_in_bst_helper(tree, target, closest):
    """Helper function to find the closest value in BST through iterative traversal.

    Args:
        tree: Current node being examined
        target: The target value we're comparing against
        closest: The closest value found so far

    Returns:
        The closest value to target found in the BST
    """
    current_node = tree

    # Traverse the tree while current_node is not None
    while current_node is not None:
        # Update closest if current node's value is closer to target
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value

        # Decide which direction to traverse based on target value
        if target < current_node.value:
            # If target is smaller, go left (BST property: left subtree has smaller values)
            current_node = current_node.left
        elif target > current_node.value:
            # If target is larger, go right (BST property: right subtree has larger values)
            current_node = current_node.right
        else:
            # If we find an exact match, we can break early
            break

    return closest


# Example tree data structure
tree_dict = {
    "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},  # Root node 10
        {"id": "15", "left": "13", "right": "22", "value": 15},  # Right child of root
        {"id": "22", "left": None, "right": None, "value": 22},  # Right child of 15
        {"id": "13", "left": None, "right": "14", "value": 13},  # Left child of 15
        {"id": "14", "left": None, "right": None, "value": 14},  # Right child of 13
        {"id": "5", "left": "2", "right": "5-2", "value": 5},  # Left child of root
        {"id": "5-2", "left": None, "right": None, "value": 5},  # Right child of 5
        {"id": "2", "left": "1", "right": None, "value": 2},  # Left child of 5
        {"id": "1", "left": None, "right": None, "value": 1},  # Left child of 2
    ],
    "root": "10",
}

# The tree structure represented by this dictionary:
#            10
#          /    \
#        5       15
#      /   \     / \
#     2     5   13  22
#    /           \
#   1             14

# Test Case:

# Build the tree
tree = build_tree(tree_dict)

# Find closest value
result = find_closest_value_in_bst(tree, 12)

print(result)  # Output: 13

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `find_closest_value_in_bst` function.

### Time Complexity:

- **Best Case**: O(1) - When the target value is equal to the root node's value, the loop breaks immediately after the first comparison.
- **Average Case**: O(log n) - In a balanced BST, with each comparison, we eliminate half of the remaining tree
(similar to binary search).
- **Worst Case**: O(n) - If the BST is completely unbalanced (essentially a linked list), we might have to traverse all `n` nodes.

### Space Complexity:

- **Best/Average/Worst Case**: O(1) - The algorithm uses a constant amount of additional space (only a few variables like
`current_node` and `closest`), regardless of the input size. No recursion or additional data structures are used.

### Summary:

- **Time Complexity**: O(log n) on average (balanced BST), O(n) in the worst case (unbalanced BST).
- **Space Complexity**: O(1) in all cases.

This is an **iterative** solution, which avoids the recursion stack space that a recursive approach would require (O(log n) on
average for a balanced BST, O(n) in the worst case for an unbalanced BST). Thus, the space complexity is optimized.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Here's a detailed breakdown of our code, explaining each part and how it works together to build a **Binary Search Tree (BST)**
and **find the closest value to a given target**:

---

## 1. **BST Node Class**

```
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### 🔹Purpose:

Defines a **binary search tree node** with:

* A `value`
* A pointer to a `left` child
* A pointer to a `right` child

---

## 2. **Build a BST from Dictionary Data**

```
def build_tree(data):
    if not data:
        return None

    nodes = {}
    ...
```

### 🔹Input:

A dictionary that simulates a tree with:

* `"id"` — Unique string identifier for each node
* `"value"` — Integer value stored in the node
* `"left"` / `"right"` — IDs of left and right children

### 🔹Step-by-Step:

#### 🔸 First Pass: Create all nodes

```
for node_data in data["nodes"]:
    node = BST(node_data["value"])
    nodes[node_data["id"]] = node
```

* Creates each `BST` object
* Stores in a dictionary `nodes` with `id` as key

#### 🔸 Second Pass: Connect children

```
for node_data in data["nodes"]:
    node = nodes[node_data["id"]]

    if node_data["left"] is not None:
        node.left = nodes[node_data["left"]]

    if node_data["right"] is not None:
        node.right = nodes[node_data["right"]]
```

* Links `left` and `right` references using the `id`s

#### 🔸 Return root:

```
return nodes[data["nodes"][0]["id"]]
```

* Assumes the first node in the list is the root

---

## 3. **Finding the Closest Value in BST**

### 🔹Function:

```
def find_closest_value_in_bst(tree, target):
    return find_closest_value_in_bst_helper(tree, target, tree.value)
```

* Calls a helper function with:

  * the tree root
  * the target value
  * initial closest value (starting from root's value)

---

## 4. **Helper Function: Actual Logic**

```
def find_closest_value_in_bst_helper(tree, target, closest):
    current_node = tree

    while current_node is not None:
        ...
```

### 🔹Logic Inside Loop:

```
if abs(target - closest) > abs(target - current_node.value):
    closest = current_node.value
```

* If the current node is closer to the target than the closest seen so far, update `closest`

```
if target < current_node.value:
    current_node = current_node.left
elif target > current_node.value:
    current_node = current_node.right
else:
    break  # Exact match
```

* Standard BST traversal:

  * If target is less, go **left**
  * If greater, go **right**
  * If equal, stop

### 🔹Return:

```
return closest
```

* Returns the closest value found during traversal

---

## 5. **Tree Structure from Dictionary**

```
tree_dict = {
    "nodes": [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "13", "left": None, "right": "14", "value": 13},
        {"id": "14", "left": None, "right": None, "value": 14},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": None, "right": None, "value": 5},
        {"id": "2", "left": "1", "right": None, "value": 2},
        {"id": "1", "left": None, "right": None, "value": 1},
    ],
}
```

* The BST structure built from this has:

  * Root: `10`
  * Left subtree rooted at `5`
  * Right subtree rooted at `15`

---

## 6. **Test Case**

```
tree = build_tree(tree_dict)
result = find_closest_value_in_bst(tree, 12)
print(result)  # Output: 13
```

### 🔹How It Works:

* Target: `12`
* Closest path followed:

  * Start at `10` → `abs(12-10)=2`, closest so far: `10`
  * Move to right → node `15`

    * `abs(12-15)=3` → `closest` stays `10`
  * Move to left → node `13`

    * `abs(12-13)=1` → update `closest` to `13`
  * Move to left → `None` → end

✅ Final closest value: **13**

---

## 🧠 Time and Space Complexity

### 🔹Average Case:

* **Time:** O(log n) – Balanced BST
* **Space:** O(1) – Iterative approach

### 🔹Worst Case:

* **Time:** O(n) – Skewed tree (like a linked list)
* **Space:** O(1)

---

## ✅ Summary

* `build_tree()` builds a `BST` from a dictionary-like data source.
* `find_closest_value_in_bst()` performs an **efficient search** by **navigating** the tree in a way that prunes unnecessary paths.
* The implementation uses **iterative logic** for better space efficiency.

---

Here's an **ASCII visualization** of your Binary Search Tree (BST) structure built from `tree_dict`:

```
           10
         /    \
       5       15
     /   \    /   \
    2     5  13    22
   /           \
  1            14
```

### Explanation:

* **Root** is `10`.
* `10` has:

  * Left child: `5`
  * Right child: `15`
* The left `5` has:

  * Left child: `2`
  * Right child: another `5` (ID `"5-2"`)
* `2` has:

  * Left child: `1`
* `15` has:

  * Left child: `13`, which has a right child `14`
  * Right child: `22`

### Tree traversal from root to find closest to 12:

* Start at `10` (current closest: 10)
* Move right to `15` → difference increases
* Move left to `13` → closer than 10 → update
* Move left from `13` → no node → stop

So, closest value is `13`.

"""
