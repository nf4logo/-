length = float(input("Length of the room in feet: "))
width = float(input("Width of the room in feet: "))
price = float(input("Cost per square yard: "))
area_feet = length * width
area_yards = area_feet / 9.0
cost = area_yards * price
print("The area is", area_feet, "square feet. That is", area_yards, "yards, which will cost $", cost)
