# This is a program for creating a Dictionary of Student marks and retrieve the marks based on their name from the dictionary.
# If students name is not found, giving an appropriate message.

# Creating a dictionary with 4 students names and marks.
dictionary_students={"Alpha":40,"Beta":70,"Gamma":90,"Theta":99}
#taking input of the student name
student_name = input("Enter the student's name: ")
#checking for details of the student in dictionary and printing corresponding marks.
if student_name in dictionary_students:
    print(f"{student_name} marks: {dictionary_students[student_name]}")
else:
    print("Student not found. ")