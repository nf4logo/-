# program to check if you need gas.
# Next station is 200 km away

size = float(input("How big is your tank (liters)? "))
full = float(input("How full is your tank (e.g 50 for half full)? "))
mileage = float(input("What is your gas mileage (km per liter)? "))
range = (size - 5) * full / 100 * mileage       # 增加5公升的缓冲区
print("size of tank: "+ str(size) + "\npercent full: " + str(full) + "%\nkm per liter: ")
print("You can go another", range, "km.")
print("The next gas station is 200 km away.")
if range <= 200:
    print("Get Gas Now!")
else:
    print("You can wait for the next station.")
