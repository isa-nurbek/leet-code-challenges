# Problem Description:

"""
                                                BST Construction

Write a `BST` class for a Binary Search Tree. The class should support:

- Inserting values with the `insert` method.
- Removing values with the `remove` method; this method should only remove the first instance of a given value.
- Searching for values with the `contains` method.

> Note that you can't remove values from a single-node tree. In other words, calling the `remove` method on a single-node tree
should simply not do anything.

Each `BST` node has an integer `value`, a `left` child node, and a `right` child node. A node is said to be a valid `BST` node if
and only if it satisfies the `BST` property: its `value` is strictly greater than the values of every node to its left; its `value`
is less than or equal to the values of every node to its right; and its children nodes are either valid `BST` nodes themselves or `None`.


## Sample Usage:
```
// Assume the following BST has already been created:

         10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

// All operations below are performed sequentially.

insert(12):   10
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /        /  \
     1        12  14

remove(10):   12
            /     \
           5      15
         /   \   /   \
        2     5 13   22
      /           \
     1            14

contains(15): true
```

## Optimal Time & Space Complexity:
```
Average: (all 3 methods): O(log(n)) time | O(1) space - where `n` is the number of nodes in the BST.
Worst: (all 3 methods): O(n) time | O(1) space - where `n` is the number of nodes in the BST.
```

"""

# =========================================================================================================================== #

# Solution:


# Binary Search Tree (BST) node class
class BST:
    def __init__(self, value):
        # Initialize a BST node with a value, and set left and right children to None
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Insert a new value into the BST
        if value < self.value:
            # If the value is less than current node's value, go to the left subtree
            if self.left is None:
                # If left child is empty, create a new node here
                self.left = BST(value)
            else:
                # Otherwise, recursively insert into the left subtree
                self.left.insert(value)
        else:
            # If the value is greater or equal, go to the right subtree
            if self.right is None:
                # If right child is empty, create a new node here
                self.right = BST(value)
            else:
                # Otherwise, recursively insert into the right subtree
                self.right.insert(value)
        return self  # Return the tree to allow method chaining

    def contains(self, value):
        # Check if the BST contains a given value
        if value < self.value:
            # If value is less than current node, search left subtree
            if self.left is None:
                return False  # Value not found
            else:
                return self.left.contains(value)
        elif value > self.value:
            # If value is greater than current node, search right subtree
            if self.right is None:
                return False  # Value not found
            else:
                return self.right.contains(value)
        else:
            # Found the value
            return True

    def remove(self, value, parent=None):
        # Remove a value from the BST
        if value < self.value:
            # If value is less than current node, go left
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            # If value is greater than current node, go right
            if self.right is not None:
                self.right.remove(value, self)
        else:
            # Found the node to remove
            if self.left is not None and self.right is not None:
                # Case 1: Node has two children
                # Replace value with minimum value from right subtree
                self.value = self.right.get_min_value()
                # Remove the duplicate value from right subtree
                self.right.remove(self.value, self)
            elif parent is None:
                # Case 2: Node is root with one or zero children
                if self.left is not None:
                    # Replace with left child's value and pointers
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    # Replace with right child's value and pointers
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # Node is root with no children - single node tree
                    pass  # In practice, might want to handle this case differently
            elif parent.left == self:
                # Case 3: Node is left child with one or zero children
                # Replace parent's left pointer with our non-null child (if any)
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                # Case 4: Node is right child with one or zero children
                # Replace parent's right pointer with our non-null child (if any)
                parent.right = self.left if self.left is not None else self.right
        return self  # Return the tree to allow method chaining

    def get_min_value(self):
        # Get the minimum value in the BST (leftmost node)
        if self.left is None:
            return self.value  # Found the leftmost node
        else:
            return self.left.get_min_value()  # Recurse left

    def __str__(self):
        # String representation of the BST for visualization
        return self._visualize()

    def _visualize(self, level=0):
        # Helper method for tree visualization (recursive)
        ret = "\t" * level + repr(self.value) + "\n"  # Current node
        for child in [self.left, self.right]:
            if child:
                # Add visualization of children with increased indentation
                ret += child._visualize(level + 1)
        return ret


# Example usage
def main():
    # Initialize BST with root value 10
    bst = BST(10)
    print("Initial BST:")
    print(bst)

    # List of operations to perform
    operations = [
        ("insert", 5),
        ("insert", 15),
        ("insert", 2),
        ("insert", 5),
        ("insert", 13),
        ("insert", 22),
        ("insert", 1),
        ("insert", 14),
        ("insert", 12),
        ("remove", 10),
        ("contains", 15),
    ]

    # Perform each operation
    for i, (method, value) in enumerate(operations, 1):
        print(f"\nOperation {i}: {method}({value})")

        if method == "insert":
            bst.insert(value)
        elif method == "remove":
            bst.remove(value)
        elif method == "contains":
            result = bst.contains(value)
            print(f"Contains {value}? {result}")
            continue  # Skip tree visualization for contains

        print("Current BST:")
        print(bst)


if __name__ == "__main__":
    main()

# Output:

"""
Initial BST:
10

Operation 1: insert(5)
Current BST:
  10
 /
5

Operation 2: insert(15)
Current BST:
  10
 /  \
5   15

Operation 3: insert(2)
Current BST:
    10
   /  \
  5   15
 /
2

Operation 4: insert(5) (again - duplicates go to right)
Current BST:
    10
   /  \
  5   15
 /  \
2    5

Operation 5: insert(13)
Current BST:
    10
   /  \
  5   15
 / \  /
2  5 13

Operation 6: insert(22)
Current BST:
    10
   /  \
  5   15
 / \  / \
2  5 13 22

Operation 7: insert(1)
Current BST:
       10
      /  \
     5   15
    / \  / \
   2  5 13 22
  /
 1

Operation 8: insert(14)
Current BST:
       10
      /  \
     5   15
    / \  / \
   2  5 13 22
  /    / \
 1    12 14

Operation 9: insert(12)
Current BST:
      10
     /  \
    5   15
   / \  / \
  2  5 13 22
 /    / \
1    12 14

Operation 10: remove(10)
Current BST:
      12
     /  \
    5   15
   / \  / \
  2  5 13 22
 /      \
1       14

Operation 11: contains(15)
Contains 15? True
"""

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Here's the time and space complexity analysis for each method in the BST class:

### 1. `__init__` (Constructor)
- **Time Complexity**: O(1) - Only initializes a node.
- **Space Complexity**: O(1) - Only allocates memory for a single node.

### 2. `insert(value)`
- **Time Complexity**:  
  - **Average Case**: O(log n) - In a balanced BST, the height is log n, so we traverse log n nodes.  
  - **Worst Case**: O(n) - If the tree is skewed (like a linked list), we traverse all n nodes.  
  
- **Space Complexity**:  
  - **Average Case**: O(log n) (recursive stack space).  
  - **Worst Case**: O(n) (if the tree is skewed).  
  - **Iterative Implementation**: O(1) (no extra space).  

### 3. `contains(value)`
- **Time Complexity**:  
  - **Average Case**: O(log n) - Balanced tree height is log n.  
  - **Worst Case**: O(n) - Skewed tree.  
  
- **Space Complexity**:  
  - **Average Case**: O(log n) (recursive stack).  
  - **Worst Case**: O(n).  
  - **Iterative Implementation**: O(1).  

### 4. `remove(value, parent)`
- **Time Complexity**:  
  - **Average Case**: O(log n) - Finding the node takes O(log n), and replacing it (if needed) also takes O(log n).  
  - **Worst Case**: O(n) - Skewed tree.  
  
- **Space Complexity**:  
  - **Average Case**: O(log n) (recursive stack).  
  - **Worst Case**: O(n).  
  - **Iterative Implementation**: O(1).  

### 5. `get_min_value()`
- **Time Complexity**:  
  - **Average Case**: O(log n) - Traverse left until the smallest node.  
  - **Worst Case**: O(n) - If the tree is left-skewed.  
  
- **Space Complexity**:  
  - **Average Case**: O(log n) (recursive stack).  
  - **Worst Case**: O(n).  
  - **Iterative Implementation**: O(1).  

### General Notes:
- **Balanced BST**: All operations (insert, delete, search) are O(log n) on average.  
- **Unbalanced BST (worst case)**: Operations degrade to O(n).  
- **Space Complexity**: Recursive implementations use stack space proportional to tree height. Iterative versions reduce this to O(1).  

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code implements a **Binary Search Tree (BST)** in Python with the following operations:

* `insert(value)`: Adds a value to the BST.
* `contains(value)`: Checks if a value exists in the BST.
* `remove(value)`: Removes a node with a given value from the BST.
* `get_min_value()`: Finds the minimum value in a subtree (used in deletion).
* A tree visualization method using `__str__()` for easy printing.

---

### 🔧 **Class Definition: `BST`**

```
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

* **Constructor**: Initializes a node with:

  * `value`: the value of the node.
  * `left`, `right`: child pointers (start as `None`).

---

### 🌱 **Insert Method**

```
def insert(self, value):
    if value < self.value:
        if self.left is None:
            self.left = BST(value)
        else:
            self.left.insert(value)
    else:
        if self.right is None:
            self.right = BST(value)
        else:
            self.right.insert(value)
    return self
```

* **Recursively** finds the correct spot for the new value.
* Goes **left** if the value is smaller, **right** if larger or equal.
* Duplicates are inserted in the **right subtree**.
* Returns the current tree to allow chaining (e.g., `tree.insert(5).insert(10)`).

---

### 🔍 **Contains Method**

```
def contains(self, value):
    if value < self.value:
        return False if self.left is None else self.left.contains(value)
    elif value > self.value:
        return False if self.right is None else self.right.contains(value)
    else:
        return True
```

* Recursively searches the tree.
* Returns `True` if value exists, `False` otherwise.

---

### ❌ **Remove Method**

```
def remove(self, value, parent=None):
    ...
```

Handles 3 cases:

#### Case 1: Value is in a **left** or **right** subtree.

* Recurse until value is found.

#### Case 2: Node to delete has **two children**.

```
if self.left is not None and self.right is not None:
    self.value = self.right.get_min_value()
    self.right.remove(self.value, self)
```

* Replace node's value with **min value from right subtree**.
* Recursively delete that min value node.

#### Case 3: Node has **one child or no child**.

```
elif parent is None:  # root node
```

* If it's the root, copy data from child to self.
* Else update parent’s left or right pointer to bypass the node.

#### Helper method:

```
def get_min_value(self):
    if self.left is None:
        return self.value
    return self.left.get_min_value()
```

---

### 🖼️ **Tree Visualization**

```
def __str__(self):
    return self._visualize()
```

Recursively builds a string representation of the tree with indentation:

```
def _visualize(self, level=0):
    ret = "\t" * level + repr(self.value) + "\n"
    for child in [self.left, self.right]:
        if child:
            ret += child._visualize(level + 1)
    return ret
```

This makes it easy to **print the tree** to see its structure.

---

### 🚀 **Main Function: Execution and Testing**

```
def main():
    bst = BST(10)
```

Initial tree: `10`

```python
operations = [
    ("insert", 5),
    ("insert", 15),
    ("insert", 2),
    ("insert", 5),
    ("insert", 13),
    ("insert", 22),
    ("insert", 1),
    ("insert", 14),
    ("insert", 12),
    ("remove", 10),
    ("contains", 15),
]
```

Performs a series of **inserts**, one **remove**, and one **contains** operation.

* Insertion builds the tree.
* Deletion of `10` (the root node) tests the **two children case**.
* Finally, `contains(15)` checks if `15` exists.

```
if __name__ == "__main__":
    main()
```

Runs the test only when the script is executed directly.

---

### 📈 Example Visualization Before and After Deletion

Before deletion of `10`:

```
10
	5
		2
			1
		5
	15
		13
			12
			14
		22
```

After deletion of `10`, it gets replaced by `12` (minimum from right subtree):

```
12
	5
		2
			1
		5
	15
		13
			14
		22
```

---

### ✅ Summary

| Method     | Purpose                            |
| ---------- | ---------------------------------- |
| `insert`   | Adds a node maintaining BST rules  |
| `contains` | Searches the BST for a value       |
| `remove`   | Deletes a node with all edge cases |
| `__str__`  | Nicely prints the BST structure    |

---

Let's walk through each operation in the order it's performed and visualize the **Binary Search Tree (BST)** using **ASCII
diagrams** after each step.

---

### **Initial State**

```
bst = BST(10)
```

```
10
```

---

### **1. insert(5)**

* 5 < 10 → goes to left of 10

```
10
/
5
```

---

### **2. insert(15)**

* 15 > 10 → goes to right of 10

```
   10
  /  \
 5   15
```

---

### **3. insert(2)**

* 2 < 10 → left
* 2 < 5 → left of 5

```
     10
    /  \
   5   15
  /
 2
```

---

### **4. insert(5)**

* 5 < 10 → left
* 5 == 5 → goes to right of first 5 (duplicates go to right)

```
     10
    /  \
   5   15
  / \
 2   5
```

---

### **5. insert(13)**

* 13 > 10 → right
* 13 < 15 → left of 15

```
     10
    /  \
   5   15
  / \  /
 2   5 13
```

---

### **6. insert(22)**

* 22 > 10 → right
* 22 > 15 → right of 15

```
     10
    /  \
   5   15
  / \  / \
 2   5 13 22
```

---

### **7. insert(1)**

* 1 < 10 → left
* 1 < 5 → left
* 1 < 2 → left of 2

```
       10
      /  \
     5   15
    / \  / \
   2   5 13 22
  /
 1
```

---

### **8. insert(14)**

* 14 > 10 → right
* 14 < 15 → left
* 14 > 13 → right of 13

```
       10
      /  \
     5   15
    / \  / \
   2   5 13 22
  /        \
 1         14
```

---

### **9. insert(12)**

* 12 > 10 → right
* 12 < 15 → left
* 12 < 13 → left of 13

```
       10
      /  \
     5   15
    / \  / \
   2   5 13 22
  /     / \
 1    12  14
```

---

### **10. remove(10)**

* 10 is the root.
* It has **two children**.
* Replace 10 with **smallest value in right subtree** → `12`.
* Then remove node `12` from its original location.

#### Before Removal:

```
       10
      /  \
     5   15
    / \  / \
   2   5 13 22
  /     / \
 1    12  14
```

#### After Replacing 10 → 12:

```
       12
      /  \
     5   15
    / \  / \
   2   5 13 22
  /       \
 1        14
```

---

### **11. contains(15)**

* 15 > 12 → go right
* Found in the tree.

✔️ **Output: `True`**

---

### ✅ Final BST (after all operations):

```
       12
      /  \
     5   15
    / \  / \
   2   5 13 22
  /       \
 1        14
```

"""
