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
def get_lowest_common_manager(top_manager, report_one, report_two):
    return get_org_info(top_manager, report_one, report_two).lowest_common_manager


def get_org_info(manager, report_one, report_two):
    num_important_reports = 0

    for direct_report in manager.direct_reports:
        org_info = get_org_info(direct_report, report_one, report_two)

        if org_info.lowest_common_manager is not None:
            return org_info
        num_important_reports += org_info.num_important_reports

    if manager == report_one or manager == report_two:
        num_important_reports += 1
    lowest_common_manager = manager if num_important_reports == 2 else None

    return OrgInfo(lowest_common_manager, num_important_reports)


class OrgInfo:
    def __init__(self, lowest_common_manager, num_important_reports):
        self.lowest_common_manager = lowest_common_manager
        self.num_important_reports = num_important_reports


# Define the OrgChart structure
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.direct_reports = []

    def add_direct_reports(self, reports):
        self.direct_reports = reports


# Build the org chart
nodes = {}
for name in ["A", "B", "C", "D", "E", "F", "G", "H", "I"]:
    nodes[name] = OrgChart(name)

# Set up direct reports
nodes["A"].add_direct_reports([nodes["B"], nodes["C"]])
nodes["B"].add_direct_reports([nodes["D"], nodes["E"]])
nodes["C"].add_direct_reports([nodes["F"], nodes["G"]])
nodes["D"].add_direct_reports([nodes["H"], nodes["I"]])
# E, F, G, H, I have no direct reports (already initialized as empty)

# Run the test
top_manager = nodes["A"]
report_one = nodes["E"]
report_two = nodes["I"]

lcm = get_lowest_common_manager(top_manager, report_one, report_two)
print(lcm.name)  # Output: "B"
