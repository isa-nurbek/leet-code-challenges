# Generate Div Tags

Write a function that takes in a positive integer `number_of_tags` and returns a list of all the valid strings that you can generate with that number of matched `<div></div>` tags.

A string is valid and contains matched `<div></div>` tags if for every opening tag `<div>`, there's a closing tag `</div>` that comes after the opening tag and that isn't used as a closing tag for another opening tag. Each output string should contain exactly `number_of_tags` opening tags and `number_of_tags` closing tags.

For example, `given number_of_tags = 2`, the valid strings to return would be: `["<div></div><div></div>", "<div><div></div></div>"]`.

> Note that the output strings don't need to be in any particular order.

## Sample Input

```plaintext
number_of_tags = 3
```

## Sample Output

```plaintext
[
    "<div><div><div></div></div></div>",
    "<div><div></div><div></div></div>",
    "<div><div></div></div><div></div>",
    "<div></div><div><div></div></div>",
    "<div></div><div></div><div></div>",
]

// The strings could be ordered differently.
```

## Hints

<details>
<summary><b>Hint 1</b></summary>

The brute-force approach to solve this problem is to generate every single possible string that contains `number_of_tags` tags and to then check all of those strings to see if they're valid. Can you think of a better way to do this?

</details>

<details>
<summary><b>Hint 2</b></summary>

To solve this problem optimally, you'll have to incrementally build valid strings by adding `<div>` and `</div>` tags to already valid partial strings. While doing this, you can avoid creating strings that will never lead to a valid final string by following two rules:

- If a string has fewer opening tags than `number_of_tags`, it's valid to add an opening tag to the end of it.
- If a string has fewer closing tags than opening tags, it's valid to add a closing tag to the end of it.

</details>

<details>
<summary><b>Hint 3</b></summary>

Using the rules defined in Hint #2, write a recursive algorithm that generates all possible valid strings. You'll need to keep track of how many opening and closing tags each partial string has available (at each recursive call), and you'll simply follow the rules outlined in Hint #2. Once a string has no more opening and closing tags available, you can add it to your final list of strings. Your first call to the function will start with an empty string as the partial string and with `number_of_tags` as the number of opening and closing tags available. For example, after you add an opening tag to a partial string, you'll recursively call the function like this:
`recursive_function(partial_string_with_extra_opening_tag, opening_tags - 1, closing_tags)`

</details>

## Optimal Time & Space Complexity

`O(4ⁿ / √n)` time | `O(n · 4ⁿ / √n)` space - where `n` is the input number.
