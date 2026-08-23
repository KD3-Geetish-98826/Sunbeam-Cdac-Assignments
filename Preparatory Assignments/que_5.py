""" Q5. Character Classification 
Accept a string from the user and count/display the number of: 
- Uppercase letters 
- Lowercase letters 
- Digits 
- Other characters 
Display an appropriate message for each category. """


user_string = input("Enter a string: ")

uppercase_count = 0
lowercase_count = 0
digit_count = 0
other_count = 0

for char in user_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        other_count += 1

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Other characters: {other_count}")
