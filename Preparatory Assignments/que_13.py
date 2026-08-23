""" Q13. Find Duplicate Strings 
Declare an array/list containing a few strings, including some duplicate strings. 
Write a program to identify and display the duplicate strings. 
If a string occurs more than once, display that string only once in the output. """

def find_duplicates(string_list):
    duplicates = set()
    seen = set()
    
    for string in string_list:
        if string in seen:
            duplicates.add(string)
        else:
            seen.add(string)
    
    return list(duplicates)

# Example usage
string_list = ["apple", "banana", "orange", "apple", "grape",
                "banana", "kiwi", "mango", "grape"]
duplicates = find_duplicates(string_list)
print("Duplicate strings:", duplicates)
