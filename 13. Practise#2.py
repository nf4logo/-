# define a function with a list argument
def printInfo(info):
    print(info[0])
    print(info[1], end = " ")
    print(info[2])
    print(info[3], end = "")
    if info[4] != "":
        print(",", info[4])
    else:
        print("")
    print(info[5])
    print(info[6])

# call the function and pass a list
printInfo(["Sam White", "45", "Main St.", "Ottawa", "ON", "K2M 2E9", "Canada"])
printInfo(["Mu Xin", "20", "Great St.", "Hong Kong", "", "234567", "China"])
