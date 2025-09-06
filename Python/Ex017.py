#Python Exercise #017 – Calculating the Hypotenuse of a Right Triangle

#This program calculates the length of the hypotenuse of a right triangle using the Pythagorean theorem 📐.  

#The user enters the lengths of the **opposite leg** and the **adjacent leg**.  
#The program then computes the hypotenuse using the formula:  

#    hypotenuse = √(opposite² + adjacent²)  
import math
input_opposite = float(input("Enter the length of the opposite leg: "))
input_adjacent = float(input("Enter the length of the adjacent leg: "))
hypotenuse = (input_opposite**2 + input_adjacent**2)**0.5
print(f"The length of the hypotenuse is: {hypotenuse:.2f}")

