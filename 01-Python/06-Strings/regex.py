"""Simple example of regular expressions.

Regex is used to find patterns in strings.
"""

import re

text = "My phone number is 9876543210"
match = re.search(r"\d+", text)  # Find digits in the string

if match:
    print("Found:", match.group())
    # Output: Found: 9876543210
else:
    print("No match found")
    # Output: No match found
