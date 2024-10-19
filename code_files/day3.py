"""
Day - 3

Functions 
"""
# basic function

def greet():
    print("Hello!")















# function with parameters
def greet_with_name(name):
    print("Hello, {}!".format(name))

# greet_with_name()








# return values
def return_greeting(name):
    return ("Hello, {}!".format(name))


var = return_greeting("something")


def perimeter(a, b):
    return 2 * (a + b)

# 2(l + b)
# l = int(input("Enter L:"))
# b = int(input("Enter B:"))
# l_plus_b = add(l, b)
# print("Perimiter = ", 2 * l_plus_b)



# scope
x = 10 # global variable
def change_value():
    x = 5 # local variable
    print(x) # 5









# modular code example
def calculate_area(radius):
    return 3.14 * radius * radius

def print_area(radius):
    area = calculate_area(radius)
    print(f"Area of a circle: {area}")











# recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)












# test - 1
a = 50
def func(b):
    global a
    a = a + b
    return a
c = func(10)
print("c:", c)
print("a:", a)