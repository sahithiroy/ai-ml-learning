"""Example of custom exception."""

class AgeTooSmallError(Exception):
    pass

age = int(input("Enter your age: "))

if age < 18:
    raise AgeTooSmallError("You must be at least 18 years old.")
else:
    print("Access granted.")
