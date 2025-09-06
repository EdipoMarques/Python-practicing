#Python Exercise #016 – Extracting the Integer Part of a Real Number
#This program reads a real number entered by the user and displays its integer part only 🔢.  

#For example:  
#- If the user inputs 6.127 → the program will output 6 as the integer part.  
#- If the user inputs -4.89 → the program will output -4 as the integer part.  
#
#To achieve this, the program uses Python’s built-in functions or the math library to truncate the decimal part of the number.

import math
num = float(input("Enter here a number: "))
print(f"The integer part of the number {num} is {math.trunc(num)}")
#or
print(f"The integer part of the number {num} is {int(num)}")
