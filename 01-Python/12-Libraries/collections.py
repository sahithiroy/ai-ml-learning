"""Examples for the collections module.

The collections module provides useful container data types like Counter and defaultdict.
"""

from collections import Counter

items = ["apple", "apple", "banana", "cherry"]
count = Counter(items)
print(count)           # Output: Counter({'apple': 2, 'banana': 1, 'cherry': 1})
print(count["apple"]) # Output: 2
