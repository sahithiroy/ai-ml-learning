"""Example of finally block."""

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("This always runs.")
