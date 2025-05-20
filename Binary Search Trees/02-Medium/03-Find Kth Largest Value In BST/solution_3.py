# Problem Description:

"""
                                                Find Kth Largest Value In BST

Write a function that takes in a `Binary Search Tree (BST)` and a positive integer `k` and returns the `k`th largest integer
contained in the BST.

You can assume that there will only be integer values in the BST and that `k` is less than or equal to the number of nodes in
the tree.

Also, for the purpose of this question, duplicate integers will be treated as distinct values. In other words, the second largest
value in a BST containing values `{5, 7, 7}` will be `7`—not `5`.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Input:
```
tree =   15
       /     \
      5      20
    /   \   /   \
   2     5 17   22
 /   \         
1     3   

k = 3
```

## Sample Output:
```
17
```

## Optimal Time & Space Complexity:
```
O(h + k) time | O(h) space - where `h` is the height of the tree and `k` is the input parameter.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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


# O(n) time | O(1) space
# Morris Traversal
def find_kth_largest_value_in_bst(tree, k):
    current = tree
    count = 0

    while current is not None:
        if current.right is None:
            # If no right child, process current node
            count += 1
            if count == k:
                return current.value
            # Move to the left child
            current = current.left
        else:
            # Find the predecessor (in-order predecessor) in right subtree
            predecessor = current.right
            while predecessor.left is not None and predecessor.left != current:
                predecessor = predecessor.left

            if predecessor.left is None:
                # First time visiting - set thread/link to current node
                predecessor.left = current
                # Move to right child first
                current = current.right
            else:
                # We've already visited this predecessor - remove thread
                predecessor.left = None
                # Process current node (in-order visit)
                count += 1
                if count == k:
                    return current.value
                # Move to left child
                current = current.left

    return None  # In case k is larger than number of nodes


# Example tree data structure
tree_dict = {
    "nodes": [
        {"id": "15", "left": "5", "right": "20", "value": 15},
        {"id": "20", "left": "17", "right": "22", "value": 20},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "17", "left": None, "right": None, "value": 17},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": None, "right": None, "value": 5},
        {"id": "2", "left": "1", "right": "3", "value": 2},
        {"id": "3", "left": None, "right": None, "value": 3},
        {"id": "1", "left": None, "right": None, "value": 1},
    ],
    "root": "15",
}

# The tree structure represented by this dictionary:

#           15
#        /     \
#       5      20
#     /   \   /   \
#    2     5 17   22
#  /   \
# 1     3

# Test Case:

# Build the tree
tree = build_tree(tree_dict)

# Find closest value
result = find_kth_largest_value_in_bst(tree, 3)

print(result)  # Output: 17

# =========================================================================================================================== #

# Big O Analysis:

"""
# Time and Space Complexity Analysis:

This code implements an algorithm to find the k-th largest value in a Binary Search Tree (BST) using **Morris Traversal**,
which allows in-order traversal without recursion or a stack by temporarily modifying the tree structure.

### **Time Complexity Analysis**

- **Morris Traversal** visits each node **at most twice** (once to establish the temporary links and once to traverse after
the links are removed).
- **Total Operations**: For a BST with `n` nodes, each node is visited a constant number of times, leading to **O(n)** time complexity.

### **Space Complexity Analysis**

- Morris Traversal uses **O(1) extra space** (no recursion or stack is used; only a few pointers are maintained).
- Thus, the space complexity is **O(1)**.

### **Summary**
- **Time Complexity**: **O(n)** (worst case, where we traverse all nodes).
- **Space Complexity**: **O(1)** (constant extra space).

### **Optimization Consideration**

If the BST is balanced, a more efficient approach (O(h + k), where `h` is the tree height) could be achieved using reverse
in-order traversal with a stack, but Morris Traversal ensures O(1) space at the cost of slightly higher constant factors in time.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let's walk through each part of the code — understanding what it does, how it works, and the role each function/class plays.

---

## 🔷 1. Class Definition: `BST`

```
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

This defines a **Binary Search Tree (BST) node**.

* Each node has:

  * `value`: the value it stores
  * `left`: pointer to the left child (smaller values)
  * `right`: pointer to the right child (larger values)

---

## 🔷 2. Function: `build_tree(data)`

This function builds a BST from a dictionary that defines a tree structure.

### 📌 How it works:

#### 🔹 Step 1: Create All Nodes

```
for node_data in data["nodes"]:
    node = BST(node_data["value"])
    nodes[node_data["id"]] = node
```

* Loops over the list of node dictionaries in `data["nodes"]`.
* Creates a `BST` object with the given `value`.
* Stores it in a dictionary `nodes` using the `"id"` as the key.

#### 🔹 Step 2: Connect Nodes

```
for node_data in data["nodes"]:
    node = nodes[node_data["id"]]
    if node_data["left"] is not None:
        node.left = nodes[node_data["left"]]
    if node_data["right"] is not None:
        node.right = nodes[node_data["right"]]
```

* Loops again and links the children (left and right) using their IDs.

#### 🔹 Step 3: Return Root

```
return nodes[data["nodes"][0]["id"]]
```

* Returns the root node. Assumes the first node in the list is the root.

---

## 🔷 3. Function: `find_kth_largest_value_in_bst(tree, k)`

This function uses **Morris Traversal** to find the **k-th largest value** in the BST **in O(n) time and O(1) space**.

---

## 📘 Background: BST Properties

In a BST:

* Left child < parent < right child
* An **in-order traversal** (left → root → right) gives **sorted order**
* A **reverse in-order traversal** (right → root → left) gives **descending order**

---

## 📘 Morris Traversal (Reverse In-Order)

Morris Traversal allows **in-order traversal without recursion or a stack**, by **modifying the tree temporarily**.

It uses **"threaded binary trees"** — temporarily links the tree’s right children to go back up the tree.

---

## 📌 Steps:

```
current = tree
count = 0
```

* `current`: starts at root
* `count`: how many nodes we’ve visited in reverse order

---

### 🔹 Main Loop

```
while current is not None:
```

* Traverse the tree in **reverse in-order** (right → root → left)

---

### 🔸 Case 1: No Right Child

```
if current.right is None:
    count += 1
    if count == k:
        return current.value
    current = current.left
```

* If no right child, this is the largest available node right now.
* Increase count. If `count == k`, return this node’s value.
* Move to left child next.

---

### 🔸 Case 2: Has Right Child (Find Inorder Predecessor)

```
predecessor = current.right
while predecessor.left is not None and predecessor.left != current:
    predecessor = predecessor.left
```

* Find the leftmost node in the right subtree (reverse in-order predecessor).
* If its left is `None`, make it point back to `current`.

---

### 🔸 Create a Temporary Thread

```
if predecessor.left is None:
    predecessor.left = current
    current = current.right
```

* Threading: temporarily link `predecessor.left` to `current`
* Move right (descending)

---

### 🔸 Remove Thread and Visit Node

```
else:
    predecessor.left = None
    count += 1
    if count == k:
        return current.value
    current = current.left
```

* Restore tree structure (remove thread)
* Visit `current` (this is the next k-th largest)
* Move left

---

### 🔹 Final Return

```
return None
```

* If `k` is more than number of nodes, return `None`.

---

## 🔷 4. Tree Data Example

```
tree_dict = {
    "nodes": [
        {"id": "15", "left": "5", "right": "20", "value": 15},
        {"id": "20", "left": "17", "right": "22", "value": 20},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "17", "left": None, "right": None, "value": 17},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": None, "right": None, "value": 5},
        {"id": "2", "left": "1", "right": "3", "value": 2},
        {"id": "3", "left": None, "right": None, "value": 3},
        {"id": "1", "left": None, "right": None, "value": 1},
    ],
    "root": "15",
}
```

### Tree Visualization:

```
           15
         /    \
       5       20
     /   \    /   \
    2     5  17   22
  /   \
 1     3
```

---

## 🔷 5. Test Run: Find 3rd Largest

```
tree = build_tree(tree_dict)
result = find_kth_largest_value_in_bst(tree, 3)
print(result)  # Output: 17
```

### Sorted (descending) values in BST:

```
[22, 20, 17, 15, 5, 5, 3, 2, 1]
```

* `3rd` largest = **17**

---

## ✅ Summary

| Component                                | Purpose                                                        |
| ---------------------------------------- | -------------------------------------------------------------- |
| `BST` class                              | Defines tree nodes                                             |
| `build_tree(data)`                       | Builds BST from dictionary                                     |
| `find_kth_largest_value_in_bst(tree, k)` | Finds k-th largest using **Morris Reverse In-Order Traversal** |
| `Morris Traversal`                       | Traverses BST in O(n) time and **O(1) space**                  |
| Test Output                              | `17` (3rd largest in BST)                                      |

---

Here’s the **ASCII visualization** of your BST from the dictionary `tree_dict`:

```
               15
             /    \
           5        20
         /   \     /   \
        2     5   17   22
      /   \
     1     3
```

### Node values:

* The root is **15**
* Left subtree rooted at **5**

  * Left child is **2**, which has children **1** and **3**
  * Right child is another node with value **5** (ID: `"5-2"`)
* Right subtree rooted at **20**

  * Left child: **17**
  * Right child: **22**

This is a **Binary Search Tree**, so each node’s left child is less than the node, and the right child is greater.

"""
