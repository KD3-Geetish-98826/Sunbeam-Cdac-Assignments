""" Q7. Multiplication Tables 
Accept two numbers from the user and display the multiplication tables for all numbers from the first 
number to the second number. 
Example: 
For input 5 and 10, display the multiplication tables of 5, 6, 7, 8, 9, and 10.  """

start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

if start_num > end_num:
    print("Starting number should be less than or equal to the ending number.")
else:
    for num in range(start_num, end_num + 1):
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")