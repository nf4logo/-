# program to print multiplication table up to 10
print("Which multiplication table would you like?")
number = int(input())
print("Here's your table:")
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
