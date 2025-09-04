# Python Exercise #010 – Currency Converter: BRL to USD
# This program reads how much money a person has in their wallet (in BRL – Brazilian Real)
# and shows how many US Dollars they can buy, based on a fixed exchange rate.

# Example:
# Rate:   US$1.00 = R$3.27

m = float(input("how much money do you hae in your wallet in reals? "))
dolar = 3.27

total = dolar * m 
print(f"You have {total} dolars in your wallet.")
