"""
Day - 2

Control Structures 
"""

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# basic if statement
# if x == y:
#     print("x equals y")

# exit()















# if else
# if x == y:
#     print("x equals y")
# else:
#     print("x not equal to y")

# exit()















# elif
# if x > y:
#     print("x greater than y")
# elif x < y:
#     print("x less than y")
# else:
#     print("x equals y")

# exit()



# Logical operators
# is_sunny = False
# has_umbrella = True
# is_raining = True

# if is_sunny and not is_raining:
#     print("You can go for a walk!")
# elif is_raining or not has_umbrella:
#     print("You might want to stay indoors.")
# else:
#     print("Be prepared.")

# exit()









# for loop
# for i in range(1, 11):
#     print("For loop output:", i)

# exit()

# while loop
# count = 0
# while count < 10:
#     print(count)
#     count += 1 # count++

# exit()

# break
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# exit()

# continue
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# exit()



























age = int(input("Please enter your age: "))

# Identify the problem - 1
# if age >= 18:
#     print("Adult")
# elif age <= 17 and age >= 13:
#     print("Teenager")
# else:
#     print("Child")

# exit()



















# Identify the problem - 2
if age >= 18:
    print("Adult")
elif age <= 17 and age >= 13:
    print("Teenager")
elif age < 0:
    print("Invalid age")
else:
    print("Child")