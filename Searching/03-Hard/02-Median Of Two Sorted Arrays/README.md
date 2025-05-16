# Median Of Two Sorted Arrays

You're given `two sorted arrays` of integers `array_one` and `array_two`. Write a function that returns the `median` of these arrays.

You can assume both arrays have at least one value. However, they could be of different lengths. If the `median` is a decimal value, it should not be rounded (beyond the inevitable rounding of floating point math).

## Sample Input

```plaintext
array_one = [1, 3, 4, 5]
array_two = [2, 3, 6, 7]
```

## Sample Output

```plaintext
3.5 

// The combined array is [1, 2, 3, 3, 4, 5, 6, 7]
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

The `median` value of the combined array will always have the same number of integers to its left and its right. Therefore the goal is to find the element at the middle index (or the average of the middle indices if the array has an even length).

</details>

<details>
<summary><b>Hint 2</b></summary>

A naive approach would be to iterate through both arrays simultaneously, with each iteration moving forward in the array with the lower current value until passing half of the total values. This solution would have a linear time complexity, but can you find a way to improve it to be `logarithmic`?

</details>

<details>
<summary><b>Hint 3</b></summary>

Try considering just the smaller of the two arrays. Start with the median of that array, and temporarily assume that all of the values to its left of that median are to the left of the overall median, and all of the values to the right are to the right of the overall median. Assuming this is correct, could you also place a dividing point in the larger array, to ensure there are the correct number of values on either side of the combined median? And now can you find a way to do a binary search with just the smaller array to find the actual correct dividing point?

</details>

<details>
<summary><b>Hint 4</b></summary>

The value at the dividing point in `array_one` must be smaller than the value at the index after the dividing point of `array_two`. The value at the dividing point in `array_two` must be smaller than the value at the index after the dividing point of `array_one`. If either of these conditions are not met, then the binary search must continue to either include more or less elements from that smaller array.

</details>

## Optimal Time & Space Complexity

`O(log(min(n, m))` time | `O(1)` space - where `n` is the length of `array_one` and `m` is the length of `array_two`.
