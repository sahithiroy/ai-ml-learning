"""Nested structures in Python

Nested structures are data structures inside other data structures.
For example, a list can contain dictionaries, or a dictionary can contain lists.

This is useful when you want to store related data together.
"""

# Example 1: List of dictionaries
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
]
print(students)

# Example 2: Dictionary containing a list
person = {
    "name": "Charlie",
    "hobbies": ["reading", "music", "sports"]
}
print(person)

# Example 3: Nested dictionary
company = {
    "employee": {
        "name": "Daisy",
        "role": "Developer"
    }
}
print(company)
