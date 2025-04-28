# Sweet And Savory

You're hosting an event at a food festival and want to showcase the best possible pairing of two dishes from the festival that complement each other's flavor profile.

Each dish has a flavor profile represented by an integer. A negative integer means a dish is sweet, while a positive integer means a dish is savory. The absolute value of that integer represents the intensity of that flavor. For example, a flavor profile of `-3` is slightly sweet, one of `-10` is extremely sweet, one of `2` is mildly savory, and one of `8` is significantly savory.

You're given an array of these dishes and a target combined flavor profile. Write a function that returns the best possible pairing of two dishes (the pairing with a total flavor profile that's closest to the target one). Note that this pairing must include one sweet and one savory dish. You're also concerned about the dish being too savory, so your pairing should never be more savory than the target flavor profile.

All dishes will have a positive or negative flavor profile; there are no dishes with a 0 value. For simplicity, you can assume that there will be at most one best solution. If there isn't a valid solution, your function should return `[0, 0]`. The returned array should be sorted, meaning the sweet dish should always come first.

## Sample Input

```plaintext
dishes = [-3, -5, 1, 7]   
target = 8
```

## Sample Output

```plaintext
[-3, 7]

// The combined profile of 4 is closest without going over
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

The sweet and savory dishes are essentially two different lists that have been combined into one. It can be helpful to first separate them.

</details>

<details>
<summary><b>Hint 2</b></summary>

Looking at all possible pairs will be inefficient. Would sorting the lists first help improve the time complexity?

</details>

<details>
<summary><b>Hint 3</b></summary>

Try using a two pointer approach to find the best pairing. Start with a current pairing, and move the savory pointer until the pairing gets too savory. If the dish is too savory, then move the sweet pointer. Do this through the entire lists, keeping track of the best pairing you find.

</details>

## Optimal Time & Space Complexity

`O(n * log(n))` time | `O(n)` space - where `n` is number of dishes.
