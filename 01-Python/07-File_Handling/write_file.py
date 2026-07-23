'''
Writing to a file:
Used to create or overwrite a text file.

Real-world use:
We use this to save user input, reports, or program results.

Code:
'''

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python!\n")
    file.write("This file was written using Python.")

# Output:
# The file output.txt will be created with the above text.
