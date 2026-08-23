""" Q9. Number System Conversion 
Accept an integer number from the user and display its: 
- Binary equivalent 
- Octal equivalent 
- Hexadecimal equivalent 
Sample: 
Enter Number: 20 

Given Number: 20 
Binary equivalent: 10100 
Octal equivalent: 24 
Hexadecimal equivalent: 14 """


num = int(input("Enter Number: "))
print(f"\nGiven Number: {num}")
print(f"Binary equivalent: {bin(num)[2:]}")
print(f"Octal equivalent: {oct(num)[2:]}")
print(f"Hexadecimal equivalent: {hex(num)[2:].upper()}")