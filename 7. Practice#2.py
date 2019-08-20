# program to check age and gender of soccer players
# accept girls who are 10 to 12 years old

age = float(input("What is your age? "))
if 10 <= age <= 12:
    gender = input ("Are you male or femal ('m' or 'f')? ")
    if gender == "f":
        print("You can play on the team!")
    else:
        print("Only girls are allowed on this team.")
else:
    print("You are not the right age.")
