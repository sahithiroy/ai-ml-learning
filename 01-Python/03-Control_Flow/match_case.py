'''
match-case statement:
Used for pattern matching in Python 3.10+.

Real-world use:
We use match-case when a value needs to be compared with many possible options.
Example: selecting a menu option or handling different command types.

Example:
'''

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")
