# Python Exercise #011 – Wall Area and Paint Calculator
#
# This program calculates the area of a wall and determines how much paint is needed to cover it.  
#
# The user provides the **width** and **height** of the wall (in meters).  
# The program then calculates:  
# 1. The wall area (width × height).  
# 2. The amount of paint required, assuming that **1 liter of paint covers 2 m²**.

w = float(input("Type here the width of the wall: "))
h = float(input("Type here the height of the wall: "))
area = w * (h**2)

