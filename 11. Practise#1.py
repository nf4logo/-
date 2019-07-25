# Countdown timer asks the user where to start

import time
startNum = int(input("How many seconds? "))
for i in range(startNum, 0, -1):
    print(i)
    time.sleep(1)
print("BLAST OFF!")
