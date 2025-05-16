# Optimal Assembly Line

One of the most efficient ways to run a factory is to use an assembly line, with multiple stations performing different assembling steps simultaneously in order to save time. But an assembly line is only as fast as its slowest station/step; for example, if an assembly line has `100` different steps performed by `100` different stations, with `99` steps taking `1` minute each to complete and `1` step taking `1` hour to complete, then the entire assembly line is dramatically slowed down by the `1-hour-long` step.

Write a function that takes in a `non-empty` array of positive integers `step_durations` and a positive integer `num_stations`. The input array of integers represents the times that the various steps in an assembly process take, and the input integer represents the number of stations that this assembly process has access to. For this particular assembly process, a single station can perform multiple steps, so long as these steps are performed in order, meaning that a single station can perform multiple steps whose times appear consecutively in the `step_durations` array. Your function should return the longest duration of a single station in the assembly line after optimizing the assembly line (i.e., minimizing its slowest station/step).

You can assume that there will never be more stations than steps.

## Sample Input

```plaintext
step_durations = [15, 15, 30, 30, 45]
num_stations = 3
```

## Sample Output

```plaintext
60  

// Station 1 does steps 0 and 1. Station 2 does steps 2 and 3. Station 3 does step 4.
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

First try considering what the range of possible solutions are. What is the smallest possible solution and the largest possible solution?

</details>

<details>
<summary><b>Hint 2</b></summary>

The smallest possible solution would be the largest duration in `step_durations` in the case that this step was the only step done by its station. The largest possible solution would be the sum of all of the `step_durations` if they were all done by one solution.

</details>

<details>
<summary><b>Hint 3</b></summary>

Given this smallest and largest possible solution, you can do a `binary search` between the values to find the smallest potential solution that is actually valid.

</details>

<details>
<summary><b>Hint 4</b></summary>

You can check if a potential solution is valid by during a single iteration through the `step_durations` array. If a step has a duration larger than the potential solution's max station duration, then that can't be a correct solution. Otherwise, combine that step with the previous steps if the combination of them is not larger than the potential solution's max station duration. If it can't be combined with previous steps, then it must require a new station. Keep track of how many stations are required and ensure it is less than or equal to `num_stations`.

</details>

## Optimal Time & Space Complexity

`O(n * log(m))` time | `O(1)` space - where `n` is the length of steps, and `m` is the sum of all values in steps.
