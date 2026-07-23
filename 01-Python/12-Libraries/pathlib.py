"""Examples for the pathlib module.

The pathlib module provides an object-oriented way to work with file paths.
"""

from pathlib import Path

path = Path("demo.txt")
print(path.name)      # Output: demo.txt
print(path.exists())  # Output: False if the file does not exist
