""" Q4. Student Grade 
Write a program to calculate the grade of a student. 
The student has five subjects, and marks for each subject are entered from the keyboard. Assume that each 
subject is evaluated out of 20 marks, making the total marks out of 100. 
 
 
Assign the grade according to the following rules: 
Total Marks Grade 
90–100 Ex 
80–89 A 
70–79 B 
60–69 C 
Below 60 F 
Display the total marks and the corresponding grade.  """


subject1 = float(input("Enter marks for subject 1 (out of 20): "))
subject2 = float(input("Enter marks for subject 2 (out of 20): "))
subject3 = float(input("Enter marks for subject 3 (out of 20): "))
subject4 = float(input("Enter marks for subject 4 (out of 20): "))
subject5 = float(input("Enter marks for subject 5 (out of 20): "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
print(f"Total Marks: {total_marks}")

if total_marks >= 90:
    grade = "Ex"
elif total_marks >= 80:
    grade = "A"
elif total_marks >= 70:
    grade = "B"
elif total_marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")