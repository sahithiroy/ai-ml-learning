'''
Membership operators in Python are used to test whether a value is present in a sequence.

They are:
- in     : returns True if the value exists in the sequence
- not in : returns True if the value does not exist in the sequence

Examples:
'''

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("banana" not in fruits) # False
print("grape" not in fruits)  # True

name = "Python"
print("P" in name)            # True
print("z" in name)            # False
