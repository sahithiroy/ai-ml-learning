'''
pathlib:
Used to work with file paths in a cleaner and more modern way.

Real-world use:
We use pathlib when creating, reading, or checking files and folders.

Code:
'''

from pathlib import Path

file_path = Path("notes.txt")
file_path.write_text("Hello from pathlib", encoding="utf-8")

# Output:
# A file named notes.txt will be created.
