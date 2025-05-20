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


# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
def find_closest_value_in_bst(tree, target):
    # Start the helper function with the tree's root value as initial closest
    return find_closest_value_in_bst_helper(tree, target, tree.value)


# Recursive helper function to find closest value
def find_closest_value_in_bst_helper(tree, target, closest):
    # Base case: if we've reached a leaf node, return current closest
    if tree is None:
        return closest

    # Check if current node's value is closer than previous closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value  # Update closest if current node is better

    # Decide which subtree to explore next based on target value
    if target < tree.value:
        # Target is smaller, so search in left subtree
        return find_closest_value_in_bst_helper(tree.left, target, closest)
    elif target > tree.value:
        # Target is larger, so search in right subtree
        return find_closest_value_in_bst_helper(tree.right, target, closest)
    else:
        # Found exact match, return it immediately
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

Let's analyze the time and space complexity of the given `find_closest_value_in_bst` algorithm.

### Time Complexity:

- **Best Case:** O(1) - When the target value is equal to the root node's value.
- **Average Case:** O(log n) - In a balanced BST, with each recursive call, we eliminate half of the remaining tree
(similar to binary search).
- **Worst Case:** O(n) - If the BST is completely unbalanced (essentially a linked list), we might have to traverse all nodes.

### Space Complexity:

- **Best Case:** O(1) - When the target is found at the root (no recursive calls).
- **Average Case:** O(log n) - Due to the recursion stack in a balanced BST (depth of recursion is log n).
- **Worst Case:** O(n) - If the BST is completely unbalanced, the recursion stack could grow to size n.

### Explanation:

1. **Time Complexity:**
   - The algorithm works by traversing a path from the root to a leaf, adjusting the closest value along the way.
   - In a balanced BST, the height is log n, so the number of recursive calls is O(log n).
   - In the worst case (unbalanced BST), the height is n, leading to O(n) time.

2. **Space Complexity:**

   - The space is determined by the recursion stack.
   - For a balanced BST, the maximum stack depth is O(log n).
   - In the worst case (unbalanced BST), it's O(n).

### Notes:

- The algorithm could be optimized to use an iterative approach (instead of recursion), reducing the space complexity to O(1)
in all cases while keeping the same time complexity.
- The initial closest value is set to `tree.value`, which is a reasonable starting point.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code defines a **binary search tree (BST)**, builds it from a given data structure, and finds the **closest value to a given
target** in the BST. Let's break it down in detail:

---

### 🔶 Class: `BST`

```
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

* A basic class to represent a **node** in a Binary Search Tree.
* Each node stores:

  * `value`: the integer value of the node.
  * `left`: reference to the left child (or `None` if it doesn’t exist).
  * `right`: reference to the right child.

---

### 🔶 Function: `build_tree(data)`

```
def build_tree(data):
    if not data:
        return None
```

* **Input**: A dictionary `data` that contains node descriptions with `id`, `value`, `left`, and `right`.
* **Output**: The root of the constructed BST.

#### Step-by-step logic:

##### Step 1: Create all `BST` node objects.

```
    nodes = {}
    for node_data in data["nodes"]:
        node = BST(node_data["value"])
        nodes[node_data["id"]] = node
```

* A dictionary `nodes` maps each node's `"id"` to a `BST` node object created using its `"value"`.

##### Step 2: Set left and right children.

```
    for node_data in data["nodes"]:
        node = nodes[node_data["id"]]
        if node_data["left"] is not None:
            node.left = nodes[node_data["left"]]
        if node_data["right"] is not None:
            node.right = nodes[node_data["right"]]
```

* For each node, assign the `left` and `right` child using references to the already created node objects.

##### Step 3: Return the root node.

```
    return nodes[data["nodes"][0]["id"]]
```

* Assumes the first node in the list is the root.

---

### 🔶 Function: `find_closest_value_in_bst(tree, target)`

This is the public wrapper that calls the helper function.

```
def find_closest_value_in_bst(tree, target):
    return find_closest_value_in_bst_helper(tree, target, tree.value)
```

* It starts the recursion from the root (`tree`) and sets the initial closest value as the root's value.

---

### 🔶 Function: `find_closest_value_in_bst_helper(tree, target, closest)`

This is a **recursive** helper function.

```
def find_closest_value_in_bst_helper(tree, target, closest):
    if tree is None:
        return closest
```

* Base case: if we've reached a null node, return the closest value found so far.

```
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
```

* If the current node's value is **closer to the target** than the previously stored closest value, update it.

```
    if target < tree.value:
        return find_closest_value_in_bst_helper(tree.left, target, closest)
    elif target > tree.value:
        return find_closest_value_in_bst_helper(tree.right, target, closest)
    else:
        return closest
```

* Traverse:

  * Go **left** if the target is smaller (because BST has smaller values on the left).
  * Go **right** if the target is larger.
  * If the value matches the target exactly, return it.

---

### 🔶 Input Tree Structure (`tree_dict`)

This dictionary describes a binary search tree:

```
          10
         /  \
        5    15
       / \     \
      2   5     22
     /
    1
         \
         13
           \
           14
```

(Visualizing the `13 -> 14` part as part of the right subtree of `15`.)

---

### 🔶 Running the Code

```
result = find_closest_value_in_bst(tree, 12)
print(result)  # Output: 13
```

* **Target**: `12`
* The traversal will go:

  * Start at `10` → update closest (difference = 2)
  * Go right to `15` → difference is 3 (no update)
  * Go left to `13` → difference is 1 → update closest
  * Go right to `14` → difference is 2 (no update)

Closest = `13`

---

### ✅ Summary

* **BST nodes** are created using a class.
* **Tree is built** from a dictionary of nodes with references.
* The **closest value** is found by recursive traversal, comparing each node’s value to the target and tracking the minimum
absolute difference.
* **Efficient**: Average time complexity is `O(log n)` for balanced BSTs, worst-case is `O(n)` for skewed trees.

---

Here’s an **ASCII visualization** of the Binary Search Tree (BST) represented by `tree_dict`:

```
               10
             /    \
           5       15
         /   \     / \
        2     5   13  22
       /           \
      1             14
```

### Explanation:

* Root: `10`
* Left subtree of `10`:

  * Node `5`, with:

    * Left child: `2`

      * Left child: `1`
    * Right child: another `5` (`id = "5-2"`)
* Right subtree of `10`:

  * Node `15`, with:

    * Left child: `13`

      * Right child: `14`
    * Right child: `22`

### Path Traversed to Find Closest to 12:

To find the closest value to `12`:

1. Start at `10` → closest so far = 10
2. Move right to `15` (target > 10) → closest remains 10 (|15 - 12| = 3, |10 - 12| = 2)
3. Move left to `13` (target < 15) → update closest to 13 (|13 - 12| = 1)
4. Move right to `14` → no update (|14 - 12| = 2 > 1)

✅ Final closest = **13**

"""
