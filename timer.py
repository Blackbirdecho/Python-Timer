import os
import time

sec = int(0)
min = int(0)
hour = int(0)
run = input("Enter R to run")
while run.lower()=="r":
    if sec > 59:
        sec = 0
        min = min+1
    if min > 59:
        min = 0
        hour = hour + 1
    os.system('cls')
    sec = (sec + 0.1)
    print(hour,":",min,":",sec,":")
    time.sleep(0.1)
