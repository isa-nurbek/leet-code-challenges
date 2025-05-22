# Problem Description:

"""
                                                Validate Three Nodes

You're given `three nodes` that are contained in the same `Binary Search Tree`: `node_one`, `node_two`, and `node_three`. Write a
function that returns a boolean representing whether one of `node_one` or `node_three` is an ancestor of `node_two` and the other
node is a descendant of `node_two`. For example, if your function determines that `node_one` is an ancestor of `node_two`, then it
needs to see if `node_three` is a descendant of `node_two`. If your function determines that `node_three` is an ancestor, then it
needs to see if `node_one` is a descendant.

A *descendant* of a node `N` is defined as a node contained in the tree rooted at `N`. A node `N` is an ancestor of another node
`M` if `M` is a descendant of `N`.

It isn't guaranteed that `node_one` or `node_three` will be ancestors or descendants of `node_two`, but it is guaranteed that all
three nodes will be unique and will never be `None`. In other words, you'll be given valid input nodes.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
tree =    5
       /     \
      2       7
    /   \   /   \
   1     4 6     8
  /     /
 0     3  

// This tree won't actually be passed as an input; it's here to help you visualize the problem.

node_one = 5  // The actual node with value 5.
node_two = 2  // The actual node with value 2.
node_three = 3  // The actual node with value 3.
```

## Sample Output:
```
True 

// node_one is an ancestor of node_two, and node_three is a descendant of node_two.
```

## Optimal Time & Space Complexity:
```
O(d) time | O(1) space - where `d` is the distance between `node_one` and `node_three`.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value, left=None, right=None):
        # Binary Search Tree node constructor
        self.value = value  # The value stored in the node
        self.left = left  # Left child node
        self.right = right  # Right child node


def build_tree(data):
    # Builds a BST from dictionary representation
    if not data:
        return None  # Empty tree if no data

    # Create all nodes first and store them in a dictionary by their IDs
    nodes = {}
    for node_data in data["nodes"]:
        node = BST(node_data["value"])
        nodes[node_data["id"]] = node

    # Connect the nodes by setting left and right children based on the IDs
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]
        if node_data["left"] is not None:
            node.left = nodes[node_data["left"]]
        if node_data["right"] is not None:
            node.right = nodes[node_data["right"]]

    # Return the root node of the tree
    return nodes[data["root"]]


# O(h) time | O(1) space
def validate_three_nodes(node_one, node_two, node_three):
    """
    Validates if one of two relationships exists between three nodes in a BST:
    1. node_one is ancestor of node_two, and node_two is ancestor of node_three
    2. node_three is ancestor of node_two, and node_two is ancestor of node_one

    Args:
        node_one: First node in BST
        node_two: Second node in BST
        node_three: Third node in BST

    Returns:
        True if either of the two relationships exists, False otherwise
    """
    # Check if node_two is a descendant of node_one
    if is_descendant(node_two, node_one):
        # If yes, check if node_three is a descendant of node_two
        # This validates relationship 1: node_one -> node_two -> node_three
        return is_descendant(node_three, node_two)

    # Check if node_two is a descendant of node_three
    if is_descendant(node_two, node_three):
        # If yes, check if node_one is a descendant of node_two
        # This validates relationship 2: node_three -> node_two -> node_one
        return is_descendant(node_one, node_two)

    # If neither relationship exists, return False
    return False


def is_descendant(node, target):
    """
    Checks if target node is an ancestor of given node in a BST (if node is descendant of target)

    Args:
        node: The potential descendant node to start searching from
        target: The potential ancestor node we're looking for

    Returns:
        True if target is ancestor of node (node is descendant of target), False otherwise
    """
    # Traverse from node upwards towards root looking for target
    while node is not None and node is not target:
        # BST property: if target value is less than current node value,
        # search in left subtree, otherwise search right subtree
        node = node.left if target.value < node.value else node.right

    # If we found the target, return True (node is descendant)
    # If we hit None, return False (target is not ancestor)
    return node is target


# Tree representation as a dictionary
tree_dict = {
    "nodes": [
        {"id": "0", "left": None, "right": None, "value": 0},
        {"id": "1", "left": "0", "right": None, "value": 1},
        {"id": "2", "left": "1", "right": "4", "value": 2},
        {"id": "3", "left": None, "right": None, "value": 3},
        {"id": "4", "left": "3", "right": None, "value": 4},
        {"id": "5", "left": "2", "right": "7", "value": 5},
        {"id": "6", "left": None, "right": None, "value": 6},
        {"id": "7", "left": "6", "right": "8", "value": 7},
        {"id": "8", "left": None, "right": None, "value": 8},
    ],
    "root": "5",  # Root node ID
}


# Build the tree from the dictionary
root = build_tree(tree_dict)

# Test Case: validate_three_nodes(5, 2, 3)

node_one = root  # 5 (root node)
node_two = root.left  # 2
node_three = root.left.right.left  # 3

print(validate_three_nodes(node_one, node_two, node_three))
# Output: True

# Visual representation of the tree:
#            5
#         /     \
#        2       7
#      /   \   /   \
#     1     4 6     8
#    /     /
#   0     3

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

### Time Complexity:

1. **`is_descendant(node, target)` function**:
   - This function traverses from `node` to `target` in a BST.
   - In the worst case, this is an O(h) operation, where `h` is the height of the tree. This is because we might traverse from
   the root to a leaf (or vice versa) in the worst case.

2. **`validate_three_nodes(node_one, node_two, node_three)` function**:
   - This function calls `is_descendant` up to 2 times (in the worst case).
   - The first call (`is_descendant(node_two, node_one)`) is O(h).
   - If the first condition is true, it calls `is_descendant(node_three, node_two)`, which is another O(h) operation.
   - Similarly, if the second condition is checked, it calls `is_descendant` twice again (each O(h)).
   - Thus, the total time complexity is **O(h)** (since we perform a constant number of O(h) operations).

### Space Complexity:

- Both functions use **constant extra space** (no recursion, no additional data structures). The traversal is done iteratively.
- Thus, the space complexity is **O(1)**.

### Summary:
- **Time Complexity:** O(h) (where h is the height of the BST).
- **Space Complexity:** O(1).

### Notes:
- In a balanced BST, `h = O(log n)`, where `n` is the number of nodes.
- In the worst case (unbalanced BST, like a linked list), `h = O(n)`.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's go through our code step-by-step to fully understand how it works and what each part does. We're building a **Binary Search
Tree (BST)** and implementing a function that checks if one of three nodes is in between the other two in the BST hierarchy.

---

### 📌 1. **`class BST` — Tree Node Definition**

```
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

* This is a basic class for a node in a binary search tree.
* Each node stores:

  * `value`: the integer value of the node.
  * `left`: reference to the left child node.
  * `right`: reference to the right child node.

---

### 📌 2. **`build_tree(data)` — Constructing the Tree**

```
def build_tree(data):
    if not data:
        return None
```

* This function takes a **dictionary** representation of a tree and constructs the actual tree using `BST` node objects.

#### Step-by-step:

```
nodes = {}
for node_data in data["nodes"]:
    node = BST(node_data["value"])
    nodes[node_data["id"]] = node
```

* First, all nodes are created individually and stored in a dictionary with their IDs as keys (so we can easily look them up later).

```
for node_data in data["nodes"]:
    node = nodes[node_data["id"]]
    if node_data["left"] is not None:
        node.left = nodes[node_data["left"]]
    if node_data["right"] is not None:
        node.right = nodes[node_data["right"]]
```

* Then the left and right children are connected using the IDs.

```
return nodes[data["root"]]
```

* Finally, the function returns the root node using the root ID from the dictionary.

---

### 📌 3. **`validate_three_nodes(node_one, node_two, node_three)`**

```
def validate_three_nodes(node_one, node_two, node_three):
    if is_descendant(node_two, node_one):
        return is_descendant(node_three, node_two)

    if is_descendant(node_two, node_three):
        return is_descendant(node_one, node_two)

    return False
```

This function checks:

* If **`node_two`** is in between **`node_one`** and **`node_three`** in the BST hierarchy.

How?

* First checks if `node_two` is a descendant of `node_one`, and if so, whether `node_three` is a descendant of `node_two`.
If yes, then the order is `node_one` → `node_two` → `node_three`.
* Then checks the reverse: `node_three` → `node_two` → `node_one`.

This logic ensures that `node_two` lies in the path between the other two nodes.

---

### 📌 4. **`is_descendant(node, target)`**

```
def is_descendant(node, target):
    while node is not None and node is not target:
        node = node.left if target.value < node.value else node.right

    return node is target
```

This function checks if `target` is a descendant of `node`.

It uses the property of BSTs:

* If `target.value` is smaller than `node.value`, go left.
* If `target.value` is greater, go right.
* Stop when you reach the target or hit `None`.

Time complexity is **O(h)** where `h` is the height of the tree.

---

### 📌 5. **Test Tree Structure & Use Case**

#### Tree Dict:

```
tree_dict = {
    "nodes": [...],  # Describes nodes and their left/right child by ID
    "root": "5"
}
```

This dictionary represents the tree visually as:

```
          5
        /   \
       2     7
     /  \   / \
    1    4 6   8
   /    /
  0    3
```

### 📌 6. **Test Case Analysis**

```
node_one = root              # Node 5
node_two = root.left         # Node 2
node_three = root.left.right.left  # Node 3
```

Checking:

* Is 2 a descendant of 5? ✅ (5 → 2)
* Is 3 a descendant of 2? ✅ (2 → 4 → 3)

Result: `True`

---

### ✅ Final Output

```
print(validate_three_nodes(node_one, node_two, node_three))  # True
```

This confirms that **Node 2 lies between Node 5 and Node 3** in the BST hierarchy.

---

### Summary

| Component                | Purpose                                                           |
| ------------------------ | ----------------------------------------------------------------- |
| `BST` class              | Represents a node in the binary search tree.                      |
| `build_tree()`           | Builds the tree from a dictionary input.                          |
| `validate_three_nodes()` | Checks if one node lies between two others in the tree hierarchy. |
| `is_descendant()`        | Checks if a node is in the subtree of another.                    |

---

Here is the **ASCII visualization** of your binary search tree from the dictionary input:

```
            5
          /   \
         2     7
       /  \   / \
      1    4 6   8
     /    /
    0    3
```

### 🔍 Node Values with Structure:

* Root is **5**
* **5.left = 2**, **5.right = 7**
* **2.left = 1**, **2.right = 4**
* **1.left = 0**
* **4.left = 3**
* **7.left = 6**, **7.right = 8**

### 📌 Test Case Breakdown:

We're calling:

```
validate_three_nodes(5, 2, 3)
```

So:

* `node_one` = 5
* `node_two` = 2
* `node_three` = 3

### ✔ Path through the tree:

* 5 → 2 → 4 → 3

This means `2` lies **between** `5` and `3`, so the result is `True`.

"""
