""" Q15. Count Occurrences of Alphabets 
Accept a string from the user and count the occurrence of each alphabet, without considering the difference 
between uppercase and lowercase letters. 
Ignore spaces, digits, and special characters. 
Display the count for each alphabet that occurs in the input. 
Sample Input: 
 
 
Welcome to SunBeam. 
Sample Output: 
A : 1 
B : 1 
C : 1 
E : 3 
L : 1 
M : 2 
N : 1 
O : 2 
S : 1 
T : 1 
U : 1 
W : 1 """

def count_alphabets(input_string):
    # Create a dictionary to store the count of each alphabet
    alphabet_count = {}

    # Convert the string to lowercase to make the count case-insensitive
    input_string = input_string.lower()

    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is an alphabet
        if char.isalpha():
            # If the character is already in the dictionary, increment its count
            if char in alphabet_count:
                alphabet_count[char] += 1
            # If the character is not in the dictionary, add it with a count of 1
            else:
                alphabet_count[char] = 1

    return dict(sorted(alphabet_count.items()))

# Accept input from the user
input_str = input("Enter a string: ")
# Call the function and display the result
result = count_alphabets(input_str)
for alphabet, count in result.items():
    print(f"{alphabet} : {count}")