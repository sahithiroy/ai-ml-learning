'''
nested if:
An if statement inside another if statement.

Real-world use:
We use nested if when one decision depends on another decision.
Example: first check if the user is logged in, then check if they have permission.

Example:
'''

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("You need an ID")
else:
    print("You are too young")
