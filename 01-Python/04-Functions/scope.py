'''
Scope:
Scope defines where a variable is accessible.

Real-world use:
We use scope to control which parts of the program can use a variable.
Example: local variables inside a function are not available outside it.

Code:
'''

x = "global"

def show():
    y = "local"
    print(x)
    print(y)

# Output: global
# Output: local
show()
