# program to print multiplication table up to 10 (while loop)
print("Which multiplication table would you like?")
number = int(input())
print("Here's your table:")
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i = i + 1
