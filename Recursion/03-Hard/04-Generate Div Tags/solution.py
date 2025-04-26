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


# O(4ⁿ) time | O(4ⁿ) space
def generate_div_tags(number_of_tags):
    """
    Generates all possible valid combinations of a given number of div tags.

    Args:
        number_of_tags (int): The number of div tag pairs to generate

    Returns:
        list: A list of strings containing all valid div tag combinations
    """
    matched_div_tags = []
    # Start the recursive generation with full count of opening and closing tags needed
    generate_div_tags_from_prefix(number_of_tags, number_of_tags, "", matched_div_tags)
    return matched_div_tags


def generate_div_tags_from_prefix(
    opening_tags_needed, closing_tags_needed, prefix, result
):
    """
    Recursively generates valid div tag combinations by building them character by character.

    The approach uses backtracking to explore all possible valid sequences where:
    1. We never close a tag that hasn't been opened
    2. We end with all tags properly closed

    Args:
        opening_tags_needed (int): How many more opening <div> tags we can add
        closing_tags_needed (int): How many more closing </div> tags we can add
        prefix (str): The current string being built
        result (list): Accumulator for valid complete strings
    """

    # Base case: all tags have been properly opened and closed
    if closing_tags_needed == 0:
        result.append(prefix)
        return

    # If we can still open more tags (more <div> available)
    if opening_tags_needed > 0:
        # Add an opening tag and recurse, decreasing opening tags needed
        new_prefix = prefix + "<div>"
        generate_div_tags_from_prefix(
            opening_tags_needed - 1, closing_tags_needed, new_prefix, result
        )

    # We can add a closing tag if we have unclosed opening tags
    # (opening_tags_needed < closing_tags_needed means we have open tags to close)
    if opening_tags_needed < closing_tags_needed:
        # Add a closing tag and recurse, decreasing closing tags needed
        new_prefix = prefix + "</div>"
        generate_div_tags_from_prefix(
            opening_tags_needed, closing_tags_needed - 1, new_prefix, result
        )


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
