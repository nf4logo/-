quarters = int(input("How many quarters? "))
dimes = int(input("How many dimes? "))
nickels = int(input("How many nickels? "))
pennies = int(input("How many pennies? "))
total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
print("You have a total of $", total)
