""" Q12. Reverse a String 
Write a program to reverse a given string without using a built-in string-reversal function such as 
strrev() or slicing syntax. 
Example: 
Input:  SUNBEAM 
Output: MAEBNUS  """

#loop method to reverse a string without using built-in functions

""" def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string """

input_str = input("Enter a string: ")
reverse_string = input_str[::-1]  
print("Reversed string:", reverse_string)

