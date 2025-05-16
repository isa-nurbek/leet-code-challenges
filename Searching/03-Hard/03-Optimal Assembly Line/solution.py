# Problem Description:

"""
                                             Optimal Assembly Line

One of the most efficient ways to run a factory is to use an assembly line, with multiple stations performing different assembling
steps simultaneously in order to save time. But an assembly line is only as fast as its slowest station/step; for example, if an
assembly line has `100` different steps performed by `100` different stations, with `99` steps taking `1` minute each to complete
and `1` step taking `1` hour to complete, then the entire assembly line is dramatically slowed down by the `1-hour-long` step.

Write a function that takes in a `non-empty` array of positive integers `step_durations` and a positive integer `num_stations`.
The input array of integers represents the times that the various steps in an assembly process take, and the input integer
represents the number of stations that this assembly process has access to. For this particular assembly process, a single station
can perform multiple steps, so long as these steps are performed in order, meaning that a single station can perform multiple steps
whose times appear consecutively in the `step_durations` array. Your function should return the longest duration of a single station
in the assembly line after optimizing the assembly line (i.e., minimizing its slowest station/step).

You can assume that there will never be more stations than steps.


## Sample Input:
```
step_durations = [15, 15, 30, 30, 45]
num_stations = 3
```

## Sample Output:
```
60

// Station 1 does steps 0 and 1. Station 2 does steps 2 and 3. Station 3 does step 4.
```

## Optimal Time & Space Complexity:
```
O(n * log(m)) time | O(1) space - where `n` is the length of steps, and `m` is the sum of all values in steps.
```

"""

# =========================================================================================================================== #

# Solution:


# O(n * log(m)) time | O(1) space
def optimal_assembly_line(step_durations, num_stations):
    """
    Finds the minimum possible maximum station duration when assembling products
    with given step durations across a fixed number of stations.

    Uses binary search to efficiently find the optimal solution.

    Args:
        step_durations: List of durations for each assembly step
        num_stations: Number of available workstations

    Returns:
        The minimum possible maximum duration across all stations
    """
    # Initialize binary search bounds:
    # - The minimum possible max duration is the duration of the longest single step
    # - The maximum possible max duration is the sum of all step durations (all steps in one station)
    left, right = max(step_durations), sum(step_durations)
    max_station_duration = float("inf")  # Will store the optimal solution

    # Binary search loop to find the minimal maximum station duration
    while left <= right:
        # Try a potential solution in the middle of current search range
        potential_max_station_duration = (left + right) // 2

        # Check if we can distribute steps with this maximum duration
        if is_potential_solution(
            step_durations, num_stations, potential_max_station_duration
        ):
            # If yes, try to find a better (smaller) solution
            max_station_duration = potential_max_station_duration
            right = potential_max_station_duration - 1
        else:
            # If no, we need to try larger durations
            left = potential_max_station_duration + 1

    return max_station_duration


def is_potential_solution(step_durations, num_stations, potential_max_station_duration):
    """
    Checks if it's possible to distribute the assembly steps across stations
    without exceeding the given maximum station duration.

    Args:
        step_durations: List of durations for each assembly step
        num_stations: Number of available workstations
        potential_max_station_duration: The maximum duration we're testing

    Returns:
        True if the steps can be distributed within the given constraints,
        False otherwise
    """
    stations_required = 1  # At least one station needed
    current_duration = 0  # Tracks duration of current station

    for step_duration in step_durations:
        # Check if adding this step would exceed current station's capacity
        if current_duration + step_duration > potential_max_station_duration:
            # Need to use a new station
            stations_required += 1
            current_duration = step_duration  # Start new station with this step

            # Early exit if we've already exceeded station count
            if stations_required > num_stations:
                return False
        else:
            # Add step to current station
            current_duration += step_duration

    return stations_required <= num_stations


# Test Cases:

print(optimal_assembly_line([15, 15, 30, 30, 45], 3))
# Output: 60

print(optimal_assembly_line([1, 2, 3, 4, 5], 3))
# Output: 6

print(optimal_assembly_line([30, 5, 20, 10], 2))
# Output: 35

# =========================================================================================================================== #

# Big O Analysis:

"""
## Time and Space Complexity Analysis:

Let's analyze the time and space complexity of the given `optimal_assembly_line` algorithm.

### Time Complexity:

1. **Binary Search Component**:
   - The binary search runs between `left = max(step_durations)` and `right = sum(step_durations)`.
   - Each iteration reduces the search space by half, so the number of iterations is `O(log(sum(step_durations) - max(step_durations)))`.

2. **Feasibility Check (`is_potential_solution`)**:
   - This function iterates through all `step_durations` exactly once, performing `O(1)` operations per step.
   - Thus, its time complexity is `O(n)`, where `n` is the number of steps.

3. **Overall Time Complexity**:
   - Since the binary search performs `O(log(S))` iterations (where `S = sum(step_durations) - max(step_durations)`) and each
   iteration calls `is_potential_solution` in `O(n)` time, the total time complexity is: O(n log S)

### Space Complexity:

- The algorithm uses a constant amount of additional space (for variables like `left`, `right`, `max_station_duration`, etc.).
- The `is_potential_solution` function also uses only `O(1)` extra space (for `stations_required` and `current_duration`).
- Thus, the **space complexity is `O(1)`** (no additional space proportional to input size is used).

### Summary:
- **Time Complexity**: `O(n log S)` where `n` is the number of steps and `S = sum(step_durations) - max(step_durations)`.
- **Space Complexity**: `O(1)` (constant space).

This is an efficient solution for the assembly line balancing problem, leveraging binary search to minimize the maximum station duration.

"""

# =========================================================================================================================== #

# Detailed Code Explanation:

"""
This code solves a problem commonly known as the **Assembly Line Balancing Problem**, where you want to divide a sequence of tasks
(each with a fixed time duration) among a limited number of workstations in such a way that the **maximum time assigned to any 
workstation** is minimized.

---

## **Goal**

Given:

* A list of **step durations** (e.g., `[15, 15, 30, 30, 45]`)
* A number of **stations** (e.g., `3`)

The goal is to **partition** the steps into the given number of stations such that:

* The **maximum total time** on any one station is minimized.
* Steps must be assigned in order (no rearranging).

---

## **Code Breakdown**

### `optimal_assembly_line(step_durations, num_stations)`

This is the **main function** that performs a **binary search** on the answer.

### Step-by-step:

1. **Initialize bounds for binary search:**

   ```
   left = max(step_durations)
   right = sum(step_durations)
   ```

   * The **minimum possible maximum time** on any station (`left`) is the longest individual step (since each step must be fully assigned).
   * The **maximum possible time** (`right`) is if all steps are assigned to one station.

2. **Binary search loop:**

   ```
   while left <= right:
       potential_max_station_duration = (left + right) // 2
   ```

   * Try the **midpoint** between left and right as a guess for the max station load.

3. **Check if this guess is feasible** using helper function:

   ```
   if is_potential_solution(step_durations, num_stations, potential_max_station_duration):
   ```

   * If it's possible to assign all steps to `num_stations` without exceeding this `potential_max_station_duration`,
   it might be the answer, but we try for **a smaller one**.

   * If not, we try **a larger** duration.

---

### `is_potential_solution(step_durations, num_stations, potential_max_station_duration)`

This function **checks whether we can assign the tasks** into the given number of stations such that **no station exceeds
the given potential max duration**.

1. Start with 1 station and 0 duration:

   ```
   stations_required = 1
   current_duration = 0
   ```

2. Loop through each step:

   ```
   for step_duration in step_durations:
       if current_duration + step_duration > potential_max_station_duration:
           stations_required += 1
           current_duration = step_duration
       else:
           current_duration += step_duration
   ```

   * If adding a step exceeds the current station's capacity, start a **new station**.
   * Otherwise, add the step to the current station.

3. After the loop, check how many stations were needed:

   ```
   return stations_required <= num_stations
   ```

---

## **Example Explanation**

### Test: `optimal_assembly_line([15, 15, 30, 30, 45], 3)`

* Possible grouping with minimum max load of **60**:

  * Station 1: 15 + 15 + 30 = 60
  * Station 2: 30
  * Station 3: 45

### Test: `optimal_assembly_line([1, 2, 3, 4, 5], 3)`

* Optimal grouping with max load **6**:

  * Station 1: 1 + 2 + 3 = 6
  * Station 2: 4
  * Station 3: 5

### Test: `optimal_assembly_line([30, 5, 20, 10], 2)`

* Optimal grouping with max load **35**:

  * Station 1: 30 + 5 = 35
  * Station 2: 20 + 10 = 30

---

## ✅ **Summary**

* **Binary Search** is used to minimize the **maximum load per station**.
* `is_potential_solution()` checks whether a specific load limit can be achieved with the given number of stations.
* The algorithm runs efficiently with **O(n log sum)** complexity, where `n` is the number of steps.

---

Let's visualize how the `optimal_assembly_line` function works using **ASCII diagrams**, showing how the tasks are distributed
across stations in a way that minimizes the **maximum duration per station**.

---

### ✅ Test Case:

```
optimal_assembly_line([15, 15, 30, 30, 45], 3)
# Expected output: 60
```

### 🧱 Step Durations:

```
[15, 15, 30, 30, 45]
```

---

### 🔎 Goal:

Split these tasks across **3 stations** such that no station has a total duration over 60 (the optimal max).

---

### ✅ Final Partitioning (One Possible Optimal):

```
Station 1: [15][15][30] -> 15 + 15 + 30 = 60
Station 2:       [30]    -> 30
Station 3:            [45] -> 45
```

### ASCII Visualization:

```
Station 1: |■■■■■■■■■■■■■■■|■■■■■■■■■■■■■■■|■■■■■■■■■■■■■■■■■■■■■■■■|
            15             15             30   --> total: 60

Station 2:                            |■■■■■■■■■■■■■■■■■■■■■■■■|
                                      30                       --> total: 30

Station 3:                                          |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■|
                                                    45                             --> total: 45
```

---

### 🧪 Test Case:

```
optimal_assembly_line([1, 2, 3, 4, 5], 3)
# Expected output: 6
```

### Final Partitioning:

```
Station 1: [1][2][3] -> 6
Station 2:       [4] -> 4
Station 3:          [5] -> 5
```

### ASCII Visualization:

```
Station 1: |■|■■|■■■|           --> total: 6
            1  2   3

Station 2:         |■■■■|       --> total: 4
                    4

Station 3:              |■■■■■| --> total: 5
                         5
```

---

### ⚙️ How Binary Search Helps:

Imagine a ruler where:

```
left  = max(step_durations) = 45
right = sum(step_durations) = 135
```

Binary search checks values like:

* mid = (45 + 135) // 2 = 90
* Is 90 feasible? → Yes → Try smaller
* mid = (45 + 89) // 2 = 67
* Is 67 feasible? → Yes → Try smaller
* …
* Eventually lands on **60** as the smallest max station load that works.

"""
