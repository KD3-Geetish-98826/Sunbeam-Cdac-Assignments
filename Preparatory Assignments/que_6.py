""" Q6. Matrix Multiplication 
Write a program to perform multiplication of two matrices. 
Accept the dimensions and elements of both matrices from the user. Check whether matrix multiplication is 
possible before performing the operation. 
Condition: The number of columns in the first matrix must be equal to the number of rows in the second 
matrix. 
Display the resulting matrix. """

print("Matrix Multiplication")
print("Enter dimensions for the first matrix:")
rows1 = int(input("Number of rows: "))
cols1 = int(input("Number of columns: "))
print("Enter dimensions for the second matrix:")
rows2 = int(input("Number of rows: "))
cols2 = int(input("Number of columns: "))

if cols1 != rows2:
    print("Matrix multiplication is not possible. The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
else:
    print("Enter elements for the first matrix by rows:")
    matrix1 = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            element = int(input(f"Enter element [{i}][{j}]: "))
            row.append(element)
        matrix1.append(row)

    print("Enter elements for the second matrix by rows:")
    matrix2 = []
    for i in range(rows2):
        row = []
        for j in range(cols2):
            element = int(input(f"Enter element [{i}][{j}]: "))
            row.append(element)
        matrix2.append(row)

    result_matrix = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            sum_product = 0
            for k in range(cols1):
                sum_product += matrix1[i][k] * matrix2[k][j]
            row.append(sum_product)
        result_matrix.append(row)

    print("Resulting Matrix:")
    for row in result_matrix:
        print(row)
