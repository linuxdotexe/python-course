"""
Day - 1

Input, Output, and String Formatting 
"""

# Input function
# input()
# Store values in variables
# x = input()
# print("Value of x:", x)
# print(type(x))
# y = input("Enter greeting: ")

# input() by default takes string input
# print(type(x))
# which can be converted to other datatypes
# num = int(input("Enter an integer only: "))
# decimal = float(input("Enter a floating point number: "))
# print(type(num))
# print(decimal)
# Print function
# x = input("Enter value of x: ")
# print(x)
# print("The value of x is", x)

# String formatting - Basic Concatenation
name = input("Enter name: ")
# print("Hello " + name + "!")

# String formatting - F-Strings
age = int(input("Please enter your age: "))
print(f"Hello, {name}! You are {age} years old.")

# String formatting - format() method
print("Hello, {}!".format(name))


# String formatting - Positional formatting
print("Hello, {1}! You are {0} years old.".format(age, name))
