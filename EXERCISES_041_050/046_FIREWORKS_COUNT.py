# library
from time import sleep

# input
time = int(input("Input the time, in seconds, to count: "))

# processing
for c in range (time,-1,-1):
    print(c)
    sleep(0.5)
print("HAPPY NEW YEAR!")

