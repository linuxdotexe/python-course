"""
Day - 5

Dictionaries
"""

# * creating an empty dictionary
empty_dict = {}

# * creating a dictionary with elements
student = {"name": "John", "age": 20, "grade": "A"}


# * accessing dictionary values using keys
name = student["age"]
# print(name)

# exit()


# * modifying a value in a dictionary
student["age"] = 21
# print(student["age"])

# exit()


# * adding a new key-value pair to a dictionary
student["major"] = "Computer Science"
# print(student)

# exit()


# * deleting a key-value pair
# del student["grade"]
# print(student)

# exit()


# * using the .get() method to access values safely
age = student.get("subject")
# print(age)

# exit()


# * using the .pop() method to remove a key-value pair
major = student.pop("major", "Not found")
# print(student)
# print(f"Removed major: {major}")

# exit()


# * using the .update() method to add or modify multiple key-value pairs
student.update({"age": 22, "grade": "B"})
# print(student)

# exit()


# * iterating through dictionary keys
# for key in student:
#   print(key)

# exit()


# * iterating through dictionary values
# for value in student.values():
#   print(value)

# exit()


# * iterating through key-value pairs using .items()
# for key, value in student.items():
#   print(f"{key}: {value}")

# exit()


# * checking if a key exists in the dictionary
# if "name" in student:
#     print("Name exists")

# exit()


# * dictionary length
# length = len(student)
# print(length)

# exit()


# * nested dictionaries
students = {"Alice": {"age": 22, "grade": "A"}, "Bob": {"age": 23, "grade": "B"}}
# print(students)

# exit()


# * accessing values in a nested dictionary
alice_age = students["Bob"]["age"]
print(alice_age)

exit()
