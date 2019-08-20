# Countdown timer asks the user where to start
# and prints stars beside each number

import time
startNum = int(input("How many seconds? "))

for i in range(startNum, 0, -1):
    print(i, end="")
    for k in range(i):
        print("*", end="")
    print()
    time.sleep(1)
print("BLAST OFF!")
