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


# O(n + k) time | O(n) space
# Iterative Stack-Based
def find_kth_largest_value_in_bst(tree, k):
    # Initialize an empty stack to keep track of nodes to visit
    stack = []
    # Start with the root node of the BST
    current = tree
    # Counter to keep track of how many largest elements we've processed
    count = 0

    # Infinite loop that we'll break out of when done
    while True:
        # Traverse as far right as possible (to find largest values first)
        while current is not None:
            stack.append(current)
            current = current.right

        # If stack is empty, we've processed all nodes
        if not stack:
            break

        # Pop the most recent node (which is the next largest)
        current = stack.pop()
        count += 1  # Increment our count of processed nodes

        # If we've reached the k-th largest, return its value
        if count == k:
            return current.value

        # Move to the left subtree (which contains values smaller than current node,
        # but potentially larger than other nodes we've processed)
        current = current.left

    # If we exit the loop without finding k elements, return None
    return None


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

Let's analyze the time and space complexity of the given `find_kth_largest_value_in_bst` function.

### **Time Complexity: O(h + k)**

- **h**: Height of the BST.
- **k**: The k-th largest element to find.

#### **Explanation:**
1. The algorithm performs an **in-order traversal in reverse** (right-root-left) to visit nodes in descending order.
2. In the worst case, we may traverse **all the way down to the rightmost leaf** (O(h)) before starting to pop nodes from the stack.
3. Then, we pop **k** nodes to reach the k-th largest element.
4. Hence, the total time is **O(h + k)**.

### **Space Complexity: O(h)**

- **h**: Height of the BST (due to the stack).

#### **Explanation:**

1. The stack stores nodes along the **rightmost path** of the BST.
2. In the worst case (a skewed BST), the stack can hold **all nodes** (O(n)), but in a balanced BST, it's **O(log n)**.
3. Hence, the space complexity is **O(h)**.

### **Summary:**
- **Time Complexity:** **O(h + k)**  

  - Worst case (skewed tree): **O(n + k)**  
  - Best case (balanced tree): **O(log n + k)**  
  
- **Space Complexity:** **O(h)**  

  - Worst case (skewed tree): **O(n)**  
  - Best case (balanced tree): **O(log n)**  

This approach efficiently finds the k-th largest element by leveraging **reverse in-order traversal** with a stack.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
Let’s go through our code step-by-step to understand how it builds a Binary Search Tree (BST) from dictionary data and finds the
**k-th largest** value using an **iterative reverse in-order traversal**.

---

## 🔹 1. `BST` Class

```
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

This defines a **Binary Search Tree (BST) node** with:

* `value`: the value of the node,
* `left`: reference to the left child,
* `right`: reference to the right child.

---

## 🔹 2. `build_tree(data)` Function

This function builds the BST using a dictionary that specifies the structure of the tree.

### 📌 Step-by-Step:

```
if not data:
    return None
```

If input data is empty, return `None`.

### 🧱 First Pass: Create nodes and store them in a dictionary

```
nodes = {}
for node_data in data["nodes"]:
    node = BST(node_data["value"])
    nodes[node_data["id"]] = node
```

* Iterates over all node data,
* Creates `BST` node objects,
* Stores them in `nodes` dictionary using their `"id"` as key.

### 🔗 Second Pass: Connect children

```
for node_data in data["nodes"]:
    node = nodes[node_data["id"]]
    if node_data["left"] is not None:
        node.left = nodes[node_data["left"]]
    if node_data["right"] is not None:
        node.right = nodes[node_data["right"]]
```

* Iterates again to assign left and right children using references stored in the dictionary.

### 🪵 Return root

```
return nodes[data["nodes"][0]["id"]]
```

* Returns the root node, which is assumed to be the **first node** in the list.

> This works because your `tree_dict` defines the root node `"15"` as the first element in the `"nodes"` list.

---

## 🔹 3. `find_kth_largest_value_in_bst(tree, k)`

### 🎯 Goal:

Find the k-th **largest** value in the BST.

> In-order traversal (Left → Root → Right) gives **ascending order**.
>
> Reverse in-order (Right → Root → Left) gives **descending order** — ideal for finding the k-th largest.

### 📌 Code Breakdown:

```
stack = []
current = tree
count = 0
```

* `stack`: simulates recursion stack for traversal.
* `current`: pointer to traverse the tree.
* `count`: number of nodes visited so far.

### 🔁 Main Loop:

```
while True:
    while current is not None:
        stack.append(current)
        current = current.right
```

* Go as far **right** as possible (largest values first), pushing nodes onto the stack.

```
if not stack:
    break
```

* Exit loop if no more nodes.

```
current = stack.pop()
count += 1
```

* Visit node, increment count.

```
if count == k:
    return current.value
```

* If it’s the k-th node, return its value.

```
current = current.left
```

* Move to the left child to continue reverse in-order.

---

## 🔹 4. `tree_dict` Explanation

The dictionary represents this tree:

```
           15
        /     \
       5      20
     /   \   /   \
    2     5 17   22
  /   \
 1     3
```

The `"id"` values are just string identifiers for connecting nodes.

---

## 🔹 5. Test Case

```
tree = build_tree(tree_dict)
result = find_kth_largest_value_in_bst(tree, 3)
print(result)
```

### 🔎 Tree Values in Descending Order:

`[22, 20, 17, 15, 5, 5, 3, 2, 1]`

* 1st largest: `22`
* 2nd largest: `20`
* 3rd largest: `17` ✅

So the output is:

```
17
```

---

## ✅ Summary

| Component                                | Purpose                                                                 |
| ---------------------------------------- | ----------------------------------------------------------------------- |
| `BST` class                              | Node structure with `value`, `left`, `right`                            |
| `build_tree(data)`                       | Creates and links BST nodes from a dictionary                           |
| `find_kth_largest_value_in_bst(tree, k)` | Iteratively finds the k-th largest value via reverse in-order traversal |
| `tree_dict`                              | Sample tree structure                                                   |
| `result = 17`                            | Because `17` is the 3rd largest value in BST                            |

---

Here is an ASCII visualization of the Binary Search Tree (BST) built from your `tree_dict`:

```
               15
             /    \
           5       20
         /   \    /   \
        2     5  17   22
       / \
      1   3
```

### 🌳 Explanation:

* `15` is the root.
* `5` is the left child of `15`, and `20` is the right child.
* `2` and another `5` are children of the left `5`.
* `1` and `3` are children of `2`.
* `17` and `22` are children of `20`.

---

### 🔢 Reverse In-Order Traversal (Right → Root → Left):

Traversal order (for `k-th` **largest** values):

```
22 → 20 → 17 → 15 → 5 → 5 → 3 → 2 → 1
```

So:

* 1st largest = **22**
* 2nd largest = **20**
* 3rd largest = **17** ✅

"""
