'''
Variables:
variables are used to store data in a program. In Python, you can create a variable by assigning a value to it using the equals sign (=). For example:
x = 5  # This creates a variable named 'x' and assigns it the value of 5.
you can also assign values of different data types to variables, such as strings, lists, and dictionaries. For example:
name = "John"  # This creates a variable named 'name' and assigns it the value of "John".
Python is a dynamically typed language, which means you don't have to declare the data type of a variable when you create it. 
The interpreter will automatically determine the data type based on the value assigned to the variable.

Types of variables:
- Numeric variables (int, float, complex)
- String variables
- Boolean variables
- List variables
- Tuple variables
- Dictionary variables
- Set variables

Rules for naming variables:
- Variable names must start with a letter or an underscore (_).
- Variable names can only contain letters, numbers, and underscores.
- A variable name cannot start with a number
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.python kewords are reserved words that have special meaning in Python. You cannot use them as variable names.
 Some examples of Python keywords include: if, else, while, for, def, class, and return.



'''
#create a variable by assigning a value to it using the equals sign (=)
x = 5  # This creates a variable named 'x' and assigns it the value of 5.
print(x)  # This will print the value of the variable 'x'.

#Multi Wordsvariable names:
#In Python, you can use underscores to separate words in variable names. This is known as snake_case. For example:
first_name = "John"  # This creates a variable named 'first_name' and assigns it the value of "John".
print(first_name)  # This will print the value of the variable 'first_name'.

#In python, you can also use camelCase for variable names, where the first word is lowercase and subsequent words are capitalized. For example:
lastName = "Doe"  # This creates a variable named 'lastName' and assigns it the value of "Doe".
print(lastName)  # This will print the value of the variable 'lastName'.

#In Python, you can also use PascalCase for variable names, where the first letter of each word is capitalized. For example:
FullName = "John Doe"  # This creates a variable named 'FullName' and assigns it the value of "John Doe".
print(FullName)  # This will print the value of the variable 'FullName'.

#In Python, you can also use kebab-case for variable names, where words are separated by hyphens. However, this is not a common practice in Python and is not recommended. For example:
#full-name = "John Doe"  # This will raise a syntax error because hyphens are not allowed in variable names.


#Assign multiple values to multiple variables in one line
a, b, c = 1, 2, 3
print(a)  # This will print the value of the variable 'a'.
print(b)  # This will print the value of the variable 'b'.  
print(c)  # This will print the value of the variable 'c'.




'''
Global variables and local variables:
Global variables are defined outside of any function and can be accessed from anywhere in the program. 
Local variables are defined inside a function and can only be accessed within that function.
'''
#example of global variable
x=10  # This is a global variable
def my_function():
    print(x) # This will print the value of the global variable 'x'.
my_function() #output: 10

#another example of global variable
def my_function():
    global x  # This tells Python that we want to use the global variable 'x' instead of creating a new local variable.
    x = 5  # This will change the value of the global variable 'x' to 5.
    print(x) # This will print the value of the global variable 'x'.
my_function() #output: 5

#example of local variable
def my_function():
    y=5  # This is a local variable
    print(y) # This will print the value of the local variable 'y'.
my_function() #output: 5



#Exercise:
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
#output: Python is fantastic
print("Python is " + x)
#output: Python is awesome
