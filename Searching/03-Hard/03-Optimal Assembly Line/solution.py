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
    left, right = max(step_durations), sum(step_durations)
    max_station_duration = float("inf")

    while left <= right:
        potential_max_station_duration = (left + right) // 2

        if is_potential_solution(
            step_durations, num_stations, potential_max_station_duration
        ):
            max_station_duration = potential_max_station_duration
            right = potential_max_station_duration - 1
        else:
            left = potential_max_station_duration + 1

    return max_station_duration


def is_potential_solution(step_durations, num_stations, potential_max_station_duration):
    stations_required = 1
    current_duration = 0

    for step_duration in step_durations:
        if current_duration + step_duration > potential_max_station_duration:
            stations_required += 1
            current_duration = step_duration
        else:
            current_duration += step_duration

    return stations_required <= num_stations


# Test Cases:

print(optimal_assembly_line([15, 15, 30, 30, 45], 3))
# Output: 60

print(optimal_assembly_line([1, 2, 3, 4, 5], 3))
# Output: 6

print(optimal_assembly_line([30, 5, 20, 10], 2))
# Output: 35
