""" Q8. Student Details Using a Structure/Class 
Create a Student structure/class containing the following information: 
- Student name 
- Roll number 
- Total marks 
The roll number may contain both letters and numbers. 
Accept the student details from the user and display the data as entered.  """

class Student:
    def __init__(self, name, roll_number, total_marks):
        self.name = name
        self.roll_number = roll_number
        self.total_marks = total_marks

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Total Marks: {self.total_marks}")

student = Student(input("Enter student name: "), input("Enter roll number: "), float(input("Enter total marks: ")))
student.display_details()

 