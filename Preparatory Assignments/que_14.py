""" Q14. String Palindrome 
Write a program to check whether a given string is a palindrome. 
A palindrome reads the same forward and backward. 
Examples: 
Input:  MADAM 
Output: Palindrome 
 
Input:  HELLO 
Output: Not a Palindrome  """

def is_palindrome(s):
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("Palindrome")
else:
    print("Not a Palindrome")