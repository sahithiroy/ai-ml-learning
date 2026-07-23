'''
Reading a file:
Used to read the contents of a text file.

Real-world use:
We use this to open saved data such as notes, logs, or configuration files.

Code:
'''

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Output:
# This is a sample file.
# It contains text for learning file handling.
