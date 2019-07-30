nameList = []
print("Enter 5 names (press the Enter key after each name):")
for i in range(5):
    name = input()
    nameList.append(name)
print("The names are", nameList)
print("The sorted names are", sorted(nameList))
print("The third name you entered is:", nameList[2])

indexNum = int(input("Replace one name. Which one? (1-5):")) - 1
newName = input("New name: ")
nameList[indexNum] = newName
print("The names are", nameList)
