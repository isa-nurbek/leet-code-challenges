# Problem Description:

"""

                                            Generate Div Tags

Write a function that takes in a positive integer `number_of_tags` and returns a list of all the valid strings that you can generate
with that number of matched `<div></div>` tags.

A string is valid and contains matched `<div></div>` tags if for every opening tag `<div>`, there's a closing tag `</div>` that
comes after the opening tag and that isn't used as a closing tag for another opening tag. Each output string should contain exactly
`number_of_tags` opening tags and `number_of_tags` closing tags.

For example, `given number_of_tags = 2`, the valid strings to return would be: `["<div></div><div></div>", "<div><div></div></div>"]`.

Note that the output strings don't need to be in any particular order.


## Sample Input
```
number_of_tags = 3
```

## Sample Output
```
[
    "<div><div><div></div></div></div>",
    "<div><div></div><div></div></div>",
    "<div><div></div></div><div></div>",
    "<div></div><div><div></div></div>",
    "<div></div><div></div><div></div>",
] // The strings could be ordered differently.
```

## Optimal Time & Space Complexity:
```
O((2n)!/((n!((n + 1)!)))) time | O((2n)!/((n!((n + 1)!)))) space - where `n` is the input number.
```
"""

# =========================================================================================================================== #

# Solution:


# O((2n)!/((n!((n + 1)!)))) time | O((2n)!/((n!((n + 1)!)))) space
def generate_div_tags(number_of_tags):
    matched_div_tags = []
    generate_div_tags_from_prefix(number_of_tags, number_of_tags, "", matched_div_tags)

    return matched_div_tags


def generate_div_tags_from_prefix(
    opening_tags_needed, closing_tags_needed, prefix, result
):

    if opening_tags_needed > 0:
        new_prefix = prefix + "<div>"
        generate_div_tags_from_prefix(
            opening_tags_needed - 1, closing_tags_needed, new_prefix, result
        )

    if opening_tags_needed < closing_tags_needed:
        new_prefix = prefix + "</div>"
        generate_div_tags_from_prefix(
            opening_tags_needed, closing_tags_needed - 1, new_prefix, result
        )

    if closing_tags_needed == 0:
        result.append(prefix)


# Test Cases:

print(generate_div_tags(3))
# Output:
"""
[
    "<div><div><div></div></div></div>",
    "<div><div></div><div></div></div>",
    "<div><div></div></div><div></div>",
    "<div></div><div><div></div></div>",
    "<div></div><div></div><div></div>",
] 
"""

print(generate_div_tags(1))
# Output: ["<div></div>"]
