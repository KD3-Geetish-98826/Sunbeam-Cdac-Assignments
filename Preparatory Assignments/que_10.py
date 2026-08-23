""" Q10. Sort Student Names 
Read at most 10 student names and store them in an appropriate array/list. 
Sort the names in alphabetical order and display the sorted names. Use appropriate library function for 
sorting. """

student_names = []
for i in range(10):
    name = input(f"Enter name of student {i + 1} (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    student_names.append(name)

student_names.sort()
print("\nSorted Student Names:")
for name in student_names: 
    print(name)