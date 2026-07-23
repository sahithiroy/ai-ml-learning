"""Day 11: Context Managers

Topics:
- with
- __enter__
- __exit__
- contextlib

Context managers help manage resources such as files, database connections,
and temporary directories automatically.
"""

import os
import time


class ContextManagerDemo:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False


# 1. with statement
print("Example 1: with statement")
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello from context manager")
print("File written")  # Output: File written
print()


# 2. Custom context manager using __enter__ and __exit__
print("Example 2: __enter__ and __exit__")

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False

with FileManager("demo.txt", "w") as file:
    file.write("Hello from custom manager")
print("Custom file manager completed")  # Output: Custom file manager completed
print()


# 3. Custom context manager with a helper class
print("Example 3: custom context manager")

with ContextManagerDemo("temp_demo.txt") as file:
    file.write("Temporary file created")

os.remove("temp_demo.txt")
print("Temporary file removed")  # Output: Temporary file removed
print()


# Practice builds
# 1. File Manager
print("Practice 1: File Manager")

class FileManagerPractice:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False

with FileManagerPractice("practice_file.txt", "w") as file:
    file.write("Practice file")
print("File manager practice complete")  # Output: File manager practice complete
print()


# 2. Database Connection Manager
print("Practice 2: Database Connection Manager")

class DatabaseConnection:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        print("Connected")

    def disconnect(self):
        self.connected = False
        print("Disconnected")

class DatabaseConnectionManager:
    def __enter__(self):
        self.db = DatabaseConnection()
        self.db.connect()
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.disconnect()
        return False

with DatabaseConnectionManager() as db:
    print("Using database connection")  # Output: Using database connection
print()


# 3. Timer Context Manager
print("Practice 3: Timer Context Manager")

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()
        print(f"Elapsed: {self.end - self.start:.4f} seconds")
        return False

with Timer() as timer:
    time.sleep(0.01)
print()


# 4. Temporary Directory Manager
print("Practice 4: Temporary Directory Manager")

class TemporaryDirectoryManager:
    def __init__(self, name):
        self.name = name
        self.path = None

    def __enter__(self):
        self.path = self.name
        os.mkdir(self.path)
        return self.path

    def __exit__(self, exc_type, exc_value, traceback):
        if os.path.exists(self.path):
            os.rmdir(self.path)
        return False

with TemporaryDirectoryManager("temp_dir_demo") as path:
    print(f"Created directory: {path}")
print("Temporary directory cleaned up")  # Output: Temporary directory cleaned up
