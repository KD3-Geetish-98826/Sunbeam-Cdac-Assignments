""" Q3. Fibonacci Series 
Write a program to generate and display the first n terms of the Fibonacci series.  """

n_terms = int(input("Enter the number of terms for the Fibonacci series: "))

# First two terms of the Fibonacci series
a, b = 0, 1

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci series up to 1 term:")
    print(a)
else:
    print("Fibonacci series:")
    for i in range(n_terms):
        print(a, end=" ")
        a, b = b, a + b