'''
CSV files:
Used to store data in a table-like format.

Real-world use:
We use CSV files for data such as student records, sales data, or contact lists.

Code:
'''

import csv

rows = [
    ["Name", "Age"],
    ["Alice", 20],
    ["Bob", 25]
]

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# Output:
# A file named data.csv will be created with table rows.
