# Description:

"""
                                    Valid IP Addresses

You're given a string of length 12 or smaller, containing only digits. Write a function that returns all the possible
IP addresses that can be created by inserting three `.`s in the string.

An IP address is a sequence of four positive integers that are separated by `.`s, where each individual integer is 
within the range `0 - 255`, inclusive.

An IP address isn't valid if any of the individual integers contains leading `0`s. For example, `"192.168.0.1"` is a 
valid IP address, but `"192.168.00.1"` and `"192.168.0.01"` aren't, because they contain `"00"` and `01`, respectively.
Another example of a valid IP address is `"99.1.1.10"`; conversely, `"991.1.1.0"` isn't valid, because `"991"` is greater than 255.

Your function should return the IP addresses in string format and in no particular order. If no valid IP addresses can be
created from the string, your function should return an empty list.


## Sample Input:
```
string = "1921680"
```

## Sample Output:
```
[
  "1.9.216.80",
  "1.92.16.80",
  "1.92.168.0",
  "19.2.16.80",
  "19.2.168.0",
  "19.21.6.80",
  "19.21.68.0",
  "19.216.8.0",
  "192.1.6.80",
  "192.1.68.0",
  "192.16.8.0"
]
// The IP addresses could be ordered differently.
```

## Optimal Time & Space Complexity:
```
`O(1)` time | `O(1)` space.
```

"""

# =========================================================================================================================== #

# Solution:


# O(1) time | O(1) space.
def valid_IP_addresses(string):
    # This list will store all valid IP addresses found
    IP_addresses_found = []

    # Loop through the string to find the first part of the IP address
    # The first part can be 1 to 3 characters long (min(len(string), 4) ensures we don't go out of bounds)
    for i in range(1, min(len(string), 4)):
        # Initialize a list to store the four parts of the IP address
        current_IP_address_parts = ["", "", "", ""]

        # Assign the first part of the IP address
        current_IP_address_parts[0] = string[:i]

        # Check if the first part is valid
        if not is_valid_part(current_IP_address_parts[0]):
            continue  # If not valid, skip to the next iteration

        # Loop through the string to find the second part of the IP address
        # The second part can be 1 to 3 characters long
        for j in range(i + 1, i + min(len(string) - i, 4)):
            # Assign the second part of the IP address
            current_IP_address_parts[1] = string[i:j]

            # Check if the second part is valid
            if not is_valid_part(current_IP_address_parts[1]):
                continue  # If not valid, skip to the next iteration

            # Loop through the string to find the third part of the IP address
            # The third part can be 1 to 3 characters long
            for k in range(j + 1, j + min(len(string) - j, 4)):
                # Assign the third and fourth parts of the IP address
                current_IP_address_parts[2] = string[j:k]
                current_IP_address_parts[3] = string[k:]

                # Check if both the third and fourth parts are valid
                if is_valid_part(current_IP_address_parts[2]) and is_valid_part(
                    current_IP_address_parts[3]
                ):
                    # If all parts are valid, join them with dots to form a valid IP address
                    IP_addresses_found.append(".".join(current_IP_address_parts))

    # Return the list of all valid IP addresses found
    return IP_addresses_found


def is_valid_part(string):
    # Convert the string to an integer to check if it's a valid IP part
    string_as_int = int(string)

    # Check if the integer value is greater than 255 (invalid for an IP part)
    if string_as_int > 255:
        return False

    # Check if the length of the string matches the length of the integer when converted back to string
    # This ensures there are no leading zeros (e.g., "01" is invalid)
    return len(string) == len(str(string_as_int))


# Test Case 1
print(valid_IP_addresses("1921680"))
# Output:
# [
#     "1.9.216.80",
#     "1.92.16.80",
#     "1.92.168.0",
#     "19.2.16.80",
#     "19.2.168.0",
#     "19.21.6.80",
#     "19.21.68.0",
#     "19.216.8.0",
#     "192.1.6.80",
#     "192.1.68.0",
#     "192.16.8.0",
# ]

# Test Case 2
print(valid_IP_addresses("255255255255"))
# Output: ['255.255.255.255']

# Test Case 3
print(valid_IP_addresses("100100"))
# Output: ['1.0.0.100', '10.0.10.0', '100.1.0.0']

# =========================================================================================================================== #

# Big O:

"""
## Time and Space Complexity Analysis

### Time Complexity:

The time complexity of the `valid_IP_addresses` function can be analyzed as follows:

1. **Outer Loop (i)**: This loop runs for a maximum of 3 iterations (since `i` ranges from 1 to the 
minimum of `len(string)` and 4). In each iteration, it processes the first part of the IP address.

2. **Middle Loop (j)**: This loop runs for a maximum of 3 iterations for each iteration of the outer loop.
It processes the second part of the IP address.

3. **Inner Loop (k)**: This loop also runs for a maximum of 3 iterations for each iteration of the middle loop.
It processes the third and fourth parts of the IP address.

4. **Validation**: The `is_valid_part` function is called for each part of the IP address. This function runs
in constant time `O(1)` because it performs a simple integer conversion and length check.

Given that each loop runs for a maximum of 3 iterations, the total number of iterations is (3 * 3 * 3 = 27).
Therefore, the time complexity is **O(1)** because the number of iterations is constant and does not depend
on the length of the input string.

However, if we consider the length of the input string `n`, the loops are constrained by the length of the string,
so the time complexity can be more accurately described as **O(n^3)** in the worst case, where `n` is the length 
of the input string. This is because the loops are nested and each loop can run up to `n` times.

### Space Complexity:

The space complexity is determined by the storage used for the `IP_addresses_found` list and the `current_IP_address_parts` list.

1. **IP_addresses_found**: This list stores all valid IP addresses found. In the worst case, the number of valid IP
addresses is constant (e.g., for a string of length 12, there is only one valid IP address: "255.255.255.255").
Therefore, the space used by this list is **O(1)**.

2. **current_IP_address_parts**: This list always contains 4 parts of the IP address, so its space usage is constant, **O(1)**.

Thus, the overall space complexity is **O(1)** because the space used does not grow with the input size.

### Summary:
- **Time Complexity**: `O(1)`, but in the worst case - `O(n^3)`, where `n` is the length of the input string.
- **Space Complexity**: O(1), constant space.

"""

# =========================================================================================================================== #

# Code Explanation:

"""
### **Detailed Explanation of the Code**

The function `valid_IP_addresses(string)` is designed to generate all possible valid IPv4 addresses from
a given numeric string. Let's go through the implementation step by step.

---

### **Understanding an IPv4 Address**
An IPv4 address consists of four octets (parts), separated by dots (`.`), where:
- Each octet must be between `0` and `255`.
- Each octet cannot have leading zeros unless it is `0` itself (e.g., `"01"` is invalid but `"0"` is valid).
- The total length of the string must allow exactly four octets.

---

### **How the Function Works**
#### **Step 1: Initialize a List to Store Valid IPs**
```
IP_addresses_found = []
```
This list stores all the valid IP addresses generated.

---

#### **Step 2: Loop to Generate the First Octet**
```
for i in range(1, min(len(string), 4)):
```
- The first loop extracts the first part (first octet) of the potential IP address.
- We iterate `i` from `1` to `min(len(string), 4)`. This ensures that the first part has at most 3 digits
(as an octet can be at most 3 digits long).
- The candidate first octet is stored in:
  ```
  current_IP_address_parts[0] = string[:i]
  ```
- **Validation**: Check if this octet is valid using the helper function `is_valid_part()`. If invalid, `continue` to the next `i`.

---

#### **Step 3: Loop to Generate the Second Octet**
```
for j in range(i + 1, i + min(len(string) - i, 4)):
```
- The second loop extracts the second octet from the remaining string.
- The candidate second octet is:
  ```
  current_IP_address_parts[1] = string[i:j]
  ```
- **Validation**: If invalid, skip further processing for this `j`.

---

#### **Step 4: Loop to Generate the Third and Fourth Octets**
```
for k in range(j + 1, j + min(len(string) - j, 4)):
```
- The third loop extracts the third octet.
- The remaining part of the string automatically becomes the fourth octet.
- The third and fourth octets are stored in:
  ```
  current_IP_address_parts[2] = string[j:k]
  current_IP_address_parts[3] = string[k:]
  ```
- **Validation**: Both must be valid octets.

---

#### **Step 5: If All Four Parts Are Valid, Store the IP Address**
```
if is_valid_part(current_IP_address_parts[2]) and is_valid_part(current_IP_address_parts[3]):
    IP_addresses_found.append(".".join(current_IP_address_parts))
```
- If all four octets are valid, we join them using `"."` and store them in `IP_addresses_found`.

---

### **Helper Function: `is_valid_part(string)`**
```
def is_valid_part(string):
    string_as_int = int(string)

    if string_as_int > 255:
        return False

    return len(string) == len(str(string_as_int))
```
This function checks whether a given octet is a valid IP segment:
- It converts the string to an integer.
- If the integer is greater than `255`, return `False`.
- **To check for leading zeros**, the function ensures that converting the number back to a string doesn’t 
change its length. For example:
  - `"01"` as an integer is `1`, which becomes `"1"` again, so it is **invalid**.
  - `"0"` remains `"0"`, so it is **valid**.

---

Let's break down the three test cases and analyze how the function generates valid IPv4 addresses for each.

## **Test Case 1: `valid_IP_addresses("1921680")`**
**Input:** `"1921680"`

### **Step-by-Step Execution**
We need to split `"1921680"` into four valid octets. The function explores various partitioning combinations
while ensuring each octet is valid.

### **Valid IP Addresses Generated:**
1. `"1.9.216.80"`  
   - First: `"1"` ✅
   - Second: `"9"` ✅
   - Third: `"216"` ✅
   - Fourth: `"80"` ✅

2. `"1.92.16.80"`  
   - First: `"1"` ✅
   - Second: `"92"` ✅
   - Third: `"16"` ✅
   - Fourth: `"80"` ✅

3. `"1.92.168.0"`  
   - First: `"1"` ✅
   - Second: `"92"` ✅
   - Third: `"168"` ✅
   - Fourth: `"0"` ✅

4. `"19.2.16.80"`  
   - First: `"19"` ✅
   - Second: `"2"` ✅
   - Third: `"16"` ✅
   - Fourth: `"80"` ✅

5. `"19.2.168.0"`  
   - First: `"19"` ✅
   - Second: `"2"` ✅
   - Third: `"168"` ✅
   - Fourth: `"0"` ✅

6. `"19.21.6.80"`  
   - First: `"19"` ✅
   - Second: `"21"` ✅
   - Third: `"6"` ✅
   - Fourth: `"80"` ✅

7. `"19.21.68.0"`  
   - First: `"19"` ✅
   - Second: `"21"` ✅
   - Third: `"68"` ✅
   - Fourth: `"0"` ✅

8. `"19.216.8.0"`  
   - First: `"19"` ✅
   - Second: `"216"` ✅
   - Third: `"8"` ✅
   - Fourth: `"0"` ✅

9. `"192.1.6.80"`  
   - First: `"192"` ✅
   - Second: `"1"` ✅
   - Third: `"6"` ✅
   - Fourth: `"80"` ✅

10. `"192.1.68.0"`  
    - First: `"192"` ✅
    - Second: `"1"` ✅
    - Third: `"68"` ✅
    - Fourth: `"0"` ✅

11. `"192.16.8.0"`  
    - First: `"192"` ✅
    - Second: `"16"` ✅
    - Third: `"8"` ✅
    - Fourth: `"0"` ✅

### **Final Output**
```
[
    "1.9.216.80",
    "1.92.16.80",
    "1.92.168.0",
    "19.2.16.80",
    "19.2.168.0",
    "19.21.6.80",
    "19.21.68.0",
    "19.216.8.0",
    "192.1.6.80",
    "192.1.68.0",
    "192.16.8.0",
]
```

---

## **Test Case 2: `valid_IP_addresses("255255255255")`**
**Input:** `"255255255255"`

### **Step-by-Step Execution**
The function explores all possible ways to split `"255255255255"` into four valid octets:
1. `"255"` ✅ (valid)
2. `"255"` ✅ (valid)
3. `"255"` ✅ (valid)
4. `"255"` ✅ (valid)

Since `"255.255.255.255"` is the **only** valid way to split the string while ensuring all segments are
within range and have no leading zeros, the function returns:

### **Final Output**
```
['255.255.255.255']
```

---

## **Test Case 3: `valid_IP_addresses("100100")`**
**Input:** `"100100"`

### **Step-by-Step Execution**
We need to split `"100100"` into four valid octets:

1. **First Octet Choices**:
   - `"1"` ✅
   - `"10"` ✅
   - `"100"` ✅

2. **Valid IP Addresses Generated:**

   - `"1.0.0.100"`  
     - First: `"1"` ✅
     - Second: `"0"` ✅
     - Third: `"0"` ✅
     - Fourth: `"100"` ✅
   
   - `"10.0.10.0"`  
     - First: `"10"` ✅
     - Second: `"0"` ✅
     - Third: `"10"` ✅
     - Fourth: `"0"` ✅
   
   - `"100.1.0.0"`  
     - First: `"100"` ✅
     - Second: `"1"` ✅
     - Third: `"0"` ✅
     - Fourth: `"0"` ✅

### **Final Output**
```
['1.0.0.100', '10.0.10.0', '100.1.0.0']
```

---

## **Summary of Test Cases**

| Test Case | Input            | Expected Output                            |
|-----------|------------------|--------------------------------------------|
| **1**     | `"1921680"`      | Multiple valid IP addresses                |
| **2**     | `"255255255255"` | `['255.255.255.255']` (only 1 possibility) |
| **3**     | `"100100"`       | `['1.0.0.100', '10.0.10.0', '100.1.0.0']`  |

---

### **Summary**
- The function systematically extracts potential IP segments.
- It validates each segment using the `is_valid_part()` function.
- If all four segments are valid, the IP is stored.
- The final output is a list of all possible valid IPv4 addresses.

"""
