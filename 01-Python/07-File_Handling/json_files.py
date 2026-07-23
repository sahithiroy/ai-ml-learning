'''
JSON files:
Used to store data in a readable key-value structure.

Real-world use:
We use JSON for configuration files, APIs, and storing structured data.

Code:
'''

import json

person = {"name": "Alice", "age": 20}

with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person, file)

# Output:
# A file named person.json will be created with: {"name": "Alice", "age": 20}
