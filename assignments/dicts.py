# Create a dictionary with 3 students and their grades (e.g., {"Alice": 85, "Bob": 78, "Charlie": 92}).
grades = {"Alice": 85, "Bob": 78, "Charlie": 92}
# Print the dictionary.
print(grades)
# Add a new student with their grade.
student_name = input("Enter new student name: ")
grades[student_name] = int(input(f"Enter grade for {student_name}: "))
print(grades)

# Update the grade of an existing student.
update_name = input("Enter student to update: ")
grades[update_name] = int(input(f"Enter new grade for {update_name}: "))
print(grades)
# Delete a student by name.
delete_name = input("Enter student to remove: ")
grades.pop(delete_name)
# Print all students with their updated grades.
print(f"Updated grades: {grades}")