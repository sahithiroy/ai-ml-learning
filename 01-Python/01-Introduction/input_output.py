'''
    
The input() function is used to take input from the user. The input() function reads a line from the console and returns it as a string. 
In this case, the user has entered the number 5, which is then printed to the console using the print() function.
The print() function is used to display output to the console. It can take multiple arguments and will print them separated by spaces.
In this case, the print() function is used to display the string "You entered:" followed by the value of the variable user_input, which contains the input provided by the user.
# Taking input from the user
user_input = input("Enter a number: ")  # This will prompt the user to enter a number and store it in the variable 'user_input'.
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:" followed by the value of 'user_input'.

'''
# Taking input from the user
user_input = input("Enter a number: ")  # This will prompt the user to enter a number and store it in the variable 'user_input'.
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:" followed by the value of 'user_input'.


#Taking the input as integer
user_input = int(input("Enter a number: "))  # This will prompt the user to enter a number, convert it to an integer, and store it in the variable 'user_input'.    
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:"

#Taking the input as float
user_input = float(input("Enter a number: "))  # This will prompt the user to enter a number, convert it to a float, and store it in the variable 'user_input'.
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:" followed by the value of 'user_input'.

#Taking the input as string
user_input = str(input("Enter a string: "))  # This will prompt the user to enter a string and store it in the variable 'user_input'.
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:"

#Taking the input as boolean
user_input = bool(input("Enter a boolean value (True/False): "))  # This will prompt the user to enter a boolean value and store it in the variable 'user_input'.
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:" followed by the value of 'user_input'.

#Taking the input as list
user_input = list(input("Enter a list of values separated by commas: ").split(','))  # This will prompt the user to enter a list of values separated by commas, split the input string into a list, and store it in the variable 'user_input'.
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:" followed by the value of 'user_input'.

#Taking the input as tuple
user_input = tuple(input("Enter a tuple of values separated by commas: ").split(','))# This will prompt the user to enter a tuple of values separated by commas, split the input string into a tuple, and store it in the variable 'user_input'.
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:" followed by the value of 'user_input'.

#Taking the input as dictionary
user_input = dict(item.split(':') for item in input( "Enter a dictionary of key-value pairs separated by commas (key:value): ").split(','))  # This will prompt the user to enter a dictionary of key-value pairs separated by commas, split the input string into a dictionary, and store it in the variable 'user_input'.
# Displaying the output 
print("You entered:", user_input)  # This will print the string "You entered:" followed by the value of 'user_input'.

#Taking the input as set
user_input = set(input("Enter a set of values separated by commas: ").split(','))  # This will prompt the user to enter a set of values separated by commas, split the input string into a set, and store it in the variable 'user_input'.
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:" followed by the value of 'user_input'.

#Taking the input as frozenset
user_input = frozenset(input("Enter a frozenset of values separated by commas: ").split(','))  # This will prompt the user to enter a frozenset of values separated by commas, split the input string into a frozenset, and store it in the variable 'user_input'.
# Displaying the output
print("You entered:", user_input)  # This will print the string "You entered:" followed by the value of 'user_input'.