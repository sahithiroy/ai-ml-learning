'''
Logical operators in Python are used to combine conditional statements.

They are:
- and : returns True if both conditions are True
- or  : returns True if at least one condition is True
- not : reverses the result of a condition

Examples:
'''

age = 25
has_id = True

print(age > 18 and has_id)      # True
print(age > 30 and has_id)      # False
print(age > 18 or has_id)       # True
print(age > 30 or has_id)       # True
print(not has_id)               # False

is_student = False
print(not is_student)           # True
