# Ambiguous Measurements

This problem deals with measuring cups that are missing important measuring labels. Specifically, a measuring cup only has two measuring lines, a `Low (L)` line and a `High (H)` line. This means that these cups can't precisely measure and can only guarantee that the substance poured into them will be between the `L` and `H` line. For example, you might have a measuring cup that has a Low line at `400ml` and a high line at `435ml`. This means that when you use this measuring cup, you can only be sure that what you're measuring is between `400ml` and `435ml`.

You're given a list of measuring cups containing their low and high lines as well as one `low` integer and one `high` integer representing a range for a target measurement. Write a function that returns a boolean representing whether you can use the cups to accurately measure a volume in the specified `[low, high]` range (the range is inclusive).

> Note that:

- Each measuring cup will be represented by a pair of positive integers `[L, H]`, where `0 <= L <= H`.
- You'll always be given at least one measuring cup, and the `low` and `high` input parameters will always satisfy the following constraint: `0 <= low <= high`.
- Once you've measured some liquid, it will immediately be transferred to a larger bowl that will eventually (possibly) contain the target measurement.
- You can't pour the contents of one measuring cup into another cup.

## Sample Input

```plaintext
measuring_cups = [
  [200, 210],
  [450, 465],
  [800, 850],
] 

low = 2100
high = 2300
```

## Sample Output

```plaintext
True

"""
We use cup [450, 465] to measure four volumes:
First measurement: Low = 450, High = 465
Second measurement: Low = 450 + 450 = 900, High = 465 + 465 = 930
Third measurement: Low = 900 + 450 = 1350, High = 930 + 465 = 1395
Fourth measurement: Low = 1350 + 450 = 1800, High = 1395 + 465 = 1860

Then we use cup [200, 210] to measure two volumes:
Fifth measurement: Low = 1800 + 200 = 2000, High = 1860 + 210 = 2070
Sixth measurement: Low = 2000 + 200 = 2200, High = 2070 + 210 = 2280

We've measured a volume in the range [2200, 2280].
This is within our target range, so we return `True`.

Note: there are other ways to measure a volume in the target range.
"""
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

Start by considering the last cup that you'll use in your sequence of measurements. If it isn't possible to use any of the cups as the last cup, then you can't measure the desired volume.

</details>

<details>
<summary><b>Hint 2</b></summary>

If the cup that you're going to use last has a measuring range of `[100, 110]` and you want to measure in the range of `[500, 550]`, then after you pick this cup as the last cup, you need to measure a range of `[400, 440]`. Now, you can simply pick the last cup you'll use to measure this new range. If you continue these steps, you'll eventually know if you're able to measure the entire range or not.

</details>

<details>
<summary><b>Hint 3</b></summary>

`Hint #2` should give you an idea of how to solve this problem recursively. Try every cup as the last cup for the starting range, then recursively try to measure the new ranges created after using the selected last cups. If you ever reach a point where one cup can measure the entire range, then you're finished and you can measure the target range. Try to think of a way to optimize this recursive approach, since it might involve a lot of repeated calculations.

</details>

## Optimal Time & Space Complexity

`O(low * high * n)` time | `O(low * high)` space - where `n` is the number of measuring cups.
