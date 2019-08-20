# program to calculate store discount
# 10% off for $10 or less; 20% off for more than $10

price = float(input("Enter the price of the item: "))
if price <= 10:
    print("You got 10% off, your final price will be $" + str(price*0.9))
else:
    print("You got 20% off, your final price will be $" + str(price*0.8))
