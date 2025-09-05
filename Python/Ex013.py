#Python Exercise #013 – Salary Adjustment with 15% Increase
#This program calculates the new salary of an employee after applying a 15% raise 💼.  
#
#The user enters the **current salary**.  
#The program then applies a 15% increase and displays the **new salary**.  

salary = float(input("Enter here your salary: $"))
increase = salary * 0.15
new_salary = salary + increase
print(f"Your new salary after a 15% increase is: ${new_salary}")
