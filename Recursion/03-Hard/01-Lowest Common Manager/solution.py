# Problem Description:

"""

                                          Lowest Common Manager

You're given three inputs, all of which are instances of an `OrgChart` class that have a `direct_reports` property pointing to
their direct reports. The first input is the top manager in an organizational chart (i.e., the only instance that isn't anybody
else's direct report), and the other two inputs are reports in the organizational chart. The two reports are guaranteed to be
distinct.

Write a function that returns the lowest common manager to the two reports.


## Sample Input
```
// From the organizational chart below.
top_manager = Node A
report_one = Node E
report_two = Node I
          A
       /     \
      B       C
    /   \   /   \
   D     E F     G
 /   \
H     I
```

## Sample Output
```
Node B
```

## Optimal Time & Space Complexity:
```
O(n) time | O(d) space - where `n` is the number of people in the org and `d` is the depth (height) of the org chart.
```
"""

# =========================================================================================================================== #

# Solution:


# O(n) time | O(d) space
# Function to get the lowest common manager of two reports in an organization hierarchy
def get_lowest_common_manager(top_manager, report_one, report_two):
    # This is a wrapper function that calls the helper function and returns just the lowest_common_manager
    return get_org_info(top_manager, report_one, report_two).lowest_common_manager


# Recursive helper function that returns both the lowest common manager (if found) and count of important reports
def get_org_info(manager, report_one, report_two):
    # Tracks how many of the two important reports we've found in this subtree
    num_important_reports = 0

    # Check all direct reports of the current manager
    for direct_report in manager.direct_reports:
        # Get org info for each subtree
        org_info = get_org_info(direct_report, report_one, report_two)

        # If we've found the lowest common manager in a subtree, bubble it up immediately
        if org_info.lowest_common_manager is not None:
            return org_info

        # Add any important reports found in this subtree to our count
        num_important_reports += org_info.num_important_reports

    # Check if current manager is one of the important reports
    if manager == report_one or manager == report_two:
        num_important_reports += 1

    # If we've found both important reports in this subtree, current manager is the LCA
    lowest_common_manager = manager if num_important_reports == 2 else None

    # Return an OrgInfo object containing our findings for this subtree
    return OrgInfo(lowest_common_manager, num_important_reports)


# Simple class to hold information about a subtree
class OrgInfo:
    def __init__(self, lowest_common_manager, num_important_reports):
        # The LCA if found in this subtree
        self.lowest_common_manager = lowest_common_manager
        # Count of important reports found (0, 1, or 2)
        self.num_important_reports = num_important_reports


# Define the OrgChart structure (basic tree node)
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.direct_reports = []  # Children in the org hierarchy

    def add_direct_reports(self, reports):
        self.direct_reports = reports


# Build the org chart (this is test data)
# Create all nodes first
nodes = {}
for name in ["A", "B", "C", "D", "E", "F", "G", "H", "I"]:
    nodes[name] = OrgChart(name)

# Set up reporting relationships (build the tree)
nodes["A"].add_direct_reports([nodes["B"], nodes["C"]])
# A is CEO with B and C as direct reports

nodes["B"].add_direct_reports([nodes["D"], nodes["E"]])  # B manages D and E
nodes["C"].add_direct_reports([nodes["F"], nodes["G"]])  # C manages F and G
nodes["D"].add_direct_reports([nodes["H"], nodes["I"]])  # D manages H and I
# E, F, G, H, I are leaf nodes (no direct reports)

# Run the test
top_manager = nodes["A"]  # CEO of the organization
report_one = nodes["E"]  # First employee we care about
report_two = nodes["I"]  # Second employee we care about

# Find the lowest manager that both reports share
lcm = get_lowest_common_manager(top_manager, report_one, report_two)
print(lcm.name)
# Output: "B" (since B is the lowest manager that oversees both E and I)

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis

### Time Complexity:

- **Tree Traversal**: The algorithm performs a depth-first search (DFS) traversal of the organizational tree. Each node is
visited exactly once.
- **Operations per Node**: For each node, the algorithm checks its direct reports (children) and performs constant-time
operations (comparisons, additions).
- **Overall**: If `n` is the number of nodes (employees) in the organizational tree, the time complexity is **O(n)**,
since each node is processed once.

### Space Complexity:

- **Recursion Stack**: The space complexity is determined by the maximum depth of the recursion stack, which corresponds
to the height of the tree.
  - In the **best case** (balanced tree), the height is `O(log n)`, so the space complexity is `O(log n)`.
  - In the **worst case** (unbalanced tree, e.g., a linked list), the height is `O(n)`, so the space complexity is `O(n)`.
- **Auxiliary Data**: The `OrgInfo` objects are created in each recursive call but are not stored beyond their scope, so they
don't contribute to additional space complexity beyond the recursion stack.

### Summary:
- **Time Complexity**: **O(n)** (where `n` is the number of nodes in the tree).
- **Space Complexity**: **O(h)** (where `h` is the height of the tree, ranging from `O(log n)` in balanced trees to `O(n)`
in unbalanced trees).

### Notes:
- The algorithm efficiently finds the LCM by leveraging post-order traversal and propagating information about found reports
(`num_important_reports`) upwards.
- The worst-case space complexity occurs when the tree is highly unbalanced (e.g., a degenerate linked list), where the recursion
depth equals the number of nodes.

This analysis assumes that the tree is represented with pointers/references (as in the given `OrgChart` class). If the tree were
represented differently (e.g., an adjacency list), the space complexity might vary slightly, but the overall trends remain the same.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
## 💼 **Problem Statement**

You're given an **organizational chart (org chart)** — a tree-like hierarchy where each employee (node) may have zero or more
direct reports (children). The goal is to find the **lowest common manager (LCM)** for any two given employees.

> ✅ The **Lowest Common Manager** is the lowest person in the org chart who manages both employees directly or indirectly.

---

## 🧠 **High-Level Idea**

We use a **recursive post-order traversal** of the org chart to determine:

- How many of the target reports (employee1 and employee2) exist in the subtree rooted at the current node.
- If both are found in the subtree, then the current node is their **lowest common manager**.

---

## 🔍 **Step-by-Step Code Walkthrough**

### ➤ `get_lowest_common_manager(top_manager, report_one, report_two)`
This is the **entry function** that kicks off the process. It calls the recursive helper:

```
return get_org_info(top_manager, report_one, report_two).lowest_common_manager
```

---

### ➤ `get_org_info(manager, report_one, report_two)`
This function does the **real work** recursively.

#### 🔁 For every node (`manager`):

1. Initialize a counter: `num_important_reports = 0`
    - This counts how many of the target employees (`report_one` and `report_two`) are found in the subtree rooted at this manager.

2. For each **direct report** of the current manager:
    - Recursively call `get_org_info(...)`.
    - If any subtree already returned a `lowest_common_manager`, it means we’ve already found our answer, so **short-circuit and return early**.
    - Otherwise, accumulate the `num_important_reports` found in those subtrees.

3. After checking all direct reports:
    - If the current manager **is** one of the two target employees, increment the counter.
    - If `num_important_reports == 2`, it means the current `manager` is the **lowest common manager** of the two reports.

4. Return an `OrgInfo` object that keeps track of:
    - The lowest common manager (if found at this level).
    - The number of important reports found.

```
if manager == report_one or manager == report_two:
    num_important_reports += 1

lowest_common_manager = manager if num_important_reports == 2 else None
return OrgInfo(lowest_common_manager, num_important_reports)
```

---

### ➤ `OrgInfo` class
This is a simple **helper class** to store:
- `lowest_common_manager`
- `num_important_reports`

Used to pass this info up the recursive call stack.

---

### ➤ `OrgChart` class
Defines the structure of each employee node:
- `name`: the employee's name.
- `direct_reports`: a list of employees that report directly to this employee.

```
def add_direct_reports(self, reports):
    self.direct_reports = reports
```

---

## 🧱 **Org Chart Built in Example**

Here's how the tree looks:

```
          A
        /   \
       B     C
     /  \   / \
    D    E F   G
   / \
  H   I
```

So:
- `A` is the top manager.
- `E` reports to `B`.
- `I` reports to `D`, which reports to `B`.

Thus, both `E` and `I` ultimately report up to `B`.

So the **Lowest Common Manager of E and I is `B`**.

---

## ✅ **Output**

```
print(lcm.name)  # Output: "B"
```

---

## 📌 Summary of Key Concepts

| Concept        | Explanation                                                               |
|----------------|---------------------------------------------------------------------------|
| Tree Traversal | We use **post-order traversal** so we analyze children before the parent. |
| Base Cases     | Return early if LCM is already found in a child.                          |
| Bottom-Up      | We count how many of the target employees are found in the subtree.       |
| Short-Circuit  | Optimization: If a child returns LCM, no need to check the rest.          |
| Reusability    | OrgInfo makes the recursion clean and testable.                           |

---

Here’s an **ASCII diagram** showing the **org chart** first, and then a **visual simulation of the recursive traversal** when
finding the lowest common manager of `E` and `I`.

---

## 🧱 Org Chart Structure

```
             A
           /   \
         B       C
       /   \    / \
     D      E  F   G
    / \
   H   I
```

---

## 🔁 Recursive Traversal Trace

We're trying to find the **Lowest Common Manager (LCM)** for `E` and `I`.  
The traversal starts from the top (`A`) and goes **post-order**: left subtree → right subtree → node itself.

### Legend:
- ✅ = target found
- ❌ = target not found
- ★ = lowest common manager found here

---

```
Traversal Start: get_org_info(A)

→ Traverse B
  → Traverse D
    → Traverse H: ❌ (returns OrgInfo(None, 0))
    → Traverse I: ✅ (returns OrgInfo(None, 1))
    → D is not target → total important reports: 1
    → return OrgInfo(None, 1)
    
  → Traverse E: ✅ (it's a target)
    → return OrgInfo(None, 1)

  → B is not target, but subtree has:
       - D subtree found 1 target
       - E subtree found 1 target
    → total = 2
    → ★ Found LCM at B → return OrgInfo(B, 2)

→ Since LCM is found at B, A returns early with OrgInfo(B, 2)
```

---

## ✅ Final Result

```
lcm = get_lowest_common_manager(A, E, I)
print(lcm.name)  # → "B"
```

---

Let’s walk through the **call stack** for the function calls — as if we’re tracing it during runtime.

We'll simulate how each call to `get_org_info(manager, report_one, report_two)` is added to the **call stack**, what it returns,
and when it's popped off the stack.

---

### 🎯 Goal: Find LCM of `E` and `I`

We’ll show:
- The **call stack** state (`→` means we’re descending, `←` means we’re returning).
- **What the function is doing**.
- What it **returns**.

---

## 🧵 Initial Call

```
→ get_org_info(A)
```

---

## 📥 Recursive Descent into Left Subtree of A

```
→ get_org_info(A)
  → get_org_info(B)
    → get_org_info(D)
      → get_org_info(H)   # H has no children
        - Not E or I → return OrgInfo(None, 0)
      ← return OrgInfo(None, 0)

      → get_org_info(I)   # I is target
        - Found I → return OrgInfo(None, 1)
      ← return OrgInfo(None, 1)

    - D is not E or I
    - D sees 1 important report → return OrgInfo(None, 1)
  ← return OrgInfo(None, 1)
```

---

## 🧭 Continue in B → Now go to E

```
  → get_org_info(E)   # E is target
    - Found E → return OrgInfo(None, 1)
  ← return OrgInfo(None, 1)

- B is not target
- Total reports found under B = 1 (from D) + 1 (from E) = 2
- ✅ LCM is B → return OrgInfo(B, 2)
← return OrgInfo(B, 2)
```

---

## ❌ A gets the answer early → Skips Right Subtree

Since `OrgInfo.lowest_common_manager` is **not None**, A skips checking C.

```
→ get_org_info(A) sees LCM already found at B
← return OrgInfo(B, 2)
```

---

## 🧾 Final Stack Unwinding

```
Stack unwinds:
  get_org_info(H) → OrgInfo(None, 0)
  get_org_info(I) → OrgInfo(None, 1)
  get_org_info(D) → OrgInfo(None, 1)
  get_org_info(E) → OrgInfo(None, 1)
  get_org_info(B) → OrgInfo(B, 2)
  get_org_info(A) → OrgInfo(B, 2)
```

---

## ✅ Final Output

```
print(lcm.name)  # "B"
```

"""
