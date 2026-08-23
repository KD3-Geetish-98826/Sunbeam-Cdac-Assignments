""" Q11. Employee Details and Salary Increment 
Create an Employee structure/class containing: 
- First name 
- Last name 
- Monthly salary 
Write appropriate functions/methods to: 
1. Initialize employee details. 
2. Display employee details. 
3. Modify the employee's salary. 
4. Calculate and display yearly salary. 
 
 
Create two Employee objects. 
Display the yearly salary of both employees. Then give each employee a 10% salary increase and display 
their yearly salary again. """

class Employee:
    def __init__(self, first_name, last_name, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.monthly_salary = monthly_salary

    def display_details(self):
        print(f"Employee Name: {self.first_name} {self.last_name}")
        print(f"Monthly Salary: {self.monthly_salary}")

    def modify_salary(self, new_salary):
        self.monthly_salary = new_salary

    def calculate_yearly_salary(self):
        return self.monthly_salary * 12

employee1 = Employee(input("Enter first name of employee 1: "), input("Enter last name of employee 1: "), float(input("Enter monthly salary of employee 1: ")))
employee2 = Employee(input("Enter first name of employee 2: "), input("Enter last name of employee 2: "), float(input("Enter monthly salary of employee 2: ")))
print("\nEmployee 1 Details:")
employee1.display_details()
print("\nEmployee 2 Details:")
employee2.display_details()

print("\nYearly Salary of Employee 1:", employee1.calculate_yearly_salary())
print("Yearly Salary of Employee 2:", employee2.calculate_yearly_salary())

# Give each employee a 10% salary increase
employee1.modify_salary(employee1.monthly_salary * 1.1)
employee2.modify_salary(employee2.monthly_salary * 1.1)

print("\nAfter 10% Salary Increase:")
print("Yearly Salary of Employee 1:", employee1.calculate_yearly_salary())
print("Yearly Salary of Employee 2:", employee2.calculate_yearly_salary())
