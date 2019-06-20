# program to print multiplication table
# user inputs how high they want it to go
print("Which multiplication table would you like?")
number = int(input())
print("How high do you want to go?")
max = int(input())
print("Here's your table:")
i1 = 1
while i1 <= max:
    print(number, "x", i1, "=", number * i1)
    i1 = i1 + 1
# for i2 in range(1, max + 1):
#     print(number, "x", i2, "=", number * i2)
