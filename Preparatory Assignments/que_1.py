""" Q1. Find the Maximum Number 
Accept n numbers through command-line arguments and find and display the maximum number. 
Note: Assume that at least one number is provided. """

import sys

arg = sys.argv[1:]  

if len(arg) == 0:
    print("Please provide at least one number as a command-line argument.")
    sys.exit(1)

max_no = float(arg[0])  

for num_str in arg:
    cor_no = float(num_str)
    if cor_no > max_no:
        max_no = cor_no

print("The maximum number is:", max_no)
