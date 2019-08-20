wordsDic = {}
while 1:
    command = input("Add or look up a word (a/l)? ")

    if command == "a":
        word = input("Type the word: ")
        defi = input("Type the definition: ")
        wordsDic[word] = defi
        print("Word added!")
    elif command == "l":
        word = input("Type the word: ")
        if word in wordsDic:
            print(wordsDic[word])
        else:
            print("That word isn't in the dictionary yet.")
    elif command == "q":
        break
    else:
        print("Invalid command. Please re-enter or enter q to quit.")
