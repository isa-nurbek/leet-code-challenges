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
