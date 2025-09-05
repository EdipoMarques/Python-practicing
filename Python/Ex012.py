#012 – Price Calculator with 5% Discount
#
#This program calculates the new price of a product after applying a 5% discount 🛒.  
#
#The user provides the **original price** of the product.  
#The program then applies a 5% discount and shows the **final discounted price**.  
#
#💡 Example:  
#If the original price is $100.00 → the program will calculate 5% off and return $95.00.

price = float(input("Enter the original price of the product: $"))
discount = price * 0.05
final_price = price - discount
print(f"The final price after a 5% discount is: ${final_price}")
